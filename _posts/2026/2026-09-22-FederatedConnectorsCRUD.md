---
title: "Microsoft 365 Copilot 연합 커넥터, 생성·수정·삭제 액션까지 지원"
date: 2026-09-22T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - FederatedConnector
  - Governance
  - ThirdParty
excerpt: "Microsoft 365 Copilot의 연합(federated) 커넥터가 서드파티 서비스에서 생성·수정·삭제(CRUD) 액션까지 지원합니다. 모든 액션은 사용자 승인과 사용자 권한 범위 내에서만 실행됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Microsoft 365 Copilot 연합 커넥터, 생성·수정·삭제 액션까지 지원

그동안 Microsoft 365 Copilot의 연합(federated) 커넥터는 주로 조회(read) 중심이었습니다. 이제 서드파티 서비스에 대해 **생성(create), 수정(update), 삭제(delete)** 액션까지 수행할 수 있도록 범위가 넓어집니다.

---

## 핵심 내용과 안전장치

- **2026년 10월부터** 연합 커넥터가 서드파티 서비스에서 생성·수정·삭제 액션을 지원합니다.
- 모든 액션은 **사용자 승인(user approval)**을 거쳐야 실행됩니다.
- 액션은 **사용자 본인의 권한(user's permissions)** 범위 내에서만 수행됩니다 — 즉 에이전트가 사용자보다 더 큰 권한으로 데이터를 변경할 수 없습니다.
- 관리자는 **관리센터에서 커넥터를 검토하고 비활성화**할 수 있습니다.
- 사용자가 이 기능을 받기 위해 별도로 취할 조치는 없습니다.

## 관리자 체크리스트

관리자는 어떤 연합 커넥터가 쓰기 작업을 수행할 수 있게 됐는지 관리센터에서 검토하고, 보안 정책상 허용되지 않는 커넥터는 사전에 비활성화할 수 있습니다.

## 한국 조직을 위한 체크포인트

- "사용자 권한 범위 내에서만" 실행된다는 원칙은 권한 상승(privilege escalation) 우려를 완화하는 핵심 장치입니다. 다만 사용자 승인 UX가 실제로 어떻게 노출되는지는 롤아웃 이후 직접 확인해볼 필요가 있습니다.
- 외부 SaaS 도구(ERP, 티켓팅 시스템 등)와 연동된 커넥터를 쓰는 조직이라면, 10월 적용 전에 어떤 커넥터에 쓰기 권한을 허용할지 내부 정책을 미리 정리해두는 것이 좋습니다.
- 관리센터의 커넥터 검토·비활성화 기능을 활용해, 민감한 시스템과 연동된 커넥터는 화이트리스트 방식으로 운영하는 것을 권장합니다.

---

> **원문**: Microsoft 365 Copilot: Federated Copilot connectors support create, update, and delete actions (MC1476316) — [mc.merill.net에서 보기](https://mc.merill.net/message/MC1476316) | [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
