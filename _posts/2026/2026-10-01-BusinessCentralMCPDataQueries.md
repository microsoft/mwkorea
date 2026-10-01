---
title: "Business Central MCP Server, 기존 API에 없는 데이터도 질의한다"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - BusinessCentral
  - MCP
  - DataQuery
  - CopilotStudio
  - Dynamics365
excerpt: "Business Central MCP Server에 사용자 지정 데이터 질의를 정의·검증·실행하는 도구가 추가됩니다. 기존 API가 없는 데이터도 MCP 애플리케이션에서 질의할 수 있어 에이전트 통합 범위가 넓어집니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Business Central MCP Server, 기존 API에 없는 데이터도 질의한다

Dynamics 365 Business Central MCP Server에 사용자 지정 데이터 질의를 **정의하고, 검증하고, 실행하는** 새 MCP 도구가 추가됩니다. 기존 API가 제공되지 않는 데이터도 MCP 애플리케이션에서 조회할 수 있게 하는 기능입니다.

에이전트 개발자는 필요한 API가 없어 통합을 포기하거나 별도 확장을 만들던 일부 시나리오를 MCP 질의로 처리할 수 있습니다. 다만 조회 범위가 넓어지는 만큼 성능과 권한 통제가 중요합니다.

---

## 제공되는 흐름

- 사용자 지정 데이터 query 정의
- query 유효성 검증
- 검증된 query 실행
- 기존 API가 없는 Business Central 데이터 조회

정의·검증·실행을 분리한 구조는 에이전트가 임의 질의를 바로 실행하는 위험을 줄이는 데 유용합니다. 실제 세부 스키마와 제한은 배포 문서에서 확인해야 합니다.

## 개발 시나리오

예를 들어 Copilot Studio 에이전트나 MCP 클라이언트가 표준 API에 없는 집계·조합 데이터를 읽어 업무 질문에 답할 수 있습니다. 별도 REST API를 만들기 전에 MCP query로 요구사항을 충족할 수 있는지 검토할 수 있습니다.

다만 이 기능을 쓰기 전에 다음을 확인해야 합니다.

- 호출 identity가 실제로 접근할 수 있는 회사·테이블·필드 범위
- 대량 조회, 필터 누락, 반복 호출에 대한 성능 제한
- 민감 필드가 에이전트 응답으로 노출되지 않도록 하는 정책
- query 정의와 실행의 감사 로그
- 기존 표준 API나 Business Central 확장이 더 적합한 경우

## 일정

GA는 **2026년 10월**로 예정되어 있습니다. 처음에는 읽기 전용의 좁은 질의로 시작하고, 실행 시간과 반환 행 수를 측정해 운영 한도를 정하는 것이 좋습니다.

> **출처**: 원문 ID **RM573312** · [mc.merill.net 원문](https://mc.merill.net/message/RM573312) · [Microsoft 365 Roadmap 573312](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=573312)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
