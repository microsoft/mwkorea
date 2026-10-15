---
title: "Agent Builder에서 프롬프트를 예약 실행한다: 시간·요일 단위 워크플로 기능 출시 일정 조정"
date: 2026-10-14T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - AgentBuilder
  - Workflow
  - Agent
  - Automation
excerpt: "Microsoft 365 Copilot Agent Builder에서 에이전트 프롬프트를 매시간·매일·매주·매월·매년 자동 실행하는 워크플로를 만들 수 있습니다. 2026년 10월 13일 일정이 조정되어 10월 말 시작, 11월 말 완료 예정입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Agent Builder에서 프롬프트를 예약 실행한다: 시간·요일 단위 워크플로 기능 출시 일정 조정

Microsoft 365 Copilot의 Agent Builder에 **프롬프트를 정해진 주기로 자동 실행하는 워크플로(스케줄 프롬프트)** 기능이 도입됩니다. 고객 피드백에서 "더 많은 자동화와 선제적 인사이트"가 요청된 것이 배경이며, 사용자가 매번 직접 프롬프트를 입력하지 않아도 Copilot 에이전트가 반복 업무를 수행하게 됩니다.

이 내용은 Message Center 공지 MC1302906(2026년 5월 6일 최초 게시)이며, 2026년 10월 13일 **일정이 업데이트**되었습니다.

![Agent Builder에서 워크플로 만들기 메뉴](/mwkorea/assets/images/2026-10-14-CopilotAgentBuilderScheduledPrompts/image1.png)

---

## 일정

- 일반 공급(GA, 전 세계): **2026년 10월 말 시작**(기존 9월 초), **11월 말 완료**(기존 9월 말) 예정

## 핵심 기능

- 에이전트별로 **프롬프트 텍스트, 트리거·반복 패턴, 날짜·시간·표준 시간대**를 지정하는 워크플로 생성
- 지원 반복 주기: **매시간, 매일, 매주, 매월, 매년**
- Agent Builder 안에서 워크플로 **보기, 편집, 미리 보기, 삭제** 가능
- 상단 메뉴의 "Create a workflow for this agent" / "Manage workflows"로 접근

![워크플로 프롬프트와 예약 설정(매주 금요일 오후 1:30)](/mwkorea/assets/images/2026-10-14-CopilotAgentBuilderScheduledPrompts/image2.png)

## 알아둘 제한사항

- 워크플로는 **사용자별**로 구성되며, **만든 사용자에게만** 실행됩니다.
- 에이전트를 공유해도 **워크플로는 공유되지 않습니다**.
- **초안 또는 게시되지 않은 에이전트**에서는 예약 워크플로가 실행되지 않습니다.
- 기본적으로 **활성화**되어 있으며, 기존 테넌트·Copilot 정책을 따릅니다.
- 대상: Microsoft 365 Copilot(Premium)에서 Agent Builder로 에이전트를 만들고 관리하는 사용자

## 활용 시나리오

- 매주 금요일 오후에 프로젝트 진행 현황 요약 받기
- 매일 아침 특정 주제의 최신 동향 정리
- 월말마다 정기 리포트 초안 준비

## 관리자·도입 담당자 체크포인트

- 별도 관리자 조치는 필요 없습니다.
- 에이전트를 만드는 사용자에게 기능 제공 사실을 안내하고, 사내 문서·교육 자료를 업데이트하세요.
- 개인정보·컴플라이언스 요청은 기존 DSR(Data Subject Request) 절차를 사용합니다.
- 실제 출시 일정은 다시 조정될 수 있으므로 Message Center를 계속 확인하세요.

---

> **원문**: MC1302906 — [Microsoft 365 Copilot: Schedule prompts in Agent Builder](https://mc.merill.net/message/MC1302906) / [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
