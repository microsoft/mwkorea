---
title: "에이전트도 내 업무 취향을 기억한다: Work IQ 메모리 읽기 기능 예고"
date: 2026-11-05T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - MCP
  - Agent
  - Personalization
excerpt: "Work IQ MCP에 사용자 메모리 프로필을 읽는 경로가 추가됩니다. 읽기 전용 범위와 관리자 정책, 개인화 설정의 관계를 도입 담당자 관점에서 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트도 내 업무 취향을 기억한다: Work IQ 메모리 읽기 기능 예고

에이전트에게 일을 맡길 때마다 선호하는 답변 형식이나 업무 배경을 다시 설명해야 한다면, 자동화의 이점도 줄어듭니다. Microsoft는 Work IQ를 통해 인증된 사용자의 메모리 프로필을 에이전트가 참고할 수 있도록 확장할 예정입니다.

2026년 11월 5일 공개된 MC1539004의 핵심은 **개인화 정보를 읽는 새로운 MCP 경로**입니다. 모든 사람의 기억을 공유하거나 에이전트가 메모리를 마음대로 수정하는 기능과는 다릅니다.

---

## 무엇을 읽을 수 있나요?

새 경로는 `/memory/me/coreMemories`입니다. 출시 시점의 프로필에는 Custom Instructions, Saved Memories, 채팅 기록에서 도출한 메모리가 포함됩니다. 프로필은 향후 발전할 수 있다고 안내되어 있습니다.

이 경로는 **`fetch` 도구만 지원하는 읽기 전용**입니다. Work IQ MCP로 메모리를 쓰거나 수정할 수 없으며, 인증된 사용자 본인의 프로필만 사용할 수 있습니다. 다른 사용자에게 해당 프로필이 공유되는 구조도 아닙니다.

## 관리자 정책과 개인 설정이 함께 적용됩니다

관리자 제어 위치는 다음과 같습니다.

`Microsoft 365 Admin center > Agents > Tools > Registry > Work IQ MCP > Policies`

여기에 메모리 읽기를 제어하는 정책이 추가되며, 다른 읽기 정책처럼 기본적으로 활성화됩니다. 별도 관리자 작업은 필수가 아니지만, 에이전트의 개인화 정보 접근을 관리하려는 조직은 이 정책을 검토해야 합니다.

사용자의 `Copilot Chat > Settings > Personalization` 설정도 존중됩니다.

| 설정 | 비활성화했을 때의 영향 |
|---|---|
| Enhanced personalization | Copilot Memory가 꺼지고 MCP 경로에서도 제공되지 않음 |
| Customize Copilot | Custom Instructions가 프로필에서 제외됨 |
| Saved memories | 저장된 메모리가 제외됨 |
| Chat history & work insights | 채팅 기록과 Microsoft 365 활동에서 도출한 인사이트가 제외됨 |

Enhanced personalization과 사용자 설정 변경은 적용까지 **최대 48시간** 걸릴 수 있습니다. 정책 변경 직후의 결과만 보고 반영 실패로 판단하지 않도록 운영 절차에 이 지연을 포함하는 것이 좋습니다.

## 일정과 도입 체크포인트

원문은 전 세계 일반 공급을 **2026년 12월 초 시작, 12월 말 완료 예상**으로 안내합니다. 이 글 작성 시점에 모든 테넌트에 이미 제공된 기능으로 이해하면 안 됩니다.

대상은 Work IQ MCP 서버에 접근할 수 있는 에이전트를 사용하고, 해당 개인화 설정이 정보 포함을 허용한 사용자입니다. 국내 조직에서는 메모리 읽기 정책의 기본 활성화 여부를 확인하고, 사용자가 어떤 설정으로 정보 범위를 조절할 수 있는지 안내하는 것이 우선입니다.

## 마무리

이번 변화는 에이전트의 개인화 수준을 높이면서도 **사용자 본인·읽기 전용·설정 존중**이라는 경계를 둔다는 데 의미가 있습니다. 업무 에이전트를 설계할 때도 메모리를 수정하는 기능으로 오해하지 않고, 설정 반영 지연까지 고려해야 합니다.

> **출처**: [MC1539004 — Work IQ expands memory capabilities to agents](https://mc.merill.net/message/MC1539004). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제공되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
