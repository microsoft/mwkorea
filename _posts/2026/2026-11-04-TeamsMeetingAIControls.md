---
title: "Teams 회의 AI 정책이 두 개로 나뉩니다: AI 사용과 전사를 따로 관리하세요"
date: 2026-11-04T00:00:00 KST
categories:
  - Copilot
tags:
  - Teams
  - Copilot
  - Governance
  - Transcription
excerpt: "Teams의 기존 Copilot 회의 정책이 MeetingAI와 TranscriptionWithMeetingAI로 분리됩니다. 11월 3일 수정 공지 기준 Targeted Release는 12월, 전 세계 GA는 2027년 1월 예정으로 기존 스크립트 점검이 필요합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Teams 회의 AI 정책이 두 개로 나뉩니다: AI 사용과 전사를 따로 관리하세요

회의에서 AI를 허용할지와 전사를 시작할지는 서로 다른 결정입니다. Teams는 이 두 판단을 더 명확하게 구분하도록 기존 Copilot 회의 정책을 개편합니다.

관리자에게 중요한 부분은 화면 이름 변경만이 아닙니다. 기존 동작은 자동 이전되지만, **PowerShell로 정책을 읽고 수정하는 자동화는 새 속성으로 전환**해야 합니다.

---

## 새 정책과 회의 옵션

| 구분 | 역할 |
|---|---|
| `MeetingAI` | Copilot, Facilitator, Intelligent Recap 등 회의 AI 사용 제어 |
| `TranscriptionWithMeetingAI` | 회의 AI를 켰을 때 전사를 자동 시작할지 제어 |
| 기존 `Transcription` | 전사 자체를 허용할지 제어하며 계속 유지 |

회의 옵션에는 **Who can manage AI**, **Who can use AI**, **Start Transcription with AI**가 제공됩니다. 주최자는 허용된 범위에서 AI 관리·사용 대상을 정하고, 전사 없이 Copilot을 쓰는 회의에서도 Intelligent Recap 생성 여부를 관리할 수 있습니다.

## 기존 설정은 한 번 자동 매핑

예를 들어 저장된 전사를 필수로 요구하던 설정은 AI 켜짐과 변경 불가능한 전사 시작 설정으로 옮겨집니다. 전사 없이 Copilot을 허용하던 설정은 AI 켜짐과 전사 자동 시작 꺼짐으로 표현됩니다.

**AI를 강제로 끄면 연동된 전사 시작도 꺼집니다. 이후 전사 시작을 다시 켜면 AI 강제 끄기 상태는 유지되지 않습니다.** 서로 다른 정책의 조합이 실제 의도와 맞는지 확인해야 합니다.

새 제어가 활성화되면 기존 `Copilot` 정책을 직접 수정하려는 요청은 새 정책을 사용하라는 안내를 반환합니다. 자동 이전이 된다고 해서 오래된 관리 스크립트까지 계속 동작하는 것은 아닙니다.

## 최신 공지의 배포 일정

11월 3일 수정 본문 기준 일정은 다음과 같습니다.

- **Targeted Release**: 2026년 12월 초 시작, 12월 중순 완료 예정.
- **전 세계 GA**: 2027년 1월 초 시작, 1월 중순 완료 예정.

초기 공지의 11월 일정을 그대로 적용하면 안 됩니다. 이 글의 날짜는 수집 피드의 수정 시각을 KST로 변환한 기준이며, 원 공지 최초 게시일은 10월 30일입니다.

## 한국 조직의 준비 사항

회의 정책 스크립트, 운영 문서, 헬프데스크 가이드를 새 속성 이름에 맞춰 점검하세요. 배포 이후에는 자동 매핑 결과를 확인하고, 전사·AI 사용 정책이 조직의 기록 및 개인정보 보호 기준과 일치하는지 검토하는 것이 좋습니다. 정책 변경 자체가 기존 고객 데이터의 처리·저장 방식을 바꾸는 것은 아니라고 원문은 설명합니다.

> **출처**: MC1532253 — [Enhanced Copilot and AI controls for meetings](https://mc.merill.net/message/MC1532253). [Microsoft 365 Roadmap 577399](https://www.microsoft.com/microsoft-365/roadmap?searchterms=577399). 실제 출시 일정·기능은 변경될 수 있습니다.
