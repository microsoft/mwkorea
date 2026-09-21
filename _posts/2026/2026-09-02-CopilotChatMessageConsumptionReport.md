---
title: "Copilot Chat 종량제 비용을 메시지 단위로 보기: 새 사용량 보고서"
date: 2026-09-02T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotChat
  - PayAsYouGo
  - UsageReport
  - CostManagement
  - AdminCenter
excerpt: "Microsoft 365 관리 센터에 Copilot Chat 종량제의 청구 메시지를 보여 주는 Message consumption 보고서가 추가됩니다. 현재 공개 미리 보기에서 제공되는 범위와 2027년 1월로 변경된 정식 출시 일정, 관리자가 확인할 항목을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Chat 종량제 비용을 메시지 단위로 보기: 새 사용량 보고서

Copilot Chat과 에이전트를 종량제로 운영하면 총비용만 보는 것으로는 어느 사용자나 에이전트에서 소비가 늘었는지 파악하기 어렵습니다. Microsoft는 청구 대상 메시지의 흐름을 여러 수준으로 나눠 볼 수 있는 **Message consumption** 사용량 보고서를 Microsoft 365 관리 센터에 제공합니다.

메시지 센터 **MC1069563**은 이 기능이 Microsoft 365 Copilot Chat의 **pay-as-you-go 청구 정책**에 연결된 소비를 관리하기 위한 것이라고 설명합니다. 이 공지는 좌석형 Microsoft 365 Copilot 라이선스 사용량 보고서가 아니며, 종량제 모델에는 Microsoft Copilot 라이선스가 필요하지 않다고 명시합니다.

---

## 보고서에서 확인할 수 있는 항목

보고서는 청구 메시지의 총량, 누적 추이, 일별 시계열을 제공합니다. 세부적으로는 다음 기준으로 소비를 확인할 수 있습니다.

- 사용자별
- 종량제 청구 정책별
- 에이전트별
- 에이전트와 사용자 조합별
- 테넌트 전체

사용자가 청구 메시지를 **2,000개 초과** 소비하면 과다 지출을 완화하기 위한 알림도 표시됩니다. 이 수치는 공지가 설명한 사용자 소비 알림 기준이며, 자동 차단 한도나 모든 청구 정책의 예산 상한이라는 뜻은 아닙니다.

![Microsoft 365 관리 센터의 Message consumption 보고서](/mwkorea/assets/images/2026-09-02-CopilotChatMessageConsumptionReport/image1.png)

## 미리 보기의 데이터 범위와 전제 조건

공개 미리 보기에서는 최대 **30일**의 메시지 소비 이력을 표시합니다. 2025년 5월 3일 이전 사용량은 보고서에서 제공되지 않습니다.

보고서를 보려면 Microsoft 365 관리 센터 또는 Microsoft Power Platform 관리 센터에서 Copilot 종량제 청구를 설정하고, 조직에서 에이전트 사용을 활성화해야 합니다. 설정 뒤 관리 센터의 **Reporting > Usage > Microsoft 365 Copilot > Message consumption**에서 확인할 수 있으며 기능은 기본 제공됩니다.

## 현재 상태와 변경된 일정

| 단계 | 최신 공지 |
|---|---|
| 공개 미리 보기 | 현재 사용 가능 |
| 정식 출시, 전 세계 | 2027년 1월 초 시작, 1월 말 완료 예정 |

2026년 9월 1일 업데이트에서 정식 출시가 기존 **2026년 9월**에서 **2027년 1월**로 변경됐습니다. 따라서 지금 사용할 수 있다는 표현은 공개 미리 보기 기준입니다. 정식 기능의 범위나 보존 기간이 미리 보기와 같을 것이라고 미리 단정하면 안 됩니다.

## 비용 관리 담당자의 준비 사항

배포 전에 필수 작업은 없으며 일정에 따라 자동 제공됩니다. 다만 종량제 비용을 실제로 관리하려면 다음 운영 절차를 마련하는 것이 좋습니다.

- 통합 앱과 에이전트를 관리하는 담당자에게 새 보고서 위치 안내
- 청구 정책별 소유자와 비용 검토 주기 지정
- 사용자·에이전트·에이전트-사용자 조합별 급증 원인 확인
- 2,000개 초과 알림을 예산 검토나 사용자 안내 절차에 연결
- 내보내거나 공유한 사용량 데이터의 접근 범위와 보존 정책 점검

보고서는 소비 가시성을 제공하지만 청구 구성을 대신하거나 지출을 자동 최적화하지는 않습니다. 미리 보기에서는 30일 범위라는 제한을 고려해 재무 기록이나 장기 추세 분석에 필요한 데이터 보관 방식을 별도로 검토하세요.

---

> **출처**
>
> - 원문 ID: **MC1069563** — *Microsoft 365 admin center: Usage reports to manage metered consumption costs for Microsoft 365 Copilot Chat (preview)*
> - 원문: [MC1069563](https://mc.merill.net/message/MC1069563)
> - Microsoft 365 Roadmap: [490738](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=490738)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
