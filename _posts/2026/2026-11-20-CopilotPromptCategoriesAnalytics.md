---
title: "Copilot을 어디에 쓰는지 더 세밀하게: 프롬프트 분석이 13개 범주로 바뀝니다"
date: 2026-11-20T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotDashboard
  - Agent365
  - BusinessAnalytics
  - Adoption
excerpt: "Copilot Dashboard와 Agent 365 Business Analytics의 프롬프트 분류가 13개 범주·41개 하위 범주로 세분화됩니다. 2026년 12월 배포 예정인 변경의 분석 위치와 라이선스별 집계 범위, 기존 지표 전환 시 주의사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot을 어디에 쓰는지 더 세밀하게: 프롬프트 분석이 13개 범주로 바뀝니다

Copilot 도입 성과를 설명할 때 활성 사용자 수만으로는 부족합니다. 직원들이 정보를 찾는지, 자료를 분석하는지, 콘텐츠를 만드는지 알아야 다음 교육과 활용 확산 방향을 정할 수 있습니다.

Message Center 공지 MC1560923에 따르면 **Microsoft Copilot Dashboard와 Agent 365 Business Analytics에 향상된 프롬프트 범주가 도입**됩니다. Copilot Chat의 업무 활용을 기존보다 세밀하게 나누어 보는 변화입니다.

---

## 4개 기존 범주를 13개 범주·41개 하위 범주로 대체

기존 Copilot Dashboard의 다음 네 범주는 제거되고 새로운 체계로 대체됩니다.

- Ask and find
- Catch up
- Draft and brainstorm
- Other

새 체계는 **13개 범주와 41개 하위 범주**로 구성됩니다. 원문은 정보 찾기, 콘텐츠 분석, 글쓰기·콘텐츠 생성, 요약 등을 예로 들지만 전체 분류 목록을 제공하지는 않습니다.

따라서 새 범주를 임의로 모두 나열하거나, 기존 네 범주와 일대일로 대응한다고 가정해서는 안 됩니다. 기존 분류를 설명하는 사내 가이드와 교육 자료는 업데이트가 필요합니다.

## 어디에서 어떤 지표를 보나요?

| 화면 | 제공되는 분석 |
|---|---|
| Copilot Dashboard의 Adoption 탭 | 범주별 Copilot Chat 사용자 수와 비율 |
| Copilot Dashboard의 Impact 탭 | 범주별 프롬프트 수와 비율 |
| Agent 365 Business Analytics의 Use cases 페이지 | 범주·하위 범주 Treemap, 프롬프트 범주별 표, 직무·조직·그룹별 Heatmap |

기존 대시보드와 분석의 필터를 이용해 그룹·조직·직무별 차이를 살펴볼 수 있습니다. 다만 **사용자 비율과 프롬프트 비율은 서로 다른 지표**이므로, 이용자 저변과 사용량 집중도를 구분해서 해석하는 편이 좋습니다.

## 집계 대상과 개인정보 관련 경계

이 기능은 **Microsoft 365 Copilot 라이선스를 보유한 사용자의 Copilot Chat 사용량**을 대상으로 합니다. Microsoft 365 Copilot 라이선스가 없는 사용자의 Copilot Chat 이용은 포함하지 않습니다.

또한 테넌트 간 동일한 범주 이름을 사용하며, **사용자가 입력한 프롬프트 원문 텍스트는 대시보드에 표시되지 않습니다.** 상세 범주가 생긴다고 해서 관리자가 개별 입력 내용을 읽게 되는 변화로 설명해서는 안 됩니다.

기존에 Copilot Dashboard 또는 Agent 365 Business Analytics에 접근할 수 있던 사용자가 새 범주를 볼 수 있으며, 별도 설정 없이 기본 적용됩니다.

## 일정과 도입 담당자 체크포인트

공지 기준 전 세계 GA 배포는 **2026년 12월 중순 시작, 12월 말 완료 예상**입니다. 관리자에게 필수 조치는 요구하지 않습니다.

도입 담당자는 기존 범주를 사용하는 월간 보고서와 교육 자료를 확인해 두면 좋습니다. 전환 전후를 비교할 때에는 분류 체계와 집계 대상을 함께 적고, 새 체계의 과거 데이터 처리 방식은 실제 제품과 문서에서 확인해야 합니다. 원문에는 과거 데이터 재분류 범위나 성과 개선 수치가 제시되어 있지 않습니다.

## 마무리

세밀해진 분류는 “얼마나 많이 쓰는가”를 넘어 “어떤 업무에 쓰는가”를 이해하는 데 도움이 됩니다. 다만 활용 범주의 변화 자체를 생산성 향상으로 단정하지 말고, 조직의 실제 업무 목표와 함께 해석해야 합니다.

> **출처:** Message Center **MC1560923**, [Enhanced prompt categories for Microsoft 365 Copilot in Microsoft Copilot Dashboard and Agent 365 Business Analytics](https://mc.merill.net/message/MC1560923). [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap)에서 관련 업데이트를 확인할 수 있습니다. 이 공지에는 개별 Roadmap ID가 명시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
