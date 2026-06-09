---
title: "[긴급 편성] Copilot Studio 대규모 업데이트 총정리 — 재구축, 새 에이전트 경험, 그리고 5월 신기능까지"
date: 2026-06-10T10:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Agent
  - Orchestrator
  - Workflow
  - ClassicVsNew
  - ComputerUse
  - Voice
  - WorkIQ
  - MCP
excerpt: "Copilot Studio가 처음부터 재설계되어 전 세계 정식 출시(GA)되었고, 자연어 지시 기반의 '새 에이전트 경험'이 공개 미리 보기로 등장했습니다. 새 agentic 오케스트레이터, 9→4개 구성 탭, 스킬·새 워크플로 디자이너·MCP, Classic vs New 비교, 그리고 컴퓨터 사용 에이전트 GA·실시간 음성·Work IQ A2A까지 — 한 편에 모두 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# [긴급 편성] Copilot Studio 대규모 업데이트 총정리

에이전트를 만들다 보면 늘 같은 벽에 부딪힙니다. "단순한 한두 단계는 잘 되는데, 여러 단계가 얽힌 실제 업무를 맡기면 중간에 흐름이 끊긴다"는 것이죠. Microsoft가 고객들로부터 가장 많이 들어온 피드백도 바로 이 지점이었습니다 — 더 유능한 에이전트, 자연스럽게 함께 작동하는 워크플로, 그리고 끝까지 무너지지 않고 다단계 작업을 수행하는 안정성.

그 피드백을 바탕으로 Microsoft는 **Copilot Studio를 처음부터 다시 설계(rebuilt)** 했고, 이 업데이트는 **전 세계 정식 출시(GA)** 되었습니다. 동시에 토픽·플로 대신 **자연어 지시로 만드는 '새 에이전트 경험(New agent experience)'** 이 공개 미리 보기로 등장했고, 같은 흐름에서 **컴퓨터 사용 에이전트 GA·새 워크플로·실시간 음성·Work IQ 상호운용성** 까지 함께 발표됐습니다.

이번 긴급 편성은 이 모든 변화를 **한 편에 묶어** 정리합니다. 도입을 검토하는 메이커·IT 담당자·개발자가 "지금 무엇을, 어느 경험으로 시작할 것인가"를 판단할 수 있도록 핵심만 짚어 드립니다.

> **이 글의 한 줄 요약**
> 재구축된 Copilot Studio가 **GA** 되었고, 자연어 지시 기반의 **새 에이전트 경험**이 **미리 보기**로 추가됐습니다. 기존(classic) 경험과 **공존하지만 마이그레이션은 불가**하므로, 새 에이전트는 처음부터 어느 경험으로 만들지 선택해야 합니다.

---

## 한눈에 보는 이번 업데이트

| 영역 | 핵심 변화 | 상태 |
| --- | --- | --- |
| 빌딩 경험 | 새 agentic 오케스트레이터, 구성 탭 9→4개, 스킬 지원 | **GA** |
| 새 에이전트 경험 | 자연어 지시 기반 단일 화면(Build/Preview/Evaluate/Monitor) | 미리 보기 |
| 워크플로 | 새 비주얼 디자이너, 에이전트 노드, MCP 서버 | 미리 보기/얼리 릴리스 |
| 컴퓨터 사용 에이전트 | UI 자동화 GA, 워크플로 임베드 | **GA**(임베드 미리 보기) |
| 실시간 음성 | Dynamics 365 Contact Center 음성 에이전트 | **GA**(북미) |
| Work IQ | REST API·CLI, 원격 MCP, 에이전트 간(A2A) 통신 | **GA** |

---

## 1. 재구축된 Copilot Studio — 더 안정적인 에이전트

처음부터 기대한 대로 동작하는 에이전트를 더 쉽게 만들도록, 지시(instruction) 준수 능력과 복잡한 작업 처리 방식을 강화했습니다. 새 빌딩 경험은 핵심 구성만 전면에 배치해 **구성 탭을 9개에서 4개로 줄였습니다.**

### 새 agentic 오케스트레이터

새로운 **코딩 하네스(coding harness)와 CLI 레이어** 위에 구축되어, 지시 준수력과 장기 과제(long-horizon) 수행 능력이 한층 강해졌습니다.

- **재귀적 작업 실행(recursive task execution)** 으로 복잡하고 동적인 문제를 단계적으로 훨씬 잘 풀어냅니다.
- **대용량 콘텐츠 처리** 와 **풍부한 파일 출력** 이 가능해 문서·데이터 활용 시나리오가 새롭게 열립니다.

### 새 에이전트 빌딩 인터페이스

**지시(instructions)·스킬(skills)·도구(tools)·지식(knowledge)을 한 화면에서** 볼 수 있게 했고, 전체 페이지 테스트 경험은 **인라인 chain-of-thought(사고 과정)와 tool calling(도구 호출)** 을 보여줍니다. "왜 그렇게 판단했는지"를 빌딩 단계에서 바로 확인할 수 있습니다.

### 스킬(Skills) 지원

에이전트의 **재사용 가능한 지시를 Markdown으로 작성**해 두고 필요 시 로드(load on demand)할 수 있습니다. **기존 GitHub Copilot 또는 Claude Code 스킬도 그대로 임포트**할 수 있다는 점이 특히 흥미롭습니다.

> 새 에이전트 빌딩 디자이너는 [aka.ms/copilotstudio](https://aka.ms/copilotstudio)에서 바로 사용해 볼 수 있습니다.

---

## 2. 새 에이전트 경험(미리 보기) — 자연어로 만드는 에이전트

재구축과 같은 흐름에서, 작성·런타임을 재설계한 **'새 에이전트 경험'** 이 공개 미리 보기로 추가됐습니다. 핵심 철학은 세 가지입니다.

- **자연어 우선(natural-language-first)** — 토픽·플로·분기 로직 대신, 목적과 행동을 **평범한 말로 설명**하면 시스템이 구성을 생성합니다.
- **단일 화면(single-surface)** — 지식·도구·스킬·설정을 **하나의 통합 뷰**에서 다룹니다.
- **향상된 오케스트레이션(enhanced orchestration)** — 모든 에이전트가 더 깊은 추론과 높은 응답 품질을 제공하는 새 런타임 위에서 동작합니다.

### 탭 기반 작성 화면

| 탭 | 역할 |
| --- | --- |
| **Build** | 정체성·지식·도구·스킬·모델 구성 |
| **Preview** | 미리 보기 채팅에서 대화형 테스트 |
| **Evaluate** | 테스트 세트로 품질 측정 |
| **Monitor** | 최근 작업·접근 파일·활동 검토 |

품질 평가(Evaluate)와 모니터링(Monitor)이 별도 단계가 아니라 **작성 화면의 일부**로 들어온 것이 특징입니다. 에이전트 수명주기는 **Create → Build → Test → Publish → Monitor** 흐름을 따릅니다.

---

## 3. Classic vs New — 무엇이 어떻게 다른가

가장 많이 받게 될 질문이 "내가 지금 쓰는 건 어느 경험인가?"입니다.

> **빠른 구분법**
> 왼쪽 내비게이션에 **Topics / Knowledge / Actions / Settings** 가 따로 보이면 **Classic**입니다.
> 상단에 **Build / Preview / Evaluate / Monitor** 탭이 보이면 **New(미리 보기)** 입니다.

### 핵심 차이 비교

| 항목 | Classic(기존) | New(새 경험, 미리 보기) |
| --- | --- | --- |
| 작성 방식 | 토픽·플로·분기 로직, 명시적 노드 | 자연어 설명으로 시작, 시스템이 구성 생성 |
| 화면 구성 | 캔버스 중심, 영역별 분리 | 정체성·지식·도구·스킬·설정을 단일 화면 통합 |
| 동작 원리 | 명시적 토픽 트리거와 대화 설계 | 지시(instructions)와 추론 기반 |
| 오케스트레이션 | classic / generative 모드 **선택 가능** | 향상된 런타임 **일괄 적용**(전환 옵션 없음) |
| 평가·모니터링 | 별도 단계 | 작성 화면에 내장(Evaluate·Monitor) |

### 새 경험이 더 잘하는 것

- **높은 응답 품질** — 특히 **Microsoft 365 데이터** 시나리오에서 기존 경험이 따라오지 못하는 품질을 냅니다.
- **자연어 작성** — 유능한 에이전트를 만드는 **진입 장벽이 크게 낮아집니다.**
- **단순해진 멘탈 모델** — 토픽·트리거·노드를 **'지시를 가진 하나의 에이전트 객체'** 로 대체합니다.
- **내장된 평가·모니터링** 과, 새 기능이 집중되는 **향후 투자 방향**.

### 아직은 기존 경험이 더 나은 것

- **토픽 기반 대화 설계** — 모든 단계를 **정밀·결정론적으로 제어**해야 한다면 기존 경험이 유리합니다.
- **구성 가능한 오케스트레이션** 과 오랜 기간 다듬어진 **성숙한 기능 세트**.

> **중요 — 두 경험 간 마이그레이션은 없습니다.**
> 새 경험에서 만든 에이전트는 기존 경험으로 옮길 수 없고, 그 반대도 불가능합니다. 두 경험이 **근본적으로 다른 아키텍처와 오케스트레이션 런타임**을 쓰기 때문입니다. 새 경험을 쓰려면 **새 에이전트를 새로 만들어야** 하며, 기존 에이전트는 그대로 계속 동작합니다.

### 어느 경험을 선택할까

- **새 경험** — 새 에이전트를 만들고 향상된 오케스트레이션·응답 품질을 원할 때, 자연어 기반의 단순한 작성 모델을 원할 때, 특히 **조직·M365 데이터 추론**이 주 용도일 때.
- **기존 경험** — 기존 에이전트를 유지·확장할 때, **명시적 토픽 로직으로 흐름을 정밀 제어**해야 할 때, 아직 새 경험에 없는 기능에 의존할 때.

---

## 4. 더 지능적인 end-to-end 워크플로

새 **워크플로 디자이너**는 흩어진 도구를 꿰매는 대신 **단일 캔버스에서 end-to-end로 설계**하는 비주얼 환경을 제공합니다.

- **새 워크플로 디자이너** — [직관적인 비주얼 디자이너](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-designer?tabs=workflows)로, **노드 단위 테스트**와 견고한 **버전 관리**를 지원합니다.
- **에이전트 노드(Agent nodes)** — if-then 로직으로 담을 수 없는 판단(맥락 추론, 도구 오케스트레이션, 다중 소스 지식 검색)이 필요할 때 [워크플로 안에서 에이전트를 직접 호출](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/automate-business-processes-with-agents-plus-workflows-in-microsoft-copilot-studio/)합니다.
- **MCP 서버(미리 보기)** — [MCP 지원 도구](https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/use-mcp-compliant-tools-agent-workflows)의 폭넓은 생태계에 연결하되, **Microsoft의 보안·권한·규정 준수 경계 안에서** 동작합니다.

결과적으로 **결정론적 오케스트레이션 + 적응형 실행** — 필요한 곳은 구조화, 가치 있는 곳은 적응 — 을 한곳에서 결합할 수 있습니다.

---

## 5. 함께 온 5월 신기능

### 컴퓨터 사용 에이전트(Computer-using agents) 정식 출시

API가 없는 레거시·벤더 포털처럼 **UI로만 다룰 수 있는 업무**를 자동화하는 컴퓨터 사용 에이전트가 **GA** 되었습니다. 자격 증명을 더 안전하게 관리하고, 시나리오별 **모델 선택**이 가능하며, 화면이 바뀌어도 깨지지 않고 **적응**합니다. 다단계 **워크플로에 직접 임베드**(미리 보기)도 가능합니다.

> **현장 사례 — Graebel**
> 글로벌 인재 이동(talent mobility) 기업 Graebel은 API가 없던 자사 'Global Connect' 플랫폼 탓에 기존 자동화가 번번이 깨졌습니다. 컴퓨터 사용 역량으로 만든 **Service Order Agent**는 비정형 이메일을 해석하고, 비즈니스 규칙으로 검증한 뒤, UI로 Global Connect를 직접 조작하고, 예외는 워크플로로 에스컬레이션합니다. 30개 이상의 이전 서비스 범주로 확장 중이며, 수작업 감소와 처리 속도 향상을 거두고 있습니다.

### 실시간 음성 에이전트(Real-time voice) 정식 출시

[Dynamics 365 Contact Center](https://www.microsoft.com/en-us/dynamics-365/products/contact-center)를 통해 **북미 지역에서 실시간 음성 에이전트가 GA** 되었습니다. 발신자를 식별하고, 질문에 답하고, 대화 중 행동을 취하며, **맥락을 유지한 채 상담사에게 인계**합니다. 서버-투-서버(S2S) 음성도 지원하며, 대규모 운영을 위한 **음성 에이전트 거버넌스 가이드**(에스컬레이션 테스트·모니터링·보안·컴플라이언스)도 함께 제공됩니다.

### Work IQ 상호운용성·확장성

[Work IQ의 새 상호운용성·확장성 기능](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq)이 에이전트·워크플로·엔터프라이즈 도구를 환경 너머로 연결합니다.

- **Work IQ REST API와 CLI** — 기존 운영·개발 워크플로에 유연하게 통합
- **원격 MCP 서버 지원** — 도구·서비스·리소스를 표준화된 방식으로 연결해 일회성 통합 부담을 줄임
- **에이전트 간(A2A) 통신 GA** — 에이전트들이 정보를 교환하고 작업을 위임하며 협업

---

## 도입 관점 체크포인트

- **새 에이전트는 '경험 선택'이 첫 결정** — 두 경험은 공존하되 마이그레이션이 불가하므로, 새 에이전트의 성격(자연어·추론 중심인가, 정밀한 토픽 제어가 필요한가)에 따라 처음부터 경험을 선택해야 합니다.
- **M365 데이터 시나리오라면 새 경험 우선 검토** — 조직 데이터 추론 품질에서 새 런타임의 이점이 가장 큽니다.
- **결정론 + 지능의 결합** — 예측 가능한 단계는 워크플로로, 열린 작업은 에이전트로, 둘을 결합해 프로세스를 end-to-end로 자동화하는 설계 패턴이 명확해졌습니다.
- **자동화 범위 확장** — 컴퓨터 사용 에이전트 GA로 API 없는 레거시까지, A2A로 시스템 간 협업까지 대상이 넓어졌습니다.
- **거버넌스 유지** — MCP 연결·음성 에이전트 모두 보안·권한·컴플라이언스 경계 안에서 운영되도록 가이드가 함께 제공됩니다.
- **마이그레이션 부담 최소화** — 신규·기존 경험이 공존하므로, 기존 자산을 안전하게 운영하며 본인 속도로 새 경험을 탐색할 수 있습니다.

---

## 시작하기

모든 메이커는 [Copilot Studio](https://copilotstudio.microsoft.com) 홈 상단의 **"Try now"** 를 클릭해 간결해진 빌딩 인터페이스와 현대화된 오케스트레이터를 바로 써볼 수 있습니다. 새 에이전트를 만들 때 어느 경험으로 시작할지 선택하면 되고, 기존 에이전트는 그대로 동작합니다.

> 새 에이전트 경험은 미리 보기 단계이므로, 정식 출시 전까지 기능과 동작이 변경될 수 있습니다.

---

## 마무리

이번 개편의 메시지는 분명합니다 — **하나의 통합 플랫폼에서 AI로 모든 업무 프로세스를 현대화**하라는 것입니다. 새 agentic 오케스트레이터로 더 안정적인 에이전트를 만들고, 자연어 기반의 새 경험으로 진입 장벽을 낮추며, 새 워크플로·컴퓨터 사용·음성·Work IQ로 자동화의 폭을 넓히되 거버넌스는 유지합니다.

복잡한 다단계 업무를 에이전트에게 맡겨 보고 싶었지만 안정성 때문에 망설였다면, 지금이 새 Copilot Studio를 직접 시험해 볼 좋은 시점입니다.

---

> **출처**
> - Microsoft Copilot Studio Blog — "Meet the new Copilot Studio: rebuilt for more complex, multi-step work" ([techcommunity.microsoft.com](https://techcommunity.microsoft.com/blog/copilot-studio-blog/meet-the-new-copilot-studio-rebuilt-for-more-complex-multi-step-work/4526488))
> - Microsoft Copilot Blog — "New and improved computer-using agents, a new workflows experience, and real-time voice experiences" ([microsoft.com](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/))
> - Microsoft Learn — "Agents overview (preview)" 및 "Classic vs. new agent experience (preview)" (Microsoft Copilot Studio 문서)
> - 자세한 내용은 각 원문을 참조하세요.
