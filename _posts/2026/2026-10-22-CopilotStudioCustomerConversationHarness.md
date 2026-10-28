---
title: "Copilot Studio 고객 대화 harness 공개 프리뷰: 음성·채팅·사람을 하나의 흐름으로"
date: 2026-10-22T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - CustomerConversationHarness
  - ContactCenterIntelligence
  - Agent365
  - Omnichannel
  - PublicPreview
excerpt: "Microsoft가 Copilot Studio의 customer conversation harness를 공개 프리뷰로 발표했습니다. 전문 에이전트 협업, 생성형 스킬과 토픽의 결합, 음성·채팅의 맥락 유지와 상담원 연결을 지원하며, 일부 기능은 앞으로 순차 제공됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 고객 대화 harness 공개 프리뷰: 음성·채팅·사람을 하나의 흐름으로

고객은 웹 채팅에서 설명한 내용을 전화 상담에서 다시 반복하고 싶어 하지 않습니다. 기업 입장에서도 자연스럽게 대화하는 AI와 정확한 절차를 따르는 상담 시스템을 별개로 운영하면 연결 지점마다 맥락이 끊기기 쉽습니다.

Microsoft는 Copilot Studio에 **customer conversation harness**의 공개 프리뷰를 발표했습니다. 고객 접점 연결, 의도 이해, 지식과 도구 사용, 사람에게 넘기기와 문제 해결까지 대화 전반을 다루도록 설계된 실행 기반과 전용 빌더입니다.

원문 발행은 2026년 10월 21일이며, 피드 시각을 한국 시간으로 환산한 이 글의 날짜는 10월 22일입니다. **공개 프리뷰 발표와 모든 기능의 즉시 제공은 다릅니다.** 원문도 여러 기능은 지금 제공되지만 나머지는 향후 몇 주에 걸쳐 배포된다고 설명합니다.

![고객 대화 harness를 소개하는 원문 이미지](/mwkorea/assets/images/2026-10-22-CopilotStudioCustomerConversationHarness/image1.png)

---

## 하나의 에이전트에서 음성과 채팅을 함께 설계합니다

새 conversational agent builder는 음성과 채팅 경험을 하나의 에이전트에서 구성하도록 지원합니다. 원문은 에이전트가 기본적으로 옴니채널을 지원하고, 여러 언어를 이해하며, 채널을 인지한다고 설명합니다.

디지털 채널과 음성 채널 사이를 이동할 때 맥락과 메모리를 유지하는 것이 핵심입니다. 다만 지원 언어 목록이나 한국어 음성의 세부 제공 범위는 이 발표에서 명시하지 않으므로 별도 확인이 필요합니다.

## 전문 에이전트 팀과 외부 코드 자산을 연결합니다

각 하위 에이전트는 담당 업무에 맞는 자체 지식과 도구를 가질 수 있습니다. 깊은 추론이 필요한 업무와 지연·비용에 민감한 업무를 분담하는 식입니다.

![전문 에이전트 협업을 설명하는 원문 이미지](/mwkorea/assets/images/2026-10-22-CopilotStudioCustomerConversationHarness/image2.png)

중요한 구분은 **에이전트마다 별도 모델을 선택하는 기능은 GA 시점의 계획**이라는 점입니다. 공개 프리뷰 발표에 등장했다고 이미 모두 이용할 수 있다고 해석하면 안 됩니다.

Microsoft Foundry에서 코드로 만든 사용자 지정 에이전트를 팀에 추가하는 확장성도 소개됩니다. 기존 pro-code 자산을 버리지 않고 대화형 고객 응대 흐름에 결합하는 접근입니다.

![Foundry 확장을 설명하는 원문 화면](/mwkorea/assets/images/2026-10-22-CopilotStudioCustomerConversationHarness/image3.png)

## Work IQ·Foundry IQ·Fabric IQ로 업무 맥락을 확보합니다

원문은 Microsoft IQ가 harness에 통합되어 각 에이전트에서 활용된다고 설명합니다.

| 연결 대상 | 발표에서 설명한 활용 |
|---|---|
| Work IQ | SharePoint의 환불 정책과 Teams에서 합의한 예외 등 Microsoft 365 업무 맥락 |
| Foundry IQ | 제품 설명서·보증 조건과 Azure AI Search로 인덱싱한 대규모 지식 |
| Fabric IQ | 비즈니스 데이터에 대한 추론 |

특히 Work IQ 접근은 에이전트 **자신의 identity**를 사용하고 기존 기업 데이터 접근·보안 정책을 존중한다고 명시합니다. 고객과 대화하는 에이전트가 임의로 모든 직원 데이터에 접근한다는 뜻이 아닙니다.

외부 고객에게 답하는 시나리오에서는 내부 문서의 권한뿐 아니라 답변에 포함해도 되는 정보 범위를 검토하는 것이 좋습니다. 이는 도입상 권고이며 발표가 특정 데이터 유출 방지 구성을 자동 보장한다는 의미는 아닙니다.

## 생성형 스킬과 결정적 토픽을 같은 에이전트에 섞습니다

상담 업무에는 유연성이 필요한 부분과 순서를 바꿀 수 없는 부분이 공존합니다. 새 harness에서는 스킬마다 프롬프트 중심의 생성형 동작 또는 정해진 단계의 **topic**을 사용하도록 구성할 수 있습니다.

예를 들어 안내 대화는 생성형으로, 정확한 단계가 필요한 절차는 토픽으로 구성하는 방식입니다. 원문은 카드 추천, 잔액 조회와 결제 같은 업무를 예로 들지만, 구체적인 금융 시스템 연결이나 규제 준수 절차까지 제공하는 설명은 아닙니다.

![생성형 스킬과 토픽 결합을 설명하는 원문 화면](/mwkorea/assets/images/2026-10-22-CopilotStudioCustomerConversationHarness/image4.png)

## 음성 설정과 전화 배포, 그리고 음성 생체인증

음성은 부가 채널이 아니라 기본 경험으로 다뤄집니다. 음성 모델 선택, voice fonts, 말투와 발화 스타일을 지정하는 speech instructions, **DTMF 동작**, 음성 민감도 등을 구성할 수 있다고 안내합니다.

빌더 안에서 테스트와 평가를 수행하고, 전화번호를 확보해 에이전트를 배포하는 흐름도 소개합니다. 전화번호 제공 국가, 지역별 제약과 비용은 이 글에서 확인되지 않았으므로 한국 번호를 바로 발급받을 수 있다고 단정하지 않습니다.

![음성 기능 설정을 보여주는 원문 GIF](/mwkorea/assets/images/2026-10-22-CopilotStudioCustomerConversationHarness/image5.gif)

Contact Center Intelligence와 함께 제공하는 **voice biometrics**는 고객이 용건을 말하는 동안 고유한 voiceprint로 신원을 검증하도록 지원합니다. 조직이 요구하는 정확도 수준에 맞추는 구조로 설명되며, 통화가 끊긴 뒤 다시 걸었을 때 대화를 이어가는 경험도 제시합니다.

생체인증 정확도 수치, 오인식률이나 구체적인 데이터 보존 기간은 발표에 없습니다. 한국 도입에서는 음성 생체정보 처리의 동의·보존·대체 인증 수단을 별도로 검토해야 합니다.

## Teams 직원과 기존 컨택센터로 넘깁니다

기본 제공되는 사람 연결 기능으로 수신 전화를 **Teams queue**에 에스컬레이션할 수 있습니다. 반면 **Teams chat으로 직접 연결하는 기능은 곧 제공할 예정**이라고 원문은 구분합니다.

![Teams를 통한 직원 연결 관련 원문 화면](/mwkorea/assets/images/2026-10-22-CopilotStudioCustomerConversationHarness/image6.png)

더 완전한 컨택센터가 필요하면 새 [Microsoft Contact Center Intelligence](https://ccai.microsoft.com/about)와 연계할 수 있습니다. 기존 전화 인프라·라우팅·대기열을 유지하면서 IVR와 챗봇 현대화, 상담원 협업, 고급 생체인증, 통화 채점과 인사이트를 연결하는 방향입니다.

![Contact Center Intelligence 연결을 설명하는 원문 이미지](/mwkorea/assets/images/2026-10-22-CopilotStudioCustomerConversationHarness/image7.webp)

## Agent 365 거버넌스와 사용량 기반 과금

원문은 이 harness로 만든 에이전트가 생성 시점부터 **Agent 365**에 나타나며, 관리자가 소유자·채널·Entra agent ID·지식·도구·권한·사용량 등을 확인할 수 있다고 설명합니다.

![고객 대화 에이전트의 관리 관련 원문 화면](/mwkorea/assets/images/2026-10-22-CopilotStudioCustomerConversationHarness/image8.png)

과금은 Copilot Studio의 다른 영역과 마찬가지로 **Copilot Credits 기반 사용량 과금**을 사용합니다. 발표에는 통화당 가격이나 음성 생체인증을 포함한 전체 비용표가 없으므로 무료 기능으로 소개해서는 안 됩니다.

## 시작하기와 도입 체크포인트

시작 경로는 Copilot Studio의 **“more ways to build”**입니다. 원문은 [customer conversation harness 설명](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview-customer-conversation?branch=pr-en-us-2486)과 [Contact Center Intelligence 발표](https://aka.ms/CCI_Blog)를 추가 자료로 제공합니다. 문서 링크는 원문에 실린 그대로이며, 실제 사용 전 현재 문서와 테넌트 가용성을 확인해야 합니다.

도입 시에는 좁은 고객 응대 시나리오를 정하고, 생성형·토픽 처리 경계, 에이전트별 지식과 권한, 사람에게 넘기는 조건, 전화·생체정보 처리, 크레딧 예산을 함께 점검하는 접근을 권합니다. 이는 운영 준비를 위한 제안입니다.

## 마무리

이번 발표의 중심은 음성 봇 하나를 추가하는 것이 아닙니다. **여러 에이전트, 기업 지식, 정해진 절차와 사람 상담원을 하나의 고객 대화 흐름으로 묶는 것**입니다. 프리뷰에서 실제 제공되는 범위와 GA 계획을 구분하면서 업무별로 검증하는 것이 중요합니다.

> **출처**: [Introducing the customer conversation harness in Microsoft Copilot Studio](https://techcommunity.microsoft.com/t5/copilot-studio-blog/introducing-the-customer-conversation-harness-in-microsoft/ba-p/4563954). 자세한 내용은 원문 참조.
