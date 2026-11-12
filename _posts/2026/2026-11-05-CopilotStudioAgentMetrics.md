---
title: "Copilot Studio 에이전트도 운영 지표로 관리: 성공률과 세션 알림 예고"
date: 2026-11-05T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - PowerPlatform
  - Monitoring
  - Agent
excerpt: "Power Platform Monitor에 Copilot Studio 에이전트의 성공률과 일별 세션 수 지표가 추가됩니다. Managed Environments에서는 임계값과 선택적 이메일 알림으로 운영 이상을 파악할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 에이전트도 운영 지표로 관리: 성공률과 세션 알림 예고

에이전트를 만들고 배포한 뒤에는 “실제로 잘 해결하고 있는가”를 확인해야 합니다. 사용량만 늘고 업무 해결률이 떨어지는 상황이라면 운영 담당자가 이를 빠르게 발견할 수 있어야 합니다.

Microsoft는 MC1538998을 통해 **Power Platform Monitor의 Copilot Studio 에이전트 지표와 알림**을 안내했습니다. 대화형 에이전트뿐 아니라 자율 에이전트의 상태와 사용량도 관리 범위에 포함됩니다.

---

## 새로 제공되는 두 가지 지표

| 지표 | 의미 |
|---|---|
| Agent session success rate | 성공한 자율 작업 또는 해결된 대화형 세션의 백분율 |
| Recent agent sessions | 하루 동안 발생한 고유 에이전트 세션 수 |

성공률과 세션 수는 서로 다른 질문에 답합니다. 전자는 업무 해결 상태를, 후자는 얼마나 사용되고 있는지를 파악하는 기준입니다. 단순 메시지 수와 고유 세션 수를 혼동하지 않는 것이 중요합니다.

원문은 관리자가 **자신의 관리 범위에 속한 에이전트**의 운영 상태와 사용량을 모니터링할 수 있다고 설명합니다. 성공 판정의 세부 계산식이나 집계 지연은 제시하지 않습니다.

## 임계값 알림은 Managed Environments에서

Managed Environments에 있는 에이전트에는 사용자 지정 임계값을 구성할 수 있습니다. 세션 성공률이 설정한 기준 아래로 내려가는 에이전트를 식별하고, 선택적으로 이메일 알림을 받을 수 있습니다.

따라서 지표 제공과 사용자 지정 알림 조건을 구분해야 합니다. 모든 환경에 같은 알림 구성 기능이 제공된다고 확대 해석하면 안 됩니다.

## 도입 담당자가 준비할 사항

필수 조치는 없으며, 원문은 인지 목적의 안내라고 명시합니다. 일반 공급은 **2026년 12월 4일까지 도달 예정**입니다.

운영 측면에서는 관리 대상 에이전트와 환경 유형을 먼저 정리하는 것이 좋습니다. 이후 업무 중요도에 맞는 성공률 기준과 알림 수신 담당자를 정하면, 이상을 발견했을 때 실제 대응으로 이어가기 쉬워집니다. 이는 원문에 나온 수치 기준이 아니라 조직별로 설계할 운영 권고입니다.

## 마무리

이번 변화는 에이전트를 “만들어 두는 자동화”에서 **성과와 상태를 관찰하는 운영 서비스**로 다루는 데 도움이 됩니다. 성공률과 사용량을 함께 보고, Managed Environments의 알림 조건을 구분해 적용하는 것이 핵심입니다.

> **출처**: [MC1538998 — Power Platform - Copilot Studio agent metrics and alerts](https://mc.merill.net/message/MC1538998). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제공되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
