---
title: "Copilot Analytics에서 Cowork의 도입과 업무 영향을 확인합니다"
date: 2026-09-15T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Cowork
  - CopilotAnalytics
  - VivaInsights
excerpt: "Copilot Analytics의 Consumption 대시보드와 Viva Insights Advanced Insights에 Cowork 도입·영향 지표가 추가됐습니다. 역할별 조회 범위와 50개 라이선스 조건, 관리 제어의 범위를 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Analytics에서 Cowork의 도입과 업무 영향을 확인합니다

조직이 Cowork에 Copilot 크레딧을 투자한 뒤에는 단순 소비량뿐 아니라 어떤 업무에 쓰였고 어느 정도의 추가 작업을 가능하게 했는지 파악해야 합니다. Microsoft는 Copilot Analytics의 Consumption 대시보드에 Cowork 도입 및 영향 인사이트를 추가하고, Viva Insights Advanced Insights에도 관련 지표를 확장했습니다.

이 기능은 전 세계에서 현재 일반 공급 중이며 적격 역할에 기본으로 활성화됩니다. 리더와 관리자는 조직 범위에 맞는 현황을 보고, 분석가는 세부 데이터를 사용해 맞춤형 보고서를 만들 수 있습니다.

---

## 확인할 수 있는 Cowork 인사이트

새 인사이트는 Cowork 사용 패턴, 사용자가 Cowork로 완료하는 작업, 그리고 Cowork가 가능하게 한 추가 업무량의 추정치인 **Cowork assisted hours**를 보여 줍니다. 조직은 이를 통해 사용량과 업무 결과를 함께 살펴보고 Copilot 투자와 채택 프로그램을 조정할 수 있습니다.

경로는 Consumption 대시보드의 **Microsoft 365 services** 탭입니다. **Credit usage breakdown by service** 영역에서 Cowork 옆의 **Deep dive**를 선택하면 도입과 영향 상세 보기에 접근할 수 있습니다.

## 역할별 조회 범위

대상은 경영진을 포함한 리더, 조직 범위 접근 권한이 있는 관리자, 전역 파티션에 접근하는 Insights Analyst, 전역 관리자입니다.

- 리더는 조직 전체의 도입과 영향에 대한 테넌트 수준 보기를 사용할 수 있습니다.
- 관리자는 자신에게 허용된 조직 범위의 인사이트를 봅니다.
- 적격 역할은 My company 보기에서 테넌트 전체 Cowork 도입·영향 정보를 확인할 수 있습니다.
- Insights Analyst는 Advanced Insights의 표준 person query로 Cowork 사용 지표를 분석합니다.
- 분석 결과는 CSV, Power BI 또는 Microsoft Fabric으로 내보내 맞춤 보고에 활용할 수 있습니다.

테넌트 수준 보기에는 **Cowork credits used의 비용 데이터가 표시되지 않습니다**. 따라서 도입·영향 지표와 비용 거버넌스 보고서는 목적에 맞게 별도로 다뤄야 합니다.

## 라이선스와 접근 조건

이 인사이트를 보려면 조직에 Microsoft 365 Copilot 라이선스 사용자가 최소 50명 있어야 합니다. 반면 인사이트를 조회하는 적격 리더나 관리자 본인에게 Microsoft 365 Copilot 라이선스가 반드시 필요한 것은 아닙니다.

기능은 모든 Microsoft 365 테넌트에 제공되지만, 실제 데이터 표시에는 위 라이선스 규모 조건과 역할별 권한이 적용됩니다. 조직 간 비교나 소규모 팀 단위 해석을 계획할 때 이 전제를 먼저 확인해야 합니다.

## 관리자 제어에서 주의할 점

전역 관리자는 Copilot dashboard의 **VFAM 제어**로 접근을 관리할 수 있습니다. 그러나 이 제어를 끄면 Cowork 인사이트만 선택적으로 숨기는 것이 아니라 **Copilot dashboard 전체 경험이 비활성화**됩니다. Cowork 지표 공개 여부만을 이유로 끄기 전, 기존 대시보드 사용자와 보고 프로세스에 미칠 영향을 검토해야 합니다.

공지상 별도의 규정 준수 고려 사항은 식별되지 않았지만, 조직의 일반적인 데이터 거버넌스와 역할 설계를 적용해 검토할 필요가 있습니다.

## 도입을 위한 권장 조치

즉시 필요한 관리자 조치는 없습니다. 다만 기본 활성화되는 기능이므로 다음을 권장합니다.

1. Cowork 도입·영향 인사이트를 계속 활성화할지 검토합니다.
2. 리더와 관리자가 자신의 조회 범위를 이해하도록 안내합니다.
3. Insights Analyst가 표준 person query와 내보내기 경로를 사용할 수 있도록 준비합니다.
4. Copilot Analytics 관련 내부 문서와 교육 자료를 갱신합니다.
5. VFAM 제어가 Cowork만이 아니라 전체 대시보드에 영향을 준다는 점을 변경 관리 절차에 명시합니다.

분석 시에는 크레딧 소비, 작업 유형, assisted hours를 하나의 맥락에서 보되 추정 지표를 확정된 절감 시간처럼 해석하지 않는 것이 중요합니다. 사용 패턴과 정성적 업무 결과를 함께 검토해야 투자 판단의 품질을 높일 수 있습니다.

---

> 원문: MC1472032 — [Microsoft 365 Copilot: Insights Copilot Analytics cowork adoption impact](https://mc.merill.net/message/MC1472032)  
> 로드맵: [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
