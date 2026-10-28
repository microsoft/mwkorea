---
title: "상담센터의 하루를 조정하는 Intraday Agent: 대기열 예측부터 근무 편차 대응까지"
date: 2026-10-21T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - CustomerService
  - IntradayAgent
  - AutonomousAgents
excerpt: "Dynamics 365 Customer Service의 Intraday Agent는 당일 대기열 수요와 상담원 일정 준수 상태를 모니터링하고 대응하는 자율 에이전트로 소개됐습니다. 로드맵은 실시간 재예측과 일정 조정을 설명하며, 일반 제공 목표는 2027년 3월입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 상담센터의 하루를 조정하는 Intraday Agent: 대기열 예측부터 근무 편차 대응까지

상담센터는 아침에 세운 계획만으로 하루를 운영하기 어렵습니다. 예상보다 문의가 몰리거나 상담원의 활동 일정이 달라지면 대기열과 서비스 수준에 바로 영향을 줍니다.

Roadmap 577184는 Dynamics 365 Customer Service의 **Intraday Agent**를 이러한 당일 운영 상황을 관리하는 자율 AI 에이전트로 소개합니다. 아직 개발 중인 로드맵 항목이며, 일반 제공이 완료된 기능으로 소개하는 글은 아닙니다.

---

## 대기열 수요를 추적하고 다시 예측합니다

원문이 제시한 대기열 관리 기능은 실시간 물량 모니터링, 예측 수요와 실제 물량의 큰 차이 탐지, 실시간 재예측입니다. 감독자에게 선제적인 알림과 권고를 보내는 것도 포함됩니다.

대응 작업으로는 일정 조정, 휴식 시간 재배치, 상담원 재할당 등을 자동화해 **SLA 성과 유지**를 지원한다고 설명합니다. 업무 요구에 맞춰 완화 조치의 지침을 사용자 지정할 수 있습니다.

## 상담원 활동 일정의 편차에도 대응합니다

두 번째 축은 근무 일정 준수(adherence) 추적입니다. 예정된 교대 활동과 실제 활동을 비교하고, 늦은 로그인·길어진 휴식·이른 로그아웃 같은 편차를 탐지합니다.

원문은 휴식 재조정, 교대 연장, 초과근무 활성화, 유연한 채널 재배정 등을 자율적인 완화 조치의 예로 듭니다. 이 영역도 업무에 맞는 지침을 설정할 수 있다고 안내합니다.

## 한국 조직에서는 자동화 경계를 먼저 정하세요

기능 설명에 근무 시간과 초과근무 조정이 포함된 만큼, 도입 검토에서는 **어떤 변경을 자동 실행하게 하고 어떤 변경은 승인받게 할지**를 먼저 정하는 것이 좋습니다. 이는 운영상의 권고이며, 원문이 특정 승인 기능이나 국내 근로 규정 준수를 보장한다는 뜻은 아닙니다.

상담원에게 영향을 주는 결정은 근무 계약, 내부 운영 기준과 함께 검토해야 합니다. 원문에는 정량적인 비용 절감률이나 SLA 개선 수치가 없으므로 효과를 확정적으로 제시할 수 없습니다.

## 제공 일정

로드맵의 상태는 **In development**, 프리뷰 목표는 **2026년 9월**, GA 목표는 **2027년 3월**입니다. 대상은 Web, Worldwide Standard Multi-Tenant로 표시됩니다. 프리뷰 목표 월이 지났다는 이유만으로 모든 테넌트에서 이용 가능하다고 단정하지 마세요.

## 마무리

Intraday Agent가 지향하는 변화는 운영자가 상황을 발견한 뒤 수동으로 조정하는 방식에서, **모니터링·재예측·대응을 연결하는 방식**으로의 전환입니다. 실제 도입은 가용성과 실행 권한을 확인하고 좁은 범위에서 검증하는 접근이 적절합니다.

> **출처**: [RM577184 — Dynamics 365 Customer Service: Manage intraday operations with AI agent](https://mc.merill.net/message/RM577184) · [Microsoft 365 Roadmap 577184](https://www.microsoft.com/microsoft-365/roadmap?id=577184). 실제 출시 일정·기능은 변경될 수 있습니다.
