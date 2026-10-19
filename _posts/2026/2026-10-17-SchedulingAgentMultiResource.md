---
title: "현장 일정도 팀 단위로 최적화: Scheduling Operations Agent의 다중 리소스 확장"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - FieldService
  - SchedulingOperationsAgent
excerpt: "Scheduling Operations Agent가 여러 리소스의 일정을 함께 최적화하도록 확장됩니다. 일정 보드·Copilot에서는 최대 5개, 최적화 계획에서는 최대 30개 리소스를 다루며 적용 전 비교·검토를 지원합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 현장 일정도 팀 단위로 최적화: Scheduling Operations Agent의 다중 리소스 확장

현장 서비스에서는 한 사람의 일정을 잘 짜는 것만으로 충분하지 않습니다. 여러 작업자의 가용 시간, 이미 배정된 일정, 아직 배정하지 않은 수요를 함께 고려해야 합니다.

Dynamics 365 Field Service의 Scheduling Operations Agent는 이런 다중 리소스 최적화를 확장합니다. 담당자가 제안을 검토한 뒤 반영하는 방식이므로, 자동 배정과 사람의 판단을 함께 설계하는 것이 중요합니다.

---

## 두 가지 규모의 최적화

- **일정 보드 또는 Copilot에서 최대 5개 리소스**를 직접 최적화합니다.
- **최적화 계획을 사용하면 최대 30개 리소스**에 대한 임시 최적화를 수행합니다.
- 사용자 지정 목표와 목적별 가중치, 사용자 지정 최적화 범위를 설정할 수 있습니다.

에이전트는 가용성·현재 일정·미배정 요구를 바탕으로 구성된 제약조건을 지키면서 선택한 목표에 맞는 일정을 제안합니다. 배차 담당자는 현재 일정과 제안 일정을 비교한 후 변경을 적용할 수 있습니다.

## 전제조건과 일정

기존 Scheduling Operations Agent 공개 프리뷰를 기반으로 한 확장이며, 에이전트가 활성화된 조직에 새 기능이 자동 활성화된다고 설명합니다. 로드맵의 프리뷰 표기는 **2026년 6월**, GA 목표는 **2027년 3월**입니다. 프리뷰와 GA를 혼동하지 마세요.

## 도입 체크포인트

먼저 5개 리소스 범위에서 제약조건과 가중치가 원하는 운영 정책을 반영하는지 확인하고, 더 큰 범위는 계획 기반으로 비교하는 방식이 유용합니다. “최적화”가 무엇을 우선하는지 목표를 명확히 정해야 제안도 평가할 수 있습니다.

[Scheduling Operations Agent 문서](https://learn.microsoft.com/en-us/dynamics365/field-service/soa-overview)에서 환경별 조건을 확인하세요.

> 출처: 원문 ID **RM576884**, [MC 아카이브](https://mc.merill.net/message/RM576884), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576884). 실제 출시 일정·기능은 변경될 수 있습니다.
