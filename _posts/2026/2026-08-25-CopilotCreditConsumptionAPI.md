---
title: "Copilot 크레딧, 어디로 새는지 직접 들여다보기: Power Platform API로 테넌트 전체 소비 뷰 만들기"
date: 2026-08-25T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - CopilotCredits
  - PowerPlatformAPI
  - Dataverse
  - Governance
  - CostManagement
  - GitHubCopilotHarness
excerpt: "Power Platform 관리 센터의 기본 보고서로는 부족할 때, Power Platform API로 테넌트 용량과 에이전트별 일일 소비를 직접 가져올 수 있습니다. GitHub Copilot harness가 빌드·미리 보기·평가 단계에서도 크레딧을 소비하면서 이 가시성이 더 중요해졌습니다. MCSCAT 팀이 API 호출 방법과 Dataverse 기반 커뮤니티 솔루션을 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 크레딧, 어디로 새는지 직접 들여다보기: Power Platform API로 테넌트 전체 소비 뷰 만들기

Power Platform 관리 센터(PPAC)에는 테넌트의 Copilot 크레딧 소비 보고서가 이미 있습니다. **Licensing > Copilot Studio** 아래에서 볼 수 있고, 많은 조직에게는 이것이 출발점이자 충분한 답입니다.

문제는 그다음입니다. 원문의 표현을 그대로 옮기면, **"읽을 수는 있지만 형태를 바꾸거나 원본 행을 소유할 수는 없습니다."** 특정 에이전트의 추세선을 보면서 어떤 채널이 소비를 견인했는지 함께 보고 싶거나, 청구 대상과 비청구를 나눠 보고 싶거나, 보고 기간을 넘어서는 이력을 남기고 싶을 때 벽에 부딪힙니다.

그리고 이 문제가 **지금 더 중요해진 이유**가 있습니다. **GitHub Copilot harness는 에이전트가 프로덕션에서 실행될 때만이 아니라, 메이커가 빌드·미리 보기·평가하는 동안에도 크레딧을 소비**합니다.

Microsoft Copilot Studio Customer Advisory Team(MCSCAT)의 이번 글은 두 가지를 다룹니다. **테넌트 용량과 리소스별 소비를 노출하는 Power Platform 라이선싱 엔드포인트**, 그리고 그 결과를 **Dataverse의 일일 이력으로 만드는 커뮤니티 솔루션**입니다.

![Copilot 크레딧 소비 대시보드](/mwkorea/assets/images/2026-08-25-CopilotCreditConsumptionAPI/image1.png)

---

## 시작 전에 — 두 가지 전제

원문이 서두에서 분명히 하는 점이 있습니다.

**1. PPAC부터 보세요**

이 커뮤니티 솔루션은 **PPAC 보고서를 대체하는 것이 아닙니다.** API 데이터를 가져와 Dataverse에 보관하고 자체 보고서를 만들어야 할 **구체적인 이유가 있는 조직**을 위한 것입니다.

**2. 짝이 되는 글이 있습니다**

비용 관리의 나머지 절반 — **용량 할당, 에이전트별 한도 설정, 그 강제** — 는 동료 **Lewis Baybutt**가 쓴 [Adopting the GitHub Copilot Harness: Cost Control and Governance in Copilot Studio](https://microsoft.github.io/mcscatblog/posts/copilot-harness-cost-governance/)에서 다룹니다. 이 글이 소비를 **보이게 만드는 방법**이라면, 그 글은 그 소비에 **경계를 두는 방법**입니다. 함께 읽기를 권합니다.

---

## 1. Power Platform API로 크레딧 소비 조회하기

자체 보고 환경을 만들어야 한다면, [Microsoft Power Platform API](https://learn.microsoft.com/rest/api/power-platform/)가 `https://api.powerplatform.com`을 통해 테넌트 용량과 일일 리소스 소비를 노출합니다.

### 테넌트 용량 조회

```
GET https://api.powerplatform.com/licensing/entitlements/MCSMessages?api-version=2024-10-01
```

이 경로는 Copilot 크레딧에 대해 다음 값을 반환합니다.

- **entitled**(부여된)
- **allocated**(할당된)
- **consumed**(소비된)
- **available**(가용)
- **status**(상태)
- **pay-as-you-go** 값

응답에는 **최근 완료된 사용 날짜(latest completed usage date)** 도 포함됩니다. 통합 로직이 상세 소비 데이터가 얼마나 최신인지 판단하는 데 쓰입니다.

### 에이전트별 소비 조회

```
GET https://api.powerplatform.com/licensing/entitlements/MCSMessages/resources
    ?fromDate={yyyy-MM-dd}
    &toDate={yyyy-MM-dd}
    &includeFields=users%2Ctags%2CasOfDate
    &pageSize=5000
    &continuationtoken={token}
    &api-version=2024-10-01
```

**하루씩 요청하면 깔끔한 일일 이력**이 만들어집니다.

주의할 점이 있습니다. **채널, 기능, 모델, 환경 같은 차원이 다르면 같은 날 같은 에이전트에 대해 여러 행이 반환**됩니다. **continuation token을 따라 모든 페이지를 가져온 뒤**, 보고서가 답해야 할 질문에 맞춰 행을 집계해야 합니다.

### 응답에서 얻는 정보

| 정보 | 활용 |
|---|---|
| **에이전트 ID·표시 이름** | 개별 에이전트 식별·비교 |
| **환경 ID** | 환경별 소비 그룹화 |
| **사용 날짜** | 일일 추세 구성, 이력 보존 |
| **청구·비청구 크레딧** | 용량을 차감하는 것과 API가 별도 보고하는 것 구분 |
| **보고된 사용자 수** | 반환된 행 단위의 도입 맥락 파악 |
| **기능·도구·모델·채널·지식 소스** | 소스가 해당 차원을 제공할 때 소비 기여 요인 설명 |

### 환경 이름 해석

소비 행에는 **환경 이름이 포함되지 않습니다.** 환경 ID는 별도 경로로 해석합니다.

```
GET https://api.powerplatform.com/environmentmanagement/environments?api-version=2024-10-01
```

이 두 엔드포인트를 조합하면 테넌트 전체의 일일 이력을 만들고, 에이전트·환경을 비교하고, 청구와 비청구를 분리하며, 가용한 경우 채널 등의 차원 맥락을 더할 수 있습니다.

---

## harness별 텔레메트리 차이 — 중요합니다

원문이 별도 박스로 강조하는 내용입니다.

> **표준 harness 에이전트**는 기능(feature), 도구(tool), 모델(model), 채널(channel), 지식 소스(knowledge source) 세부 정보를 제공할 수 있습니다.
>
> **GitHub Copilot harness 에이전트**는 현재 **기능을 `Process Agent`로 보고**하며 **도구·모델·지식 소스 값을 제공하지 않습니다.**
>
> 해당 필드가 비어 있는 것은 **소스 텔레메트리의 특성이지, 통합 구현의 데이터 누락이 아닙니다.**

GitHub Copilot harness로 만든 에이전트의 소비를 분석하려는 조직이라면 이 제약을 먼저 알고 시작해야 합니다. "왜 값이 안 나오지?" 하고 디버깅에 시간을 쓰는 상황을 피할 수 있습니다.

### 지원 범위에 대한 안내

원문은 또 하나의 경계를 명시합니다.

> 핵심 경로와 응답 모델은 Microsoft가 문서화했습니다. 다만 **일부 선택적 rich 메타데이터는 공개 참조 문서에 완전히 기술되어 있지 않으므로**, 통합을 업데이트할 때 **보고서가 의존하는 필드를 직접 테스트**하세요.

---

## 2. 커뮤니티 솔루션 — Dataverse에 이력 남기기

API 호출은 오늘의 질문에 답합니다. **응답을 저장해 두면 재사용·비교·시간에 따른 보고가 가능한 이력**이 됩니다. [copilot-credit-consumption 커뮤니티 솔루션](https://github.com/PetrosFeleskouras/copilot-credit-consumption)이 이 패턴을 Power Platform 솔루션으로 패키징했습니다.

### 구성 요소

단일 솔루션 가져오기로 배포되며, 다음을 포함합니다.

- **일일 Power Automate 흐름**
- **Dataverse 테이블 3개**
- **보안 역할 1개**
- **Power Apps Code App**

검증된 V2 패키지는 [v2.0.0 릴리스](https://github.com/PetrosFeleskouras/copilot-credit-consumption/releases/tag/v2.0.0)에서 받을 수 있습니다.

### 동작 방식

1. **예약된 Power Automate 흐름**이 매일 용량·리소스 소비·환경 엔드포인트를 호출합니다.
2. **첫 실행에서 최대 180일 이력**을 가져옵니다. 이후 실행은 **최근 7일을 갱신**해 소스 업데이트가 자동 반영됩니다.
3. **Dataverse**가 상세 소비 이력, 테넌트 용량 스냅샷, 최신 동기화 상태를 **3개의 전용 테이블**에 저장합니다.
4. 포함된 **Power Apps Code App**이 그 테이블을 읽어 대화형 대시보드로 만듭니다.

### 데이터를 소유하면 생기는 것

데이터가 Dataverse에 있으므로 하나의 API 응답이나 고정된 보고서에 묶이지 않습니다.

- **자체 정책에 따른 이력 보존**
- **읽기 전용 보안 역할을 통한 접근 통제**
- **Power BI, Excel, 기타 애플리케이션 연결**

### 포함된 대시보드

- 용량 상태
- 청구·비청구 추세
- 상위 에이전트·환경
- 유연한 필터
- 상세 레코드
- Excel 내보내기
- API가 채널 등 rich 메타데이터를 제공하는 경우 해당 차원으로 소비 설명

> 이 패키지는 **표준 Power Platform 구성 요소로만** 만들어졌으며, 가져오기 과정에서 내용을 검사할 수 있고 조직의 일반적인 Power Platform 프로세스로 배포할 수 있습니다.

---

## 한국 도입 담당자를 위한 체크포인트

- **PPAC로 먼저 충분한지 판단하세요**: 원문도 "많은 조직에게는 기본 보고서가 출발점"이라고 명시합니다. **자체 구축이 필요한 구체적 이유**(장기 이력 보존, 특정 차원 분석, 사내 BI 통합 등)가 있을 때 이 경로를 택하세요.
- **GitHub Copilot harness 도입 시 특히 중요**: harness가 **빌드·미리 보기·평가 단계에서도 크레딧을 소비**합니다. 메이커가 늘어날수록 프로덕션 실행과 무관한 소비가 쌓입니다. **개발 단계 소비를 별도로 추적**할 필요가 있다면 이 가시성이 필수적입니다.
- **harness별 필드 차이를 사전에 확인**: GitHub Copilot harness는 기능이 `Process Agent`로만 나오고 도구·모델·지식 소스는 비어 있습니다. **보고서 설계 전에 어떤 차원이 실제로 채워지는지** 테스트하세요.
- **continuation token 처리를 빠뜨리지 마세요**: 페이지가 나뉘어 반환되므로 **모든 페이지를 순회하지 않으면 데이터가 누락**됩니다. 자체 구현 시 가장 흔한 실수 지점입니다.
- **환경 ID → 이름 매핑 필요**: 소비 행에 환경 이름이 없습니다. **별도 환경 관리 경로 호출**을 통합에 포함해야 보고서가 읽을 만해집니다.
- **문서화되지 않은 필드 의존 주의**: 일부 rich 메타데이터는 공개 문서에 완전히 기술되어 있지 않습니다. **해당 필드에 의존하는 보고서는 업데이트 때마다 검증**하세요.
- **비용 통제와 함께 설계**: 소비를 보이게 만드는 것과 한도를 거는 것은 별개입니다. 짝이 되는 [비용 통제·거버넌스 글](https://microsoft.github.io/mcscatblog/posts/copilot-harness-cost-governance/)을 함께 검토해 **가시성 + 경계**를 한 세트로 준비하세요.
- **커뮤니티 솔루션의 성격 인지**: Microsoft 공식 제품이 아닌 **커뮤니티 솔루션**입니다. 표준 구성 요소로 만들어져 검사 가능하지만, 도입 시 사내 검토 절차를 거치는 것이 좋습니다.

---

## 마무리

원문의 정리를 그대로 옮기면 이렇습니다.

- **PPAC에서 시작하라.** 기본 보고서가 많은 조직의 요구를 충족한다.
- **필요할 때 만들어라.** 다른 보고 경험이 필요하다면 API와 커뮤니티 솔루션이 경로를 제공한다.
- **Power Platform API가 원천이다.** 테넌트 용량, 에이전트별 일일 소비, 크레딧 사용처를 이해할 차원을 노출한다.
- **사용 가능한 세부 정보는 harness에 따라 다르다.** 표준 harness는 더 풍부한 차원을, GitHub Copilot harness는 현재 더 제한적인 뷰를 제공한다.
- **커뮤니티 솔루션이 데이터를 재사용 가능하게 만든다.** 일일 흐름이 소비·용량·동기화 정보를 Dataverse에 저장해 단일 API 호출을 넘어 이력이 남는다.
- **보고 경험은 선택할 수 있다.** 포함된 Code App을 쓰거나 Power BI·Excel 등을 연결하면 된다.

원문은 마지막에 이렇게 묻습니다. **Copilot Studio를 대규모로 운영 중이신가요? 지금 소비를 어떻게 추적하고 계신가요 — 관리 센터인가요, 직접 구축한 이력인가요?**

---

> **출처**
>
> - 원문 제목: *Where Are Your Copilot Credits Going? Build a Tenant-Wide View with the Power Platform API*
> - 링크: [https://microsoft.github.io/mcscatblog/posts/copilot-credit-consumption-api/](https://microsoft.github.io/mcscatblog/posts/copilot-credit-consumption-api/)
>
> 자세한 내용은 원문을 참조하세요.
