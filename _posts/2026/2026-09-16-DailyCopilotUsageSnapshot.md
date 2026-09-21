---
title: "Viva Insights에 매일 갱신되는 Copilot 사용 현황 보고서가 제공됩니다"
date: 2026-09-16T00:00:00 KST
categories:
  - Copilot
tags:
  - VivaInsights
  - CopilotAnalytics
  - PowerBI
  - Adoption
excerpt: "Viva Insights Advanced Insights에 최근 3개월의 Copilot 활동을 매일 갱신하는 Power BI 보고서와 쿼리가 추가됐습니다. 필요한 역할과 라이선스, 지원하지 않는 지표, 분석 준비 사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Viva Insights에 매일 갱신되는 Copilot 사용 현황 보고서가 제공됩니다

Copilot 도입 현황을 운영하려면 월간 집계만으로는 최근 교육이나 캠페인의 효과를 빠르게 파악하기 어렵습니다. Microsoft는 Viva Insights Advanced Insights에 **Microsoft 365 Copilot latest usage snapshot**이라는 Power BI 보고서와 쿼리를 추가해 분석가가 더 신선한 사용 데이터를 확인할 수 있도록 했습니다.

이 보고서는 최대 3개월의 활동을 담고 매일 갱신됩니다. 다만 실시간 데이터는 아니며 일반적으로 현재 날짜보다 2~3일 전까지의 활동이 반영되고 실제 지연 시간은 달라질 수 있습니다.

---

## 보고서가 제공하는 분석

Adoption overview 페이지에서는 조직 전체의 Copilot 사용을 중심으로 다음 내용을 볼 수 있습니다.

- 시간에 따른 도입 추세
- 조직 그룹별 채택 수준
- Microsoft 365 앱 및 Copilot 기능별 사용 현황
- 조직 속성과 기간 필터를 사용한 세분화

분석가는 조직 속성과 시간 범위를 조합해 채택이 활발한 영역과 낮은 영역을 비교할 수 있습니다. 포함된 일별 데이터 쿼리를 기반으로 추가 분석도 가능하며, CSV 다운로드와 Power BI 커넥터, Microsoft Fabric을 통한 내보내기를 지원합니다.

![Copilot 최신 사용 현황 보고서의 Adoption overview](/mwkorea/assets/images/2026-09-16-DailyCopilotUsageSnapshot/image1.png)

## 누가 사용할 수 있나

대상은 Viva Insights 웹 앱에서 Advanced Insights와 Power BI를 사용하는 **Insights Analyst 역할** 보유자입니다. 분석 대상 사용자에게는 Microsoft 365 Copilot 라이선스와 Viva Insights 라이선스가 모두 할당돼 있어야 합니다.

조직 차원의 중요한 전제도 있습니다. 이 기능을 사용하려면 조직에 Microsoft 365 Copilot 라이선스가 최소 50개 있어야 합니다. 조건을 충족한 조직의 적격 분석가에게 보고서가 기본 제공되며 별도의 관리자 구성이 필요하지 않습니다. 기존 Copilot Analytics 보고서와 쿼리는 변경되지 않습니다.

## 현재 포함되지 않는 지표

최신 사용 현황 보고서가 모든 Copilot Analytics 지표를 대신하는 것은 아닙니다. 현재 다음 항목은 보고서와 쿼리에서 지원하지 않습니다.

- Copilot이 요약하거나 재구성한 회의 시간 및 회의 수 관련 지표
- Teams에서 Copilot이 요약한 회의 시간
- Copilot assisted hours 및 금액 환산 값
- Copilot for Sales 관련 모든 지표
- 파워 유저와 관련된 지표

따라서 기존 경영 보고서를 새 스냅샷으로 교체하기 전, 필요한 KPI가 지원 목록에 있는지 확인해야 합니다. 이 보고서는 최근 사용 흐름을 빠르게 보는 목적에 적합하며, 영향·가치 지표까지 모두 제공하는 종합 성과 보고서는 아닙니다.

## 출시 일정과 변경된 계획

공개 미리 보기는 2026년 7월 초 시작해 7월 말 완료됐습니다. 전 세계 일반 공급은 당초 11월로 안내됐으나 9월 초로 앞당겨졌고, 2026년 9월 초 배포가 완료됐습니다. 이 일정은 9월 15일 공지 업데이트에서 최종 반영됐습니다.

## 조직의 준비 사항

추가 관리자 설정은 없지만 실제 활용을 위해 다음을 확인하는 것이 좋습니다.

1. 적절한 분석가에게 Viva Insights의 Insights Analyst 역할이 부여돼 있는지 확인합니다.
2. 분석 대상 사용자의 Microsoft 365 Copilot 및 Viva Insights 라이선스를 점검합니다.
3. 분석가 PC의 Power BI Desktop을 최신 버전으로 준비합니다. 구버전이라면 제거 후 최신 버전을 설치하도록 안내됐습니다.
4. 데이터가 2~3일 지연될 수 있음을 대시보드 이용자에게 명확히 알립니다.
5. 기존 KPI와 새 보고서에서 지원하지 않는 지표를 구분해 보고 체계를 설계합니다.

도입 캠페인 직후의 단기 변화를 살피고 부서별 교육 우선순위를 정하는 데 특히 유용합니다. 일별 변화를 과도하게 해석하기보다 충분한 기간과 그룹 규모를 두고 추세를 비교하는 운영 원칙도 함께 마련하는 것이 좋습니다.

---

> 원문: MC1314949 — [Microsoft Viva Copilot Analytics: Daily Copilot usage snapshot with fresh data](https://mc.merill.net/message/MC1314949)  
> 로드맵: [Microsoft 365 Roadmap 561325](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=561325)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
