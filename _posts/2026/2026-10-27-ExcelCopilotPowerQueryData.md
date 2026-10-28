---
title: "Excel 데이터 준비도 말로 요청하세요: Copilot이 만드는 Power Query"
date: 2026-10-27T00:00:00 KST
categories:
  - Copilot
tags:
  - Excel
  - Copilot
  - PowerQuery
  - DataTransformation
  - Roadmap
excerpt: "Excel의 새로운 get data skill은 필요한 데이터와 준비 방법을 자연어로 설명하면 연결·변환·로드를 돕습니다. 결과는 Power Query 쿼리로 남아 검토·편집·새로 고침할 수 있으며, 원본에 따라 인증이 필요합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Excel 데이터 준비도 말로 요청하세요: Copilot이 만드는 Power Query

Excel 분석에서 시간을 많이 쓰는 단계는 차트를 그리기 전의 데이터 준비입니다. 필요한 원본을 연결하고, 구조를 바꾸고, 분석에 쓸 수 있는 형태로 불러와야 합니다.

Microsoft 365 Roadmap의 **RM577745**는 이 과정을 자연어로 요청하는 새로운 **get data skill**을 소개합니다. 중요한 점은 일회성 결과만 만드는 것이 아니라, 사용자가 검토하고 다시 실행할 수 있는 **Power Query 쿼리**로 연결한다는 것입니다.

---

## 요청에서 통합 문서까지의 흐름

원문이 설명하는 처리 흐름은 다음과 같습니다.

1. 필요한 데이터와 준비 방법을 자연어로 설명합니다.
2. 새 get data skill이 데이터를 연결하고 변환합니다.
3. Power Query를 이용해 결과를 통합 문서에 로드합니다.
4. 생성된 쿼리를 사용자가 검사·편집·새로 고침합니다.

기존에는 사용자가 직접 구성해야 했던 쿼리 작성 과정을 Copilot이 도와주는 구조입니다. 원문은 지원하는 모든 데이터 원본이나 변환 종류의 목록까지 제시하지는 않습니다.

## 왜 Power Query로 남는 것이 중요한가요?

업무 데이터는 한 번만 분석하고 끝나는 경우보다 주기적으로 다시 확인해야 하는 경우가 많습니다. 결과값만 받으면 다음 실행에 같은 작업을 반복해야 하지만, 쿼리가 남으면 처리 과정을 확인하고 수정할 수 있습니다.

따라서 이 기능은 “AI가 데이터를 대신 정리했다”보다 **“검토 가능한 데이터 준비 절차를 AI와 함께 만든다”**는 관점에서 보는 편이 좋습니다. 다만 원문이 말하는 새로 고침 가능성과 자동 예약 실행은 같은 의미가 아닙니다.

## 인증과 품질 검토는 별도입니다

데이터 원본에 따라 **인증이 필요할 수 있습니다**. 자연어로 요청한다고 원본 시스템의 접근 권한이 없어지는 것은 아닙니다.

실무에서는 쿼리의 원본과 변환 단계를 먼저 확인하고, 결과의 행 수·열 형식·누락값을 원본과 비교하는 것을 권장합니다. 이는 제품의 추가 기능에 대한 주장이 아니라, AI가 만든 데이터 처리 결과를 업무에 쓰기 위한 검토 절차입니다.

## 제공 일정

| 구분 | 원문에 표시된 내용 |
|---|---|
| 플랫폼 | Web |
| 대상 클라우드 | Worldwide, Standard Multi-Tenant |
| 일반 공급 목표 | 2026년 10월 |
| 수집 시점 상태 | Rolling out |

배포 중인 기능이므로 조직과 계정에 따라 실제 사용 가능 시점은 다를 수 있습니다. 구체적인 라이선스·원본 지원 조건은 실제 제공 안내를 확인해야 합니다.

## 마무리

이번 변화의 중심은 **자연어 요청과 재사용 가능한 쿼리의 결합**입니다. 반복 보고용 데이터를 준비하는 팀이라면, 시험용 원본에서 쿼리의 재현성과 새로 고침 결과부터 확인해 보세요.

> **출처**: RM577745 — [Excel: Get and transform data with Copilot in Excel](https://mc.merill.net/message/RM577745) · [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&searchterms=577745). 실제 출시 일정·기능은 변경될 수 있습니다.
