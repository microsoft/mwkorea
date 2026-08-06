---
title: "Agent 365 2026년 7월 업데이트 — 파트너 위험 신호, 비용 관리, 멀티테넌트까지"
date: 2026-08-04T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent365
  - AgentGovernance
  - EntraAgentID
  - CostManagement
  - MultiTenant
  - RegistrySync
excerpt: "Microsoft Agent 365의 2026년 7월 업데이트가 공개됐습니다. Darktrace·Cyera·Zenity 파트너 위험 신호 통합, Copilot Credit 비용 관리 강화, 조직 전체 도입 대시보드 GA, 타 플랫폼 에이전트를 끌어오는 Registry sync GA, 멀티테넌트 관리 공개 미리 보기가 핵심입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Agent 365 2026년 7월 업데이트 — 파트너 위험 신호, 비용 관리, 멀티테넌트까지

조직에 에이전트가 하나둘 늘어나기 시작하면, 처음에는 즐겁습니다. 그런데 어느 시점이 되면 질문이 바뀝니다. "누가 만든 에이전트가 몇 개나 돌고 있죠?", "이 에이전트는 어떤 데이터에 접근하나요?", "이번 달 크레딧은 왜 이렇게 나왔나요?"

여러 테넌트, 여러 에이전트 플랫폼, 여러 부서에 에이전트가 흩어지기 시작하면 가시성과 통제는 급격히 어려워집니다. **Microsoft Agent 365**는 바로 이 문제를 다루는 엔터프라이즈 컨트롤 플레인이며, 2026년 7월 업데이트가 공개됐습니다.

이번 업데이트의 다섯 축은 **파트너 위험 신호 통합**, **사용량 기반 AI 비용 관리**, **조직 전체 도입 인사이트**, **타 플랫폼 에이전트 탐색·거버넌스 확장**, **멀티테넌트 중앙 관리**입니다. 하나씩 정리해 드립니다.

![Agent 365 2026년 7월 업데이트](/mwkorea/assets/images/2026-08-04-Agent365WhatsNewJuly2026/image1.png)

---

## 1. Darktrace·Cyera·Zenity — 파트너 위험 신호를 Agent Registry로

에이전트가 업무 핵심에 들어올수록, IT·보안 팀은 ID·데이터·위협 활동에 걸친 위험 신호를 확인하기 위해 여러 포털을 오가야 했습니다. 이 파편화된 시야는 에이전트의 **전체 위험 프로필**을 파악하기 어렵게 만듭니다.

Agent 365는 Microsoft Entra, Defender, Purview의 네이티브 신호를 이미 **Agent Details의 Security 탭**에 모아 보여 주고 있었습니다. 이번 업데이트로 **서드파티 보안 솔루션의 위험 신호까지** Agent Registry에 들어옵니다. 시작은 **Darktrace, Cyera, Zenity** 세 곳입니다.

> "Microsoft는 Agent 365의 약속으로서 업계에서 가장 신뢰할 수 있고 포괄적인 AI 거버넌스·보안 경험을 제공하는 데 전념하고 있습니다. 보안 생태계 파트너와의 통합을 통해 고객은 기존 보안 투자 가치를 극대화하면서 에이전트 생태계 전반의 위험 신호를 통합적으로 볼 수 있습니다."
> — Nirav Shah, CVP, Agent 365 and Agent Cloud

### 어떻게 연결되나

핵심 연결고리는 **Microsoft Entra Agent ID**입니다. 관리자가 기능을 활성화하면, Agent 365가 파트너가 생성한 위험 신호를 받아 Entra Agent ID를 기준으로 **해당 에이전트 레코드에 정확히 매칭**합니다. 즉 Entra Agent ID가 신원 앵커(identity anchor) 역할을 하며, 거버넌스 워크플로의 중심은 Agent 365에 그대로 유지됩니다.

![Agent Registry의 파트너 위험 신호](/mwkorea/assets/images/2026-08-04-Agent365WhatsNewJuly2026/image2.png)

### 관리자가 얻는 것

- **통합된 단일 뷰(One consolidated view)** — Entra·Defender·Purview의 네이티브 신호와 지원되는 파트너 솔루션의 탐지를 하나의 에이전트 위험 신호 카운트로 묶어, 주의가 필요한 에이전트를 빠르게 식별합니다.
- **위험 우선순위(Risk prioritization)** — 위험 신호를 **High / Medium / Low**로 분류하고, 각 위험 신호 유형별 **발생 횟수**를 함께 표시합니다. 반복 패턴을 찾아 조사·조치로 연결할 수 있습니다.
- **동의 기반 설계(Consent by design)** — 파트너 통합은 **선택 사항**이며, 관리자가 **Microsoft 365 관리 센터 > Agents > Settings**에서 파트너 위험 신호를 활성화하기 전까지는 **어떤 파트너 데이터도 흐르지 않습니다.** 일부 파트너는 자사 제품에서의 추가 설정도 요구할 수 있습니다.

> "Darktrace / SECURE AI의 행동 기반 접근은 AI 에이전트가 어떻게 동작하고 그 행위가 사람·데이터·인프라와 어떻게 연결되는지에 대한 조직별 고유한 이해를 만들어 냅니다."
> — Ed Jennings, President and CEO, Darktrace

> "Cyera Agent Guardian의 데이터 위험 신호를 Agent Registry로 가져오면서, Agent 365는 Microsoft 네이티브 신호와 데이터 컨텍스트를 결합한 하나의 통합 뷰를 제공합니다."
> — Tamar Bar-Ilan, Co-Founder & CTO, Cyera

> "AI 에이전트는 이제 모든 기업의 현실입니다. 파일럿으로 시작한 것이 전사 규모 배포가 되고 있으며, 깊이 있는 보안 축 없이는 불가능합니다."
> — Ben Kliger, CEO of Zenity

이 신호를 실어 나르는 **Agent 365 파트너 API**는 생태계 전반의 보안 벤더에게 열려 있으며, 지원 제공사 목록은 앞으로 확대될 예정입니다.

---

## 2. Cost Management — 에이전트 AI 비용에 예측 가능성 부여

에이전트 사용이 늘면 **소비량 파악, 예산 관리, 사용량 기반 비용의 예측 가능성**이 과제가 됩니다. Microsoft 365 관리 센터의 **Cost Management**는 사용량 기반 에이전트 서비스의 **Copilot Credit** 지출을 중앙에서 모니터링·통제하는 기능이며, 이번 릴리스는 **Cowork와 Work IQ 지출**에 초점을 맞춥니다.

주요 개선 사항은 다음과 같습니다.

- **지출 알림 신뢰성 향상**
- **정책 할당 일관성 개선**
- **사용자별 초과분(per-user overage) 처리 강화**
- **Microsoft 365 및 Power Platform 관리 경험 전반의 선불 용량(prepaid capacity) 가시성 향상**

### 정책 충돌 시 선택 기준이 명확해집니다

한 사용자가 **동일 서비스에 대해 여러 지출 정책에 속해 있을 때**, 적용 정책은 이제 명확한 기준으로 선택됩니다.

1. **사용자별 한도가 가장 높은 정책**
2. 동률이면 **전체 정책 한도가 가장 큰 정책**
3. 그래도 동률이면 **가장 최근에 생성된 정책**

선택된 정책은 **전부 그대로 적용**됩니다. 여러 정책의 설정이 뒤섞이지 않으므로, 관리자가 각 사용자에게 어떤 과금 구성과 한도가 적용될지 예측할 수 있습니다.

### 실행 중인 작업의 초과분 보호

작업이 이미 실행 중인 상태에서 사용자의 개인 한도를 초과하는 경우, Microsoft는 해당 작업을 **끝까지 완료하도록 허용하되, 그로 인해 발생한 사용자별 초과분을 정책의 공유 풀에서 차감하거나 청구하지 않을 수 있습니다.** 나머지 구성원을 위한 크레딧을 보호하기 위한 조치입니다.

### 용량 팩 크레딧의 정확한 표시

Cost Management는 **다른 관리 센터를 통해 이미 소비되거나 할당된 크레딧**(예: Power Platform 환경이나 에이전트에 할당된 용량)을 구분합니다. 따라서 지출 정책 설정 시 표시되는 금액이 **실제 남아 있는 선불 용량**에 더 가깝게 반영됩니다.

![Cost Management](/mwkorea/assets/images/2026-08-04-Agent365WhatsNewJuly2026/image3.png)

---

## 3. Agent 365 Dashboard — 조직 전체 도입 인사이트 (GA)

**Agent 365 대시보드가 정식 출시(GA)**되었습니다. 비즈니스 리더에게 조직 전반의 **에이전트 도입, 참여도, 비즈니스 임팩트**를 하나의 화면으로 제공합니다.

- Agent 365의 텔레메트리를 **단일 리포팅 경험**으로 통합
- 에이전트가 실제로 어떻게 쓰이는지, **도입이 가속되는 곳과 정체된 곳**을 식별
- AI 투자, 배포 전략, 변화 관리에 대한 근거 기반 의사결정 지원

분석가는 **팀·사업부·지역별 필터링**으로 사용 현황을 평가할 수 있고, 리더는 **활성 사용자 수, 리텐션 추이, 성과가 좋은 상위 에이전트, 전반적 참여 패턴** 같은 핵심 지표를 모니터링할 수 있습니다. **인터랙티브 드릴다운**으로 개별 에이전트 성능까지 파고들 수 있어, 성공적인 배포를 찾아내고 최적화 기회를 발굴하며 가장 큰 가치를 내는 에이전트에 투자를 집중할 수 있습니다.

![Agent 365 Dashboard](/mwkorea/assets/images/2026-08-04-Agent365WhatsNewJuly2026/image4.png)

---

## 4. Registry sync — 타 플랫폼 에이전트까지 한곳에서 (GA)

이번 업데이트에서 가장 눈에 띄는 항목일 수 있습니다. **Registry sync가 정식 출시(GA)**되어, **Microsoft 플랫폼 밖에 존재하는 에이전트까지 탐색·인벤토리화**할 수 있게 됐습니다.

AI 관리자가 지원되는 생태계 에이전트 플랫폼을 안전하게 연결하면, 에이전트와 메타데이터가 **일 단위 또는 주 단위 주기**로 Agent 365 레지스트리에 동기화됩니다. 이로써 에이전트 자산 전체에 대한 **단일 권위 있는 기록 시스템(system of record)**이 만들어집니다.

### GA 시점 지원 플랫폼

| 구분 | 플랫폼 |
|---|---|
| GA 시점 지원 | Amazon Bedrock, Google Cloud Gemini Enterprise Agent Platform, Anthropic Claude, Databricks Genie, Salesforce Agentforce |
| 곧 지원 예정 | Snowflake, Oracle OCI, UIPath |

### 가시성을 넘어 거버넌스까지

Registry sync는 단순 조회에 그치지 않습니다. **기반 플랫폼 API가 지원하는 범위 내에서**, 관리자는 Agent 365에서 직접 에이전트 수준의 거버넌스 조치를 취할 수 있습니다. 여기에는 **동기화된 에이전트 삭제** 같은 수명 주기 관리 작업이 포함됩니다.

즉 개발·런타임 환경은 각 업무에 가장 적합한 플랫폼을 계속 사용하면서, **관리 평면은 하나로 통일**하는 구조입니다. Microsoft가 만든 에이전트든, 사내에서 개발한 에이전트든, 생태계 플랫폼에서 만든 에이전트든 조직 전체를 한눈에 볼 수 있게 됩니다.

![Registry sync](/mwkorea/assets/images/2026-08-04-Agent365WhatsNewJuly2026/image5.png)

---

## 5. 멀티테넌트 에이전트 관리 (공개 미리 보기)

여러 고객사를 지원하는 파트너와 복잡한 멀티테넌트 환경을 운영하는 기업 모두, 일관된 가시성과 통제가 필요합니다. **멀티테넌트 에이전트 관리가 공개 미리 보기(public preview)**로 제공됩니다. 관리자는 Microsoft 365 관리 센터의 Agent 365에서 **연결된 테넌트 전반의 에이전트를 중앙에서 조회·관리**할 수 있습니다.

**All tenants > Agents**에서 가능한 작업은 다음과 같습니다.

- 통합된 에이전트 인벤토리 조회
- 사용자 지정 에이전트 추가
- 선택한 테넌트들에 에이전트 배포
- 테넌트별 가용성·권한 비교
- 에이전트 위험 및 활동 검토
- 필요 시 에이전트 차단 또는 가용성 변경

또한 **테넌트 전환기(tenant switcher)**를 사용해 **위임된 액세스(delegated access)**로 연결된 테넌트에 진입할 수 있습니다. 해당 테넌트에 별도 관리자 계정을 유지할 필요가 없습니다. 적용 가능한 라이선스 요건을 충족하면 에이전트 위험 검토도 가능합니다.

### 전제 조건

이 기능은 기존 **교차 테넌트 관리 관계**와 **GDAP(Granular Delegated Admin Privileges)** 위에서 동작합니다.

- **파트너**: Partner Center에서 관계를 구성
- **기업**: Microsoft Entra Tenant Governance를 통해 구성

사용 가능한 테넌트와 관리 작업은 **활성 테넌트 관계와 관리자의 위임된 역할**에 따라 결정됩니다.

시작하려면 먼저 **테넌트 관계와 위임 역할 할당을 점검**한 뒤, MS Learn 문서에서 전제 조건·지원 역할·기능·라이선스 세부 사항을 확인하시기 바랍니다.

![멀티테넌트 에이전트 관리](/mwkorea/assets/images/2026-08-04-Agent365WhatsNewJuly2026/image6.png)

---

## 한국 고객을 위한 체크포인트

- **Entra Agent ID 정비가 선행 조건입니다.** 파트너 위험 신호 매칭의 기준이 Entra Agent ID이므로, 에이전트 ID 체계가 정리되어 있지 않으면 통합의 효과가 반감됩니다.
- **파트너 통합은 옵트인입니다.** 관리자가 명시적으로 켜기 전까지 파트너 데이터가 흐르지 않습니다. 이미 Darktrace·Cyera·Zenity를 사용 중이라면 기존 보안 투자를 그대로 살릴 수 있는 경로입니다.
- **비용 정책 중복을 지금 점검하세요.** 정책 선택 기준(사용자별 한도 → 전체 한도 → 최신 생성 순)이 명확해진 만큼, 현재 사용자들이 여러 정책에 중복 소속되어 있지 않은지 확인해 두시면 예산 예측이 쉬워집니다.
- **멀티클라우드 에이전트 현황부터 파악하세요.** Registry sync가 Bedrock·Gemini·Claude·Databricks·Agentforce를 지원하므로, 사업부별로 다른 플랫폼을 쓰고 있는 조직이라면 실제 에이전트 자산 규모를 처음으로 정확히 셀 수 있는 기회입니다.
- **파트너·MSP는 GDAP 관계 점검이 먼저입니다.** 멀티테넌트 관리는 기존 GDAP 위에 얹히는 구조이므로, Partner Center의 위임 관계 정비 없이는 사용할 수 없습니다.

---

## 시작하기

- [Microsoft 365 관리 센터에서 Agent 365 시작하기](https://admin.cloud.microsoft/)
- MS Learn의 Agent 365 문서에서 전제 조건, 지원 역할, 기능, 라이선스 세부 사항 확인

---

## 마무리

2026년 7월 업데이트를 관통하는 메시지는 분명합니다. Agent 365는 **"Microsoft 에이전트를 관리하는 도구"에서 "조직의 모든 에이전트를 관리하는 컨트롤 플레인"으로** 범위를 넓히고 있습니다. 서드파티 보안 신호를 받아들이고, 경쟁 플랫폼의 에이전트를 레지스트리에 담고, 여러 테넌트를 한 화면에서 관리하는 방향입니다.

에이전트가 파일럿 단계를 넘어 전사 확산으로 가고 있는 조직이라면, 지금이 **에이전트 자산 인벤토리와 거버넌스 체계를 세울 시점**입니다.

---

> **출처**: [*What's new in Agent 365 – July 2026*](https://techcommunity.microsoft.com/t5/agent-365-blog/what-s-new-in-agent-365-july-2026/ba-p/4543654) (Microsoft Tech Community, Agent 365 Blog — By Alex Pozin and Samer Baroudi)
>
> 자세한 내용은 원문 참조.
