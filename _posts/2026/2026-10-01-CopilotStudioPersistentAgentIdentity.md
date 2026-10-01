---
title: "Copilot Studio 에이전트에 독립 Microsoft 365 계정이 생긴다"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - AgentIdentity
  - Microsoft365
  - Governance
  - EntraID
excerpt: "Copilot Studio 에이전트에 메일함·Teams presence·Office 접근을 갖춘 독립 Microsoft 365 ID를 부여할 수 있게 됩니다. 공유 업무 프로세스의 주체를 명확히 하면서 관리자가 정책과 접근을 통제할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 에이전트에 독립 Microsoft 365 계정이 생긴다

Copilot Studio 메이커가 에이전트에 **자체 계정**을 부여할 수 있게 됩니다. 에이전트는 공유 비즈니스 프로세스를 수행하는 독립 Microsoft 365 identity로서 메일함, Teams presence, Office 접근을 사용할 수 있습니다.

지금까지 사용자나 연결 소유자의 신원에 의존하던 자동화와 달리, 에이전트 자체를 첫 번째 클래스의 관리 대상(entity)으로 운영할 수 있다는 점이 핵심입니다.

---

## persistent identity가 제공하는 것

- 에이전트 자체 메일함
- Teams에서 식별 가능한 presence
- Office 리소스 접근
- 팀을 가로지르는 공유 프로세스의 지속적 실행 주체
- 관리자의 접근·정책·사용 통제

담당자가 바뀌거나 퇴사해도 에이전트 프로세스가 개인 계정에 묶여 중단되는 문제를 줄일 수 있습니다. 사용자 입장에서도 누가 보낸 메일인지, 사람이 아니라 어떤 에이전트가 참여했는지를 더 명확히 알 수 있습니다.

## 거버넌스 체크포인트

독립 ID는 편리하지만 사람 계정과 같은 수준의 수명 주기 관리가 필요합니다.

1. 에이전트 소유자와 업무 목적을 등록합니다.
2. 최소 권한과 조건부 액세스 적용 가능 범위를 확인합니다.
3. 메일함 보존, eDiscovery, 감사 정책을 검토합니다.
4. Teams·Office 접근 범위를 업무에 필요한 리소스로 제한합니다.
5. 에이전트 폐기 시 ID와 데이터의 비활성화·보존 절차를 정합니다.

공용 서비스 계정을 단순히 에이전트로 이름만 바꾸는 방식이 아니라, 제품이 제공하는 관리형 identity 모델과 라이선스·정책 요건을 확인해야 합니다.

## 일정

Preview는 **2026년 9월**, GA는 **2026년 11월**로 예정되어 있습니다. Preview에서 만든 ID가 GA까지 어떤 정책과 관리 API를 지원하는지 확인한 뒤 프로덕션 적용 범위를 결정하는 것이 좋습니다.

> **출처**: 원문 ID **RM570430** · [mc.merill.net 원문](https://mc.merill.net/message/RM570430) · [Microsoft 365 Roadmap 570430](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=570430)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
