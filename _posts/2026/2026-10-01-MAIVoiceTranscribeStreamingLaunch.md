---
title: "실시간 1등 음성인식 모델 등장: MAI-Transcribe-2-Streaming과 새 음성 모델 MAI-Voice-2.1"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - MAI
  - Speech
  - VoiceAgent
  - Transcription
  - Foundry
excerpt: "Microsoft AI가 실시간 스트리밍 음성 인식 모델 MAI-Transcribe-2-Streaming과 다국어 음성 합성 모델 MAI-Voice-2.1·2.1-Flash를 공개했습니다. 음성 에이전트의 '듣고-이해하고-말하는' 루프를 더 빠르고 자연스럽게 만드는 조합입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 실시간 1등 음성인식 모델 등장: MAI-Transcribe-2-Streaming과 새 음성 모델 MAI-Voice-2.1

![실시간 음성인식](/mwkorea/assets/images/2026-10-01-MAIVoiceTranscribeStreamingLaunch/image1.webp)

Microsoft AI(MAI)가 2026년 10월 1일, 실시간 스트리밍 음성 인식 모델 **MAI-Transcribe-2-Streaming**과 함께 두 개의 새로운 음성 합성(TTS) 모델 **MAI-Voice-2.1**, **MAI-Voice-2.1-Flash**를 공개했습니다. MAI-Transcribe-2-Streaming은 Artificial Analysis 벤치마크에서 1위에 올랐으며, 음성 비서·콜센터 봇 같은 "음성 에이전트"를 만들 때 체감이 크게 달라지는 구성요소들입니다.

Microsoft 365 Copilot이나 Copilot Studio로 음성 기반 에이전트를 구축하는 국내 개발자·기업 입장에서, 이번 발표는 "말이 끝나기 전에 반응하는" 실시간 대화형 에이전트를 더 쉽고 저렴하게 만들 수 있는 토대가 된다는 점에서 주목할 만합니다.

---

## MAI-Transcribe-2-Streaming: 실시간 전사, 정말 빠릅니다

MAI-Transcribe-2-Streaming은 **60개 언어**에 대해 저지연 실시간 전사(transcription)를 제공하며, 언어를 자동으로 연속 감지합니다.

- Artificial Analysis에서 최종(final) 전사와 부분(partial) 전사 정확도 모두 **1위**
- 정확도 대 지연시간(accuracy-vs-latency) 평가에서 파레토 프론티어(Pareto frontier)에 위치 — 더 높은 정확도를 위해 지연시간을 크게 희생하지 않는다는 의미
- 오디오 수신 후 약 **100ms 이내**에 첫 "partial(잠정)" 전사 결과를 내놓고, 이후 맥락이 쌓이면서 결과를 보정하며 안정적인 최종 전사를 확정
- 내부 평가 기준으로 실시간 받아쓰기·자막 작업에서 경쟁 모델 대비 **2배 빠르게** 단어가 화면에 나타남
- 연말까지 도입 가격 **시간당 $0.54**로 제공

이 "잠정 결과"가 중요한 이유는, 음성 에이전트가 **사용자의 말이 끝나기 전에** 추론을 시작하거나 도구를 호출할 수 있게 해주기 때문입니다. 실시간 받아쓰기나 자막 생성에도 바로 활용할 수 있습니다.

## MAI-Voice-2.1: 하나의 목소리로 23개 언어를 자연스럽게

MAI-Voice-2.1은 Microsoft AI의 가장 강력한 다국어 TTS(음성 합성) 모델입니다.

- **23개 언어, 26개 로케일** 지원
- 하나의 "목소리"가 언어를 바꿔도 **동일한 화자**처럼 들리며, 각 언어의 억양을 자연스럽게 따라감 (영어 → 중국어 → 독일어로 전환해도 같은 목소리 유지)
- 다국어 튜터링 앱이 교사를 바꾸지 않고 언어만 전환하거나, 다국어 어시스턴트가 질문 언어에 맞춰 응답하는 시나리오에 적합
- 가격은 **100만 자당 $22**

## MAI-Voice-2.1-Flash: 대량 트래픽을 위한 초고속 버전

MAI-Voice-2.1-Flash는 같은 언어·화자 전환 기능을 지원하면서, 지연시간에 민감한 대용량 워크로드에 맞게 최적화되었습니다.

- 최대 **45초 분량의 오디오**를 생성
- 종단 간(end-to-end) 지연시간 단 **150ms**
- 기존 대비 **55% 빠른 추론**, 비교 모델 대비 **약 60% 저렴**
- 가격은 업계 최고 수준인 **100만 자당 $15**

MAI-Transcribe-2-Streaming과 짝을 이루면, 자연스럽고 지연 없는 음성 에이전트 경험을 만드는 데 최적의 조합이 됩니다.

두 음성 모델 모두 **몇 초의 참조 음성만으로 모든 지원 언어에 걸쳐 음성 클로닝**이 가능하며, 오남용을 막기 위한 동의(consent) 가드레일이 내장되어 있습니다.

---

## 왜 이 조합이 중요한가: 음성 에이전트의 루프

음성 에이전트는 결국 "듣고 → 이해하고 → 결정하고 → 말하는" 루프입니다. 이 루프가 사람이 "대화"로 느끼는 시간 안에 끝나야 하죠. MAI-Transcribe-2-Streaming과 MAI-Voice-2.1-Flash를 함께 쓰면 양쪽 끝에서 시간을 절약해, 에이전트가 추론하고 도구를 쓰고 답을 검증할 여유를 벌어줍니다.

활용 예시:

- **고객 서비스 에이전트**: 말하는 대로 실시간 전사하고, 발화가 끝나기 전에 행동을 시작하고, 자연스러운 음성으로 응답
- **다국어 어시스턴트**: 언어를 자동 감지해 23개 언어 중 어떤 언어로도 같은 목소리·같은 억양으로 응답
- **인터랙티브 학습·미디어**: 튜터링, 롤플레이, 시뮬레이션, 내레이션에 언어별로 구분된 화자 활용

---

## 시작하기

Microsoft AI는 이 세 모델이 함께 동작하는 모습을 보여주는 새로운 데모 "Chatter"를 MAI Playground에 공개했습니다.

- MAI-Voice-2.1, MAI-Voice-2.1-Flash는 [OpenRouter](https://aka.ms/mai-openrouter)에서 바로 사용 가능
- 세 모델 모두 Microsoft Foundry를 통해 제공:
  - [MAI-Transcribe-2-Streaming 문서](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe-2-streaming?context=/azure/foundry/context/context)
  - [MAI-Voice-2.1 / MAI-Voice-2.1-Flash 문서](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-voices?context=%2Fazure%2Ffoundry%2Fcontext%2Fcontext&tabs=mai-voice-2-1-flash&pivots=ai-foundry)

Copilot Studio나 Microsoft 365 Copilot 기반 에이전트에 음성 인터페이스를 더하려는 국내 개발팀이라면, 이번에 공개된 가격과 지연시간 수치를 PoC 설계에 참고할 만합니다.

---

> **출처**: [Our first streaming transcription model debuts at no. 1 on Artificial Analysis (Microsoft AI News, 2026-10-01)](https://microsoft.ai/news/our-first-streaming-transcription-model/) · 자세한 내용은 원문 참조
