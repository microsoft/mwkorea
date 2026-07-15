---
title: "Teams 에이전트 개발의 기회: 대화를 실제 업무 결과로 바꾸는 협업형 에이전트"
date: 2026-07-15T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftTeams
  - Agents
  - TeamsSDK
  - MCP
  - AgentToAgent
  - AdaptiveCards
  - MicrosoftGraph
excerpt: "Microsoft가 Teams 협업형 에이전트 개발을 다루는 월간 시리즈 Building Agents for Teams를 시작했습니다. Teams의 채팅·채널·회의에 자연스럽게 참여하는 에이전트를 Teams SDK로 만들고, 대화가 흘러가 버리기 전에 실제 업무 결과로 연결하는 방법을 소개합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Teams 에이전트 개발의 기회: 대화를 실제 업무 결과로 바꾸는 협업형 에이전트

많은 에이전트는 아직 독립형 앱이나 별도 탭 안에 머뭅니다. 사용자가 적절한 에이전트를 찾아 들어가고, 그 도구의 작업 방식에 맞춰야 합니다. 연구나 코딩처럼 집중적인 작업에는 감수할 수 있는 과정이지만, 상태 확인·데이터 조회·승인·관계자 호출처럼 매일 반복되는 작은 업무에서는 이런 마찰이 빠르게 누적됩니다.

Microsoft는 채팅·채널·회의가 이루어지는 **Microsoft Teams 안에 에이전트를 자연스럽게 참여**시켜, 대화가 지나가기 전에 아이디어를 실제 행동과 결과로 연결하려 합니다. 이를 위해 Microsoft 365 Developer Blog에서 새로운 월간 시리즈 **Building Agents for Teams**를 시작했습니다.

![Teams에서 사용자와 에이전트가 협업하는 모습](/mwkorea/assets/images/2026-07-15-BuildingAgentsForTeams/image1.webp)

---

## Teams에서 에이전트가 갖는 기회

Teams 안의 에이전트는 별도 도구라기보다 함께 일하는 사람처럼 동작합니다.

- `@mention`으로 호출합니다.
- 채널이나 그룹 채팅에 추가합니다.
- 자연어로 작업을 맡기면 해당 스레드에서 응답합니다.
- 필요할 때 회의에 참여시킵니다.

사용자는 이미 동료와 협업하는 방법을 알고 있으므로 새로운 인터페이스를 배울 필요가 적습니다. 개발자 입장에서는 에이전트를 실제 업무 흐름과 사용자 앞에 배포하는 가장 어려운 문제를 Teams가 상당 부분 해결해 줍니다.

## 왜 지금 만들어야 하나

불과 1년 전에는 에이전트를 데모하는 데 의미가 있었다면, 이제는 실제 작업을 완료하는 에이전트를 출시할 수 있는 조건이 갖춰지고 있습니다.

- LLM의 추론·작업 수행 능력이 크게 발전했습니다.
- 응답 지연이 실사용의 결정적인 장애가 되지 않을 정도로 개선됐습니다.
- 모델 사용 비용이 계속 낮아지고 있습니다.
- Model Context Protocol(MCP)이 도구·Skill·Markdown 기반 메모리를 연결하는 공통 방식을 제공합니다.
- Agent-to-Agent 통신을 통해 여러 에이전트가 역할을 나눠 협업할 수 있습니다.

MCP와 Agent-to-Agent는 Microsoft 전용 개념이 아니라 업계 전반의 에이전트 연결 표준이며, Teams 플랫폼은 이를 네이티브로 지원합니다.

## 협업형 에이전트의 두 가지 상호작용

### 비공개 상호작용

사용자 한 명과 에이전트가 문제를 해결하는 익숙한 형태입니다. Teams의 1:1 채팅은 물론, 그룹 채팅·채널·회의의 맥락에 기반하되 특정 사용자에게만 보이는 targeted message도 활용할 수 있습니다.

### 공개 상호작용

협업형 에이전트의 차별점은 공개 상호작용에서 드러납니다.

- 그룹 채팅에서 여러 구성원과 함께 일합니다.
- 채널에서 팀 전체가 에이전트의 작업 과정을 확인합니다.
- 회의에 참여해 사람들이 보는 앞에서 정보를 제공하거나 작업을 수행합니다.

이 경우 에이전트는 개인 도구가 아니라 **팀의 참여자**가 됩니다. 비공개와 공개 상호작용을 모두 안전하고 자연스럽게 설계하는 일은 어렵지만, 팀 전체가 함께 쓸 수 있는 에이전트의 가치는 훨씬 큽니다.

## Teams SDK로 에이전트 만들기

Teams SDK는 협업형 에이전트를 만들기 위한 통합 개발 도구입니다. 인증, 이벤트 라우팅, Teams 고유의 처리 방식은 SDK가 맡고 개발자는 에이전트의 실제 업무 로직에 집중할 수 있습니다.

### 지원 범위

- TypeScript, C#, Python
- 공유 도구와 메모리를 위한 Model Context Protocol
- 멀티 에이전트 작업을 위한 Agent-to-Agent 통신
- Adaptive Cards
- Message extensions
- Embedded web apps
- Dialogs
- Microsoft Graph

### 빠르게 시작하기

```powershell
npm install -g @microsoft/teams.cli
teams project new typescript my-agent
```

처음부터 거대한 범용 에이전트를 만들기보다 하나의 업무를 잘 처리하는 작은 프로젝트를 만들고 실제 팀 앞에 배포해 보는 것이 빠른 학습 방법입니다.

## 앞으로 다룰 내용

Building Agents for Teams 시리즈는 다음 주제를 심층적으로 다룰 예정입니다.

- 채널·회의에서의 공개 상호작용 설계
- 실제 코드로 구현하는 MCP와 Agent-to-Agent 패턴
- 에이전트 게시와 대규모 사용자 도달
- 개인정보 보호와 컴플라이언스 과제
- 실제 개발자·파트너 사례와 학습 내용

## 개발·도입 체크포인트

- 에이전트가 비공개로 응답해야 하는 상황과 팀 전체에 공개해야 하는 상황을 명확히 구분합니다.
- 채널·회의에서 에이전트가 실행하는 작업과 결과를 사용자가 확인할 수 있게 설계합니다.
- MCP 도구와 Microsoft Graph 권한은 최소 권한 원칙으로 구성합니다.
- 공개 대화에 민감 정보가 노출되지 않도록 개인정보·컴플라이언스 검토를 포함합니다.
- 처음에는 단일 업무와 소규모 팀을 대상으로 배포한 뒤 사용 패턴을 관찰합니다.

## 마무리

Teams 에이전트의 핵심은 대화형 UI를 하나 더 만드는 것이 아닙니다. 사람들이 이미 협업하는 채팅·채널·회의 안에서, 대화로 끝날 일을 실제 결과로 연결하는 것입니다. Teams SDK와 MCP·Agent-to-Agent 같은 표준이 성숙한 지금은 협업형 에이전트를 실험하고 배포하기 좋은 시점입니다.

---

> **원문**: [Building Agents for Teams: Turning conversations into outcomes (Microsoft 365 Developer Blog, 2026-07-14)](https://devblogs.microsoft.com/microsoft365dev/building-agents-for-teams-turning-conversations-into-outcomes/)
>
> 자세한 내용은 원문을 참조하세요.
