---
title: "조회에서 실행으로: Federated Copilot Connectors의 생성·수정·삭제 지원 예고"
date: 2026-09-23T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotConnectors
  - MCP
  - CopilotChat
  - Agent
  - Governance
excerpt: "MCP 유형의 Federated Copilot Connectors가 외부 서비스의 데이터 조회를 넘어 생성·수정·삭제 작업을 지원할 예정입니다. 2026년 10월 GA로 표기된 로드맵을 기준으로 사용자 확인, 외부 서비스 권한, 관리자 통제의 의미를 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 조회에서 실행으로: Federated Copilot Connectors의 생성·수정·삭제 지원 예고

Copilot에서 외부 업무 시스템의 정보를 조회한 다음, 실제 변경을 위해 다시 그 시스템으로 이동해야 한다면 업무 흐름이 끊깁니다. Microsoft는 이 간격을 줄이기 위해 **Federated Copilot Connectors의 작업 범위를 읽기에서 쓰기 작업까지 확대**하는 계획을 로드맵에 공개했습니다.

대상은 **MCP 유형의 Federated Copilot Connectors**입니다. RM570964는 Copilot Chat에서 외부 서비스의 콘텐츠를 생성·수정·삭제하는 커넥터 도구를 사용할 수 있게 한다고 설명합니다. 이 글은 2026년 10월 GA로 표기된 로드맵 기준이며, 지금 모든 연결에서 사용할 수 있다는 의미는 아닙니다.

---

## 무엇이 달라지나요?

현재 원문이 설명하는 Federated Copilot Connectors의 역할은 외부 서비스의 데이터를 실시간으로 읽는 것입니다. 이번 업데이트는 여기에 **create, update, delete 도구를 Copilot Chat에서 실행할 수 있도록 허용**하는 변화를 더합니다.

| 구분 | 원문에 설명된 범위 |
|---|---|
| 기존 | 외부 서비스의 데이터를 실시간 조회 |
| 업데이트 | 외부 서비스 콘텐츠의 생성·수정·삭제 도구 사용 |
| 사용자 경험 | Copilot을 떠나지 않고 작업 완료 |
| 실행 주체 | 외부 서비스에 대한 사용자 본인의 계정과 권한 |

이 설명은 모든 외부 서비스에 동일한 작업이 자동으로 생긴다는 뜻은 아닙니다. 실제로 가능한 작업은 해당 커넥터가 제공하는 도구와 연결 대상 서비스의 권한을 확인해야 합니다.

## 중요한 경계: 사용자 권한과 명시적 확인

원문은 **Copilot이 외부 서비스에서 사용자 본인의 계정과 권한으로 동작**한다고 명시합니다. 따라서 도입 검토에서는 Microsoft 365 쪽 설정만이 아니라, 연결 대상 서비스에서 사용자에게 어떤 생성·수정·삭제 권한이 부여돼 있는지도 살펴야 합니다.

또 하나의 핵심은 **모든 생성·수정·삭제 작업에 실행 전 사용자의 명시적 확인이 필요하다**는 점입니다. 이 로드맵을 사람이 확인하지 않는 무인 쓰기 자동화로 해석해서는 안 됩니다.

확인 단계가 있더라도 잘못된 대상 선택이나 과도한 권한 문제까지 자동으로 해결되는 것은 아닙니다. 실무에서는 변경 대상과 내용을 사용자가 이해하고 검토할 수 있는지까지 함께 점검하는 것이 좋습니다.

## 관리자는 무엇을 볼 수 있나요?

Microsoft는 관리자가 **Microsoft 365 admin center에서 각 커넥터의 읽기 도구와 쓰기·삭제 도구를 확인**하고, 조직 정책에 맞지 않는 커넥터를 비활성화할 수 있다고 안내합니다.

여기서 원문이 명시하는 통제 단위는 커넥터 비활성화입니다. 개별 쓰기 도구마다 별도의 차단 정책이 제공된다고 확대 해석하지 않는 것이 중요합니다. 실제 관리 화면과 세부 제어는 제공 시점의 기능을 확인해야 합니다.

## 한국 조직의 도입 체크포인트

1. 사용하는 MCP 유형 커넥터가 어떤 변경 도구를 제공하는지 목록화합니다.
2. 외부 서비스의 사용자 권한이 업무에 필요한 최소 범위인지 확인합니다.
3. 특히 삭제나 중요 정보 수정에서 사용자 확인 내용을 충분히 이해할 수 있는지 시험합니다.
4. 조직 정책에 맞지 않는 커넥터의 비활성화 기준과 담당자를 정합니다.
5. 연결 대상 서비스의 변경 이력, 복구 수단, 사고 대응 절차를 점검합니다.

마지막 항목은 운영 관점의 권고입니다. 이번 로드맵은 감사 로그의 세부 범위나 삭제 복구 기능, 지원 서비스 목록을 설명하지 않으므로, 해당 기능이 모두 포함돼 있다고 가정하면 안 됩니다.

## 일정과 마무리

상세 페이지의 **GA date는 October CY2026, 즉 2026년 10월**입니다. 정확한 배포 일자, 지원 지역, 서비스별 제공 순서는 이 항목에 명시돼 있지 않습니다.

이번 변화는 Copilot Chat을 정보를 묻는 공간에서 실제 업무를 처리하는 공간으로 확장합니다. 도입의 핵심은 기능 활성화 자체보다 **사용자 권한, 실행 전 확인, 커넥터 통제**를 하나의 운영 기준으로 준비하는 데 있습니다.

> **출처**: RM570964 — [Microsoft Copilot (Microsoft 365): Federated Copilot Connectors will support write, update and delete actions](https://mc.merill.net/message/RM570964).
> **Microsoft 365 Roadmap**: [570964](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=570964).
> 실제 출시 일정·기능은 변경될 수 있습니다.
