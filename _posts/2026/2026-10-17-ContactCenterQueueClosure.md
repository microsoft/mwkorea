---
title: "상담원이 없어도 대기를 방치하지 않게: Contact Center 큐 종료·부재 대응"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - ContactCenter
  - UnifiedRouting
excerpt: "Dynamics 365 Contact Center가 영업시간 종료와 상담원 전원 로그아웃을 감지해 대기 대화에 대체 경로를 적용합니다. 자연어로 설정한 오버플로·폴백 정책으로 음성사서함, 콜백, 다른 큐 연결을 구성하는 방향입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 상담원이 없어도 대기를 방치하지 않게: Contact Center 큐 종료·부재 대응

고객이 대기열에 들어온 뒤 영업시간이 끝나거나 상담원 모두가 로그아웃하면, 일반 대기 규칙만으로는 서비스 공백을 처리하기 어렵습니다. Dynamics 365 Contact Center는 이 두 상황을 감지해 대체 경로를 적용하는 기능을 안내했습니다.

핵심은 고객을 무조건 다른 곳으로 보내는 것이 아니라, **관리자가 미리 정한 업무 규칙으로 대기를 마무리하거나 연결을 이어 가는 것**입니다.

---

## 두 가지 상황을 구분합니다

영업 종료 전에 들어온 대화가 계속 기다리는데 큐가 운영시간 밖으로 전환되면, 구성된 오버플로 동작을 적용합니다. 음성사서함, 콜백 요청, 다른 가용 큐로 전환하는 방식이 예로 제시됩니다.

또 큐에 배정된 상담원이 모두 로그아웃한 경우에는 대기열 오버플로 타이머를 기다리지 않고 설정된 폴백을 즉시 실행합니다. 예상치 못한 일괄 로그아웃이나 휴식·휴일 공백에 대응하는 방향입니다.

## 자연어로 정책을 구성

관리자는 conversation orchestration에서 자연어 프롬프트로 두 상황의 처리 규칙을 구성합니다. “상담원 없음”과 “운영시간 종료”를 각각 시험하고, 대체 큐도 이용 불가능할 때의 운영 절차를 정하는 것이 좋습니다.

원문은 모든 채널에서 동일한 대체 동작을 보장하거나 대기시간 감소 수치를 제시하지는 않습니다.

## 일정

로드맵에는 프리뷰 **2026년 6월**, GA **2026년 10월**로 기재되어 있습니다. 관리자 등이 최종 사용자용으로 활성화하는 기능이며, 실제 환경의 지원 범위를 먼저 확인해야 합니다.

> 출처: 원문 ID **RM576759**, [MC 아카이브](https://mc.merill.net/message/RM576759), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576759). 실제 출시 일정·기능은 변경될 수 있습니다.
