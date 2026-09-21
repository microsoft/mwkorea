---
title: "기존 Teams 보존 정책의 Copilot 적용 변경: Teams 전용으로 전환 예고"
date: 2026-09-19T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftPurview
  - DataLifecycleManagement
  - Retention
  - Teams
  - Roadmap
excerpt: "Copilot 상호작용에도 적용되던 일부 레거시 Teams 보존 정책이 Teams 전용 정책으로 취급될 예정입니다. 이 변경 뒤에는 해당 정책이 Copilot 워크로드를 암묵적으로 관리하지 않으므로, 기존 보존 적용 범위를 살펴볼 필요가 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 기존 Teams 보존 정책의 Copilot 적용 변경: Teams 전용으로 전환 예고

오래전에 만든 보존 정책을 유지하고 있다면 이름과 실제 적용 범위가 같은지 확인할 필요가 있습니다. 특히 한 워크로드용 정책이 다른 서비스의 상호작용에도 적용되어 왔다면 변경 시 영향을 놓치기 쉽습니다.

로드맵 **571306**, 수집 ID **RM571306**은 일부 기존 Teams 보존 정책이 Microsoft 365 Copilot 상호작용에도 적용될 수 있으며, 이 레거시 정책을 **Teams 전용으로 전환해 취급할 예정**이라고 설명합니다.

---

## 무엇이 바뀌나요

| 구분 | 원문 설명 |
|---|---|
| 변경 대상 | Copilot에도 적용되던 일부 레거시 Teams 보존 정책 |
| 변경 후 | Teams 전용 정책으로 전환·취급 |
| Copilot 영향 | 해당 정책이 Copilot 워크로드를 더 이상 암묵적으로 관리하지 않음 |
| GA 표기 | 2026년 10월 |

대상은 **일부 레거시 정책**입니다. 모든 Teams 정책이나 모든 Copilot 보존 정책이 제거된다는 발표는 아닙니다.

## 현재 보존 범위를 점검할 때

보존 담당자는 Copilot 상호작용이 어떤 정책의 적용을 받는지 확인하고, Teams 정책의 기존 동작에 의존하는 부분이 있는지 살펴볼 수 있습니다. 변경 후에도 조직이 의도한 보존 요구를 충족하는지 검토하는 것이 목적입니다.

다만 이 로드맵 설명에는 대상 정책을 찾는 구체적인 명령, 자동 전환 절차, 별도 Copilot 정책 구성 방법이 포함되지 않았습니다. 따라서 확인되지 않은 명령으로 기존 정책을 삭제하거나 다시 만들도록 안내하지 않습니다.

## 데이터 삭제와 동일한 의미는 아닙니다

이 공지는 정책의 적용 범위를 설명합니다. 전환과 동시에 기존 Copilot 데이터가 즉시 삭제되거나 보존이 무조건 중단된다고 단정할 근거는 없습니다. 실제 데이터 처리는 다른 적용 정책과 제품 안내를 함께 살펴야 합니다.

2026년 10월 GA가 예고된 만큼, 관리 문서에 Teams와 Copilot의 보존 책임을 따로 정리하고 후속 상세 안내를 반영하는 것이 좋습니다.

---

> **출처**
>
> - 원문 ID: **RM571306** — *Microsoft Purview: Data Lifecycle Management-Legacy Teams retention policies covering Copilot will be treated as Teams-only*
> - 원문: [RM571306](https://mc.merill.net/message/RM571306)
> - [Microsoft 365 Roadmap 571306](https://www.microsoft.com/microsoft-365/roadmap?id=571306)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
