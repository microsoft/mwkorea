---
title: "Teams 채널 에이전트와 GitHub·Asana·Jira MCP 연동: 롤아웃 일시 중지 소식"
date: 2026-10-13T00:00:00 KST
categories:
  - Copilot
tags:
  - Teams
  - ChannelAgent
  - MCP
  - GitHub
  - Jira
  - Asana
  - Agent
excerpt: "Teams 채널 에이전트가 MCP로 GitHub, Asana, Jira와 협업하는 기능의 롤아웃이 일시 중지되었습니다. 기능 개요와 재개 시 준비 사항을 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Teams 채널 에이전트와 GitHub·Asana·Jira MCP 연동: 롤아웃 일시 중지 소식

Microsoft Teams의 **Channel Agent**가 **Model Context Protocol(MCP)** 서버(GitHub, Asana, Atlassian Jira)와 연동해 여러 도구에 걸친 작업을 오케스트레이션하는 기능이 있습니다. Message Center 공지 MC1182703(2025년 11월 4일 최초 게시)은 2026년 8월 20일 **롤아웃 일시 중지**로 갱신되었고, 10월 12일 다시 업데이트되었습니다.

재개 시점은 Message Center로 다시 공지될 예정입니다. (Microsoft 365 Roadmap ID 515466)

![Channel Agent MCP 연동 화면 1](/mwkorea/assets/images/2026-10-13-TeamsChannelAgentMCP/image1.png)

---

## 기능 개요

- 사용자가 Channel Agent에게 질문하면 GitHub, Asana, Jira 등 **여러 도구를 가로지르는 조율된 응답**을 받습니다.
- 사람의 협업처럼 에이전트가 작업을 **투명하게 추론**하며 정보를 수집합니다.
- 앱 간 전환을 줄여 익숙한 Teams 안에서 작업 완료 효율을 높입니다.
- **Microsoft 365 Copilot 라이선스**가 필요합니다. 데스크톱 플랫폼 대상입니다.

![Channel Agent MCP 연동 화면 2](/mwkorea/assets/images/2026-10-13-TeamsChannelAgentMCP/image2.png)

## 현재 상태와 일정

- 타깃 릴리스(전 세계): 2025년 11월 중순 시작, 완료 예정이 2026년 7월 말로 조정(기존 1월 말)되었으나 이후 **롤아웃 일시 중지**
- 일반 공급: 재개 준비가 되면 Message Center로 공지
- 재개 시 **프리뷰**로 제공되며 **관리자 활성화**가 필요합니다. 관리자가 켜지 않으면 영향이 없습니다.

## 관리자 준비 사항

- 테넌트에서 Teams Channel Agent 사용 허용
- GitHub, Asana, Jira 같은 MCP 서버 연동 앱 허용
- 사용 대상자에게 Microsoft 365 Copilot 라이선스 확인
- 내부 문서와 헬프데스크 가이드 검토
- 컴플라이언스상 확인된 사항은 없습니다.

---

> **원문**: MC1182703 — [Microsoft Teams: Channel agent orchestration with GitHub, Asana, and Jira via Model Context Protocol (MCP)](https://mc.merill.net/message/MC1182703) / [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
