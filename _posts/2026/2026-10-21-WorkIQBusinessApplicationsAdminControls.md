---
title: "Work IQ에 업무 앱 데이터를 연결할 때: 관리자·환경·메이커의 제어를 나눕니다"
date: 2026-10-21T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - PowerPlatform
  - Governance
  - MCP
excerpt: "Business Applications 데이터를 Work IQ에 활용하기 위한 관리자 제어가 공개 프리뷰로 예고됐습니다. AI 관리자, 환경 관리자, 메이커가 각각 참여 경험·환경·앱과 데이터를 선택하며, 기능 활성화가 기존 데이터 권한을 확대하지는 않습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Work IQ에 업무 앱 데이터를 연결할 때: 관리자·환경·메이커의 제어를 나눕니다

Copilot이 문서와 메일을 넘어 업무 애플리케이션의 데이터를 이해하려면 데이터 연결만큼 중요한 것이 접근 범위입니다. 어떤 AI 경험이 어떤 환경과 앱을 활용해도 되는지 조직이 결정할 수 있어야 합니다.

MC1518036은 Business Applications 데이터를 Work IQ의 grounding에 활용하기 위한 관리자 제어를 안내합니다. **2026년 11월 17일까지 공개 프리뷰 제공 예정**이며, 일반 제공(GA) 완료 공지는 아닙니다. 파일 날짜는 피드의 발행 시각을 한국 시간으로 환산한 10월 21일입니다.

---

## 세 계층이 서로 다른 범위를 결정합니다

| 담당자 | 관리 위치와 제어 범위 |
|---|---|
| AI 관리자 | Microsoft 365 관리 센터의 **Copilot > Settings**에서 Copilot의 업무 앱 이용 여부 관리. **Agents > Tools**의 Work IQ MCP를 통한 이용 가능 여부도 관리 |
| 플랫폼·환경 관리자 | Power Platform admin center(PPAC)에서 Work IQ 기능을 받을 환경과 추론·작업 대상 환경 선택. 사용자·에이전트·앱의 환경 데이터 접근 관리 |
| 메이커 | 활성화된 환경 안에서 참여할 개별 앱과 데이터 선택 |

**환경을 켰다고 모든 앱과 데이터가 자동 포함되는 것은 아닙니다.** 조직 차원의 기능 허용과 실제 데이터 참여 범위를 분리해 이해해야 합니다.

## 기존 권한은 그대로 존중됩니다

원문은 Work IQ가 업무 앱 데이터와 AI 경험의 기존 권한을 존중한다고 명시합니다. 기능 활성화는 사용자·에이전트·애플리케이션·데이터 권한을 대체하거나 확대하지 않습니다.

따라서 “Work IQ를 켰으니 데이터를 모두 볼 수 있다”거나 반대로 “기존 권한만 있으면 모든 AI 경험에서 자동 활용된다”고 단정하면 안 됩니다. 기존 접근 권한과 새로 제공되는 참여 제어를 함께 확인해야 합니다.

## 프리뷰 전에 준비할 체크포인트

우선 업무 앱 데이터의 기존 권한을 점검하고, 연결할 AI 경험과 PPAC 환경을 선택하세요. 다음으로 해당 환경에서 사용자·에이전트·앱이 접근할 수 있는 데이터를 검토하고, 메이커와 포함·제외할 앱 및 데이터 범위를 합의하는 것이 공지의 권고입니다.

한국 조직에서는 운영·개발 환경을 구분하고, 개인정보나 고객 데이터가 포함된 앱을 우선 검토하는 방식으로 준비할 수 있습니다. 이는 도입상의 제안이며, 공지가 특정 한국 규정 준수나 모든 지역의 즉시 제공을 보장하는 것은 아닙니다.

## 마무리

업무 데이터 grounding의 가치는 데이터를 많이 연결하는 데만 있지 않습니다. **어떤 경험이 무엇을 활용할 수 있는지 계층별로 통제할 수 있어야** 지속 가능한 에이전트 운영으로 이어집니다.

> **출처**: [MC1518036 — Microsoft Copilot - Admin controls to manage Business Applications in Work IQ](https://mc.merill.net/message/MC1518036) · [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) (이 공지에는 개별 Roadmap ID가 명시되지 않았습니다). 실제 출시 일정·기능은 변경될 수 있습니다.
