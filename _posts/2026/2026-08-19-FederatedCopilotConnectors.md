---
title: "데이터를 복사하지 않고 연결한다: Federated Copilot Connectors와 MCP"
date: 2026-08-19T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotConnectors
  - MCP
  - ModelContextProtocol
  - Researcher
  - Governance
  - Roadmap
excerpt: "Federated Copilot Connectors는 Model Context Protocol(MCP)을 통해 서드파티 데이터를 실시간으로 가져옵니다. 데이터를 Microsoft에 저장하거나 인덱싱하지 않고 사용자 본인의 ID로 접근하며, 관리자는 관리 센터에서 통제권을 유지합니다. 2026년 9월 정식 출시 예정입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 데이터를 복사하지 않고 연결한다: Federated Copilot Connectors와 MCP

Copilot에 사내 데이터를 연결할 때 가장 먼저 나오는 질문은 대체로 같습니다. **"그 데이터가 어디에 저장되나요?"**

기존 Copilot 커넥터 방식은 외부 데이터를 Microsoft 365에 **인덱싱**해 두고 검색에 활용하는 구조였습니다. 성능 면에서는 유리하지만, 데이터가 원래 있던 시스템 밖으로 복제된다는 점 때문에 보안·컴플라이언스 검토가 길어지는 경우가 많았습니다. 특히 금융, 공공, 제조처럼 데이터 반출에 민감한 영역에서는 이 단계에서 막히는 일이 흔했습니다.

메시지 센터 공지 **RM569212**로 안내된 **Federated Copilot Connectors in Microsoft 365 Copilot**은 접근 방식 자체를 바꿉니다. 데이터를 **가져와 쌓지 않고, 필요할 때 실시간으로 연결**합니다.

---

## 무엇이 달라지나요

### 실시간 조회, MCP 기반

Federated Copilot 커넥터는 사용자가 원하는 **서드파티 소스**에 Microsoft Copilot을 안전하게 연결하고, **Model Context Protocol(MCP)** 을 사용해 데이터를 **실시간으로 조회(retrieve in real-time)** 합니다.

MCP는 AI 모델과 외부 데이터·도구를 연결하는 개방형 프로토콜입니다. Microsoft가 이 표준 위에서 커넥터를 구현했다는 것은, 특정 벤더에 종속되지 않는 방식으로 연결 생태계를 넓히겠다는 의미로 읽힙니다.

### 저장하지 않고 인덱싱하지 않는다

공지에서 가장 분명하게 강조된 부분입니다.

> Federated Copilot 커넥터는 고객 데이터를 **Microsoft에 저장하거나 인덱싱하지 않습니다.** 접근은 **사용자 본인의 ID(user's own identity)** 를 사용해 실시간으로 이뤄집니다.

이 문장은 두 가지를 함께 담고 있습니다.

- **데이터 이동 없음** — 원본 시스템에 그대로 두고 필요할 때만 조회
- **권한 승계** — 사용자 본인의 ID로 접근하므로, 원본 시스템에서 그 사용자가 볼 수 없는 데이터는 Copilot을 통해서도 볼 수 없음

권한 승계는 특히 중요합니다. 별도의 서비스 계정으로 데이터를 긁어 오는 방식이 아니기 때문에, **원본 시스템의 접근 통제가 그대로 살아 있습니다.**

### 관리자 거버넌스 유지

데이터가 Microsoft에 쌓이지 않더라도 관리자가 손을 놓게 되는 것은 아닙니다. 관리자는 **Microsoft 365 관리 센터(Microsoft 365 Admin Center)** 를 통해 **완전한 거버넌스와 통제권(full governance and control)** 을 유지합니다.

### 지원 범위

정식 출시(GA) 시점에 Federated Copilot 커넥터는 다음 영역에서 지원됩니다.

- **Researcher 에이전트**
- **Microsoft 365 Chat**

즉 심층 조사를 수행하는 Researcher와 일상적인 Copilot 채팅 양쪽에서 외부 데이터를 업무 흐름에 끌어올 수 있습니다.

---

## 기존 방식과 무엇이 다른가

| 구분 | 기존 인덱싱 방식 | Federated 방식 |
|---|---|---|
| 데이터 위치 | Microsoft 365에 인덱싱 | 원본 시스템에 그대로 유지 |
| 조회 시점 | 사전 인덱싱된 데이터 검색 | 요청 시 실시간 조회 |
| 접근 주체 | 커넥터 구성에 따름 | 사용자 본인의 ID |
| 프로토콜 | 커넥터별 구현 | Model Context Protocol(MCP) |
| 최신성 | 인덱싱 주기에 의존 | 실시간 |

두 방식은 대체 관계라기보다 **선택지가 늘어난 것**으로 보는 편이 맞습니다. 대량 검색 성능이 중요한 데이터는 인덱싱이 유리하고, 실시간성·데이터 반출 제약이 중요한 데이터는 Federated가 적합합니다.

---

## 왜 의미가 있나요

한국의 도입 현장에서 자주 마주치는 상황에 대입해 보면 이렇습니다.

- **데이터 반출 제약이 있는 조직** — "사내 시스템 데이터를 외부 클라우드에 인덱싱할 수 없다"는 정책 때문에 연동을 포기했던 경우, 실시간 조회 방식이 대안이 됩니다.
- **최신성이 중요한 데이터** — 재고, 주문 상태, 티켓 현황처럼 수시로 바뀌는 정보는 인덱싱 주기 때문에 값이 어긋날 수 있습니다. 실시간 조회는 이 문제에서 자유롭습니다.
- **권한 체계가 복잡한 시스템** — 원본 시스템의 세밀한 권한을 인덱스에 정확히 반영하기는 어렵습니다. 사용자 ID 기반 실시간 접근은 이 문제를 구조적으로 우회합니다.
- **Researcher 활용 확대** — 심층 조사 과정에서 사내 시스템의 실제 데이터를 참조할 수 있다면, 조사 결과의 실무 적합도가 올라갑니다.

---

## 일정

| 구분 | 시점 |
|---|---|
| 정식 출시(GA) | 2026년 9월 |

**2026년 9월 정식 출시**로 임박한 일정입니다. 외부 시스템 연동을 검토 중이라면 지금이 준비 시점입니다.

---

## 도입 담당자를 위한 체크포인트

- **연결 대상 시스템의 MCP 지원 확인**: 이 방식은 **MCP를 통해** 동작합니다. 연결하려는 서드파티 소스가 MCP를 지원하는지 먼저 확인해야 합니다.
- **원본 시스템의 권한 체계 점검**: 사용자 본인의 ID로 접근하므로, **원본 시스템의 접근 통제가 그대로 결과에 반영**됩니다. 원본 권한이 느슨하면 Copilot을 통한 노출 범위도 넓어집니다. 연동 전에 원본 시스템의 권한 정리를 먼저 하세요.
- **관리 센터에서의 통제 항목 파악**: 관리자는 관리 센터를 통해 거버넌스를 유지합니다. **어떤 커넥터를 허용할지, 누구에게 허용할지**에 대한 정책을 사전에 정의해 두는 것이 좋습니다.
- **지원 범위 인지**: GA 시점 지원 범위는 **Researcher 에이전트와 Microsoft 365 Chat**입니다. 다른 Copilot 표면에서의 동작은 별도 안내를 확인해야 합니다.
- **실시간 조회의 성격 이해**: 인덱싱하지 않으므로 원본 시스템에 실시간 요청이 발생합니다. **연결 대상 시스템의 부하와 응답 속도**를 함께 검토하세요.
- **라이선스 전제**: 공지의 제품 분류에 **Microsoft Copilot (Microsoft 365)** 가 포함되어 있습니다.

---

## 마무리

"데이터를 어디에 두느냐"는 지금까지 AI 도입에서 가장 자주 걸리는 관문이었습니다. Federated Copilot Connectors는 **데이터를 옮기지 않는 선택지**를 제공하면서 이 관문을 다르게 통과하려 합니다. MCP라는 개방형 표준 위에 올린 점, 사용자 ID 기반 접근으로 권한 문제를 구조적으로 처리한 점, 그러면서도 관리자 통제권을 관리 센터에 남겨 둔 점이 함께 맞물립니다.

정식 출시가 2026년 9월로 예정되어 있습니다. 그동안 데이터 반출 문제로 미뤄 두었던 연동 과제가 있다면, 이번 방식으로 다시 검토해 볼 만합니다.

---

> **출처**
>
> - 원문 ID: **RM569212** — *Microsoft Copilot (Microsoft 365): Federated Copilot Connectors in Microsoft 365 Copilot*
> - 메시지 센터: [https://mc.merill.net/message/RM569212](https://mc.merill.net/message/RM569212)
> - Microsoft 365 로드맵: [https://www.microsoft.com/microsoft-365/roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
