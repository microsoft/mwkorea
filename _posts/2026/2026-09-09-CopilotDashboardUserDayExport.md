---
title: "Copilot 도입 효과를 일 단위로: 최근 28일 user-day 내보내기"
date: 2026-09-09T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotAnalytics
  - VivaInsights
  - Adoption
  - Governance
excerpt: "Copilot dashboard에서 비식별화된 사용자별·일별 사용 지표를 내보내는 기능이 제공됩니다. 최근 28일 분석, 최소 50개 라이선스, 전사 데이터 접근 권한과 VFAM 제어 등 실제 도입 조건을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 도입 효과를 일 단위로: 최근 28일 user-day 내보내기

Copilot 교육 다음 날 실제 사용이 늘었는지, 특정 앱 활용이 어느 요일에 집중되는지 알고 싶다면 주간 집계만으로는 부족할 수 있습니다. Copilot dashboard의 **user-day export**는 사용자·일 단위로 집계한 비식별화 지표를 내보내 단기 도입 추세를 분석하도록 돕습니다.

2026년 9월 8일 업데이트된 MC1222978은 Public Preview와 이후 GA 일정을 구분해 안내합니다. 이 글의 파일 날짜는 해당 RSS pubDate의 한국 시간 기준입니다.

---

## 무엇을 내보낼 수 있나요?

기존 user-week 내보내기에 더해, **최근 28일**의 일부 Copilot 사용 지표를 사용자·일별 행 단위 데이터로 제공합니다. Word, Excel, Teams 등 Copilot 지원 앱의 분석을 돕고 **Organization, Job function** 속성도 포함합니다.

![Copilot dashboard의 데이터 내보내기 버튼](/mwkorea/assets/images/2026-09-09-CopilotDashboardUserDayExport/image1.png)

사용량은 보통 내보낸 날짜보다 **최대 약 3일 이전까지의 활동**을 반영하며 실제 시차는 달라질 수 있습니다. 실시간 대시보드나 즉시 반영되는 감사 로그로 해석해서는 안 됩니다.

## 최소 라이선스와 접근 권한

이 기능은 **Viva Insights 웹 앱**에 적용되며 Microsoft 365 Copilot 라이선스가 최소 **50개** 필요합니다. 또한 dashboard의 **전사 수준 데이터 접근 권한**이 있어야 합니다.

대상에는 Entra ID에서 식별된 고위 리더, 관리자가 지정한 전사 사용자, 전사 접근 권한이 있는 위임 사용자, 전역 분석가와 관리자가 포함됩니다. 자기 팀 데이터에만 접근하는 그룹 관리자는 user-day 내보내기를 사용할 수 없습니다.

![일별 및 주별 데이터 내보내기 옵션](/mwkorea/assets/images/2026-09-09-CopilotDashboardUserDayExport/image2.png)

## 라이선스 변경 직후에는 해석에 주의

라이선스 할당·제거 후 **2일 이내**에 내보낸 지표는 변경을 반영하지 못할 수 있습니다. 정상 조건에서는 이 2일 구간이 지난 뒤 내보내기에 변경 영향이 반영됩니다.

이미 내보낸 파일은 나중에 자동으로 갱신되지 않습니다. 라이선스를 정리한 직후의 보고서라면 내보내기 시각과 데이터 반영 범위를 함께 기록하고 필요할 때 다시 내려받는 것이 좋습니다.

## 기존 VFAM 제어를 그대로 사용

새 별도 권한 체계를 만드는 것이 아니라 기존 user-week와 동일한 **Viva Feature Access Management(VFAM)** 설정을 사용합니다. 경로는 **Viva Insights → Copilot Metrics Export**입니다.

기존 설정은 일별·주별 내보내기에 모두 적용됩니다. 이미 내보내기를 활성화했다면 추가 구성은 필요하지 않으며, 관리자는 VFAM으로 테넌트 또는 특정 그룹의 내보내기를 비활성화할 수 있습니다.

## 일정과 한국 조직의 활용 방향

| 단계 | 9월 8일 공지 기준 |
|---|---|
| Public Preview | 2026년 5월 중순~5월 말 |
| Worldwide GA | 2026년 11월 말~12월 초 예정 |

사용 활성화 캠페인 전후나 최근 라이선스 조정의 영향을 분석하는 데 유용합니다. 다만 비식별화 지표라고 해도 조직·직무별 작은 집단을 과도하게 세분화하거나 개인 평가 자료처럼 다루지 않도록, 사내 분석 목적과 접근 정책을 먼저 정하는 것이 좋습니다.

> **출처**: [MC1222978 — Microsoft 365 Copilot: User-day export for Copilot dashboard metrics in public preview](https://mc.merill.net/message/MC1222978). [Microsoft 365 Roadmap 547749](https://www.microsoft.com/microsoft-365/roadmap?searchterms=547749). **실제 출시 일정·기능은 변경될 수 있습니다**.
