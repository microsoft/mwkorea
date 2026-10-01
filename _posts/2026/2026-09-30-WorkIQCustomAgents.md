---
title: "Work IQ가 커스텀 에이전트와 서드파티 도구까지 호출합니다"
date: 2026-09-30T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - Microsoft365Copilot
  - Agent
  - ThirdParty
  - Extensibility
excerpt: "Work IQ가 조직의 커스텀 에이전트와 지원되는 서드파티 도구를 호출하는 에이전트까지 실행할 수 있게 됩니다. 2026년 11월 정식 출시를 앞둔 Work IQ 확장성 업데이트를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Work IQ가 커스텀 에이전트와 서드파티 도구까지 호출합니다

Work IQ는 Microsoft 365 Copilot이 사용자의 업무 맥락(메일, 파일, 일정 등)을 이해하고 적절한 에이전트·스킬을 연결해 주는 계층입니다. Microsoft 365 Roadmap에 등록된 **RM570853 공지**는 이 Work IQ의 호출 범위를 한층 넓히는 내용을 담고 있습니다.

이번 글은 해당 공지를 기준으로 정리하며, 한국 시간 발행일은 9월 30일이지만 실제 배포 완료 시점과는 다를 수 있습니다.

---

## 무엇이 바뀌나요?

공지 원문은 다음과 같습니다.

> *"Enable Work IQ to invoke custom agents and agents that call supported third-party tools."*

핵심은 두 가지입니다.

- **조직이 만든 커스텀 에이전트**를 Work IQ가 호출할 수 있습니다.
- **지원되는 서드파티 도구를 호출하는 에이전트**까지 Work IQ의 오케스트레이션 범위에 포함됩니다.

지금까지 Work IQ가 Microsoft 365 생태계 내부의 데이터·에이전트 중심으로 동작했다면, 이번 변화는 조직이 구축한 커스텀 에이전트와 외부 도구 연동까지 Work IQ의 "실행 범위"로 끌어들이는 방향입니다.

## 왜 의미가 있나요?

- 조직마다 이미 구축해 둔 **커스텀 에이전트**(Copilot Studio 등으로 만든)를 Work IQ가 자연어 요청에 맞춰 자동으로 선택·호출할 수 있게 됩니다.
- **서드파티 도구**와 연동된 에이전트도 지원 대상에 포함되어, Microsoft 생태계 밖의 업무 도구까지 Copilot 대화 흐름 안에서 연결될 가능성이 커집니다.
- 이는 Microsoft가 최근 강조해 온 "에이전트의 에이전트" 오케스트레이션 전략과 맞닿아 있습니다.

## 출시 일정

| 단계 | 시점 |
|---|---|
| Preview | 2026년 10월 |
| General Availability | 2026년 11월 |

## 도입 담당자가 챙길 점

- 커스텀 에이전트를 이미 보유한 조직이라면, Work IQ 호출 대상으로 등록·거버넌스 설정이 필요한지 Preview 단계에서 확인이 필요합니다.
- 서드파티 도구 연동은 "지원되는" 도구로 한정되므로, 실제 지원 목록은 정식 문서가 공개되는 시점에 다시 확인해야 합니다.
- 보안·거버넌스 담당자는 Work IQ가 호출할 수 있는 에이전트·도구 범위가 넓어지는 만큼, Agent 365 등 거버넌스 도구와 연계해 승인 체계를 미리 점검하는 것이 좋습니다.

## 마무리

Work IQ의 호출 범위가 조직의 커스텀 에이전트와 서드파티 도구까지 넓어지는 것은, Copilot을 단일 제품이 아니라 "에이전트 오케스트레이터"로 보는 흐름의 연장선입니다. 2026년 10월 프리뷰, 11월 GA 일정에 맞춰 조직 내 에이전트 자산을 점검해 보시기 바랍니다.

> 출처: **RM570853 — Work IQ: Custom agents + 3P calls**
> 원문: https://mc.merill.net/message/RM570853
> Microsoft 365 Roadmap: https://www.microsoft.com/microsoft-365/roadmap?id=570853
> **실제 출시 일정·기능은 변경될 수 있습니다.**
