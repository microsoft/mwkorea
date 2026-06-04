---
title: "Work IQ 정식 출시 임박: 모든 에이전트를 위한 프로덕션급 인텔리전스 계층"
date: 2026-06-03T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - Agent
  - Microsoft365Copilot
  - MCP
  - A2A
  - Governance
excerpt: "엔터프라이즈 인텔리전스가 '에이전트 우선(agent-first)' 모델로 이동하고 있습니다. Work IQ는 에이전트가 조직 데이터·맥락·도구에 접근하고 추론할 수 있게 해주는 인텔리전스 계층으로, 2026년 6월 16일 API 엔드포인트(A2A·원격 MCP 서버·REST)가 정식 출시(GA)됩니다. M365 Copilot 라이선스와 무관하게 소비 기반으로 제공됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Work IQ 정식 출시 임박: 모든 에이전트를 위한 프로덕션급 인텔리전스 계층

엔터프라이즈 인텔리전스의 무게중심이 사람에서 **에이전트(agent)** 로 옮겨가고 있습니다. 지금까지 AI는 주로 "개발자나 사용자 개인"을 위한 도구였다면, 이제는 AI 에이전트가 스스로 계획하고, 추론하고, 여러 시스템을 넘나들며 행동하는 **에이전트 우선(agent-first)** 시대로 진입하고 있습니다.

이 변화의 핵심에 **Work IQ**가 있습니다. Work IQ는 에이전트가 조직의 데이터·맥락·도구에 접근해 추론할 수 있게 해주는 **워크플레이스 인텔리전스 계층**입니다. Microsoft 365는 물론 외부 시스템까지 아우르며 의미론적 이해(semantic understanding)를 지속적으로 축적하고, 권한을 인지하는(permission-aware) 거버넌스를 기본 내장합니다.

> **이 글의 한 줄 요약**
> Work IQ API 엔드포인트(A2A, 재설계된 원격 MCP 서버, REST API)가 **2026년 6월 16일 정식 출시(GA)** 됩니다. M365 Copilot 라이선스와 무관하게 **소비 기반(consumption)** 으로 제공되며, GA 이전에 이미 퍼블릭 프리뷰로 사용할 수 있습니다.

---

## 무엇이 발표되었나

- **Work IQ API 엔드포인트 GA (6월 16일)**: 에이전트 간 협업을 위한 **A2A(Agent-to-Agent)**, 재설계된 **원격 MCP 서버**, 그리고 웹 애플리케이션 연동을 위한 **REST API**가 정식 출시됩니다.
- **소비 기반 과금**: 사용량은 **Microsoft 365 Copilot 라이선스와 독립적**이며, 소비량에 따라 과금됩니다. 즉 Copilot 라이선스가 없어도 에이전트가 Work IQ 인텔리전스를 활용할 수 있습니다.
- **새로운 거버넌스·비용 관리 제어**: Microsoft 365 관리 센터에 **비용·정책·확장**을 관리할 수 있는 컨트롤이 추가되어, IT 팀이 자신 있게 운영 규모를 키울 수 있습니다.
- **퍼블릭 프리뷰 제공 중**: GA 이전에도 바로 시작할 수 있습니다 — [github.com/microsoft/work-iq](https://github.com/microsoft/work-iq)

{% include video id="yj9JX08cxtw" provider="youtube" %}

![Work IQ 아키텍처 개요](/mwkorea/assets/images/2026-06-03-WorkIQProductionReady/image1.webp)

---

## 에이전트를 위해 설계된 4가지 축

Work IQ는 사람 개발자가 아니라 **AI 에이전트가 직접** 맥락을 검색하고 시스템을 가로질러 행동하는 세계를 전제로 설계되었습니다. 채팅·맥락·도구·워크스페이스를 하나의 인텔리전스 계층으로 통합해, 에이전트가 Microsoft 365 Copilot과 동일한 수준의 깊이와 신뢰성으로 동작하게 합니다.

### Chat — 대화형 인텔리전스에 최적화

에이전트 간 협업을 위한 **A2A**와 웹 앱 상호작용을 위한 **REST**를 지원합니다. 에이전트가 작업을 위임하고, 연속성을 유지하며, Copilot 수준으로 완전히 처리된 응답을 전달할 수 있습니다.

### Context — 오케스트레이션 부담 제거

Work IQ가 조직 데이터 전반에서 맥락을 **내부적으로 조립하고 grounding** 해 에이전트가 바로 쓸 수 있는 입력을 제공합니다. 에이전트가 원시 신호를 일일이 엮거나 검색 파이프라인을 직접 관리할 필요가 없습니다.

### Tools — 빠르고 조합 가능한 액션

소수의 범용 도구·스킬 세트로 에이전트가 Microsoft 365 전반에서 추론·데이터 검색·행동을 수행합니다. 단순하고 에이전트 친화적인 표면(surface)에 **중앙집중식 거버넌스**가 적용됩니다.

### Workspaces — 장기 작업에 최적화

고볼륨·다단계 상호작용을 지원하도록 설계되어, 에이전트가 오래 이어지는 작업의 맥락을 유지할 수 있습니다.

![Work IQ 파트너 생태계](/mwkorea/assets/images/2026-06-03-WorkIQProductionReady/image2.webp)

---

## 표준 프로토콜 위에서 동작

Work IQ는 특정 프레임워크나 런타임에 묶이지 않습니다. **A2A, MCP, REST 같은 표준 프로토콜**을 통해 다양한 프레임워크·런타임에서 작동하며, 에이전트·애플리케이션·워크플로를 구축하는 공통 기반을 제공합니다. 조직이 에이전트에 점점 더 의존하게 될수록 인텔리전스는 신뢰할 수 있고, 지속적으로 갱신되며, 대규모로 동작해야 합니다. Work IQ는 바로 그 **프로덕션급(production-ready)** 요구를 겨냥합니다.

---

## 도입·개발 관점 체크포인트

- **라이선스 독립성**: Copilot 라이선스 없이도 소비 기반으로 에이전트 인텔리전스를 활용할 수 있다는 점은, 에이전트 시나리오의 비용 구조를 새롭게 설계할 여지를 줍니다.
- **거버넌스 우선 설계**: GA와 함께 관리 센터에 비용·정책 제어가 들어오므로, PoC 단계부터 **누가·무엇을·어디까지** 쓸지 정책을 함께 설계하는 것이 좋습니다.
- **표준 채택**: A2A·MCP를 따르는 만큼, 기존/신규 에이전트를 표준 프로토콜 기반으로 정렬해 두면 이식성과 확장성이 좋아집니다.

---

## 마무리

Work IQ는 "사람을 돕는 AI"에서 "에이전트를 위한 인텔리전스 인프라"로 가는 전환점입니다. 6월 16일 GA를 기점으로, 조직은 Copilot 수준의 grounding과 거버넌스를 자체 에이전트에도 적용할 수 있게 됩니다. 에이전트 우선 시대를 준비하는 팀이라면 지금 퍼블릭 프리뷰로 먼저 손에 익혀 둘 만합니다.

---

> ※ 본 글은 Microsoft 365 Developer Blog의 [Work IQ: Production-ready intelligence for every agent](https://devblogs.microsoft.com/microsoft365dev/work-iq-production-ready-intelligence-for-every-agent/)를 바탕으로 한국 독자용으로 정리했습니다. 자세한 내용과 최신 일정은 원문 및 [github.com/microsoft/work-iq](https://github.com/microsoft/work-iq)를 참조하세요. 출시 일정·기능은 변경될 수 있습니다.
