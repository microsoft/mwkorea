---
title: "Business Central 목록에서 사람과 에이전트의 변경 이력이 보인다"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - BusinessCentral
  - AgentAvatars
  - Traceability
  - Dynamics365
excerpt: "Business Central 목록에 레코드를 생성하거나 마지막으로 수정한 사용자·에이전트의 아바타가 표시됩니다. 레코드를 열지 않고도 책임 주체와 자동화 관여 여부를 빠르게 파악할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Business Central 목록에서 사람과 에이전트의 변경 이력이 보인다

Dynamics 365 Business Central의 목록 페이지에 레코드를 생성하거나 마지막으로 수정한 주체의 **아바타**가 표시됩니다. 사람뿐 아니라 시스템 사용자와 AI 에이전트도 기존 identity model에 따라 구분됩니다.

공유 데이터에서 "누가 만들었고 누가 마지막으로 바꿨는가"를 확인하려고 레코드를 하나씩 열 필요가 줄어듭니다. 특히 에이전트가 만든 레코드가 늘어나는 환경에서 자동화의 흔적을 빠르게 파악할 수 있습니다.

---

## 표시되는 정보

- 레코드 생성자 또는 마지막 수정자의 시각적 아바타
- Business Central 사용자, 시스템 사용자, AI 에이전트 구분
- 마우스를 올렸을 때 전체 표시 이름
- 제공되는 경우 레코드 업데이트 시각

이 기능은 기존 **Created By**와 **Modified By** 필드를 더 직관적으로 보여 주는 방식입니다. 새로운 권한 우회 경로를 만드는 것이 아니며 Business Central의 데이터 개인정보 보호와 권한 모델을 따릅니다.

## 활용 가치

회계, 주문 처리, 창고, 서비스, 관리 업무처럼 여러 사람이 같은 목록을 다루는 팀은 담당자를 더 빨리 찾을 수 있습니다. 에이전트가 생성·수정한 항목도 즉시 식별할 수 있어 검토 우선순위를 정하는 데 도움이 됩니다.

다만 아바타는 책임 소재를 보여 주는 단서이지 전체 감사 로그를 대체하지 않습니다. 중요한 거래의 변경 이유와 이전 값은 기존 감사·변경 로그에서 확인해야 합니다.

## 일정과 준비

GA는 **2026년 10월**로 예정되어 있습니다. 조직은 표시 이름 규칙과 에이전트 명명 규칙을 정비하고, 사용자에게 사람·시스템·에이전트 아바타의 의미를 안내하는 것이 좋습니다.

> **출처**: 원문 ID **RM573364** · [mc.merill.net 원문](https://mc.merill.net/message/RM573364) · [Microsoft 365 Roadmap 573364](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=573364)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
