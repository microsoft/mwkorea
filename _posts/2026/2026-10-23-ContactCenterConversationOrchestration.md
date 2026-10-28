---
title: "대기열 규칙을 넘어: 자연어 플레이북으로 상담 전체를 조율하기"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - ContactCenter
  - AgenticAI
  - UnifiedRouting
  - ConversationOrchestration
excerpt: "Dynamics 365 Contact Center의 conversation orchestration은 대화가 진행되는 동안 우선순위와 배정 조건을 계속 평가합니다. 자연어 플레이북, 복합 오버플로 처리와 Bullseye routing의 차이를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 대기열 규칙을 넘어: 자연어 플레이북으로 상담 전체를 조율하기

고객이 큐에 들어올 때 정한 우선순위는 10분 뒤에도 적절할까요? 담당자가 오프라인이 되거나 큐가 급격히 차면 처음의 규칙만으로는 대응하기 어렵습니다.

Roadmap RM577788의 **conversation orchestration**은 상담 시작부터 해결까지 이벤트를 지속적으로 살피는 방식입니다. 자연어 플레이북으로 의도를 정의하고, 변화하는 조건에 맞춰 실행을 조율합니다.

---

## “3분 이상 기다리면”이라는 의도를 정책으로

원문 예시는 “프리미엄 고객이 **3분 이상** 기다리고 선임 상담사가 없으면 우선순위를 올리고 콜백을 제안한다”입니다. 3분은 기능의 고정 제한이 아니라 플레이북 예제의 임계값입니다.

시나리오별 안내 템플릿으로 지시를 작성하며, 내장 검증이 게시 전 충돌을 찾도록 설계되어 있습니다. 다만 모든 운영 예외에 대한 조직의 검증을 대체한다고 보기는 어렵습니다.

## 핵심 기능 네 가지

**동적 우선순위 조정**은 대기시간, 큐 전환, 고객 등급과 맥락을 계속 평가합니다. 진입 순간 한 번 정한 우선순위를 끝까지 유지하는 방식과 다릅니다.

**복합 조건의 오버플로 처리**는 업무시간 외, 모든 담당자의 부재, 대기시간 초과와 대기 건수 초과 등에 대응합니다. 콜백 제공, 다른 큐 전환, 배정 자격 확대, 관리자 알림이나 고객 안내를 상황별로 구성할 수 있습니다. 담당자가 응답하지 않는 직통 전화의 오버플로 처리도 언급됩니다.

**이전·선호 담당자 연결**은 과거 상호작용, 큐 소속, 가용성과 업무량을 고려합니다. 비동기 대화에서는 상태와 활성 대화 한도를 존중하도록 선택할 수 있고, 선호 담당자가 불가능하면 다음 적합 담당자로 전환합니다.

**Bullseye routing**은 일정 시간 배정되지 않으면 적격 담당자 범위를 점진적으로 넓힙니다. 스킬, 숙련도와 팀 기준의 링을 정의해 전문성과 대기시간의 균형을 맞춥니다.

## 도입 시 무엇을 정해야 하나요?

우선순위 상승이 다른 고객에게 미치는 영향, 콜백 허용 시간, 담당자 범위 확대의 한계를 먼저 정하는 것이 좋습니다. 한국 고객센터에서는 VIP 정책과 상담사 숙련도, 근무 교대 기준을 같은 플레이북 안에서 충돌 없이 표현하는지가 관건입니다.

[구성 문서](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/configure-conversation-orchestration)를 확인하고 평상시뿐 아니라 대량 유입·전원 부재 상황도 점검하세요.

## 일정과 해석 주의

원문은 프리뷰 **2026년 4월**, GA **2026년 10월**을 표시하지만, 수집 시점 상태는 여전히 **In development**입니다. 목표 월에 도달했다는 이유만으로 전체 배포 완료로 단정하지 않아야 합니다.

> **출처**: [RM577788 — 자연어 플레이북 기반 conversation orchestration](https://mc.merill.net/message/RM577788) · [Microsoft 365 Roadmap 577788](https://www.microsoft.com/microsoft-365/roadmap?id=577788). 실제 출시 일정·기능은 변경될 수 있습니다.
