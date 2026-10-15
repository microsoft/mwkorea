---
title: "Azure DevOps 커넥터 연결, 2024년 9월 이전 것이라면 11월 30일 전에 다시 만드세요"
date: 2026-10-15T00:00:00 KST
categories:
  - Copilot
tags:
  - PowerPlatform
  - AzureDevOps
  - Connector
  - Agent
  - MessageCenter
excerpt: "2024년 9월 1일 이전에 만든 Azure DevOps 커넥터 연결은 곧 제거되는 레거시 앱 등록 인증 방식을 사용합니다. 2026년 11월 30일까지 제거가 완료되면 해당 연결을 쓰는 플로, 앱, 에이전트의 인증이 실패하므로 연결을 새로 만들어 교체해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Azure DevOps 커넥터 연결, 2024년 9월 이전 것이라면 11월 30일 전에 다시 만드세요

Power Platform 환경의 앱, 플로, 에이전트 중 **2024년 9월 1일 이전에 만든 Azure DevOps 커넥터 연결**을 사용하는 항목이 확인되었다는 Message Center 공지(MC1508508)가 게시되었습니다. 이 연결들은 제거 예정인 레거시 앱 등록 방식으로 인증합니다. 제거가 완료되면 해당 연결을 사용하는 플로, 앱, 에이전트는 더 이상 인증할 수 없습니다.

Copilot Studio 에이전트가 Azure DevOps 커넥터를 도구로 사용하고 있다면 특히 영향받을 수 있으므로 점검이 필요합니다.

---

## 핵심 일정

- 레거시 앱 등록 방식의 제거는 **이미 시작**되었습니다.
- 제거는 **2026년 11월 30일까지 완료**될 예정입니다.

## 필요한 조치

1. 환경에서 **2024년 9월 1일 이전에 만든 Azure DevOps 연결**을 찾습니다.
2. 새 Azure DevOps 연결을 만들고 동의(consent) 프롬프트를 완료합니다.
3. 이전 연결을 참조하는 플로, 캔버스 앱, 에이전트를 **새 연결로 업데이트**합니다.
4. 더 이상 참조하는 리소스가 없으면 **이전 연결을 삭제**합니다.

## 조치가 필요한 이유

조치하지 않으면 해당 연결을 사용하는 플로, 앱, 에이전트가 인증에 실패해 정상 동작하지 않게 됩니다.

## 체크포인트

- 환경이 여러 개라면 각 환경별로 연결 생성일을 확인하세요.
- 연결 교체 후 플로 실행 이력과 에이전트 도구 호출이 정상인지 테스트하세요.
- 연결 소유자가 퇴사·이동한 경우를 대비해 서비스 계정 또는 공유 가능한 연결 정책을 검토하세요.

---

> **출처**: Message Center 원문 ID MC1508508 — Power Platform – Recreate connections made to the Azure DevOps connector prior to September 2024 (<https://mc.merill.net/message/MC1508508>). 공식 일정은 Microsoft 365 Message Center와 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)을 참조하세요. 실제 출시 일정·기능은 변경될 수 있습니다.
