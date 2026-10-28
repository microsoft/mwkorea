---
title: "Power Pages를 AI의 업무 도구로: MCP server로 사이트 데이터 연결하기"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - PowerPages
  - MCP
  - Copilot
  - WebAPI
excerpt: "Power Pages MCP server는 사이트 데이터와 작업을 AI 클라이언트가 사용할 수 있는 도구로 노출합니다. 공개 프리뷰의 CRUD 범위, 사이트 설정과 권한 검토 포인트를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Power Pages를 AI의 업무 도구로: MCP server로 사이트 데이터 연결하기

고객 포털에서 정보를 조회하고 수정하는 일을 자연어로 처리할 수 있다면 어떨까요? Power Pages MCP server는 사이트 데이터와 작업을 AI 클라이언트가 이해하는 표준 인터페이스로 제공하는 접근입니다.

Roadmap RM577813은 메이커가 별도 사용자 지정 코드 없이 사이트의 Web API 계층을 통해 기능을 노출하는 공개 프리뷰를 설명합니다. **조회뿐 아니라 생성·수정·삭제까지 포함**된다는 점이 중요합니다.

---

## 무엇이 지원되나요?

공개 프리뷰 범위는 사이트 Web API를 통한 **Create, Read, Update, Delete(CRUD)**입니다. 메이커는 사이트 설정에서 MCP server 엔드포인트를 프로비저닝하고, AI 채팅 클라이언트는 자연어 요청으로 사이트 데이터를 다루게 됩니다.

기존 사이트의 데이터와 운영 기능을 구조화된 도구로 바꾸므로, 사용자에게 별도 화면 조작을 모두 요구하지 않는 업무 흐름을 설계할 수 있습니다.

## 조회 도구보다 쓰기 도구를 더 신중하게

업무적으로는 문의 등록·정보 조회 같은 시나리오를 생각해 볼 수 있습니다. 다만 이는 활용 아이디어이며, 모든 포털과 AI 클라이언트에서 바로 동작한다는 보장은 아닙니다.

특히 삭제·수정 작업은 조회보다 영향이 큽니다. 조직은 사이트 인증, 테이블 접근 범위, AI 클라이언트 연결 조건과 변경 확인 절차를 검토해야 합니다. “MCP를 켰다”는 이유로 기존 접근 제어를 생략해서는 안 됩니다.

## 시작하기

[Power Pages MCP 개요](https://learn.microsoft.com/en-us/power-pages/configure/mcp-overview)에서 설정과 현재 제한사항을 확인한 뒤, 테스트 사이트의 좁은 데이터 범위부터 연결하는 것이 좋습니다.

추천 순서는 읽기 시나리오 검증, 생성·수정 결과 검토, 삭제 같은 영향 큰 작업의 승인 기준 확인입니다. 이는 운영상 권장 순서이며 원문이 자동 승인 기능을 약속한 것은 아닙니다.

## 제공 일정

수집 시점 상태는 **In development**, 프리뷰는 **2026년 1월**, GA 목표는 **2027년 1월**입니다. Web 플랫폼이며 관리자·메이커가 최종 사용자를 위해 활성화하는 유형입니다.

> **출처**: [RM577813 — Power Pages MCP server](https://mc.merill.net/message/RM577813) · [Microsoft 365 Roadmap 577813](https://www.microsoft.com/microsoft-365/roadmap?id=577813). 실제 출시 일정·기능은 변경될 수 있습니다.
