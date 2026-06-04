---
title: "에이전트가 일하는 곳으로: Teams에서 만드는 협업형 에이전트 (Build 2026)"
date: 2026-06-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent
  - MicrosoftTeams
  - TeamsSDK
  - WorkIQ
  - Build2026
  - Developer
excerpt: "AI 에이전트를 만들었다면, 이제 사용자·맥락·실제 업무에 참여할 통로가 필요합니다. Microsoft Build 2026에서 Teams를 에이전트의 무대로 만드는 투자가 발표되었습니다. Teams SDK가 Python·JavaScript·C#로 정식 출시(GA)되고, Teams 개발자 CLI로 등록·설정이 자동화됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트가 일하는 곳으로: Teams에서 만드는 협업형 에이전트

AI 에이전트를 하나 만들었다고 가정해 봅시다. 그다음 필요한 것은 세 가지입니다 — **사용자**, **맥락**, 그리고 **실제 업무에 참여할 방법**. Microsoft Teams는 이 세 가지를 한 번에 제공합니다. 그리고 Microsoft Build 2026에서, 에이전트를 Teams로 데려오는 일이 **훨씬 더 쉬워진다**는 소식이 발표되었습니다.

이번 발표의 핵심은 분명합니다. 에이전트를 단순한 봇이 아니라 **일상 업무 속 동료(teammate)** 로 만드는 것 — 대화에 참여하고, 작업을 완료하고, 논의를 실제 행동으로 옮기는 존재로 만드는 것입니다.

> **이 글의 한 줄 요약**
> **Microsoft Teams SDK**가 Python·JavaScript·C#로 **정식 출시(GA)** 되었습니다. Work IQ 기반으로 채팅·채널·회의에서 일관되게 동작하는 협업형 에이전트를 단일 플랫폼으로 만들 수 있고, **Teams 개발자 CLI**가 앱 등록·설정을 자동화합니다. GCC High·DoD 같은 소버린 클라우드도 지원됩니다.

---

## 왜 Teams인가

개발자는 Teams에서 **자기 조직용 에이전트**를 만들 수도 있고, **에이전트 스토어에 게시**해 모든 사용자에게 배포할 수도 있습니다. 이미 **Linear, Cursor** 같은 파트너들이 에이전트를 업무 흐름 안에 직접 들여놓고, 대화에 참여하고 작업을 완료하며 "논의 → 실행"으로 일을 옮기는 모습을 보여주고 있습니다.

![Teams 안에서 동작하는 에이전트 데모](/mwkorea/assets/images/2026-06-03-CollaborativeAgents/image1.webp)

---

## 더 빠르게 만들고 배포하기: Teams SDK

지금까지 에이전트를 만들려면 등록(registration), 자격 증명(credentials), 매니페스트 생성, 여러 도구에 걸친 배포를 일일이 챙겨야 했습니다. 정작 흥미로운 작업에 도달하기도 전에 개발 속도가 느려졌죠.

**Microsoft Teams SDK**는 이 과정을 단순화합니다.

- **Work IQ 기반**으로 채팅·채널·회의를 가로지르는 지능형 에이전트를 **단일·일관된 플랫폼**에서 구축
- 대화 전반에서 **맥락을 인지하는(context-aware)** 일관된 상호작용 제공 → 에이전트가 어디서든 자연스럽게 업무를 지원
- 아이디어에서 동작하는 프로토타입까지의 경로를 가속
- **Python, JavaScript, C#** 로 정식 출시(GA)

---

## 반복 작업을 줄여주는 Teams 개발자 CLI

**Teams 개발자 CLI**는 앱 등록과 구성 같은 설정 작업을 자동화해, 컨텍스트 전환과 반복 작업을 줄여 줍니다. 확장된 언어 지원과 함께, 개발자가 에이전트를 구축하는 방식에 더 많은 유연성을 제공합니다.

---

## 소버린 클라우드(GCC High·DoD)까지 확장

개발 경험을 다듬는 동시에, 그 경험이 닿는 **환경의 범위도 넓어졌습니다**. Microsoft 365 Agents Toolkit과 Developer Portal이 **GCC High·DoD를 포함한 소버린 하이클라우드 환경**을 지원합니다.

- 해당 테넌트를 대상으로 하는 개발자도 **동일한 에이전트 생성·업데이트 흐름**을 그대로 사용
- 클라우드 인지(cloud-aware) 처리가 기본 내장되어 **수동 우회 작업 불필요**
- 인증 엔드포인트, 토큰 스코프, 클라우드별 서비스 라우팅이 자동 반영되어 프로비저닝과 런타임 동작을 일관되게 유지

![Teams 채널의 타깃 메시지 예시](/mwkorea/assets/images/2026-06-03-CollaborativeAgents/image2.webp)

---

## 개발자 관점 정리

| 항목 | 내용 |
|------|------|
| **무대** | Teams의 채팅·채널·회의 — 사용자·맥락·실제 업무가 모이는 곳 |
| **빌드 도구** | Teams SDK (Python/JS/C# GA), Work IQ 기반 |
| **자동화** | Teams 개발자 CLI로 등록·구성 자동화 |
| **배포** | 자기 조직용 또는 에이전트 스토어 게시 |
| **확장 환경** | GCC High·DoD 등 소버린 클라우드 지원 |

---

## 마무리

에이전트는 만든다고 끝이 아니라, **사람들이 실제로 일하는 곳에 들어가야** 비로소 가치를 냅니다. 이번 Build 2026 발표는 Teams를 그 무대로 삼아, 등록·배포의 마찰을 줄이고 에이전트를 "동료"로 끌어올리는 방향을 분명히 했습니다. 사내 자동화를 검토하는 팀이라면, Teams SDK와 개발자 CLI로 프로토타입을 빠르게 만들어 보는 것을 권합니다.

---

> ※ 본 글은 Microsoft 365 Developer Blog의 [Build collaborative agents where work happens](https://devblogs.microsoft.com/microsoft365dev/build-collaborative-agents-where-work-happens/)를 바탕으로 한국 독자용으로 정리했습니다. 자세한 내용과 최신 일정은 원문을 참조하세요. 출시 일정·기능은 변경될 수 있습니다.
