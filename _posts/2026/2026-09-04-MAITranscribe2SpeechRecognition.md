---
title: "가장 빠르고 정확하고 저렴한 음성 인식: MAI-Transcribe-2 공개"
date: 2026-09-04T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - MAI
  - SpeechRecognition
  - Transcription
  - Diarization
  - MicrosoftFoundry
  - Benchmark
excerpt: "Microsoft AI가 새 음성 인식 모델 MAI-Transcribe-2를 공개했습니다. 화자 분리, 단어 단위 타임스탬프, 구성 가능한 전사 스타일을 지원하며 FLEURS 벤치마크 60개 언어에서 1위, 경쟁 모델 대비 최대 10배 빠른 속도를 냅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 가장 빠르고 정확하고 저렴한 음성 인식: MAI-Transcribe-2 공개

회의를 녹음해 자막으로 만들거나, 상담 내용을 기록으로 남기거나, 임상 소견을 받아 적는 작업. 이런 일의 품질은 결국 **음성을 텍스트로 옮기는 모델의 정확도와 속도**에 달려 있습니다.

Microsoft AI가 새 음성 인식 모델 **MAI-Transcribe-2**를 공개했습니다. 원문의 표현을 그대로 옮기면 **"지금까지 가장 성능이 뛰어난 전사 모델일 뿐 아니라, 경쟁 모델 사이에서도 가장 뛰어나고 효율적인"** 모델입니다.

![MAI-Transcribe-2](/mwkorea/assets/images/2026-09-04-MAITranscribe2SpeechRecognition/image1.webp)

---

## 무엇이 새로운가

MAI-Transcribe-2는 **화자 분리(diarization), 구성 가능한 전사 스타일, 단어 단위 타임스탬프** 같은 새 기능으로 **Gemini 3.5 Transcribe, GPT-Transcribe, Whisper V3-Large, ScribeV2** 같은 주요 모델들을 앞서면서도, 더 넓은 범위의 실제 오디오를 처리합니다.

### 벤치마크 성적

- **FLEURS 벤치마크 60개 언어에서 1위**, 평균 단어 오류율(Word-Error-Rate) **5.2%**
- **Artificial Analysis**에서 정확도-지연 시간 **파레토 프런티어(Pareto Frontier)** 정의
- Artificial Analysis 단어 오류율 리더보드 **2위** — 이전 버전에서부터 이어진 성능 개선 흐름

---

## 하나의 모델로 더 많은 문제를 해결

MAI-Transcribe-2는 **임상 기록부터 법률 문서화, 접근성, 자막 제작**까지 실제 업무 시나리오를 겨냥해 설계됐습니다.

### 핵심 기능

| 기능 | 내용 |
|---|---|
| **더 빠른 추론** | 특히 장시간 오디오에서 지연 시간이 크게 낮아짐 — 경쟁 모델 대비 **최대 10배 빠른 처리** |
| **화자 분리(Speaker diarization)** | 녹음 안에서 화자를 구분하고 발화를 올바른 사람에게 귀속 |
| **단어 단위 타임스탬프** | 모든 단어에 정밀한 시간 정보를 부여해 정확한 정렬·검색·탐색·편집 지원 |
| **키워드 바이어싱(Keyword biasing)** | 문맥만으로는 구분하기 어려운 전문 용어·약어·이름을 인식하도록 지원 |
| **구성 가능한 전사 스타일** | **"verbatim"** — 필러 단어와 말 더듬까지 그대로 기록해 컴플라이언스·분석에 활용. **"clean"** — 필러를 제거해 더 읽기 쉬운 자막·메모·전사본 생성 |
| **코드 스위칭(Code switching)** | 힝글리시, 스팽글리시처럼 자연스럽게 섞이는 언어 조합을 포함해 언어 간 전환이 있는 대화 지원 |
| **자동 언어 식별** | 사용자가 미리 지정하지 않아도 사용 중인 언어를 정확히 감지 |
| **잡음 환경에서의 견고함** | 통제된 녹음 환경을 벗어나도 전사 품질 유지 |
| **60개 언어 지원** | 전 세계 개발자에게 품질 좋은 전사 제공 |

---

## 정확도를 희생하지 않는 효율성

MAI-Transcribe-2는 **Artificial Analysis의 정확도-지연 시간 파레토 프런티어를 이끌며**, 최고 수준의 전사 품질과 **시장 최고의 배치 속도**를 결합합니다.

Artificial Analysis가 실시한 평가에 따르면 이 모델은 다음과 같이 더 높은 정확도를 유지하면서도 훨씬 빠릅니다.

- **OpenAI GPT-Transcribe 대비 10배** 빠름
- **ElevenLabs Scribe v2 대비 7배** 빠름
- **Gemini 3.5 Transcribe 대비 5배** 빠름

낮은 지연 시간이 중요한 상황에서 명확한 우위를 보여 준다는 설명입니다.

---

## 60개 언어에서 일관된 품질

MAI-Transcribe-2는 **다른 어떤 모델보다 많은 언어에서 정확**합니다.

공개된 다국어 벤치마크 **FLEURS**에서의 평가는 테스트한 모든 언어에서 일관되게 높은 정확도 기준을 유지함을 보여 줍니다. 여러 언어를 전사해야 하는 개발자는 **단일 모델**로 처리할 수 있어 복잡성이 줄고 GPU 사용 이슈도 줄일 수 있습니다.

---

## 최고의 가격에 최고의 성능

효율성이 높다는 것은 곧 비용 효율성으로 이어집니다. MAI-Transcribe-2의 속도와 처리량 덕분에 Microsoft는 **시장에서 가장 경쟁력 있는 가격**을 제시할 수 있었습니다.

> 출시 시점 가격은 **연말까지 한시적으로 시간당 0.10달러**입니다.

![가격·속도 비교](/mwkorea/assets/images/2026-09-04-MAITranscribe2SpeechRecognition/image2.webp)

---

## 지금 사용해 보기

MAI-Transcribe-2의 기능은 다음 세 곳에서 오늘부터 체험할 수 있습니다.

- **Microsoft Foundry**
- **MAI Playground**
- **Open Router**

![MAI Playground](/mwkorea/assets/images/2026-09-04-MAITranscribe2SpeechRecognition/image3.jpg)

---

## 한국 Copilot·에이전트 독자 관점에서 왜 중요한가

전사 모델은 눈에 잘 띄지 않지만 Copilot 생태계 전반의 **입력 품질을 좌우하는 기반 계층**입니다.

- **회의 요약·자막의 원천 품질**: Teams 회의 요약, 자막, 회의록 같은 기능은 결국 음성을 얼마나 정확히 텍스트로 옮기느냐에서 시작합니다. 전사 모델이 좋아지면 그 위에 얹히는 요약·분석 기능의 품질도 함께 좋아집니다.
- **화자 분리의 실무 가치**: 여러 사람이 참여하는 회의나 상담 녹음에서 누가 무슨 말을 했는지 구분하는 것은 회의록 작성, 상담 기록, 법률 문서화에서 핵심적인 요구 사항입니다.
- **한국어 지원 범위 확인 필요**: 60개 언어를 지원한다고 명시되어 있으나, 한국어가 포함되는지와 실제 정확도는 별도로 확인이 필요합니다. Microsoft Foundry나 Playground에서 직접 테스트해 보는 것을 권합니다.
- **verbatim/clean 스타일의 활용**: 컴플라이언스 대응이 필요한 콜센터·법무 영역에서는 verbatim 스타일이, 일반 회의록이나 자막 제작에는 clean 스타일이 적합합니다. 용도에 따라 구분해 사용할 수 있는 점이 실무적으로 유용합니다.
- **비용 절감 가능성**: 시간당 0.10달러라는 한시적 가격은 대량의 오디오를 처리해야 하는 조직에게 비용 구조를 재검토할 계기가 될 수 있습니다.

---

## 마무리

음성 인식 모델의 발전은 화려하게 드러나지 않지만, Copilot이 회의·통화·현장 녹음을 이해하는 능력의 기반이 됩니다. MAI-Transcribe-2는 속도·정확도·가격 세 축에서 동시에 개선을 보여 주며, 특히 화자 분리와 구성 가능한 전사 스타일은 실제 업무에 바로 적용할 만한 기능입니다.

Microsoft Foundry, MAI Playground, Open Router에서 직접 체험해 볼 수 있습니다.

---

> **출처**
>
> - 원문 제목: *MAI-Transcribe-2 is the fastest, most accurate and cheapest speech recognition model in the world*
> - 링크: [https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/)
>
> 자세한 내용은 원문을 참조하세요.
