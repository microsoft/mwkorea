---
title: "고객부터 연결하는 AI 콜백: Contact Center의 대기 경험 바꾸기"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - ContactCenter
  - Callback
  - Agent
excerpt: "Dynamics 365 Contact Center는 고객의 대기 순서를 유지하면서 고객을 먼저 연결하는 직접 콜백 경험을 제공합니다. 콜백 프로필 구성, AI 에이전트 선택과 큐 연결 시 주의할 점을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 고객부터 연결하는 AI 콜백: Contact Center의 대기 경험 바꾸기

콜백을 신청했는데 상담사가 연결될 때 전화를 놓치면 고객과 상담사 모두 시간을 잃습니다. Dynamics 365 Contact Center의 customer-first direct callback은 고객을 먼저 준비시키는 방식으로 이 문제에 접근합니다.

Roadmap RM577801에 따르면 고객은 대기 순서를 잃지 않으며, 차례가 되면 시스템이 콜백을 시작합니다. **고객이 준비된 후 상담사가 통화에 참여**하는 것이 핵심입니다.

---

## 콜백 프로필이 제어하는 경험

관리자는 **Copilot Service admin center의 callback profiles**에서 경험을 구성합니다. 프로필에 포함되는 설정은 인사말, 대체 전화번호 수집, 콜백 제공 시간대, 재시도 로직과 AI 에이전트 선택입니다.

기본 제공 AI 에이전트가 콜백 정보를 수집할 수 있고, 조직의 AI 에이전트로 고객 확인 같은 맞춤 흐름을 구현할 수도 있습니다. 원문은 특정 인증 방식이나 국내 본인확인 규격까지 보장하지는 않습니다.

## 큐에 연결하는 단계가 중요합니다

프로필을 만드는 것으로 설정이 끝나지 않습니다. 큐의 overflow handling에서 direct callback을 선택했다면 **해당 큐에 콜백 프로필도 지정**해야 합니다.

즉, 일반 문의와 우선 고객 큐에 서로 다른 인사말·제공 시간·검증 절차를 적용할 수 있습니다. 큐별 목적과 운영 시간을 정리한 뒤 프로필을 연결하는 것이 실무적으로 유리합니다.

## 한국 고객센터의 확인 항목

대체 연락처 수집 시 안내 문구, 재시도 횟수와 시간대, 고객 미응답 처리 방식은 도입 전에 확인할 항목입니다. 사용자 지정 에이전트로 본인 확인을 추가한다면 개인정보 처리와 상담사 인계 기준도 별도로 검토해야 합니다.

이는 원문이 국내 법규 준수를 인증했다는 뜻이 아니라, 실제 운영을 위해 조직이 점검할 사항입니다.

## 제공 상태

원문은 **GA 2026년 8월, Launched**로 표시합니다. Web 플랫폼이며 관리자·메이커가 최종 사용자를 위해 활성화하는 유형입니다. 클라우드 목록에는 Worldwide와 GCC, GCC High, DoD가 표시되지만 각 환경의 실제 제공 여부는 관리 환경에서 확인해야 합니다.

> **출처**: [RM577801 — 고객 우선 직접 콜백](https://mc.merill.net/message/RM577801) · [Microsoft 365 Roadmap 577801](https://www.microsoft.com/microsoft-365/roadmap?id=577801). 실제 출시 일정·기능은 변경될 수 있습니다.
