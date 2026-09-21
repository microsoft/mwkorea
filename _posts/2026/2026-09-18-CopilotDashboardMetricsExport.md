---
title: "Copilot 사용 지표를 6개월치 내보내기: 회사 전체 접근 권한과 기본 활성화 확인"
date: 2026-09-18T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotAnalytics
  - CopilotDashboard
  - VivaInsights
  - DataExport
  - VFAM
excerpt: "Copilot Dashboard에서 최근 6개월의 사용자별·주별 사용 지표를 내보내는 기능의 일정이 갱신됐습니다. 회사 전체 데이터 접근 권한이 있는 적격 사용자에게 기본 활성화되며, 사용자는 해시 ID로 표현됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 사용 지표를 6개월치 내보내기: 회사 전체 접근 권한과 기본 활성화 확인

Copilot 도입 추세를 조직의 분석 방식으로 살펴보려면 대시보드 밖에서 지표를 분석해야 할 때가 있습니다. 다만 사용자 수준의 데이터가 내보내기에 포함된다면 누가 그 기능을 사용할 수 있는지도 함께 확인해야 합니다.

메시지 센터 **MC1173208**은 Copilot Dashboard의 데이터 내보내기 공개 프리뷰와 GA 일정을 갱신했습니다. 2026년 9월 17일 수정문은 **회사 전체 데이터 접근 권한이 있는 사용자에게 기본 활성화**되며, 내보내기 결과는 **해시 ID를 사용하는 비식별 데이터**라는 점을 다시 강조합니다.

---

## 어떤 데이터가 포함되나요

| 항목 | 원문 설명 |
|---|---|
| 기간 | 최근 6개월 |
| 집계 단위 | 사용자별·주별 |
| 사용자 표시 | 이름 대신 해시 ID |
| 사용 지표 | Word, Excel, Teams 등 앱별 Copilot 사용 |
| 추가 속성 | Organization, Job function |
| 적용 서비스 | Viva Insights 웹 앱 |
| 라이선스 조건 | Microsoft 365 Copilot 라이선스 최소 50개 |

사용량의 주간 추세를 분석하거나 라이선스와 도입 전략을 검토하는 데 활용할 수 있습니다. 원문은 ROI 측정에도 활용 가능하다고 소개하지만, 사용 지표를 내려받는 것만으로 금전적 효과가 자동 계산된다는 뜻은 아닙니다.

![Copilot Dashboard의 데이터 내보내기 기능을 소개하는 원문 화면](/mwkorea/assets/images/2026-09-18-CopilotDashboardMetricsExport/image1.png)

## 회사 전체 접근 권한이 있어야 합니다

대상은 **회사 전체 데이터에 접근할 수 있는 Copilot Dashboard 사용자**입니다. 원문은 Entra ID 정보로 식별되는 고위 리더, 관리자가 회사 전체 접근을 부여한 사용자, 같은 범위의 위임 사용자, global analyst와 관리자를 포함해 설명합니다.

반대로 **자기 팀 데이터만 볼 수 있는 그룹 관리자에게는 이 기능이 제공되지 않습니다.** 대시보드를 볼 수 있다는 사실만으로 내보내기 자격이 생기는 것은 아닙니다.

## 해시 ID가 사용돼도 데이터 관리는 필요

내보내기 결과는 사용자를 해시 ID로 표현하고 사용자별·주별 지표를 포함합니다.

![해시 사용자 ID와 주간 지표가 포함된 내보내기 출력 예시](/mwkorea/assets/images/2026-09-18-CopilotDashboardMetricsExport/image2.png)

원문은 이를 비식별 데이터라고 설명합니다. 다만 이 설명을 어떤 다른 자료와 결합해도 개인을 추정할 수 없다는 보장으로 확대할 수는 없습니다. 조직과 직무 속성도 포함되므로 내려받은 파일의 보관 장소와 공유 대상은 조직의 개인정보·데이터 관리 원칙에 맞춰 정하는 것이 좋습니다.

## VFAM으로 허용 범위를 관리

이 기능은 **적격 사용자에게 기본 활성화**되며 시작을 위한 관리자 설정이 별도로 필요하지 않습니다. 따라서 내보내기를 원하지 않는 조직도 설정을 미리 살펴야 합니다.

Viva Feature Access Management, 즉 **VFAM**에서 다음 항목으로 관리합니다.

| 구분 | 설정 |
|---|---|
| Module | Viva Insights |
| Feature | Copilot Metrics Export |
| 비활성화 범위 | 테넌트 또는 그룹 |

관리자는 회사 전체 데이터 접근 권한의 할당을 검토하고 필요한 VFAM 정책을 조정할 수 있습니다. 해당 기능을 직접 사용하는 적격 사용자 외에는 기존 사용자 업무 흐름에 영향이 없다고 원문은 안내합니다.

## 새로 안내된 일정

| 구분 | 수정된 일정 | 이전 일정 |
|---|---|---|
| 공개 프리뷰 | 2026년 10월 초 시작, 10월 하순 완료 | 2025년 12월 초~하순 |
| 전 세계 GA | 2026년 10월 중순 시작, 10월 말 완료 | 2026년 9월 초~하순 |

두 배포 구간은 원문에 이렇게 제시되어 있습니다. 이전 공지를 참고한 도입 문서가 있다면 최신 일정을 반영하고, 대상 사용자가 실제로 확인할 수 있는지 배포 상태를 살펴보세요.

이 변경을 준비할 때는 데이터 내보내기 자체보다 **권한 범위, 기본 활성화 여부, 다운로드 후 관리**를 함께 확인하는 것이 중요합니다.

---

> **출처**
>
> - 원문 ID: **MC1173208** — *Microsoft Copilot Analytics: Data export public preview for Copilot metrics in the Copilot dashboard*
> - 원문: [MC1173208](https://mc.merill.net/message/MC1173208)
> - [Microsoft 365 Roadmap 500872](https://www.microsoft.com/microsoft-365/roadmap?searchterms=500872)
> - 관련 안내: [Microsoft Viva Feature access management](https://learn.microsoft.com/viva/feature-access-management#viva-features-management)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
