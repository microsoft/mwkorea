---
title: "Business Central Payables Agent, PO 매칭 정확도를 높인다"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - BusinessCentral
  - PayablesAgent
  - PurchaseOrder
  - AccountsPayable
  - Dynamics365
excerpt: "Business Central Payables Agent가 금액과 예상 입고일을 활용해 구매 주문 행을 더 정확히 매칭합니다. 초안 완료와 입고 통제를 분리하고, 공급업체·주문·주문 행 단위 설정도 확장됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Business Central Payables Agent, PO 매칭 정확도를 높인다

Dynamics 365 Business Central의 Payables Agent가 구매 송장 초안을 구매 주문(PO)과 연결할 때 더 많은 정보를 사용합니다. 설명과 수량뿐 아니라 **Line Amount**와 **Expected Receipt Date**를 비교해 비슷한 PO 행 사이의 오매칭을 줄이는 업데이트입니다.

서비스처럼 수량이 대부분 1인 항목에서는 금액이 중요한 구분 기준입니다. 여러 주문 행이 비슷할 때는 예상 입고일도 매칭 판단에 도움이 됩니다.

---

## 달라지는 매칭 기준

에이전트가 사용하는 확장된 PO Lines 목록에는 다음 필드가 포함됩니다.

- **Line Amount**: 설명과 수량이 같거나 비슷한 서비스 행을 금액으로 구분
- **Expected Receipt Date**: 여러 후보 중 실제 거래 시점과 가까운 행을 판단

초안 경고도 수량뿐 아니라 금액 차이까지 보여 줍니다. 이 경고는 정보 제공용이며 초안 완료를 막지는 않습니다. 담당자가 차이를 검토한 뒤 계속 진행할지 결정할 수 있습니다.

## 초안 완료와 입고 통제 분리

Payables Agent는 구매 주문의 **Receipt on Invoice** 설정에 있는 `Never block draft finalization` 동작을 따릅니다. 매칭된 주문 행이 아직 입고 처리되지 않았다는 이유만으로 송장 초안 완료를 막지 않습니다.

이는 입고 여부를 **초안 작성 단계가 아니라 게시(posting) 단계의 통제**로 보는 설계입니다. 최종 게시 시점의 동작은 기존 Receipt on Invoice 설정이 계속 관장합니다.

## 설정 범위와 상속

Receipt on Invoice 설정은 다음 계층으로 확장됩니다.

1. 공급업체 설정이 새 구매 주문의 기본값이 됩니다.
2. 구매 주문 수준에서 공급업체 기본값을 재정의할 수 있습니다.
3. 구매 주문 행 수준에서 다시 개별 재정의할 수 있습니다.

상속 순서는 **공급업체 → 구매 주문 → 구매 주문 행**이며 각 단계가 상위 값을 덮어쓸 수 있습니다. 도입 전에는 기존 주문 통제 정책과 에이전트 초안 승인 절차가 충돌하지 않는지 확인해야 합니다.

## 일정과 도입 체크포인트

GA는 **2026년 10월**로 예정되어 있습니다. 회계팀은 서비스 PO, 부분 입고, 금액 차이와 같은 대표 사례를 테스트 데이터로 준비하고, 정보성 경고와 실제 게시 차단을 사용자 교육에서 명확히 구분하는 것이 좋습니다.

> **출처**: 원문 ID **RM573380** · [mc.merill.net 원문](https://mc.merill.net/message/RM573380) · [Microsoft 365 Roadmap 573380](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=573380)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
