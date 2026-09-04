---
title: "외부 데이터를 복사하지 않고 실시간으로: Federated Copilot Connectors 정식 출시"
date: 2026-09-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - FederatedConnectors
  - MCP
  - Researcher
  - Excel
  - Governance
excerpt: "Federated Copilot Connectors가 정식 출시됩니다. Model Context Protocol(MCP)로 외부 데이터를 실시간 조회하되 Microsoft 서비스에 저장하거나 인덱싱하지 않고, 사용자 본인의 ID로 접근합니다. Researcher, Microsoft 365 Chat, Excel의 Agent Mode에서 지원됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 외부 데이터를 복사하지 않고 실시간으로: Federated Copilot Connectors 정식 출시

Copilot에 외부 업무 데이터를 연결하려 할 때 가장 먼저 나오는 질문은 보통 같습니다. **데이터가 Microsoft 쪽으로 복사되는가? 어디에 저장되는가? 원래 시스템의 권한은 그대로 적용되는가?**

**Federated Copilot Connectors**는 데이터를 미리 가져와 쌓는 대신 필요할 때 원본에서 실시간으로 조회하는 방식으로 이 질문에 답합니다. Microsoft는 메시지 센터 공지 **RM501120**을 통해 이 기능의 정식 출시(GA)를 알렸습니다.

---

## 작동 방식

Federated Copilot Connectors는 **Model Context Protocol(MCP)** 을 사용해 Copilot을 널리 쓰이는 서드파티 데이터 소스에 연결합니다.

핵심 원칙은 세 가지입니다.

- 외부 데이터를 **실시간으로 조회**합니다.
- 고객 데이터를 Microsoft 서비스에 **저장하거나 인덱싱하지 않습니다.**
- 데이터 접근에는 **사용자 본인의 ID**를 사용합니다.

따라서 사용자가 원본 시스템에서 볼 수 없는 정보가 Copilot을 통해 새로 열리는 구조가 아닙니다. 원본의 사용자 권한이 접근 범위를 결정합니다.

---

## 관리자의 통제권은 유지됩니다

데이터가 Microsoft에 복제되지 않더라도 관리자는 **Microsoft 365 관리 센터**를 통해 거버넌스와 통제권을 유지합니다.

도입 관점에서는 다음 두 요구를 함께 만족시키려는 설계입니다.

| 요구 | 대응 방식 |
|---|---|
| 데이터 이동 최소화 | 저장·인덱싱 없이 실시간 조회 |
| 조직 차원의 통제 | Microsoft 365 관리 센터에서 관리 |

---

## GA 지원 범위

정식 출시 시 Federated Copilot Connectors는 다음 세 영역에서 지원됩니다.

- **Researcher 에이전트**
- **Microsoft 365 Chat**
- **Excel의 Agent Mode**

특히 Excel Agent Mode가 포함된 점이 눈에 띕니다. 외부 시스템의 최신 데이터를 분석·정리하는 흐름을 Excel 작업과 직접 연결할 수 있기 때문입니다.

---

## 동기화 커넥터와 무엇이 다른가

최근 발표된 **Self-serve sync connectors**와 이름이 비슷하지만 데이터 처리 방식은 다릅니다.

| 구분 | Federated Connector | Self-serve Sync Connector |
|---|---|---|
| 데이터 처리 | 요청 시 실시간 조회 | 사용자가 접근 가능한 콘텐츠 동기화 |
| Microsoft 저장·인덱싱 | 하지 않음 | 검색 가능하도록 동기화 |
| 주요 기반 | MCP | 동기화 커넥터 |
| 적합한 상황 | 데이터 이동 제한, 실시간성 중요 | Copilot Chat·Microsoft Search 검색 활용 |

두 방식 중 무엇이 더 좋다기보다, 조직의 데이터 정책과 사용 목적에 따라 선택해야 합니다.

---

## 일정

| 구분 | 시점 |
|---|---|
| 미리 보기(Preview) | 2025년 12월 |
| 정식 출시(GA) | 2026년 4월 |

이번 메시지 센터 항목은 정식 출시를 알리는 공지이며, 표기된 GA 날짜는 **2026년 4월**입니다. 테넌트와 기능 표면별 실제 제공 상태는 Microsoft 365 Roadmap과 관리 센터에서 확인하는 것이 좋습니다.

---

## 도입 담당자를 위한 체크포인트

- **연결 대상의 MCP 지원 여부**를 확인하세요. Federated 방식은 MCP 기반입니다.
- **원본 권한을 먼저 정비**하세요. 사용자 본인 ID로 접근하므로 원본 시스템의 과도한 권한도 그대로 영향을 줍니다.
- **관리 센터의 허용 정책**을 설계하세요. 어떤 커넥터와 데이터 소스를 허용할지 사전에 정하는 것이 좋습니다.
- **실시간 조회 부하와 응답 시간**을 검토하세요. 인덱싱 방식과 달리 요청 때마다 원본 시스템에 접근합니다.
- **세 지원 영역을 각각 시험**하세요. Researcher, Microsoft 365 Chat, Excel Agent Mode는 사용 패턴과 결과물이 다릅니다.
- **동기화 방식과 혼동하지 않도록** 사용자·관리자 문서에서 두 커넥터 유형을 구분하세요.

---

## 마무리

Federated Copilot Connectors의 핵심은 **데이터를 옮기지 않고 Copilot의 업무 맥락으로 가져오는 것**입니다. 실시간성과 권한 승계, 관리자 통제를 함께 제공해 데이터 반출이나 인덱싱 때문에 외부 연동을 미뤘던 조직에 새로운 선택지를 줍니다.

---

> **출처**
>
> - 원문 ID: **RM501120** — *Microsoft Copilot (Microsoft 365): Federated Copilot Connectors*
> - 메시지 센터: [https://mc.merill.net/message/RM501120](https://mc.merill.net/message/RM501120)
> - Microsoft 365 로드맵: [https://www.microsoft.com/microsoft-365/roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
