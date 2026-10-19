---
title: "고객이 같은 설명을 반복하지 않도록: 이전 상담원으로 이어주는 Contact Center"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - ContactCenter
  - UnifiedRouting
excerpt: "Dynamics 365 Contact Center가 이전에 응대했거나 선호하는 전문가로 대화를 연결하는 기능을 안내했습니다. 과거 이력뿐 아니라 큐 소속·현재 가용성·동시 대화 한도를 함께 고려하고, 불가하면 다른 적격 담당자로 전환합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 고객이 같은 설명을 반복하지 않도록: 이전 상담원으로 이어주는 Contact Center

같은 문제로 다시 문의했는데 처음부터 설명해야 한다면 고객과 상담원 모두 시간이 듭니다. Dynamics 365 Contact Center의 이번 기능은 이전 응대 맥락을 활용해 상담 연속성을 높이는 데 초점을 둡니다.

과거 또는 선호 전문가에게 연결하되, **그 사람이 실제로 받을 수 있는 상태인지도 함께 판단**한다는 점이 중요합니다.

---

## 과거 이력만 보고 무조건 배정하지 않습니다

과거 상호작용, 큐 소속의 적합성, 전문가의 가용성을 활용합니다. 이전·선호 전문가가 이용 불가능하면 다음으로 적합한 전문가로 전환해 서비스 수준을 유지하도록 설명합니다.

관리자는 conversation orchestration의 자연어 기반 플레이북으로 배정 논리를 정하고, 이전 담당자를 찾을 과거 조회 기간도 구성할 수 있습니다.

## 비동기 대화의 추가 조건

비동기 대화에서는 같은 전문가로 재연결하도록 선택하면서 **현재 presence 상태와 활성 대화 한도**를 확인할 수 있습니다. 고객과 연결된 이력이 있다고 업무 수용 능력을 무시하고 배정하는 구조는 아닙니다.

도입 시에는 과거 조회 기간이 너무 길거나 짧을 때의 결과, 담당자 부재 시 폴백, 큐 이동 후의 배정 동작을 확인하는 것이 좋습니다. 이는 운영 제안입니다.

## 일정

로드맵 표기는 프리뷰 **2026년 6월**, GA **2026년 10월**입니다. 관리자 등이 최종 사용자용으로 활성화하는 항목이며, 조직의 실제 라우팅 정책과 함께 평가해야 합니다.

> 출처: 원문 ID **RM576746**, [MC 아카이브](https://mc.merill.net/message/RM576746), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576746). 실제 출시 일정·기능은 변경될 수 있습니다.
