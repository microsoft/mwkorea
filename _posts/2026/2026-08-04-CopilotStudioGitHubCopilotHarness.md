---
title: "Copilot Studio에 GitHub Copilot harness가 정식 출시 — 자율 업무 프로세스를 위한 세 번째 선택지"
date: 2026-08-04T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - GitHubCopilotHarness
  - Agent
  - Workflow
  - Opus5
  - GPT56
  - UsageBasedBilling
  - CopilotCredits
excerpt: "두 달간 프리뷰로 제공되던 Copilot Studio의 새 에이전트 역량이 정식 출시되며 'GitHub Copilot harness'라는 이름을 갖게 되었습니다. Copilot Cowork와 GitHub Copilot 코딩 에이전트를 움직이는 바로 그 엔진으로, 자체 벤치마크에서 코드 분석 40.6% → 88.1% 같은 큰 폭의 개선을 보였습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio에 GitHub Copilot harness가 정식 출시

![Introducing a new harness for Copilot Studio](/mwkorea/assets/images/2026-08-04-CopilotStudioGitHubCopilotHarness/image1.png)

지난 두 달간 Copilot Studio에서 **더 복잡한 업무 프로세스를 감당하는 에이전트**를 만들 수 있는 새로운 역량이 프리뷰로 제공되어 왔습니다. 이 역량이 **프로덕션 사용을 위한 정식 공급(GA)** 상태가 되었고, 동시에 정식 명칭이 공개되었습니다.

**GitHub Copilot harness in Copilot Studio**입니다.

이름에서 짐작할 수 있듯, Microsoft의 가장 진보된 에이전트 경험인 **Copilot Cowork**와 **GitHub Copilot 코딩 에이전트**를 움직이는 바로 그 코딩·추론 엔진이 Copilot Studio에 들어왔습니다. 그동안 손이 닿지 않던 종류의 업무 — **단계가 많고, 참조할 소스가 많고, 판단이 모호한 지점이 있는 프로세스** — 를 에이전트가 맡을 수 있게 된다는 뜻입니다.

---

## GitHub Copilot harness란

새 harness는 **길고 복잡한 작업(long-horizon work)**을 위해 설계되었습니다. 사용하는 모델은 최신 프런티어 추론 모델입니다.

| 지원 모델 |
|-----------|
| **Opus 5** |
| **GPT-5.6 Sol** |
| **Fable 5** |

수행 가능한 동작은 다음과 같습니다.

- **계획 수립(plan)**
- 동적인 문제에 대한 **추론(reason)**
- **에이전틱 루프(agentic loop)** 실행
- **Skills** 활용
- **워크플로 통합**
- **다른 플랫폼의 도구·에이전트 연결**
- **다중 구성 요소로 이뤄진 풍부한 산출물** 생성

기존 harness가 "대화에 응답하는" 성격이었다면, 이쪽은 **"프로세스를 끝까지 완주하는"** 성격입니다.

---

## 실제 성능: 자체 벤치마크 수치

Microsoft는 실제 비즈니스 프로세스 평가(evals)를 대상으로 한 자체 테스트 결과를 공개했습니다. 기존 Standard harness와 비교한 수치입니다.

![GitHub Copilot harness vs Standard harness 성능 비교](/mwkorea/assets/images/2026-08-04-CopilotStudioGitHubCopilotHarness/image3.png)

| 평가 항목 | GitHub Copilot harness | Standard harness | 차이 |
|-----------|------------------------|------------------|------|
| **다중 도구 사용(Multi-tool use)** | **98.9%** | 87.0% | +11.9%p |
| **파일 분석(File analysis)** | **91.7%** | 63.5% | +28.2%p |
| **코드 분석(Code analysis)** | **88.1%** | 40.6% | +47.5%p |
| **지식 품질(Knowledge)** | **86.4%** | 66.0% | +20.4%p |

특히 눈에 띄는 것은 **코드 분석에서 40.6% → 88.1%**로 두 배 이상 뛴 부분입니다. 파일 분석도 63.5% → 91.7%로 큰 폭의 개선입니다. 이는 앞서 소개한 **에이전트 샌드박스**(Python 런타임에서 코드를 직접 실행하는 환경)가 GitHub Copilot harness와 함께 동작한다는 점을 생각하면 자연스러운 결과입니다.

> 이 수치는 Microsoft가 자체 평가 세트로 측정한 값이므로, 조직의 실제 시나리오에서는 다르게 나올 수 있습니다. 도입 검토 시에는 **자사 업무로 구성한 eval 세트로 직접 비교**해 보시기를 권합니다.

---

## 메이커를 위한 새 저작 경험

더 유능한 에이전트를 만들 수 있도록 저작 환경도 함께 개선되었습니다.

![새로워진 Copilot Studio 홈 화면 — Agent와 Workflow 생성 진입점](/mwkorea/assets/images/2026-08-04-CopilotStudioGitHubCopilotHarness/image2.png)

홈 화면에서 **Agent**와 **Workflow** 두 가지 생성 경로가 GitHub Copilot 배지와 함께 제시되고, 화면에는 **"Uses Copilot Credits"** 표시가 붙어 있습니다. 하단에는 에이전트별 크레딧 소비량(예: 11,256 credits)이나 `Incl. in license` 표시가 함께 나타나 **비용 가시성**을 제공합니다.

### 에이전트 디자이너

**agent designer**가 더 직관적으로 바뀌었습니다. 가장 중요한 도구들을 바로 손이 닿는 위치에 배치해 저작 속도를 높이면서도, **에이전트 수명 주기 관리(lifecycle management) 기능은 그대로 유지**합니다.

![에이전트 디자이너에서 Skill을 추가하고 미리보기 대화를 시작하는 과정](/mwkorea/assets/images/2026-08-04-CopilotStudioGitHubCopilotHarness/image4.gif)

### 워크플로 디자이너

**workflow designer**는 워크플로를 이해하고 편집할 수 있는 **시각적 캔버스**를 제공합니다. 다음이 가능합니다.

- **에이전트 노드 추가**
- **워크플로 evals 실행**

### 자연어 저작 (예정)

곧 **natural language authoring**이 추가됩니다. **비즈니스 목표를 말로 설명하면**, 다중 턴 대화를 거쳐 적절한 에이전트와 워크플로 조합을 조립해 주는 방식입니다.

---

## 과금 방식: 반드시 확인해야 할 부분

여기가 도입 검토에서 가장 중요한 지점입니다.

> **GitHub Copilot harness에서 실행되는 에이전트는 Microsoft 365 Copilot 라이선스 보유 여부와 관계없이 모든 작업에 사용량 기반 과금(usage-based billing)이 적용됩니다.**

과금액을 결정하는 요소는 세 가지입니다.

| 요소 | 설명 |
|------|------|
| **선택한 모델** | Opus 5 / GPT-5.6 Sol / Fable 5 등 |
| **추가한 조직 컨텍스트와 도구** | Knowledge, Tools, 커넥터 등 |
| **사용한 런타임** | 에이전트가 실제로 돌아간 시간·작업량 |

**주의할 점이 하나 더 있습니다.** 다음과 같은 **AI 기반 메이커 경험도 GitHub Copilot harness로 빌드할 경우 사용량 기반 과금 대상**입니다.

- **자연어 저작(natural language authoring)**
- **평가(evaluations)**
- **테스트(testing)**

즉, **에이전트를 만드는 과정 자체에도 크레딧이 소비**됩니다. 기존에 "만드는 건 무료, 쓰는 건 과금"이라는 감각으로 접근했다면 예산 계획을 다시 세워야 합니다.

---

## 세 개의 harness — 무엇을 골라야 하나

새 harness가 추가되었다고 해서 기존 것이 없어지지는 않습니다. 원문은 **"하나의 만능 접근법에 의존하는 대신, 시나리오에 가장 맞는 harness를 고르는 구조"**로 설명합니다.

현재 Copilot Studio가 지원하는 harness는 **세 가지**입니다.

| harness | 특징 | 적합한 시나리오 |
|---------|------|-----------------|
| **Copilot Chat harness** | Microsoft 365 Copilot Chat과 **동일한 harness** 사용 | Copilot Chat 경험을 커스터마이징할 때 |
| **Standard harness** | 현재 Copilot Studio 에이전트 **대다수가 사용** | 규칙 기반 토픽을 갖는 **대화형 에이전트** |
| **GitHub Copilot harness** | **GitHub Copilot SDK**의 힘을 활용 | 복잡한 **에이전틱 업무 프로세스 자동화** |

### 라이선스·과금 구분

이 부분을 명확히 정리해 두는 것이 중요합니다.

- **Copilot Chat / Standard harness**
  - **Microsoft 365 Copilot 라이선스 사용자**는 라이선스에 포함된 **공정 사용(fair use)** 범위 내에서 계속 이용 가능
  - 그 외 사용은 **기존 고정 요율표(fixed rate card)**로 과금
  - 기존 에이전트와 신규 에이전트 저작 모두 **계속 지원**
- **GitHub Copilot harness**
  - **라이선스와 무관하게 전부 사용량 기반 과금**

---

## 도입 담당자·메이커 체크포인트

**1. 모든 에이전트를 새 harness로 옮길 필요는 없습니다**
FAQ 응답이나 규칙 기반 안내 같은 단순 대화형 에이전트는 Standard harness가 여전히 적합하고, **라이선스 공정 사용 범위 안에서 비용 없이** 운영할 수 있습니다. GitHub Copilot harness는 **"여러 단계·여러 소스·모호한 판단"이 실제로 존재하는 프로세스**에 선택적으로 적용하세요.

**2. 비용 시뮬레이션을 먼저 하세요**
모델·도구·런타임 세 축이 모두 과금에 영향을 줍니다. 파일럿 에이전트 하나를 만들어 실제 크레딧 소비량을 측정한 뒤 전사 확산 규모를 산정하는 순서를 권합니다. 앞서 7월 업데이트에서 **지출 정책(spending policy)과 알림 기능이 개선**되었으므로 함께 설정해 두면 좋습니다.

**3. 저작 단계 과금을 팀에 공지하세요**
자연어 저작·평가·테스트가 과금 대상이라는 점을 메이커 팀이 모르면, 반복 테스트만으로도 예상치 못한 크레딧 소비가 발생할 수 있습니다.

**4. eval을 먼저 준비하세요**
harness 전환의 효과를 주장하려면 비교 기준이 필요합니다. 워크플로 디자이너에서 **워크플로 evals 실행**이 가능해졌으므로, 자사 업무로 구성한 평가 세트를 만들어 Standard 대비 개선폭을 직접 측정하는 것이 가장 설득력 있는 접근입니다.

**5. harness 선택을 아키텍처 결정으로 다루세요**
과금 모델, 지원 모델, 실행 능력이 모두 다릅니다. "어떤 harness를 쓸 것인가"는 도구 선택이 아니라 **비용 구조와 운영 방식을 결정하는 아키텍처 판단**입니다. 사내 가이드에 시나리오별 권장 harness를 정리해 두면 메이커들의 혼선을 줄일 수 있습니다.

---

## 시작하기

**GitHub Copilot harness는 지금 정식 공급 상태**이며, **Copilot Studio 홈페이지에서 바로** 해당 에이전트를 만들 수 있습니다.

Microsoft는 제품 우측 상단의 피드백 컨트롤을 통한 의견 제출을 권하고 있습니다.

---

## 마무리

Copilot Studio가 harness를 세 개로 나눈 것은 단순한 기능 추가가 아니라 **제품 전략의 분화**로 읽힙니다.

- **대화를 잘하는 에이전트**는 Standard harness로, 라이선스 안에서
- **Copilot Chat을 확장하는 에이전트**는 Copilot Chat harness로
- **일을 끝까지 완주하는 에이전트**는 GitHub Copilot harness로, 사용량 기반 과금으로

코드 분석 40.6% → 88.1%라는 수치가 보여 주듯, 세 번째 선택지는 **성능의 차원이 다릅니다.** 다만 그 성능에는 **명확한 비용이 따라붙습니다.**

따라서 지금 메이커에게 필요한 질문은 "새 harness를 쓸 것인가"가 아니라, **"우리 업무 중 어떤 것이 이 비용을 지불할 만한 복잡도를 가졌는가"**입니다. 그 판단을 위한 첫 단계는 파일럿 하나와 eval 세트 하나를 만드는 것입니다.

---

> **출처**: *More powerful agents and workflows for autonomous business processes: Introducing a new harness for Copilot Studio* — Microsoft Tech Community, Microsoft Copilot Studio Blog
> - 원문: [https://techcommunity.microsoft.com/t5/copilot-studio-blog/more-powerful-agents-and-workflows-for-autonomous-business/ba-p/4542969](https://techcommunity.microsoft.com/t5/copilot-studio-blog/more-powerful-agents-and-workflows-for-autonomous-business/ba-p/4542969)
> - 참고: [Copilot Studio 사용량 기반 과금 안내](https://aka.ms/CopilotCredits/LicensingGuide) · [워크플로 디자이너 문서](https://learn.microsoft.com/en-us/microsoft-copilot-studio/workflows-experience/flow-designer)
>
> 자세한 내용은 원문 참조.
