---
title: "Business Central 에이전트가 추가 권한을 요청할 수 있다"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - BusinessCentral
  - AgentPermissions
  - Governance
  - Dynamics365
excerpt: "Business Central에서 에이전트가 작업에 필요한 추가 권한을 요청하고 관리자가 이를 할당할 수 있게 됩니다. 에이전트 권한 운영의 병목을 줄이되 최소 권한 원칙은 그대로 지켜야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Business Central 에이전트가 추가 권한을 요청할 수 있다

Dynamics 365 Business Central이 에이전트 권한 관리를 단순화합니다. 에이전트가 작업 수행에 필요한 추가 권한을 요청하면 관리자가 그 요청을 바탕으로 권한을 할당할 수 있는 기능입니다.

에이전트 도입 과정에서 흔한 실패 원인은 기능 자체보다 권한 부족입니다. 반대로 문제를 빨리 해결하려고 과도한 권한을 부여하면 데이터 접근과 변경 위험이 커집니다. 이번 기능은 그 사이의 운영 절차를 제품 안에서 연결하는 변화로 볼 수 있습니다.

---

## 기대 효과

- 권한 부족으로 중단된 에이전트 작업의 원인을 더 쉽게 파악
- 필요한 권한을 요청 단위로 검토
- 에이전트별 권한 부여 절차의 표준화
- 운영팀과 업무 담당자 사이의 반복 문의 감소

현재 로드맵 설명에는 요청 화면, 승인 주체, 자동 만료, 감사 로그와 같은 상세 동작이 공개되지 않았습니다. 실제 배포 전까지는 기존 권한 관리 체계와 결합 방식을 확인해야 합니다.

## 거버넌스 체크포인트

추가 권한 요청을 편의 기능으로만 보지 말고 다음 원칙을 적용하는 것이 좋습니다.

1. 요청한 작업에 필요한 최소 권한만 부여합니다.
2. 읽기와 쓰기 권한을 구분하고 고위험 변경은 별도 승인합니다.
3. 에이전트별 소유자와 정기 검토 주기를 지정합니다.
4. 권한 요청·승인·사용 내역을 감사 가능한 형태로 남깁니다.
5. 임시 업무라면 권한 만료 또는 회수 절차를 운영합니다.

## 일정

GA는 **2026년 10월**로 예정되어 있습니다. 기능이 배포되면 권한 요청이 누구에게 전달되는지, 기존 permission set과 어떤 관계인지, 요청 거절 후 사용자에게 어떤 메시지가 보이는지를 먼저 검증해야 합니다.

> **출처**: 원문 ID **RM573370** · [mc.merill.net 원문](https://mc.merill.net/message/RM573370) · [Microsoft 365 Roadmap 573370](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=573370)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
