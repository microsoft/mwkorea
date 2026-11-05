---
title: "외부 앱에서 Copilot Studio 에이전트를 부르려면? MCP·A2A Python 클라이언트로 이해하기"
date: 2026-10-29T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - MCP
  - A2A
  - Python
  - EntraID
excerpt: "MCSCAT가 외부 MCP·A2A 클라이언트에서 게시된 Copilot Studio 에이전트를 호출하는 Python 샘플을 소개했습니다. 프로토콜별 검색·호출 방식, Entra 위임 인증과 대화 맥락 유지, 프리뷰 제한을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 외부 앱에서 Copilot Studio 에이전트를 부르려면? MCP·A2A Python 클라이언트로 이해하기

MCP나 A2A라고 하면 Copilot Studio가 외부 도구·에이전트를 호출하는 구성을 먼저 떠올리기 쉽습니다. 이번 MCSCAT 글은 **반대 방향**, 즉 외부 클라이언트가 게시된 Copilot Studio 에이전트를 호출하는 방법을 다룹니다.

이미 MCP 또는 A2A를 지원하는 애플리케이션·에이전트 호스트라면 같은 프로토콜로 Copilot Studio 기능을 연결할 수 있다는 접근입니다. 예제는 요리 도우미지만 핵심은 업무 에이전트에도 적용할 수 있는 연결 구조입니다.

![MCP·A2A 프로토콜 클라이언트 기술 글 대표 이미지](/mwkorea/assets/images/2026-10-29-CopilotStudioMCPA2AClients/image1.jpg)

---

## 먼저 확인할 것: 2026년 10월 기준 프리뷰

원문은 이 채널을 **GitHub Copilot harness를 대상으로 하며 early release 환경에 순차 제공되는 프리뷰**라고 명시합니다. 모든 Copilot Studio 환경에 GA로 제공된 기능으로 읽으면 안 됩니다.

가용성과 Entra 권한은 [공식 채널 설정 안내](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/publication-channels-mcp-agent-to-agent)에서 확인해야 합니다. 아래 내용은 10월 29일 원문 시점의 구현 설명이며, 최신 문서의 지원 상태가 달라질 수 있습니다.

## MCP와 A2A의 호출 방식

| 구분 | 샘플의 흐름 |
|---|---|
| MCP | Streamable HTTP 연결 → 도구 검색 → 에이전트의 `send-message` 도구 호출 |
| A2A | Agent Card와 skill 검색 → SDK 클라이언트 구성 → 스트리밍 응답 이벤트 소비 |

두 클라이언트 모두 공식 Python SDK를 사용합니다. MCP의 `mcp_client.py`에서는 `mcp.Client`, `streamable_http_client`, `list_tools()`, `call_tool()`이 핵심입니다. A2A의 `a2a_client.py`에서는 `new_text_message`, `SendMessageRequest`를 구성하고 `send_message()`가 내보내는 이벤트를 비동기로 처리합니다.

전체 구현은 [Python protocol clients 샘플](https://microsoft.github.io/CopilotStudioSamples/extensibility/copilotstudio-protocol-clients/)과 [샘플 저장소](https://github.com/microsoft/CopilotStudioSamples/tree/main/extensibility/copilotstudio-protocol-clients)에서 확인할 수 있습니다. 본문에 소개된 짧은 호출 부분만으로 인증과 오류 처리가 모두 완성되는 것은 아닙니다.

## 인증: 접근 가능한 사용자의 위임 권한

샘플은 MSAL을 사용해 에이전트 접근 권한이 있는 사용자로 브라우저 로그인합니다. 구성 요소는 다음과 같습니다.

- 단일 테넌트 데스크톱 앱 등록과 `http://localhost` 리디렉션 URI.
- MCP 호출용 **`MCS.InvokeAsMCP`** 또는 A2A 호출용 **`MCS.InvokeAsA2A`** 위임 권한.
- 획득한 액세스 토큰을 bearer token으로 전달.
- 이후 조용한 로그인을 지원하는 **OS 암호화 토큰 캐시**.

등록과 동의의 구체적인 단계는 [README의 인증 절차](https://microsoft.github.io/CopilotStudioSamples/extensibility/copilotstudio-protocol-clients/#configure-sign-in)를 따라야 합니다. 이 글이 인증 구성이나 권한 동의를 대신 수행하는 것은 아닙니다.

## 후속 질문에서는 대화 ID를 이어주세요

대화 기록은 Copilot Studio가 유지합니다. 클라이언트는 후속 메시지와 함께 MCP가 반환한 **`conversationId`** 또는 A2A의 **`context_id`**를 전달해야 합니다.

전체 스크립트에는 페이지 처리, 시간 제한, 응답 표시와 대화 ID 관리가 포함됩니다. 이 부분을 빠뜨리면 첫 질문은 동작해도 후속 질문의 맥락이 끊길 수 있습니다.

## 샘플 시작 순서

README에 따라 요리 에이전트를 가져오고 로그인 구성을 준비한 뒤, A2A에는 **Agent Card URL**, MCP에는 **MCP URL**을 사용합니다. 유제품 없는 피자를 요청한 다음 치즈 대체재를 묻는 식으로 후속 맥락을 확인할 수 있으며, `/new`는 새 대화를 시작합니다.

국내 개발팀은 먼저 허용된 테스트 환경에서 채널 가용성, 사용자 위임 권한과 대화 연속성을 확인하는 것이 좋습니다. 프로토콜 지원은 접근 통제의 대체재가 아니며, 에이전트가 다루는 데이터와 액션의 권한은 별도로 검토해야 합니다.

> **출처**: [I Read the MCP and A2A Docs So Adi Didn't Have To — MCSCAT Blog, The Custom Engine](https://microsoft.github.io/mcscatblog/posts/grumpy-protocol-clients/). 자세한 내용은 원문 참조.
