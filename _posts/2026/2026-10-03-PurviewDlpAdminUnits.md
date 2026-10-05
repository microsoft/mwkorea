---
title: "Purview DLP, 이제 관리 단위(AU) 기반으로 Copilot 정책도 위임 관리한다"
date: 2026-10-03T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftPurview
  - DLP
  - AdministrativeUnits
  - Compliance
  - Microsoft365Copilot
excerpt: "Microsoft Purview DLP가 Microsoft Entra 관리 단위(Administrative Units) 지원을 Copilot·Copilot Chat 정책까지 확장합니다. 지역·부서별로 Copilot DLP 정책 관리 권한을 위임할 수 있게 됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Purview DLP, 이제 관리 단위(AU) 기반으로 Copilot 정책도 위임 관리한다

여러 국가·부서로 구성된 조직에서는 데이터 손실 방지(DLP) 정책을 전사가 아니라 지역·부서 단위로 위임 관리하고 싶은 경우가 많습니다. Microsoft는 기존 Microsoft Entra **Administrative Units(관리 단위, AU)** 지원을 Microsoft Copilot과 Copilot Chat에 적용되는 DLP 정책까지 확장합니다.

새로운 관리 모델을 도입하는 것이 아니라, 기존 Microsoft Purview RBAC와 AU 기능을 그대로 확장하는 방식입니다.

---

## 핵심 변경 사항

- AU 범위로 제한된 관리자는 자신에게 할당된 AU 내에서 Copilot DLP 정책을 생성·조회·편집·삭제할 수 있습니다.
- 해당 관리자는 **전사 정책이나 다른 AU에 할당된 정책은 수정할 수 없습니다.**
- 기존 Purview RBAC 권한은 그대로 유지되며, 전사 Copilot DLP 정책도 지금처럼 동작합니다.
- 최종 사용자 입장에서는 새로운 워크플로우가 생기지 않습니다. Copilot 상호작용은 적용 가능한 전사 정책과 AU 정책 모두에 대해 계속 평가됩니다.
- AU 경계는 **콘텐츠의 소유자나 저장 위치가 아니라, Copilot과 상호작용을 시작한 사용자**를 기준으로 결정됩니다.

## 일정

- **Worldwide, GCC, GCC High, DoD:** 2026년 10월 말 시작, 2026년 11월 초 완료 예상

## 관리자 체크포인트

필수 조치는 없지만, AU 기반 Copilot DLP 정책 관리를 계획 중이라면 다음을 점검하세요.

- Microsoft Entra 관리 단위 구조와 멤버십 할당 검토
- Purview 역할 그룹 할당을 점검해 관리자가 담당 AU에만 배정되도록 조정
- AU 범위 정책을 만들기 전에 기존 전사 Copilot DLP 정책 재검토
- 신규 DLP 정책 생성 시 적절한 AU를 선택하고, 해당 AU 내 대상 사용자/그룹에 맞는 Copilot 정책 위치 구성

Purview DLP와 Microsoft Copilot의 기존 라이선스 요구사항은 그대로 적용됩니다.

## 마무리

글로벌 조직이나 규제 산업처럼 지역·부서별 컴플라이언스 경계가 중요한 환경에서는 이번 업데이트로 Copilot DLP 정책 관리 부담을 현업에 더 세밀하게 위임할 수 있게 됩니다. AU를 쓰지 않는 조직은 기존 정책을 바꿀 필요가 없습니다.

---

> 출처: MC1486284, [mc.merill.net 원문](https://mc.merill.net/message/MC1486284) — 실제 출시 일정·기능은 변경될 수 있습니다.
