---
title: "항상 켜져 있는 개인 에이전트 Autopilot, Frontier에서 무엇을 확인해야 할까?"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Autopilot
  - Frontier
  - Agent365
  - Governance
excerpt: "Autopilot이 2026년 11월 17일부터 Frontier 공개 프리뷰에 단계적으로 제공됩니다. 초기 미국 고객 제한과 별도 신원·과금 요건, 메모리 및 규정 준수의 프리뷰 제한을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 항상 켜져 있는 개인 에이전트 Autopilot, Frontier에서 무엇을 확인해야 할까?

프롬프트마다 일을 요청하는 방식에서 목표를 위임하고 진행을 이어가는 방식으로 Copilot 경험이 확장됩니다. MC1557730은 항상 동작하는 클라우드 기반 개인 에이전트 **Autopilot**의 Frontier 공개 프리뷰 배포를 안내합니다.

다만 한국 조직에 즉시 제공된다는 발표는 아닙니다. 초기 대상은 자격을 갖춘 미국 고객이며, 기능은 기본 꺼짐 상태입니다. 편의성만큼 독립된 에이전트 신원과 미완성 규정 준수 범위를 먼저 이해해야 합니다.

---

## 별도 계정과 실행 환경을 가진 에이전트

Autopilot은 자체 계정·신원, 저장 공간과 사서함, 원격 컴퓨터를 갖습니다. 사용자의 일을 대신 수행할 때는 해당 사용자의 권한을 사용하며, 접근 제어와 승인 가드레일로 위임 범위를 관리합니다.

중요 작업을 자동 검사하지만 **일부 작업은 개별 확인 없이 진행될 수 있습니다**. 모든 행동마다 사용자가 승인한다고 가정해서는 안 됩니다.

## 일정과 필수 요건

Frontier Public 배포는 **2026년 11월 17일** 시작하며, 테넌트 활성화 전 관리자에게 24시간 사전 통지를 제공한다고 안내합니다. 적격 고객에게 단계적으로 배포되며 GA 일정은 별도 발표 예정입니다.

책임 사용자에게 Microsoft 365 Copilot 라이선스와 소비 기반 청구 활성화가 필요합니다. 공지가 제시한 필수 제어는 다음과 같습니다.

| 영역 | 공지의 필수 제어 |
|---|---|
| 신원 | 자동 프로비저닝되는 Microsoft Entra Agent ID |
| 격리 실행 환경 | Microsoft local(MXC) |
| 감사 및 비용 | Microsoft 365 audit logs, Agent 365 cost management |

라이선스 안내에는 필수 Microsoft Security 역량으로 **Intune P1/ME3, Microsoft 365 상용 라이선스**가 제시되어 있습니다. 이는 Frontier 프리뷰 기준이며 GA 시 요구사항이 달라질 수 있습니다.

## 활성화 절차와 권장 보호 수단

관리자는 Microsoft 365 관리 센터에서 Autopilot 접근을 켜고 Copilot Credits 청구 정책을 설정한 뒤, 보안 그룹에 사용을 허용해야 합니다. 전제조건이 갖춰지면 사용자는 Copilot Home 왼쪽의 Autopilot에서 **Create Your Autopilot**을 선택하고 Teams·Copilot 앱·Outlook으로 소통합니다.

원문은 Entra ID Governance, Global Secure Access, Conditional Access, Purview DLP와 Insider Risk Management, Defender XDR 및 Dynamic Agent Risk를 강력히 권장합니다. 관련 라이선스로 Entra Suite, Purview Suite/ME5, Defender Suite/ME5, Agent 365 유료 라이선스가 안내됩니다.

가장 강한 보안 구성의 추가 권고에는 제한 프리뷰 상태인 Microsoft Perception, Entra Conditional Access 동적 제어, Entra ID Governance 동적 권한이 포함되며, 해당 구성의 과금 안내는 사용자 기반 청구로 제시됩니다. 이를 기본 기능의 GA 보장으로 해석해서는 안 됩니다.

## 반드시 검토할 프리뷰 제한

이 릴리스에서는 **메모리가 항상 켜져 있고**, Microsoft 365 Copilot 개인화 설정이 적용되지 않습니다. 또한 Autopilot 대화는 아직 **eDiscovery·보존·법적 보존(legal hold)** 대상에 포함되지 않습니다.

한국 기업의 실무 검토에서는 이러한 제한이 기록 보존 의무, 민감정보 처리, 퇴사자 데이터 관리와 충돌하지 않는지 우선 확인해야 합니다. 초기 미국 고객 제한까지 고려하면 지금은 무조건 활성화할 단계라기보다 보안·법무·IT가 함께 도입 가능 조건을 정의할 시점입니다.

> **출처**: [MC1557730](https://mc.merill.net/message/MC1557730), Microsoft 365 Message Center Archive. [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제시되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
