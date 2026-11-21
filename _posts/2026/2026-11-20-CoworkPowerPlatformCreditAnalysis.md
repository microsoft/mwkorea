---
title: "Copilot Credits는 어디서 쓰일까? Cowork로 Power Platform 사용량을 분석하는 방법"
date: 2026-11-20T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCowork
  - PowerPlatform
  - CopilotStudio
  - CopilotCredits
  - Governance
  - Preview
excerpt: "Copilot Cowork의 Power Platform Admin 프리뷰 플러그인으로 환경별 Copilot Credits 사용량을 묻고 차트로 정리하는 방법을 소개합니다. 연결 계정의 관리자 역할, 읽기 전용 범위, 누적 스냅샷과 주간 보고서의 차이를 함께 확인합니다. 정기 보고는 일정과 전달 도구의 권한·승인을 별도로 검토해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Credits는 어디서 쓰일까? Cowork로 Power Platform 사용량을 분석하는 방법

Power Platform을 운영하다 보면 “어느 환경에서 Copilot Credits를 많이 사용했나요?”라는 질문을 자주 받습니다. 답을 얻을 때마다 데이터를 내보내고 표와 차트를 다시 만들면, 간단한 질문도 작은 보고서 프로젝트가 됩니다.

Microsoft Copilot Studio Customer Advisory Team의 **The Custom Engine** 블로그는 2026년 11월 20일, **Copilot Cowork와 Power Platform Admin (Preview) 플러그인**으로 사용량을 대화형으로 분석하는 방법을 소개했습니다. 이미 Cowork를 이용하는 조직이라면 자연어 질문으로 환경별 현황을 살펴보고 후속 질문으로 차트를 만들 수 있습니다.

다만 이것은 관리 작업을 무조건 자동 실행하는 기능이 아닙니다. 플러그인은 프리뷰이며, **읽기 전용 인사이트와 안내**를 제공한다는 전제를 먼저 이해해야 합니다.

![Cowork로 Power Platform 크레딧 사용량을 분석하는 원문 소개 이미지](/mwkorea/assets/images/2026-11-20-CoworkPowerPlatformCreditAnalysis/image1.png)

---

## 시작 전: Cowork 접근 권한과 관리자 역할을 구분하세요

원문에서 요구하는 기본 조건은 Cowork 접근 권한, 플러그인 사용 가능 상태, 그리고 연결 계정의 Power Platform 데이터 접근 권한입니다.

연결 계정에는 다음 역할 중 하나가 필요합니다.

- **Power Platform Administrator**
- **Dynamics 365 Administrator**
- **Global Administrator**

플러그인이 설치되었다고 이 역할이 자동으로 부여되는 것은 아닙니다. 설치 대상에 포함되는 것, Cowork를 사용할 수 있는 것, Power Platform 데이터에 접근할 수 있는 것은 서로 다른 조건입니다.

2026년 11월 20일 확인한 [Microsoft Learn 설치·연결 문서](https://learn.microsoft.com/en-us/power-platform/admin/power-platform-admin-cowork)는 설치를 관리하는 Microsoft 365 권한과 데이터 조회용 역할을 별도로 설명합니다. Cowork 자체의 접근 설정도 별도로 확인해야 하며, 플러그인 설치만으로 Cowork 접근 권한이 생기지 않습니다.

## Power Platform Admin 플러그인 연결하기

플러그인이 조직에 제공되어 있다면 원문의 시작 절차는 다음과 같습니다.

1. Cowork의 **Customize**에서 플러그인 영역을 열고 **Power Platform Admin (Preview)**를 찾습니다.
2. 플러그인을 열어 활성화합니다.
3. 연결 요청이 나타나면 **Connect**를 선택하고, **Power Platform for Admins V2** 연결의 인증 유형을 **OAuth Connection**으로 설정해 연결합니다.

플러그인 이름은 **Power Platform Admin (Preview)**이고, 그 아래 실제 연결 이름은 **Power Platform for Admins V2**입니다. 이름이 다르다고 잘못된 연결로 판단하지 않도록 구분해 두면 좋습니다.

![Power Platform Admin 프리뷰 플러그인과 Power Platform for Admins V2 연결 상태](/mwkorea/assets/images/2026-11-20-CoworkPowerPlatformCreditAnalysis/image2.png)

플러그인이 보이지 않으면 Microsoft 365 관리자에게 설치 대상과 사용 가능 여부를 확인해야 합니다. 보충 문서에서는 관리자가 Microsoft 365 관리 센터의 **Agents → Tools → Registry**에서 Microsoft가 게시한 플러그인을 찾아 대상 사용자에게 설치하는 흐름을 안내합니다.

연결 시에는 의도한 조직과 계정인지 확인하고, 비밀번호나 토큰을 채팅에 붙여 넣지 않아야 합니다. 조회 중 데이터 접근 요청이 표시되면 내용을 검토한 뒤 사용자가 승인하는 절차가 필요할 수 있습니다.

## 첫 질문: 환경별 크레딧 소비량을 표로

원문의 첫 질문은 다음과 같습니다.

> How many credits did I have consumed per environment in Power Platform so far?

한국어로 풀면 “지금까지 Power Platform의 환경별 크레딧 사용량을 알려줘”입니다. 원문은 영어 질문으로 시연했으며, 아래 한국어 표현은 독자의 이해를 돕기 위한 예시입니다.

Cowork는 소비량, 할당된 크레딧, 환경별 스냅샷 날짜를 요약과 표로 반환합니다. 원문의 데모 화면에는 **10개 환경의 누적 소비량 145,997 Copilot Credits**, 사용량이 있는 환경 **9개(90%)**, 스냅샷 날짜 **2026년 11월 20일**이 표시됩니다.

이 수치는 **원문 작성자의 데모 테넌트 데이터**입니다. 일반 고객의 평균 사용량이나 우리 조직의 사용량을 나타내는 값이 아닙니다.

![데모 테넌트의 환경별 소비량·할당량·스냅샷 날짜를 보여주는 Cowork 응답](/mwkorea/assets/images/2026-11-20-CoworkPowerPlatformCreditAnalysis/image3.png)

## 후속 질문: 같은 데이터를 차트로 바꾸기

이어서 원문 작성자는 간단하게 요청합니다.

> Make a chart.

Cowork는 이미 대화에 있는 결과를 이용해 환경별 사용량을 시각화합니다. 데모 차트에서는 가장 사용량이 많은 환경의 소비량 **109,273 Credits**가 전체의 약 **75%**로 표시됩니다.

![동일한 데모 데이터로 생성한 환경별 크레딧 사용량 막대 차트](/mwkorea/assets/images/2026-11-20-CoworkPowerPlatformCreditAnalysis/image4.png)

특정 환경을 지정하거나, 다른 시각화를 요청하거나, 보고 기간을 좁히는 후속 질문도 가능합니다. 핵심은 차트 모양보다 **무슨 기간과 어떤 집계 기준의 데이터를 보고 있는지**입니다.

## 누적 스냅샷을 주간 사용량으로 오해하지 마세요

원문은 위 예시가 **누적 스냅샷**이며 주간 소비 보고서가 아니라고 강조합니다. “지금까지”라는 표현이 이번 달이나 지난주를 의미한다고 가정하면 안 됩니다.

실무에서는 다음처럼 조건을 명확히 주는 것이 좋습니다.

> 지난 완결된 주의 환경별 Copilot Credits 사용량을 분석해 줘. 집계 시작일과 종료일, 적용 시간대, 데이터 최신성을 먼저 확인하고, 해당 기간 데이터가 없으면 추정하지 말고 알려줘.

이는 원문에서 강조한 기간 명시를 한국 업무에 맞게 풀어 쓴 권장 예시입니다. 서로 다른 날짜의 누적 수치를 비교해 증감을 계산하려면 집계 기준과 범위가 동일한지도 확인해야 합니다.

## 정기 보고: 일정 승인과 메일 전달은 별개입니다

원문은 Cowork의 **scheduled prompts**로 반복 작업을 요청하는 방법도 소개합니다. 원문의 예시 조건은 **매주 월요일 오전 9시**, **지난 완결된 주**, **환경별 사용량과 차트**, **보고 기간과 데이터 최신성 포함**입니다.

한국 조직에서는 다음처럼 시간대와 전달 조건까지 명시하는 요청을 고려할 수 있습니다.

> 매주 월요일 오전 9시, 한국 시간 기준으로 지난 완결된 주의 Power Platform Copilot Credits 환경별 보고서를 준비해 줘. 차트, 실제 집계 날짜와 시간대, 데이터 최신성을 포함해 줘. 메일 전달이 가능하면 나에게 보내고, 불가능하면 필요한 연결이나 승인을 알려줘.

예약이 활성화되기 전에는 사용자가 제안된 **일정·시간대·전달 설정**을 검토하고 승인해야 합니다. 메일 전달은 Cowork 환경의 도구, 권한과 승인 상태에 따라 달라집니다. Power Platform Admin 플러그인은 관리 인사이트를 제공할 뿐, 자체적으로 메일 기능을 제공하는 것은 아닙니다.

## 개발자가 알아둘 별도 경로: 사용량 보고서 API도 프리뷰

대화형 분석이 아니라 시스템 연계나 장기 이력 보관이 필요하다면, 원문은 [Copilot Credit usage reports API](https://learn.microsoft.com/en-us/power-platform/admin/programmability-tutorial-download-copilot-credit-usage-reports?tabs=power-automate)를 출발점으로 제시합니다.

아래는 블로그 원문과 별도로, 2026년 11월 20일 확인한 Microsoft Learn 문서의 보충 내용입니다.

| 확인 항목 | 문서의 설명 |
|---|---|
| 제공 상태 | 공개 프리뷰이며 sovereign cloud는 현재 지원하지 않음 |
| 인증 | 위 관리자 역할을 가진 사용자 계정의 위임 인증만 지원하며 application-only 토큰은 미지원 |
| 이력 | 기본 30일 보고 창을 넘어 보관하려면 다운로드한 데이터를 별도로 유지 |
| 환경별 보고 | `BillingDetailsPerEnvironment`로 환경·권리·청구 정책별 소비 확인 |
| 리소스별 보고 | `FeatureDetailsPerResource`로 에이전트·리소스·제품·기능별 확인 |
| 집계 | `Daily`는 일별 행, `Summary`는 요청 기간 합계이며 날짜 열 생략 |

보고서는 비동기로 생성됩니다. **제출 → 상태 확인 → 다운로드** 순서이며, 제출은 `202 Accepted`와 `Location`, `Retry-After`를 반환합니다. 상태 조회가 `200 OK`여도 본문의 `status`가 `Running`이면 아직 완료가 아닙니다. 서비스가 지정한 `Retry-After` 간격을 따르고 `Succeeded` 또는 `Failed`를 확인해야 합니다.

문서는 제출·폴링·다운로드를 합치는 새 커넥터 액션과 커넥터의 JSON 출력 지원을 **2026년 12월 제공 예정**으로 안내합니다. 확인 시점에는 커넥터가 기본 CSV를 생성하므로, 문서의 미래 JSON 예제를 현재 제공 기능으로 단정하지 않아야 합니다.

## 마무리: 사용량 질문을 거버넌스의 출발점으로

Cowork의 장점은 복잡한 보고서를 먼저 설계하지 않고도 환경별 사용량 질문을 시작하고, 필요한 분석으로 이어갈 수 있다는 점입니다. 다만 생성된 표와 차트의 값은 집계 기간·데이터 최신성과 함께 읽어야 합니다.

읽기 전용 조회로 이상 징후를 찾은 뒤에는 조직의 소비 통제 정책과 연결하면 됩니다. 원문이 안내하는 [Copilot Studio 소비 통제 가이드](https://microsoft.github.io/mcscatblog/posts/copilot-harness-cost-governance/)를 참고하되, 조회 결과만으로 할당량이나 한도가 자동 변경되는 것은 아니라는 점을 기억하세요.

> **출처**: [Use Copilot Cowork to dig deep into your Power Platform credit consumption data](https://microsoft.github.io/mcscatblog/posts/copilot-cowork-credit-analysis/) — Microsoft Copilot Studio Customer Advisory Team, The Custom Engine, 2026년 11월 20일. 자세한 내용은 원문 참조.
