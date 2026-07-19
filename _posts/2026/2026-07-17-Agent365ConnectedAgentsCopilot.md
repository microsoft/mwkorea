---
title: "Agent 365 에이전트를 Copilot Chat과 선언적 에이전트에서 연결 에이전트로 사용하기"
date: 2026-07-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent365
  - Microsoft365Copilot
  - ConnectedAgents
  - AgentBuilder
  - CopilotStudio
  - Agent2Agent
  - Roadmap
excerpt: "Agent 365에 게시된 에이전트를 Microsoft 365 Copilot Chat과 선언적 에이전트(Declarative Agents)에서 연결 에이전트로 사용할 수 있게 됩니다. Agent2Agent 프로토콜을 구현한 에이전트라면 Agent Builder나 Copilot Studio에서 만든 에이전트의 연결 에이전트가 됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Agent 365 에이전트를 Copilot Chat과 선언적 에이전트에서 연결 에이전트로 사용하기

조직이 Agent 365에 등록·관리하는 에이전트가 늘어날수록, 이 에이전트들을 사용자가 직접 만드는 에이전트와 연결해 재사용하고 싶은 요구가 커집니다. 매번 같은 기능을 다시 만들기보다, 이미 관리되는 전문 에이전트에 위임하는 편이 효율적입니다.

이번 업데이트로 **Agent 365에 게시된 에이전트를 Microsoft 365 Copilot Chat과 선언적 에이전트(Declarative Agents)에서 연결 에이전트(connected agent)로 사용**할 수 있게 됩니다.

> **한 줄 요약**
> Agent 365에 게시된 에이전트는 이미 Microsoft 365 admin center에서 관리됩니다. 이 에이전트가 Agent2Agent(A2A) 프로토콜을 구현한 경우, 사용자가 Agent Builder나 Copilot Studio에서 만드는 에이전트의 연결 에이전트로 사용할 수 있습니다.

---

## 무엇이 새로워지나

Agent 365에 게시된 에이전트는 Microsoft 365 admin center를 통해 관리됩니다. 이번 변경의 핵심은 이 관리되는 에이전트를 **다른 에이전트가 연결해 활용**할 수 있다는 점입니다.

전제 조건은 다음과 같습니다.

- 에이전트가 **Agent2Agent(A2A) 프로토콜**을 구현해야 합니다.
- 이 경우 Agent Builder 또는 Copilot Studio에서 사용자가 만든 에이전트의 연결 에이전트로 사용할 수 있습니다.

## 왜 중요한가

연결 에이전트는 하나의 에이전트가 모든 일을 처리하는 대신, 전문 영역을 담당하는 다른 에이전트에 위임하는 구조를 가능하게 합니다. Agent 365의 관리되는 에이전트를 연결 에이전트로 쓸 수 있으면 다음 이점이 있습니다.

- 조직이 관리·거버넌스하는 에이전트를 재사용
- 사용자가 만든 에이전트가 전문 기능을 직접 구현하지 않고 위임
- 관리 체계 안에서 멀티 에이전트 협업 구성

## 활용 시나리오

- Copilot Studio에서 만든 부서 에이전트가 Agent 365의 전문 에이전트에 특정 질의를 위임
- Agent Builder로 만든 선언적 에이전트가 관리되는 에이전트를 연결해 기능 확장
- 조직 표준 에이전트를 여러 사용자 에이전트가 공통으로 연결

## 출시 일정

| 구분 | 내용 |
|---|---|
| GA | 2026년 8월 |
| 전제 조건 | Agent2Agent(A2A) 프로토콜 구현 |
| 사용 위치 | Microsoft 365 Copilot Chat, Declarative Agents, Agent Builder, Copilot Studio |

## 개발·도입 관점 체크포인트

- 연결하려는 Agent 365 에이전트가 A2A 프로토콜을 구현했는지 확인합니다.
- 연결 에이전트가 접근하는 데이터와 권한 범위를 점검합니다.
- 관리되는 에이전트의 소유권·수명주기와 이를 연결한 사용자 에이전트의 의존 관계를 정리합니다.
- 멀티 에이전트 위임 시 응답 품질과 오류 처리를 평가합니다.

## 마무리

Agent 365의 관리되는 에이전트를 연결 에이전트로 활용할 수 있게 되면서, 조직은 거버넌스 체계 안에서 멀티 에이전트 협업을 구성할 수 있게 됩니다. A2A 프로토콜을 기반으로 전문 에이전트를 재사용하는 구조는 에이전트 생태계를 더 효율적으로 확장하는 기반이 됩니다.

---

> ※ 본 글은 Microsoft 365 메시지 센터/로드맵 공지(**RM567670**)를 바탕으로 정리했습니다. 원문은 [Message Center Archive](https://mc.merill.net/message/RM567670)와 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 확인할 수 있으며, 실제 출시 일정·기능은 변경될 수 있습니다.
