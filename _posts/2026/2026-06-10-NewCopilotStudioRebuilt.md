---
title: "완전히 새로워진 Copilot Studio: 복잡한 다단계 업무를 위해 재설계되다"
date: 2026-06-10T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Agent
  - Workflow
  - Orchestrator
  - MCP
  - Skills
  - Automation
excerpt: "Microsoft Copilot Studio가 전면 재구축되어 전 세계 정식 출시(GA)되었습니다. 새 agentic 오케스트레이터, 9→4개로 줄어든 구성 탭, 스킬(Skills) 지원, 새 워크플로 디자이너와 MCP 서버 연결까지 — 더 안정적이고 복잡한 다단계 업무를 처리하는 에이전트를 만드는 방법을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 완전히 새로워진 Copilot Studio: 복잡한 다단계 업무를 위해 재설계되다

에이전트를 만들다 보면 늘 같은 벽에 부딪힙니다. "단순한 한두 단계는 잘 되는데, 여러 단계가 얽힌 실제 업무를 맡기면 중간에 흐름이 끊긴다"는 것이죠. Microsoft가 고객들로부터 가장 많이 들어온 피드백도 바로 이 지점이었습니다 — 더 유능한 에이전트, 자연스럽게 함께 작동하는 워크플로, 그리고 중간에 무너지지 않고 끝까지 다단계 작업을 수행하는 안정성.

이번에 Microsoft는 그 피드백을 바탕으로 **Copilot Studio를 처음부터 다시 설계(rebuilt)**했습니다. 새로워진 작성(authoring) 경험과 현대화된 AI 코어를 통해, 에이전트와 워크플로가 **더 일관되고 신뢰할 수 있는 결과**를 내도록 만든 것이 핵심입니다.

무엇보다 반가운 소식은, 이 업데이트가 **전 세계에 정식 출시(Generally Available)**되어 곧바로 프로덕션 용도의 에이전트를 만들 수 있다는 점입니다. 이번 글에서는 무엇이 새로워졌는지, 그리고 도입을 검토하는 IT 담당자·메이커·개발자 관점에서 무엇을 눈여겨봐야 하는지 정리해 드립니다.

---

## 무엇이 새로워졌나요?

이번 개편은 크게 세 갈래로 요약할 수 있습니다.

- **더 안정적인 에이전트** — 새로운 agentic 오케스트레이터와 간결해진 빌딩 인터페이스
- **더 지능적인 end-to-end 워크플로** — 새 워크플로 디자이너, 에이전트 노드, MCP 서버 연결
- **즉시 시작 가능** — 전 세계 GA, 기존(classic) 경험과 신규 경험의 공존

하나씩 자세히 살펴보겠습니다.

![재구축된 Microsoft Copilot Studio](/mwkorea/assets/images/2026-06-10-NewCopilotStudioRebuilt/image1.png)

---

## 더 안정적인 에이전트 만들기

처음부터 기대한 대로 동작하는 에이전트를 더 쉽게 만들 수 있도록, 지시(instruction) 준수 능력과 복잡한 작업 처리 방식을 강화했습니다. 그 결과 비즈니스 시나리오에서 더 일관된 결과를 얻을 수 있습니다. 또한 새 빌딩 경험은 핵심 구성만 전면에 배치해 **구성 탭을 9개에서 4개로 줄였습니다.** 더 빠르고, 더 유능하며, 더 효율적인 에이전트를 만들 수 있게 된 것이죠.

새 경험의 핵심 요소는 다음과 같습니다.

### 새 agentic 오케스트레이터

새로운 **코딩 하네스(coding harness)와 CLI 레이어** 위에 구축된 오케스트레이터로, 지시 준수력과 장기 과제(long-horizon) 수행 능력이 한층 강해졌습니다.

- **재귀적 작업 실행(recursive task execution)**을 지원해, 복잡하고 동적인 문제를 단계적으로 훨씬 잘 풀어냅니다.
- **대용량 콘텐츠 처리**가 가능하고, **풍부한 파일 출력**을 생성할 수 있어 문서·데이터 활용 시나리오가 새롭게 열립니다.

### 새 에이전트 빌딩 인터페이스

새 인터페이스는 에이전트 구축을 더 빠르고 간결하게 만들어, **지시(instructions)·스킬(skills)·도구(tools)·지식(knowledge)을 한 화면에서** 볼 수 있게 했습니다. 또한 새로운 전체 페이지(full page) 테스트 경험은 더 나은 서식과 함께 **인라인 chain-of-thought(사고 과정)와 tool calling(도구 호출)**을 보여줍니다. 에이전트가 "왜 그렇게 판단했는지"를 빌딩 단계에서 바로 확인할 수 있다는 의미입니다.

### 스킬(Skills) 지원

에이전트의 **재사용 가능한 지시를 Markdown으로 작성**해 두고, 특정 작업을 수행할 때 필요에 따라 로드(load on demand)할 수 있습니다. 흥미로운 점은, 이미 보유한 스킬을 가져올 수 있다는 것입니다 — **기존 GitHub Copilot 또는 Claude Code 스킬도 그대로 임포트**할 수 있습니다.

> 새 에이전트 빌딩 디자이너는 [aka.ms/copilotstudio](https://aka.ms/copilotstudio)에서 바로 사용해 볼 수 있습니다.

![간결해진 새 에이전트 빌딩 인터페이스](/mwkorea/assets/images/2026-06-10-NewCopilotStudioRebuilt/image2.png)

---

## 더 지능적인 end-to-end 워크플로 만들기

안정적인 자동화의 중심에는 워크플로가 있습니다. 새 **워크플로 디자이너**를 통해, 구조화된 워크플로 단계와 에이전트를 결합한 지능형 AI 기반 프로세스를 한곳에서 만들 수 있습니다.

- **새 워크플로 디자이너** — 단일 통합 작업 공간에서 agentic 자동화를 구축하는 [직관적인 비주얼 디자이너](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-designer?tabs=workflows)입니다. **노드 단위 테스트**와 견고한 **버전 관리**를 지원해, 동작하는 워크플로를 더 쉽고 빠르게 만들고·테스트하고·게시할 수 있습니다.
- **에이전트 노드(Agent nodes)** — 기존 에이전트를 [워크플로 안에서 직접 호출](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/automate-business-processes-with-agents-plus-workflows-in-microsoft-copilot-studio/)할 수 있습니다. 신뢰성이 필요한 부분은 결정론적(deterministic) 실행으로 처리하고, 더 높은 지능과 유연성이 필요한 복잡한 작업은 워크플로 내 에이전트에게 매끄럽게 넘길 수 있습니다.
- **MCP 서버(미리 보기)** — [MCP(Model Context Protocol) 지원 도구](https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/use-mcp-compliant-tools-agent-workflows)의 폭넓은 생태계에 연결할 수 있습니다. 워크플로가 작업을 실행하고 승인을 위해 사용자를 개입시키면서도, **Microsoft의 보안·권한·규정 준수 경계 안에서** 동작하도록 보장합니다.

![새 워크플로 디자이너에서 에이전트와 워크플로를 결합하는 모습](/mwkorea/assets/images/2026-06-10-NewCopilotStudioRebuilt/image3.gif)

---

## 도입 관점 체크포인트

도입을 검토하는 입장에서 이번 개편을 짚어보면 다음과 같습니다.

- **결정론 + 지능의 결합** — "예측 가능한 단계는 워크플로로, 열린 작업은 에이전트로, 그리고 둘을 결합해 업무 프로세스를 end-to-end로 자동화"하는 설계 패턴이 명확해졌습니다. 신뢰성과 유연성을 한 플랫폼에서 함께 가져갈 수 있습니다.
- **거버넌스 유지** — MCP 도구 연결도 Microsoft 보안·권한·컴플라이언스 경계 안에서 이뤄지므로, 외부 도구 확장과 통제 사이의 균형을 유지할 수 있습니다.
- **메이커 생산성** — 구성 탭 9→4개 축소, 한 화면 빌딩 경험, 노드별 테스트와 버전 관리는 메이커 워크포스를 확장(scale)하는 데 직접적으로 기여합니다.
- **마이그레이션 부담 최소화** — 신규 경험과 기존(classic) 경험이 **공존**하므로, 기존 에이전트·워크플로를 계속 관리하면서 본인 속도에 맞춰 새 경험을 탐색할 수 있습니다.

---

## 시작하기

모든 메이커는 [Copilot Studio](https://copilotstudio.microsoft.com)로 이동해 홈 화면 상단의 **"Try now"**를 클릭하면, 간결해진 빌딩 인터페이스와 현대화된 오케스트레이터로 유능한 에이전트를 만들기 시작할 수 있습니다.

![Copilot Studio 홈에서 새 경험 시작하기](/mwkorea/assets/images/2026-06-10-NewCopilotStudioRebuilt/image4.png)

앞서 언급했듯 새 경험과 기존 경험은 계속 공존하므로, 기존 자산을 안전하게 운영하면서 새로운 기능을 점진적으로 도입할 수 있습니다. Microsoft는 제품 우측 상단의 피드백 컨트롤을 통해 받은 의견으로 Copilot Studio를 계속 개선해 나갈 예정입니다.

---

## 마무리

이번 Copilot Studio 개편의 메시지는 분명합니다 — **하나의 통합 플랫폼에서 AI로 모든 업무 프로세스를 현대화**하라는 것입니다. 새 agentic 오케스트레이터로 더 안정적인 에이전트를 만들고, 새 워크플로 디자이너로 결정론적 단계와 에이전트를 결합하며, MCP 생태계로 확장하되 거버넌스는 유지합니다.

복잡한 다단계 업무를 에이전트에게 맡겨 보고 싶었지만 안정성 때문에 망설였다면, 지금이 새 Copilot Studio를 직접 시험해 볼 좋은 시점입니다.

---

> **출처**: Microsoft Copilot Studio Blog — "Meet the new Copilot Studio: rebuilt for more complex, multi-step work"
> ([techcommunity.microsoft.com](https://techcommunity.microsoft.com/t5/copilot-studio-blog/meet-the-new-copilot-studio-rebuilt-for-more-complex-multi-step/ba-p/4526488)) · 자세한 내용은 원문을 참조하세요.
