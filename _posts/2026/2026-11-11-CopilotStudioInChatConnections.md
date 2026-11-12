---
title: "에이전트와 대화하다 바로 연결: Copilot Studio의 외부 서비스 설정이 간단해집니다"
date: 2026-11-11T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Agents
  - Connectors
  - WebChat
excerpt: "Copilot Studio 에이전트가 외부 서비스 연결을 요구할 때 대화 흐름 안에서 필요한 설정을 마칠 수 있게 됩니다. 기존 연결 재사용과 조직 정책 유지, Standard harness 기반 커스텀 웹 UI의 개발 대응을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트와 대화하다 바로 연결: Copilot Studio의 외부 서비스 설정이 간단해집니다

업무 에이전트에게 일을 맡겼는데 외부 서비스 연결부터 설정하라는 안내가 나오면 흐름이 끊기기 쉽습니다. 기존에는 별도의 연결 관리 환경으로 이동해 설정을 마친 뒤 다시 대화를 시작해야 했습니다.

MC1548034는 이 과정을 줄이는 Copilot Studio의 새 연결 경험을 안내합니다. 사용자는 대화에서 필요한 서비스 연결을 설정하고 곧바로 대화로 돌아올 수 있으며, 조건에 맞는 유효한 기존 연결이 있으면 재사용할 수 있습니다.

---

## 달라지는 연결 경험

에이전트가 연결을 필요로 하면 전체 연결 관리 포털로 보내는 대신 **해당 서비스에 필요한 설정에 집중한 경험**을 제공합니다.

1. 에이전트 대화에서 필요한 외부 서비스 연결을 시작합니다.
2. 사용 중인 서비스에 필요한 설정만 완료합니다.
3. 연결을 마치면 바로 대화로 돌아가 작업을 이어갑니다.

적격한 기존 연결을 재사용할 수 있다는 점도 중요합니다. 다만 모든 연결이 자동으로 재사용된다는 의미는 아니며, 원문은 유효성과 재사용 자격을 전제로 설명합니다.

## 적용 채널과 조직 정책

연결된 에이전트는 **Microsoft Copilot, Microsoft Teams, Web Chat**에서 계속 사용할 수 있습니다.

설정 경험이 간소화되어도 **어떤 커넥터와 연결에 접근할 수 있는지를 결정하는 기존 조직 통제는 유지**됩니다. 사용자 경험 개선을 커넥터 허용 범위 확대나 접근 권한 우회로 해석해서는 안 됩니다.

관리자는 기존 커넥터·연결 정책을 점검하고, 지원 조직과 사용자에게 새로운 연결 절차를 안내하는 것이 좋습니다.

## 커스텀 웹 UI 개발자는 별도 대응이 필요합니다

이번 공지에서 놓치기 쉬운 대상은 **Standard harness를 사용해 커스텀 웹 UI로 게시한 에이전트**입니다. 해당 개발자는 새 연결 경험을 지원하도록 구현을 변경해야 합니다.

원문이 요구하는 대응은 두 가지입니다.

- 새로운 연결 창을 열 수 있도록 구현합니다.
- 연결 설정이 성공하면 대화를 계속 진행하도록 처리합니다.

대화 중 연결이 필요해지는 경로를 실제로 점검하고, 연결 완료 이후 사용자가 작업을 이어갈 수 있는지 확인해야 합니다. 원문에 없는 SDK 코드나 구체적인 API 이름은 여기서 추정하지 않습니다.

구현 세부사항은 [Support connection setup in a custom canvas](https://aka.ms/21690/support-connection-setup-in-a-custom-canvas)를 참고하세요.

## 제공 일정과 도입 포인트

공지에서는 **2026년 12월 31일까지 일반 공급(GA)에 도달할 예정**이라고 안내합니다. 공지 시점에 모든 환경에서 이미 사용 가능하다는 뜻은 아닙니다.

표준 채널 사용자에게는 대화 이탈을 줄이는 변화이고, 자체 웹 화면을 운영하는 개발 조직에는 연결 창과 대화 재개 동작을 점검해야 하는 변경입니다. 사용자 교육과 개발 대응을 나누어 준비하는 것이 좋습니다.

> 출처: [MC1548034 — Copilot Studio - Set up third-party agent connections in conversations](https://mc.merill.net/message/MC1548034)  
> [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 기재되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
