---
title: "우리 회사의 조직 용어를 Copilot이 이해하도록: Workforce Insights 관리자 작업 공간"
date: 2026-11-20T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - WorkforceInsights
  - Frontier
  - OrganizationalData
  - PeopleSkills
  - Governance
excerpt: "Workforce Insights Agent에 조직 데이터의 속성 설명과 업무 맥락을 설정하고 응답을 검증하는 관리자 작업 공간이 추가됩니다. Frontier 공개 프리뷰의 라이선스·역할 조건과 데이터 접근 및 인사 활용 제한을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 우리 회사의 조직 용어를 Copilot이 이해하도록: Workforce Insights 관리자 작업 공간

조직도에 부서명과 직책이 있다고 해서 AI가 회사의 인력 구조를 정확하게 이해하는 것은 아닙니다. 같은 약어라도 조직마다 뜻이 다르고, 특정 지표를 계산하는 기준도 다를 수 있습니다.

Message Center 공지 MC1560929는 **Workforce Insights Agent에서 조직의 정의, 속성 설명, 비즈니스 맥락을 관리하는 전용 작업 공간**을 안내합니다. 관리자가 설명을 설정하는 데서 끝나지 않고, 에이전트가 이를 어떻게 해석하는지 검증하고 예상과 다른 응답의 원인을 진단하도록 돕는 것이 핵심입니다.

---

## 무엇을 설정하고 어디에 적용하나요?

관리자는 속성의 의미, 관련 값, 약어, 사용 지침을 설명하고 조직 맥락이나 지표 계산 기준을 추가할 수 있습니다. 권한 있는 사용자는 실제 사람·조직 관련 질문으로 응답을 확인하고 대화형 조정 경험을 활용할 수 있습니다.

**이번 구성은 Workforce Insights Agent에 적용되며, 다른 Copilot 경험에는 일부 유형의 질문부터 반영됩니다.** 모든 Copilot 경험으로 확대하는 것은 향후 계획이지, 이번 공지 시점에 전체 적용이 완료되었다는 뜻은 아닙니다.

또한 에이전트에 맥락을 설정해도 **원본 시스템의 데이터 자체가 수정되지는 않습니다.** 잘못된 조직도나 보고 관계는 원천 데이터의 품질 문제로 별도 관리해야 합니다.

## 제공 조건과 관리자 역할

공지의 배포 일정은 **2026년 11월 중순부터 Frontier 테넌트에 순차 제공되는 공개 프리뷰**입니다.

| 항목 | 공지에서 설명하는 조건 |
|---|---|
| 테넌트 | Microsoft 365 Copilot 라이선스 또는 Microsoft 365 Copilot in Productivity Apps 서비스 플랜이 있고 Frontier에 등록 |
| 사용자 | 의도한 사용자의 필수 라이선스와 배포·접근 정책 확인 필요 |
| 관리자 역할 | Global Administrator, AI Administrator, Organizational Data Administrator 등 관련 역할 |
| 배포 및 접근 관리 | AI Administrator가 에이전트 배포와 접근을 관리 |
| 맥락 설정·결과 검증 | Organizational Data Administrator가 담당 가능 |

Microsoft는 데이터와 조직 맥락을 유지할 HR·People Analytics 담당자에게 **Organizational Data Administrator** 역할을 배정하는 방안을 권고합니다. 모든 담당자에게 Global Administrator를 부여해야 한다는 의미는 아닙니다.

라이선스 사용자는 관리자 정책이 허용하면 Copilot 또는 Teams 에이전트 스토어에서 에이전트를 찾아 설치할 수 있습니다. **설치 자체가 관리자 설정 권한이나 기존 권한을 넘는 데이터 조회 권한을 주지는 않습니다.**

## 데이터 준비부터 검증까지

1. **원천 데이터 확인:** 기본 데이터인 Microsoft Entra ID의 보고 관계, 조직 속성, 용어와 품질을 점검합니다.
2. **추가 데이터 검토:** Microsoft 365 관리 센터의 Organizational Data Service로 추가 또는 대체 데이터를 제공할 수 있습니다. 업로드 전 권한과 데이터 처리 요건을 검토합니다.
3. **설정 위치 확인:** 관리 설정은 기존 [Workforce Insights Admin 웹 페이지](https://aka.ms/WorkforceInsightsAdminHome)에서 [Workforce Insights Agent 홈](https://m365.cloud.microsoft/chat/?titleId=P_cee13b52-3ca2-f561-866d-5f91fdbf6689)으로 이동합니다. 속성 설명과 조직 맥락뿐 아니라 속성·접근 정책, 데이터 접근 관련 구성을 확인합니다.
4. **People Skills 검토:** 스킬 기반 질문이 필요하면 People Skills의 활성화, 설정 및 거버넌스 조건을 함께 확인합니다.
5. **접근 범위 관리:** 사용자는 직속 보고자가 있는 사람에게 데이터 범위 확대를 요청할 수 있습니다. 조직 정책에 맞게 WorkforceInsights PowerShell 모듈로 이 접근을 제어합니다.
6. **대표 질문 검증:** 알려진 데이터와 정의를 기준으로 응답을 비교하고, 설정이나 데이터 변경 후 다시 검증합니다.

## 인사 의사결정 도구로 오해하지 않기

원문은 이 에이전트가 **행동 모니터링, 성과 관리 또는 고용 의사결정을 위한 도구가 아니라고 명시**합니다. 한국 조직에서도 개인정보 보호 의무와 현지 법률, 사내 노무·데이터 처리 기준을 검토해야 합니다. 관련 지역에서는 Works Council 지침도 고려 대상입니다.

배포 범위를 사용자·그룹 단위로 제한하거나 에이전트를 제거·차단하는 관리 통제와 함께, 확장된 데이터 접근을 누가 승인하고 유지할지 운영 책임을 정하는 것이 중요합니다.

## 시작하기

[Workforce Insights Agent 문서](https://learn.microsoft.com/microsoft-365/copilot/workforce-insights-agent), [Organizational Data Service](https://learn.microsoft.com/viva/organizational-data), [People Skills 개요](https://learn.microsoft.com/copilot/microsoft-365/people-skills-overview)를 기준으로 현재 제공 범위와 설정 요건을 확인하세요.

이번 변화의 가치는 조직 데이터를 더 많이 넣는 데만 있지 않습니다. **그 데이터의 의미를 설명하고, 권한 안에서 결과를 검증하는 운영 과정**을 만드는 데 있습니다.

> **출처:** Message Center **MC1560929**, [Updates to Workforce Insights Agent (Frontier) for Admins in Microsoft 365 Copilot](https://mc.merill.net/message/MC1560929). [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap)에서 관련 업데이트를 확인할 수 있습니다. 이 공지에는 개별 Roadmap ID가 명시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
