---
title: "대기열이 변하면 상담 배정도 바뀌어야 합니다: Contact Center 대화 오케스트레이션"
date: 2026-11-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - ContactCenter
  - Copilot
  - Routing
excerpt: "Dynamics 365 Contact Center의 대화 오케스트레이션이 우선순위 조정·오버플로·선호 상담원 배정·Bullseye 라우팅을 확장합니다. 자연어 플레이북 게시 시 Copilot Credits가 소모되며 런타임 실행에는 소모되지 않는다고 안내됐습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 대기열이 변하면 상담 배정도 바뀌어야 합니다: Contact Center 대화 오케스트레이션

고객 상담은 접수 순간의 라우팅만으로 끝나지 않습니다. 대기 시간이 길어지고 상담원이 로그아웃하면, 이미 들어온 대화의 처리 방식도 바뀌어야 합니다.

Dynamics 365 Contact Center의 대화 오케스트레이션은 대화 시작부터 해결까지 상황 변화를 살피고, 관리자가 만든 **자연어 플레이북**에 따라 후속 동작을 수행합니다.

---

## 네 가지 핵심 확장

| 기능 | 동작 |
|---|---|
| 동적 우선순위 상승 | 대기 시간, 큐 이동, 고객 등급 등으로 우선순위 재평가 |
| 복합 오버플로 처리 | 영업시간 종료, 상담원 부재, 대기 시간·대기 건수 초과 등에 대응 |
| 이전·선호 상담원 연결 | 과거 상호작용, 큐 소속, 가용성, 처리 용량을 고려해 재연결 |
| Bullseye 라우팅 | 정해진 시간 안에 배정되지 않으면 스킬·숙련도·팀 등으로 후보 범위 확대 |

오버플로 동작에는 콜백 제안, 대체 큐 이동, 배정 대상 확장, 감독자 알림, 고객 상황 안내가 포함될 수 있습니다. 직통 수신 전화에서도 상담원이 없거나 받지 않을 때 오버플로를 구성할 수 있습니다.

![대화 오케스트레이션 시작 화면](/mwkorea/assets/images/2026-11-03-ContactCenterConversationOrchestration/image1.png)

## 플레이북 검증과 비용

관리자는 안내 템플릿으로 시나리오별 플레이북을 구성하고, 게시 전 내장 검증으로 충돌을 확인할 수 있습니다. 비동기 대화는 상담원 접속 상태와 활성 대화 한도를 고려하도록 선택할 수 있으며, 선호 상담원이 없으면 다음 적격 상담원으로 전환할 수 있습니다.

원문의 비용 구분은 중요합니다. **Copilot Credits는 관리자가 플레이북을 게시할 때 소모되며 런타임 실행에는 소모되지 않습니다.** 이를 Contact Center 전체 서비스가 무료라는 의미로 확장해서는 안 됩니다.

![대기 상황에 따른 우선순위 상승 구성 화면](/mwkorea/assets/images/2026-11-03-ContactCenterConversationOrchestration/image2.png)

## 일정과 시작하기

전 세계 GA는 **2026년 10월 말 시작, 11월 말 완료 예정**입니다. 기존 사용자는 현 구성을 계속 쓸 수 있고 추가 조치가 필요하지 않습니다. 신규 사용자는 사전 요구사항을 검토한 뒤 기능을 활성화하고 조직에 맞는 플레이북을 구성해야 합니다.

국내 컨택센터에서는 고객 등급, 영업시간, 스킬별 최소 기준과 에스컬레이션 책임자를 먼저 정리하는 것이 좋습니다. 자동 라우팅이 실제 서비스 수준과 공정한 업무 배분에 부합하는지 운영 지표로 확인하세요.

> **출처**: MC1536059 — [Microsoft 365 Copilot: Conversation orchestration expands routing and overflow capabilities](https://mc.merill.net/message/MC1536059). [Microsoft 365 Roadmap 577788](https://www.microsoft.com/microsoft-365/roadmap?searchterms=577788). 실제 출시 일정·기능은 변경될 수 있습니다.
