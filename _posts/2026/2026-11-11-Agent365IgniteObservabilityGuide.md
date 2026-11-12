---
title: "Ignite 2026에서 읽는 Agent 365의 다음 방향: 에이전트 관리에서 AI 관측·보안·비용까지"
date: 2026-11-11T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent365
  - MicrosoftIgnite
  - Observability
  - AgentGovernance
  - Security
  - FinOps
excerpt: "Microsoft가 Ignite 2026에서 Agent 365를 살펴볼 수 있는 역할별 세션 가이드를 공개했습니다. 에이전트 거버넌스와 보안, AI 비용·가치 측정이라는 세 축을 한국 시간 일정과 함께 정리합니다. 행사 예고에 담긴 방향성과 실제 기능의 출시 여부는 구분해 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Ignite 2026에서 읽는 Agent 365의 다음 방향: 에이전트 관리에서 AI 관측·보안·비용까지

Copilot과 에이전트를 도입한 뒤에는 새로운 질문이 생깁니다. 우리 조직에 어떤 에이전트가 있는지, 누가 책임지는지, 어떤 데이터와 도구에 접근하는지, 비용에 비해 실제 성과가 있는지를 함께 알아야 합니다. 개별 에이전트의 답변 품질만으로는 조직 전체의 운영 상태를 설명하기 어렵습니다.

Microsoft는 미국 시각 2026년 11월 10일 공개한 **Microsoft Ignite 2026: Your Guide to Agent 365**에서 이 문제를 다룰 행사 세션을 소개했습니다. 원문은 Agent 365의 방향을 에이전트 제어 평면인 *agentic control plane*에서 **AI observability platform**, 즉 AI의 사용과 동작·위험·성과를 관측하는 플랫폼으로 확장하는 것으로 설명합니다.

이번 글은 **행사 사전 안내**를 한국 독자의 관점에서 풀어 쓴 것입니다. 세션에서 다룰 주제나 시연 예고를 모든 테넌트에 이미 제공되는 기능으로 해석해서는 안 됩니다. 원문은 세부 기능별 GA·프리뷰 여부, 라이선스, 가격, 지역별 제공 조건을 확정하는 출시 문서가 아닙니다.

---

## 먼저 볼 두 세션: 무엇을 운영하고, 무엇을 관측할 것인가

Agent 365는 지난해 Ignite에서 빠르게 늘어나는 에이전트를 파악하고 통제하며 보호하기 위한 목표로 소개됐습니다. 올해 안내에서는 관측 범위를 에이전트뿐 아니라 **모델과 어시스턴트**까지 연결하고, 거버넌스·보안·재무 가시성을 함께 강조합니다.

| 세션 | 미국 태평양 시각(PT) | 한국 시각(KST) | 살펴볼 내용 |
|---|---|---|---|
| KEY01: Microsoft Ignite opening keynote | 11월 17일 10:00 | 11월 18일 03:00 | 에이전트·모델·어시스턴트의 관측 계층으로서 Agent 365의 방향 |
| [INV642: Observability at every layer of the stack](https://ignite.microsoft.com/en-US/sessions/INV642) | 11월 18일 14:00 | 11월 19일 07:00 | AI 사용 위치, 에이전트 동작, 새롭게 나타나는 위험, 투자 성과를 스택 전반에서 파악하는 접근 |

아래 일정은 원문의 행사 일정에 맞춰 정리했습니다. 11월 행사 기간의 PT는 PST(UTC−8)이므로 KST는 **17시간을 더한 시각**입니다. 행사 일정은 변경될 수 있으므로 최종 시간과 시청 방식은 [세션 카탈로그](https://ignite.microsoft.com/en-US/sessions)에서 확인하세요.

## IT 운영·거버넌스: 에이전트뿐 아니라 도구와 수명주기도 관리

IT 트랙의 핵심은 Microsoft 및 비 Microsoft 에이전트를 하나의 관리 관점에서 보고, 소유자를 지정하고, 정책과 수명주기를 관리하는 것입니다. 특히 **MCP 서버·플러그인·스킬**도 통제 대상으로 다룬다는 점이 메이커와 개발자에게 중요합니다.

### 온라인으로 볼 수 있는 브레이크아웃

| 세션 | PT / KST | 핵심 내용 |
|---|---|---|
| [BRK214: Manage and Secure your AI Agents at Enterprise Scale with Agent 365](https://ignite.microsoft.com/en-US/sessions/BRK214) | 11/18 16:15–17:00 / 11/19 09:15–10:00 | 플랫폼 전반의 중앙 가시성, 거버넌스, 보안으로 에이전트를 확장하면서 신뢰·규정 준수·운영 통제를 유지하는 방법 |
| [BRK345: Master Agent Governance with Agent 365](https://ignite.microsoft.com/en-US/sessions/BRK345) | 11/19 17:15–18:00 / 11/20 10:15–11:00 | 에이전트·소유자·접근·정책·도구·수명주기 통제를 중앙화하는 실무 사례와 데모 |

### 현장 참여형 세션

| 세션 | PT / KST | 핵심 내용 |
|---|---|---|
| [LTG1172: How Microsoft is Scaling Thousands of AI Agents with Agent 365](https://ignite.microsoft.com/en-US/sessions/LTG1172) | 11/17 14:00–14:15 / 11/18 07:00–07:15 | Microsoft 내부의 대규모 에이전트 관측·거버넌스·보안 경험 |
| [THR854: Monday morning triage: from Shadow AI to Governed AI in minutes](https://ignite.microsoft.com/en-US/sessions/THR854) | 11/17 14:00–14:25 / 11/18 07:00–07:25 | 비관리 에이전트를 찾아 고위험 항목은 Intune 정책으로 차단하고, 정당한 도구는 관리 레지스트리에 편입하는 라이브 데모 |
| [TT1650: IT Strategies for Agent Observability and Governance with Agent 365](https://ignite.microsoft.com/en-US/sessions/TT1650) | 11/17 14:00–14:45 / 11/18 07:00–07:45 | 에이전트 발견, 활동 파악, 위험 평가, 대규모 관리에 관한 전문가·동료 토론 |
| [LTG1171: Getting Started with Agent 365: Setting Up Your Agent Control Plane](https://ignite.microsoft.com/en-US/sessions/LTG1171) | 11/18 13:45–14:00 / 11/19 06:45–07:00 | 이미 실행 중인 에이전트를 발견하고 확산을 통제하는 초기 설정 |
| [LTG1238: Agent 365 in Action: Managing MCP Servers, Plugins, and Skills for AI Agents](https://ignite.microsoft.com/en-US/sessions/LTG1238) | 11/19 11:00–11:15 / 11/20 04:00–04:15 | 도구 발견·등록·거버넌스, 비승인 도구 차단, 승인 사용자에 대한 세분화된 접근 통제 |

한국 기업의 도입 담당자는 에이전트 목록에 이름만 기록하기보다 **업무 소유자, 호출 도구, 접근 데이터, 운영 종료 조건**을 함께 정리해 두면 세션 내용을 실제 운영 기준에 연결하기 쉽습니다. 이는 원문의 기능 출시 약속이 아니라, 소개된 거버넌스 주제를 적용하기 위한 준비 제안입니다.

## 보안: 에이전트의 신원과 권한부터 로컬 실행까지

원문은 에이전트가 데이터·애플리케이션·시스템에 접근할수록 보안도 에이전트 환경 전체로 확장돼야 한다고 설명합니다. 에이전트 유형 발견, 신원 부여, 최소 권한 적용, 데이터 보호, 위협 대응을 따로 떼지 않고 함께 보는 접근입니다.

| 온라인·현장 브레이크아웃 | PT / KST | 핵심 내용 |
|---|---|---|
| [BRK336: When AI acts, security has to answer: Microsoft Security for AI](https://ignite.microsoft.com/en-US/sessions/BRK336) | 11/17 14:00–14:45 / 11/18 07:00–07:45 | 앱·에이전트 보호, 접근·데이터 거버넌스, 네트워크 통제, 위험 식별과 위협 억제 |
| [BRK212: Secure the Follow-Through: Trusting Autopilot at Scale](https://ignite.microsoft.com/en-US/sessions/BRK212) | 11/18 15:00–15:45 / 11/19 08:00–08:45 | Autopilot의 접근·행동 보호, 민감 데이터 보호, 컴퓨터·앱·네트워크 전반의 활동 통제 |
| [BRK341: Inside Look at Agent 365: Lessons from Microsoft’s Office of the CISO](https://ignite.microsoft.com/en-US/sessions/BRK341) | 11/19 11:30–12:15 / 11/20 04:30–05:15 | Microsoft Office of the CISO의 에이전트 보안·거버넌스 경험 |
| [BRK339: Local agents are here. Can you find and secure them?](https://ignite.microsoft.com/en-US/sessions/BRK339) | 11/19 16:00–16:45 / 11/20 09:00–09:45 | 신뢰할 수 있는 도입을 방해하지 않으면서 로컬 에이전트를 발견하고 보호하는 방법 |

| 현장 참여형 세션 | PT / KST | 핵심 내용 |
|---|---|---|
| [THR877: AI agents: Access granted. Trust not included](https://ignite.microsoft.com/en-US/sessions/THR877) | 11/17 16:05–16:30 / 11/18 09:05–09:30 | Microsoft Entra Agent ID를 이용한 앱·데이터 연결과 최소 권한 |
| [LTG1237: Govern & protect local agents for safe access enterprise resources](https://ignite.microsoft.com/en-US/sessions/LTG1237) | 11/18 09:25–09:40 / 11/19 02:25–02:40 | Windows와 Microsoft Security를 통한 로컬 에이전트 발견·모니터링·보호 및 위험 행동 대응 |
| [TT2532: Securing AI Agents: A candid conversation with the experts](https://ignite.microsoft.com/en-US/sessions/TT2532) | 11/18 14:25–15:10 / 11/19 07:25–08:10 | 데이터·신원·런타임 전반의 에이전트 위험을 식별하고 완화하는 전문가 토론 |
| [THR857: Secure, Govern, and Scale: Protecting Microsoft Copilot and AI Agents](https://ignite.microsoft.com/en-US/sessions/THR857) | 11/19 17:30–17:55 / 11/20 10:30–10:55 | Microsoft 보안 통제로 Copilot과 에이전트를 보호하는 데모 |

메이커와 개발자는 “에이전트가 어떤 답변을 하는가” 외에도 **누구의 신원으로 실행되는지, 어떤 도구를 호출하는지, 민감 정보에 접근하는지, 위험 행동을 누가 확인하는지**를 질문 목록에 넣어 보세요. 원문에는 구체적인 설정 절차나 라이선스 전제조건이 없으므로 실제 적용 단계에서는 각 세션의 후속 문서와 테넌트 조건을 별도로 확인해야 합니다.

## 비즈니스 가치: AI 비용을 보는 것에서 성과를 판단하는 것으로

비즈니스 트랙은 사업 책임자, 재무 담당자, IT 예산 담당자를 대상으로 합니다. 공급업체별 소비 현황, 예산 가드레일, 비용 최적화, 가치 측정이 주요 주제입니다. 에이전트를 몇 개 만들었는지보다 **어떤 투자에 예산을 더 배분할 것인지**가 중요해지는 단계입니다.

| 온라인·현장 브레이크아웃 | PT / KST | 핵심 내용 |
|---|---|---|
| [BRK263: Master AI spend management with Agent 365: Govern your AI budget](https://ignite.microsoft.com/en-US/sessions/BRK263) | 11/19 09:00–09:45 / 11/20 02:00–02:45 | Agent 365와 Microsoft 365 관리 센터를 통한 예산 가드레일, 공급업체 간 소비 모니터링, 가치 측정과 지출 최적화 |
| [BRK266: Maximize your Copilot Investment: Scale with flexibility and control](https://ignite.microsoft.com/en-US/sessions/BRK266) | 11/19 10:15–11:00 / 11/20 03:15–04:00 | AI 지출 통제, 비즈니스 가치 측정, 예산에 맞춘 투자 최적화 |
| [BRK260: The next evolution of AI FinOps: From cost to value](https://ignite.microsoft.com/en-US/sessions/BRK260) | 11/19 16:00–16:45 / 11/20 09:00–09:45 | 지출 가시성에서 비용 최적화·가치 측정으로 넘어가 성과가 있는 이니셔티브를 확장하는 방법 |

| 현장 참여형 세션 | PT / KST | 핵심 내용 |
|---|---|---|
| [THR865: Navigating AI spend across your organization](https://ignite.microsoft.com/en-US/sessions/THR865) | 11/17 14:00–14:25 / 11/18 07:00–07:25 | 조직 전반의 AI 지출을 이해하는 데모 |
| [LTG1165: Preparing for usage-based billing](https://ignite.microsoft.com/en-US/sessions/LTG1165) | 11/17 15:35–15:50 / 11/18 08:35–08:50 | 가시성·거버넌스·예측·최적화·유연한 구매로 사용량 기반 과금에 대비하는 접근 |
| [LTG1170: AI That Pays Off: New Ways to Measure Value and Optimize Spend](https://ignite.microsoft.com/en-US/sessions/LTG1170) | 11/18 14:10–14:25 / 11/19 07:10–07:25 | AI 사용량·지출·비즈니스 영향을 연결하는 제품 내 ROI 보고와 최적화·확장 판단 |

여기서 ROI 보고와 사용량 기반 과금은 **행사에서 소개할 주제**입니다. 이 안내만으로 새 과금 정책의 적용일이나 구체적인 요금을 단정할 수는 없습니다. 국내 도입팀은 업무별 사용량과 지출, 성과 측정 지표를 어떤 기준으로 연결할지 미리 합의하는 데 초점을 맞추면 좋겠습니다.

## 한국에서 온라인으로 참여할 때의 체크포인트

원문은 **브레이크아웃 세션은 현장·온라인 라이브·주문형으로 제공**하고, Lightning Talk·Theater·Table Talk는 **현장 참여형**이라고 구분합니다. 위 표의 현장 세션을 온라인으로 모두 볼 수 있다고 가정하지 마세요. 한국에서 참여한다면 키노트와 브레이크아웃을 먼저 일정에 넣는 편이 현실적입니다.

미국 현지 11월 17일부터 19일까지는 **Live at Microsoft Ignite**에서도 Agent 365 관련 대화를 진행할 예정입니다. 원문은 “Bringing agentic defense to secure your agents”, “Agent 365: A year of learning, a future of opportunity” 및 대규모 AI 운영에서 FinOps가 핵심 분야가 되는 이유를 다루는 대화를 안내합니다. 개별 방송 시각은 원문에 명시되지 않았습니다.

샌프란시스코 현장 참가자는 화요일부터 목요일까지 운영되는 Hub의 Agent 365 구역에서 IT 관리, 보안, 성능·비용, 개발자·파트너 생태계 연결이라는 역할별 데모와 전문가 상담을 살펴볼 수 있습니다.

원문에는 세션에서 보여줄 **라이브 데모에 대한 설명과 세션 링크**가 있지만, 이 글에 바로 삽입할 실제 영상 iframe이나 개별 데모 영상 URL은 없습니다. 행사 후 공개되는 주문형 콘텐츠는 공식 카탈로그에서 확인하세요.

## 시작하기와 마무리

1. [Microsoft Ignite 등록 페이지](https://ignite.microsoft.com/en-US/home)와 [세션 카탈로그](https://ignite.microsoft.com/en-US/sessions)에서 참여 방식과 최종 일정을 확인합니다.
2. IT 담당자는 BRK214·BRK345, 보안 담당자는 BRK336·BRK341, 예산 담당자는 BRK263·BRK260을 중심으로 역할에 맞는 동선을 구성합니다.
3. [FinOps for AI 세션 가이드](https://techcommunity.microsoft.com/blog/finopsblog/your-guide-to-finops-for-ai-at-microsoft-ignite-2026/4569117)와 [Security for AI 세션 안내](https://aka.ms/SecureAIAtIgnite2026)를 함께 확인합니다.
4. 행사 후 실제 기능별 제공 상태와 전제조건을 확인한 다음, 소유권·도구 접근·보안·예산 운영 기준에 반영합니다.

이번 안내의 메시지는 에이전트를 만드는 일을 넘어 **조직이 AI를 어떻게 운영할 것인가**입니다. IT·보안·재무가 같은 에이전트 환경을 공통 데이터로 바라본다는 방향을 읽되, 행사 예고와 검증된 제품 제공 조건을 구분하는 것이 도입 준비의 출발점입니다.

> **출처**: [Microsoft Ignite 2026: Your Guide to Agent 365](https://techcommunity.microsoft.com/t5/agent-365-blog/microsoft-ignite-2026-your-guide-to-agent-365/ba-p/4571750) — Microsoft Tech Community, Agent 365 Blog. 원문 발행: 2026년 11월 10일 17:00 UTC(한국 시각 11월 11일 02:00). 자세한 내용은 원문 참조.
