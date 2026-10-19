---
title: "메일을 케이스로 만들기 전에 분류부터: Case Management Agent의 새 입력 단계"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - CustomerService
  - CaseManagementAgent
  - PowerAutomate
excerpt: "Case Management Agent가 수신 이메일의 제목·본문을 분석해 사용자 지정 범주와 하위 범주를 부여합니다. 분류 결과를 케이스 생성 규칙과 Power Automate에 연결해 후속 처리를 나눌 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 메일을 케이스로 만들기 전에 분류부터: Case Management Agent의 새 입력 단계

고객지원 메일함에는 문의뿐 아니라 감사 인사, 뉴스레터, 불필요한 메시지도 들어옵니다. 모든 메일에 같은 자동화를 적용하기보다 먼저 분류해 처리 경로를 나누는 것이 중요합니다.

Dynamics 365 Customer Service의 이메일 분류는 관리자가 정의한 **범주·하위 범주에 맞춰 AI가 제목과 본문을 분석**하는 기능입니다.

---

## 분류 결과를 업무 데이터로 저장합니다

부여된 범주나 하위 범주는 이메일 활동 레코드에 저장됩니다. Case Management Agent, 자동 레코드 생성 규칙, Power Automate 흐름, 보고서와 후속 프로세스가 이 값을 사용해 처리 방법을 결정할 수 있습니다.

예를 들어 정형 문의와 비지원 메일의 처리 경로를 분리하는 구성을 검토할 수 있습니다. 원문은 분류만으로 모든 불필요한 메일을 자동 삭제한다고 설명하지 않습니다.

## 관리자가 설정할 내용

범주·하위 범주의 이름과 설명을 정의하고, 특정 사서함·발신 도메인·언어 등 분류 대상 조건을 정합니다. 활성화되면 대상 수신 메일을 판별해 Case Management Agent 흐름으로 분류합니다.

관리자는 잘못 부여된 값을 수동 수정하거나 기능을 비활성화해 **새 이메일의 처리**를 중단할 수 있습니다. 기존 분류 결과가 자동으로 재평가된다는 설명은 없습니다.

## 일정과 도입 체크포인트

GA 표기는 **2026년 8월**이며 관리자 등이 최종 사용자용으로 활성화하는 기능입니다. 초기에는 범주 설명을 구체적으로 작성하고, 오분류가 케이스 생성·라우팅에 어떤 영향을 주는지 함께 확인하는 것이 좋습니다.

> 출처: 원문 ID **RM576775**, [MC 아카이브](https://mc.merill.net/message/RM576775), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576775). 실제 출시 일정·기능은 변경될 수 있습니다.
