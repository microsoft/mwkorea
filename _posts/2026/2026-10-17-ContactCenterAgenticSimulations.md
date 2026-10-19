---
title: "고객이 오기 전에 상담 흐름을 시험한다: Agentic simulations의 현재 범위"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - ContactCenter
  - ServiceOperationsAgent
  - Evaluation
excerpt: "Service Operations Agent의 agentic simulations는 자연어 시나리오로 합성 고객 대화를 만들고 상담 흐름과 KPI를 평가합니다. 현재 영어 음성 채널, DTMF 없는 흐름, 시뮬레이션당 최대 5개 대화라는 제한을 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 고객이 오기 전에 상담 흐름을 시험한다: Agentic simulations의 현재 범위

AI 상담원이나 라우팅 설정을 바꾼 뒤 실제 고객으로 문제를 발견하는 것은 부담이 큽니다. Service Operations Agent의 agentic simulations는 운영에 앞서 현실적인 고객 조건을 합성 대화로 시험하는 기능입니다.

관리자가 자연어로 시나리오를 정의하면 고객 의도·페르소나·행동이 다른 대화를 생성하고, 구성된 컨택센터를 끝까지 통과시켜 KPI를 계산합니다.

---

## 무엇을 평가하나요?

셀프서비스 AI의 의도 처리와 예외 대응, 상담원 연결 흐름과 배정 규칙, 운영 구성의 동작을 확인하는 데 활용합니다. 기본 KPI 대시보드·스코어카드와 저장·재사용 가능한 프롬프트, 사전 시나리오도 제시됩니다.

실제 고객에게 영향을 주지 않는 사전 운영 평가와 상담원 연습을 목표로 합니다. 다만 원문이 확장 준비를 언급한다고 현재 대규모 부하 시험 도구와 동일하게 해석해서는 안 됩니다.

## 한국 도입 담당자가 먼저 볼 제한

현재 범위는 **영어 음성 채널만** 지원합니다. **DTMF 기반 메뉴 상호작용이 없는 흐름**, **시뮬레이션당 최대 5개 대화**를 지원한다고 명시합니다.

따라서 한국어 음성 상담이나 버튼식 ARS 전체를 그대로 검증할 수 있다고 소개하면 안 됩니다. 현 범위에서 시험 가능한 흐름과 별도 검증이 필요한 구간을 나누는 것이 우선입니다.

## 일정과 시작하기

프리뷰 표기는 **2026년 7월**, GA 목표는 **2027년 6월**입니다. 관리자·메이커·마케터 자동 활성화 항목으로 분류되며, [시뮬레이션 구성 문서](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/configure-simulation-agent)에서 환경 조건을 확인할 수 있습니다.

> 출처: 원문 ID **RM576636**, [MC 아카이브](https://mc.merill.net/message/RM576636), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576636). 실제 출시 일정·기능은 변경될 수 있습니다.
