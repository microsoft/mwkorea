---
title: "말을 이해하고 행동하는 음성 에이전트: MAI Realtime 1"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - Realtime
  - VoiceAgent
  - Foundry
  - Dynamics365
excerpt: "MAI Realtime 1은 자연스러운 대화와 업무 도구 연결을 목표로 하는 음성 대 음성 모델입니다. 분당 0.01달러 기본 요금과 별도 추론 비용, OpenAI Realtime API 호환 및 제한 접근 프리뷰 조건을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 말을 이해하고 행동하는 음성 에이전트: MAI Realtime 1

좋은 음성 에이전트는 듣기 좋은 목소리만으로 완성되지 않습니다. 사용자가 끼어들면 멈추고, 짧은 맞장구와 발화 종료를 구분하며, 필요한 업무 시스템까지 연결해야 합니다.

Microsoft AI의 첫 **speech-to-speech 모델 MAI Realtime 1**은 대화·추론·실행을 함께 다루는 기업용 음성 경험을 목표로 합니다. 상담이나 업무 에이전트를 만드는 팀은 대기 시간뿐 아니라 별도 추론 비용과 제공 단계까지 살펴봐야 합니다.

![MAI Realtime 1 공식 소개 이미지](/mwkorea/assets/images/2026-11-18-MAIRealtimeOne/image1.jpg)

---

## 대화에서 실제 작업까지

원문은 다음 다섯 가지를 강조합니다.

| 역량 | 설명 |
|---|---|
| 자연스러운 대화 | 중간 끼어들기, 짧은 반응, 발화가 끝날 때까지 기다리기 |
| 적응형 지능 | 빠른 응답과 더 깊은 추론이 필요한 요청을 조합 |
| 견고한 이해 | 배경 소음과 다른 사람의 발화가 있는 환경의 요청 이해 |
| 실제 업무 실행 | 기업 시스템·도구와 연결해 복잡한 요청 수행 |
| 페르소나 조정 | 프롬프트로 어조·스타일·행동 조정 |

OpenAI Realtime API와의 호환도 제공해 기존 음성 앱의 시험·이전을 돕는다고 설명합니다. 호환성이 모든 옵션과 운영 동작의 완전한 동일성을 보장하는 것은 아니므로 실제 사용하는 기능은 별도 확인해야 합니다.

## “분당 0.01달러”에 포함되지 않는 비용

| 항목 | 원문 가격 |
|---|---|
| 기본 speech-to-speech | 오디오 분당 0.01달러 |
| 추가 추론 입력 | 100만 토큰당 1달러 |
| 추가 추론 출력 | 100만 토큰당 5달러 |

기본 음성 비용과 추론은 **별도 청구**입니다. 도구 호출이 많은 상담을 단순히 통화 시간에 0.01달러만 곱해 견적 내면 총비용을 과소평가할 수 있습니다.

## 성능 주장과 적용 사례

Microsoft는 Big Bench Audio, τ-Voice 및 Dynamics 365 Contact Center 평가에서 GPT Realtime 2.1 대비 품질·속도·가격의 우위를 제시합니다. 결과는 특정 구성과 업무에 따른 것이며 원문에는 모든 언어의 지연 시간이나 한국어 정확도 보장이 없습니다.

Agoda와 Reservations.ai가 시험 중이라고 소개하며, **Dynamics 365 Contact Center** 고객 서비스 및 **Dragon Copilot**의 간호사 임상 대화 연습용 AI 환자 시뮬레이션에도 도입하는 방향을 발표했습니다. 이를 모든 고객 대상 배포 완료로 읽으면 안 됩니다.

## 시작하기와 프리뷰 조건

[MAI Labs](https://labs.microsoft.ai/?model=mai-realtime-1)에서 체험하거나 [Foundry 제한 접근 프리뷰 관심 등록](https://forms.cloud.microsoft/r/AQcVUgqpZZ)을 할 수 있습니다.

원문은 프리뷰 고객에게 **공개 프리뷰 시작 전까지 청구하지 않는다**고 설명합니다. 영구 무료나 일반 공개 완료를 뜻하지 않습니다.

## 한국어 음성 에이전트의 검증 포인트

한국어 고유명사·숫자·주소 인식, 끼어들기, 소음, 상담원 전환, 도구 호출 승인과 실패 처리부터 확인하는 것이 좋습니다. 녹음·대화 기록·민감정보의 보관 정책도 함께 설계해야 합니다.

이 모델의 발표는 음성 채널의 가능성을 보여 주지만, 실제 서비스 품질과 운영 책임은 응용 시스템의 검증에 달려 있습니다.

> **출처**: [MAI Realtime 1: Leading voice AI at $0.01 per audio minute](https://microsoft.ai/news/introducing-mai-realtime-1/), Microsoft AI 뉴스 블로그. 자세한 내용은 원문 참조.
