---
title: "Copilot Studio 비용 정책을 Microsoft 365 관리자 센터에서: 선택적 이전의 핵심"
date: 2026-10-30T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - CostManagement
  - CopilotCredits
  - Administration
excerpt: "Copilot Studio의 지원 대상 리소스 비용 통제를 Microsoft 365 관리자 센터의 Cost Management로 옮길 수 있게 됩니다. 환경별 선택적 이전이며 과거·신규 사용량 보고 위치가 달라지는 점을 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 비용 정책을 Microsoft 365 관리자 센터에서: 선택적 이전의 핵심

에이전트와 사용량 기반 AI 기능이 늘면 비용 통제도 여러 관리 화면에 분산됩니다. Microsoft는 지원되는 Copilot Studio 리소스의 Copilot Credit 지출을 Microsoft 365 관리자 센터에서 관리하는 선택지를 확장합니다.

하지만 모든 Copilot Studio 관리가 한 번에 이전되는 것은 아닙니다. **비용 정책과 관련 보고만 선택적으로 이동**하고 그 외 관리는 Power Platform 관리자 센터에 남습니다.

---

## 무엇을 제어하나요?

Cost Management의 spending policy를 지원되는 환경이나 개별 에이전트에 적용하거나, 지원 환경 여러 곳에 걸쳐 적용할 수 있습니다.

대상 이해관계자는 Microsoft 365 관리자 센터에서 비용을 관리하는 AI·Global 관리자, Power Platform 환경 관리자, Copilot Credit 사용과 지출을 살피는 청구·비용 관리자입니다. 지원되는 Microsoft 플랫폼 AI 서비스와 에이전트의 비용은 조직의 현지 통화로 표시된다고 안내됐습니다.

## 환경별 선택적 이전과 보고 분리

기존 환경에 자동 적용되지 않습니다. 관리자가 환경별로 이전을 선택하며, 이전한 환경에서는 Microsoft 365 관리자 센터의 spending policy가 활성 비용 통제가 됩니다.

| 데이터·관리 항목 | 이전 후 위치 |
|---|---|
| 이전 이후 새 사용량 | Microsoft 365 관리자 센터 |
| 이전 전 사용량 이력 | Power Platform 관리자 센터에 유지 |
| 이전하지 않은 환경 | 기존 Power Platform 비용 통제 유지 |
| 비용 외 Copilot Studio 관리 | Power Platform 관리자 센터 유지 |

내부 대시보드에서 한 화면의 보고만 읽으면 이력이 끊긴 것처럼 보일 수 있으므로 전환 시점을 기록해야 합니다.

## 일정과 준비 사항

원문 기준 **2026년 11월 20일까지 GA 예정**이며, 필수 이전 조치는 없습니다. 기존 환경·에이전트·Credit 용량·지출 통제, 정책 관리 권한과 보고 절차를 검토한 뒤 생산 환경 변경을 판단하는 것이 좋습니다.

국내 운영팀에서는 예산 책임자와 기술 관리자의 역할을 정리하고, 환경별 전환 전후 사용량을 어떻게 통합 보고할지 먼저 설계하세요.

> **출처**: MC1530368 — [Microsoft Copilot Studio cost controls are expanding to Cost Management in the Microsoft 365 admin center](https://mc.merill.net/message/MC1530368). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). 원문에 개별 Roadmap ID는 표시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
