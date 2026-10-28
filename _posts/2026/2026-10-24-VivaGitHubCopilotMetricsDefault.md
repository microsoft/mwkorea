---
title: "Viva Insights의 GitHub Copilot 지표, 이제 별도 신청 없이 기본 표시됩니다"
date: 2026-10-24T00:00:00 KST
categories:
  - Copilot
tags:
  - VivaInsights
  - GitHubCopilot
  - Adoption
  - Governance
excerpt: "Viva Insights Consumption 대시보드에서 GitHub Copilot 지표가 적격 테넌트에 기본 제공됩니다. 공개 미리 보기 참여 설정은 사라지지만 기존 보고서 권한과 개인정보 설정은 유지되므로, 관리자에게 중요한 준비는 접근 범위 점검입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Viva Insights의 GitHub Copilot 지표, 이제 별도 신청 없이 기본 표시됩니다

개발자의 GitHub Copilot 사용과 일반 업무 사용자의 Microsoft 365 Copilot 활용을 따로 살펴보면, 조직 전체의 도입 현황을 파악하기 어렵습니다. Microsoft는 Viva Insights에서 두 영역의 도입·사용 현황을 함께 볼 수 있도록 기본 제공 방식을 바꿉니다.

MC1523085에 따르면 **GitHub Copilot 공개 미리 보기 opt-in 설정이 폐지**되고, 적격 테넌트에서는 Consumption 대시보드에 관련 지표가 기본으로 표시됩니다. 기능 활성화 작업보다 누가 데이터를 볼 수 있는지 확인하는 일이 중요해졌습니다.

---

## 무엇이 바뀌나요?

Viva Insights 앱 설정 페이지에서 GitHub Copilot의 공개 미리 보기 참여 설정이 제거됩니다. 롤아웃 이후에는 이 설정을 사용해 지표를 켜거나 표시를 보류할 수 없습니다.

이미 참여한 조직은 계속 지표를 보게 됩니다. 이전에 참여하지 않은 조직에서도 관련 보고서 접근 권한을 가진 사용자는 새롭게 GitHub Copilot 지표를 보게 될 수 있습니다. 다만 대상은 **eligible tenants**, 즉 자격 요건을 충족한 테넌트입니다.

## 기존 권한이 사라지는 것은 아닙니다

원문은 기존 역할, 보고서 접근 권한, 개인정보 설정이 계속 데이터 열람 범위를 결정한다고 명시합니다. 모든 직원에게 개발자 사용 데이터가 공개되는 변경은 아닙니다.

관련 대상에는 Microsoft 365 전역 관리자, 전역 파티션 접근 권한이 있는 Insights Analyst, Consumption insights를 볼 수 있는 관리자, 접근을 관리하는 Insights Administrator 등이 포함됩니다.

## 관리자 체크포인트

1. Consumption insights 및 관련 Copilot 보고서를 열람할 수 있는 사용자와 역할을 확인합니다.
2. 분석가·매니저·업무 리더·헬프데스크에 GitHub Copilot 지표가 추가로 보일 수 있음을 알립니다.
3. 기존 공개 미리 보기 opt-in 설정을 안내하던 사내 문서를 수정합니다.

원문은 기존 고객 데이터 접근 방식에 영향이 있다고 설명합니다. 이전에 참여하지 않았던 조직에서 **기존 보고서 열람자에게 지표가 새로 노출될 수 있기 때문**입니다. 자동 변경이라고 해서 거버넌스 검토를 생략해서는 안 됩니다.

## 일정

전 세계 일반 공급 롤아웃은 **2026년 11월 중순 시작, 12월 중순 완료 예정**입니다. 별도 활성화 조치는 필요하지 않습니다. 새 지표의 세부 자격 요건이나 정의는 실제 대시보드 및 관련 문서에서 확인해야 하며, 공지에 없는 수치 기준을 추정하지 않는 것이 좋습니다.

## 마무리

이번 변경은 Copilot 사용 현황을 통합해서 보는 진입 장벽을 낮춥니다. 도입 담당자는 새로운 지표를 환영하는 동시에, 조직의 보고서 권한과 내부 안내가 변경된 기본 동작에 맞는지 점검해야 합니다.

> **출처**: 원문 ID [MC1523085](https://mc.merill.net/message/MC1523085) · [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 기재되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
