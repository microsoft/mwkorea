---
title: "계정 대사부터 분개 초안까지, Excel과 Cowork의 회계 기능이 확장됩니다"
date: 2026-11-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Excel
  - Cowork
  - Finance
  - Accounting
excerpt: "Excel과 Cowork의 새 회계 기능이 계정 대사, 분개 초안, 차이 분석과 보고를 지원합니다. 11월 13일 GA 시작 예정이며 ERP 반영에는 사용자 승인이 필요하고 감사 추적의 제공 상태도 구분해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 계정 대사부터 분개 초안까지, Excel과 Cowork의 회계 기능이 확장됩니다

재무팀의 반복 업무는 숫자를 계산하는 데서 끝나지 않습니다. 잔액 차이의 원인을 찾고, 분개 근거를 정리하고, 검토자가 이해할 수 있는 보고서로 설명해야 합니다.

Microsoft는 Excel과 Cowork의 Copilot에 회계 업무 기능을 추가합니다. 핵심은 **Copilot이 준비하고 사람이 검토·승인·전기한다는 역할 분담**입니다.

---

## 어떤 업무를 돕나요?

- 계정 잔액과 거래를 비교해 차이를 찾고 대사 조정 항목을 준비합니다.
- 발생액, 재분류, 배부, 역분개, 반복 분개 초안을 만들고 필수 입력·차대 균형을 확인합니다.
- 계획 대비 실적과 주요 변동 요인을 분석하고 재무 보고를 준비합니다.
- 예산·예측, 감사, 세무, 컴플라이언스와 교육 업무도 지원합니다.

## 승인과 감사 추적의 경계

**사용자 승인 없이 ERP나 기준 시스템에 자동 전기하지 않습니다.** 기존 권한과 민감도 레이블을 존중하며 사용자가 접근 가능한 콘텐츠로 작업하고 Microsoft 365 서비스 경계 안에서 처리한다고 원문은 설명합니다.

기능 호출 시 감사 추적을 선택하면 무엇을 왜 바꿨는지 채팅 기록에 남길 수 있습니다. 다만 **원문 시점에 감사 추적은 Excel에서 제공되고 Cowork는 계획 단계**입니다. 두 환경 모두 이미 지원한다고 해석하면 안 됩니다.

ERP 읽기·쓰기에 커넥터를 별도 소스로 사용할 수 있지만 회계 기능 자체가 커넥터에 종속되지는 않습니다. 타사 회계 커넥터에는 별도 라이선스나 관리자 활성화가 필요할 수 있습니다.

## 프리뷰와 GA를 구분하세요

| 단계 | 일정·조건 |
|---|---|
| Public Preview | 2026년 10월 말~11월 중순 순차 배포, Copilot 라이선스와 Frontier 등록 필요 |
| 전 세계 GA | 2026년 11월 13일 시작, 11월 말 완료 예정, Frontier 등록 불필요 |

프리뷰 접근을 제공하려면 관리자 센터의 **Copilot > Settings > Frontier**에서 전체 적격 사용자 또는 재무팀 등 특정 사용자·그룹을 선택합니다. 관리자 자신도 Cowork 등 Frontier 기능을 보고 관리하려면 Frontier에 등록해야 한다고 안내됐습니다.

## 재무팀 도입 체크포인트

검토용 데이터와 운영 전기 권한을 분리하고, 승인자·감사 기록의 보존 기준을 정하는 것이 좋습니다. 한국 회계·세무 규정에 맞는지와 분석의 정확성은 별도 검토 대상이며, 원문이 특정 국가의 규정 준수를 자동 보장하는 것은 아닙니다.

> **출처**: MC1536053 — [Microsoft 365 Copilot: New accounting capabilities in Excel and Cowork](https://mc.merill.net/message/MC1536053). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). 원문에 개별 Roadmap ID는 표시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
