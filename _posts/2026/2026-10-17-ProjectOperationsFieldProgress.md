---
title: "현장에서 승인한 시간이 프로젝트 진척으로: Project Operations의 실행 데이터 연결"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - ProjectOperations
  - FieldService
excerpt: "Field Service에서 승인된 프로젝트 작업 시간이 Project Operations의 WBS 진척 지표에 반영됩니다. AI 기능 자체보다는 분석과 업무 판단의 기반이 되는 실행 데이터 연결 변화입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 현장에서 승인한 시간이 프로젝트 진척으로: Project Operations의 실행 데이터 연결

현장 작업은 끝났는데 프로젝트 관리 화면의 진척은 그대로라면, 관리자는 별도 자료를 대조해야 합니다. Microsoft는 승인된 Field Service 시간을 Project Operations의 작업 단위 진척에 연결하는 기능을 안내했습니다.

이 항목은 수집 필터에 포함됐지만 **본문이 설명하는 핵심은 새로운 Copilot 기능이 아니라 실행 데이터 통합**입니다. 에이전트나 분석 결과를 신뢰하려면 기반 데이터도 실제 작업을 반영해야 한다는 관점에서 살펴볼 만합니다.

---

## 무엇이 반영되나요?

프로젝트 작업에 연결해 기록한 Field Service 시간이 승인되면, Project Operations의 WBS 작업 지표에 포함됩니다. 완료 공수, 남은 공수, 완료율, 완료 시점 예상 공수와 일정 편차 등이 기존 프로젝트 규칙으로 계산됩니다.

계산은 말단 작업 수준에서 이루어지고 요약 작업과 프로젝트 최상위로 집계됩니다. 별도 새 계산식이나 실행 논리를 도입하는 것이 아니라, 기존 WBS 공수 추적에 승인된 현장 작업을 포함하는 변화입니다.

## 꼭 필요한 전제조건

**Field Service와 Project Operations 통합이 활성화되어야 하며, 시간이 프로젝트 작업 수준으로 유입되어야 합니다.** 모든 현장 시간 기록이 조건 없이 프로젝트 진척으로 바뀌는 것은 아닙니다.

작업 연결과 승인 흐름을 먼저 확인하고, 말단 작업부터 프로젝트 전체까지 지표가 올바르게 집계되는지 점검하는 것이 좋습니다.

## 일정과 참고 문서

로드맵의 GA 표기는 **2026년 7월**이며 관리자·메이커·마케터 자동 활성화 항목입니다. 환경별 조건은 [프로젝트 작업 통합 문서](https://learn.microsoft.com/en-us/dynamics365/project-operations/field-service-integration/project-operations-integration-project-task)를 확인하세요.

> 출처: 원문 ID **RM576798**, [MC 아카이브](https://mc.merill.net/message/RM576798), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576798). 실제 출시 일정·기능은 변경될 수 있습니다.
