---
title: "취소와 지연이 생겨도 다시 짜는 현장 일정: Scheduling Operations Agent"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - FieldService
  - SchedulingOperationsAgent
  - Dynamics365
  - Copilot
excerpt: "Field Service의 Scheduling Operations Agent는 변화한 현장 상황에 맞춰 기술자 일정을 제안합니다. 가동률과 작업 우선순위, 기술·지역·약속 시간을 고려하는 방식과 검토 후 적용 흐름을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 취소와 지연이 생겨도 다시 짜는 현장 일정: Scheduling Operations Agent

현장 서비스 일정은 아침에 확정했다고 끝나지 않습니다. 작업이 길어지고 고객이 취소하며, 이동 시간이 늘어나면 뒤의 예약까지 연쇄적으로 흔들립니다.

Roadmap RM577807은 Dynamics 365 Field Service의 **Scheduling Operations Agent**가 이런 상황에서 Copilot을 통해 일정을 재최적화하는 경험을 소개합니다. 핵심은 담당자가 목표를 정하고 **제안된 일정을 검토한 뒤 적용**한다는 것입니다.

---

## 어떤 상황에서 도움이 되나요?

원문은 오후 예약 취소로 생긴 빈 시간, 현재 작업 지연, 기술자의 조기 복귀, 우선순위가 낮은 작업으로 채워진 하루와 이동 동선 개선 등을 예로 듭니다.

각 상황에서 기존 예약을 하나씩 옮기기보다 해당 기술자의 더 나은 일정을 Copilot에 요청할 수 있습니다. 원문은 수초 내 제안을 받는 경험을 설명하지만, 모든 데이터 규모에서 동일한 응답 시간을 보장하는 수치로 받아들여서는 안 됩니다.

## 최적화 기준을 먼저 정하세요

사용자는 **기술자 가동률 극대화**나 **작업 지시 우선순위** 같은 업무 목표를 제시할 수 있습니다. Copilot은 기존 예약과 아직 충족되지 않은 작업을 대상으로 기술 적합성, 담당 지역과 고객 약속 시간대를 고려합니다.

Field Service 앱 어디서나 Copilot 측면 창으로 접근하는 경험이 소개됩니다. 단순히 빈 시간을 채우는 것보다 “무엇을 우선할지”를 명확히 하는 것이 중요합니다.

## 운영 전에 확인할 것

기술자별 스킬, 지역, 예약 시간과 고객 약속 시간이 정확히 입력되어 있는지 점검하세요. 잘못된 기준 데이터는 최적화 제안에도 영향을 줍니다.

원문은 사용자가 제안을 검토하고 변경을 적용하는 흐름입니다. 고객 통지나 모든 예약의 무인 변경까지 자동으로 수행된다고 가정하지 말고 [SOA 개요](https://learn.microsoft.com/en-us/dynamics365/field-service/soa-overview)에서 현재 지원 범위를 확인해야 합니다.

## 제공 일정

수집 시점은 **In development**, 프리뷰 **2025년 6월**, GA 목표 **2027년 3월**입니다. 한국의 유지보수·설치 조직이라면 소규모 기술자 그룹에서 기존 수동 배차와 제안을 비교하는 방식으로 도입을 준비할 수 있습니다.

> **출처**: [RM577807 — Scheduling Operations Agent](https://mc.merill.net/message/RM577807) · [Microsoft 365 Roadmap 577807](https://www.microsoft.com/microsoft-365/roadmap?id=577807). 실제 출시 일정·기능은 변경될 수 있습니다.
