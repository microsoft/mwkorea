---
title: "Copilot을 개인 도우미에서 조직의 에이전트로: 17개 모듈·11개 실습으로 배우는 부트캠프"
date: 2026-11-21T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotStudio
  - CopilotChat
  - CopilotCowork
  - CopilotCode
  - WorkIQ
  - Agent
  - Training
  - Governance
  - FinOps
excerpt: "Microsoft CAT가 Copilot Chat부터 Cowork, Copilot Studio 에이전트 운영까지 연결하는 부트캠프 자료를 공개했습니다. 17개 모듈과 11개 실습을 통해 개인 업무 지원을 반복 가능한 작업과 조직 공통 서비스로 발전시키는 방법을 살펴봅니다. 사내 교육을 준비할 때 확인할 환경·라이선스·거버넌스 체크포인트도 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot을 개인 도우미에서 조직의 에이전트로: 17개 모듈·11개 실습으로 배우는 부트캠프

Copilot을 도입한 조직에서 자주 만나는 다음 질문은 “누가 잘 쓰고 있는가”보다 **“잘 쓰는 방법을 어떻게 조직 전체의 역량으로 만들 것인가”**입니다. 개인이 만든 프롬프트, 반복 업무용 스킬, 부서가 함께 사용하는 에이전트는 서로 연결되어 있지만 필요한 관리 수준은 다릅니다.

Microsoft의 The Custom Engine 블로그는 2026년 11월 21일, 이 과정을 학습할 수 있는 **Copilot & Agents Bootcamp**를 소개했습니다. CAT와 CAPE 팀이 11월 10~12일 애틀랜타에서 진행한 3일 과정으로, **17개 모듈과 11개 실습의 자료가 온라인에 공개**되어 있습니다. 현장 참석 없이 자기주도 학습이나 사내 교육에 활용할 수 있다는 점이 핵심입니다.

이 글은 공개된 교육의 구성과 실습 사례를 한국의 도입 담당자·메이커·개발자 관점에서 정리합니다. 개별 기능의 GA 발표가 아니라 교육 자료 소개이므로, 실제 실습 전에 각 기능의 제공 상태와 테넌트 조건을 별도로 확인해야 합니다.

![Copilot & Agents Bootcamp 소개 이미지](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image1.png)

---

## 이름이 바뀐 이유: Copilot Studio만 알아서는 부족합니다

이 과정의 이전 이름은 **Copilot Studio Architecture Bootcamp**였습니다. 새로운 이름은 Copilot Studio의 중요성이 줄었다는 뜻이 아니라, 에이전트를 설계하기 전에 사용자의 출발점까지 이해해야 한다는 의미입니다.

사용자는 Copilot Chat에서 질문하고, Cowork에서 여러 단계의 업무를 수행하며, Copilot Code로 간단한 앱을 만들 수도 있습니다. 따라서 아키텍트는 “무엇이든 에이전트로 만들자”가 아니라 **어떤 작업을 어느 경험에 배치할지** 판단해야 합니다.

개편된 교육은 다음 범위까지 다룹니다.

- **Copilot Chat와 Work IQ**: 웹·업무 맥락을 활용한 그라운딩, 응답 모드, Researcher와 Analyst.
- **Copilot Cowork**: 여러 단계의 작업을 위한 스킬·플러그인·코드.
- **Copilot Code**: 간단한 웹 앱의 생성과 게시.
- **에이전트 harness**: Microsoft Copilot harness, Copilot Chat harness의 선언형 에이전트, Standard harness, Customer Conversation harness, Microsoft Copilot Managed Runtime의 앱.
- **운영과 거버넌스**: 크레딧 소비 계획, 에이전트 ID, ALM, 평가, Copilot Agent Kit.

원문에서 Microsoft Copilot harness는 이전에 GitHub Copilot 또는 GHCP harness로 불렸다고 설명합니다. 여기서 harness는 모델이 지시·도구·상태를 활용해 작업을 수행하도록 연결하는 실행 틀로 이해하면 됩니다. 교육에 등장하는 이름과 기능 범위는 **원문 시점의 표현**입니다.

## 세 단계로 구분하면 도구 선택이 쉬워집니다

부트캠프의 중심은 **Assisted → Repeatable → Production-ready**라는 흐름입니다. 모든 업무가 반드시 마지막 단계로 가야 한다는 뜻은 아닙니다. 재사용 범위와 운영 요구에 맞는 단계에 배치하는 것이 중요합니다.

| 단계 | 대표 경험 | 적합한 업무와 다음 단계로 이동하는 신호 |
|---|---|---|
| Assisted: 개인 업무 지원 | Copilot Chat | 업무 자료를 바탕으로 요약·답변을 얻습니다. 같은 질문과 절차를 매번 다시 구성한다면 반복 업무로 묶을 여지가 있습니다. |
| Repeatable: 반복 가능한 업무 | Copilot Cowork | 계정 브리핑이나 영업 후속 조치처럼 여러 단계의 절차를 스킬·플러그인으로 묶습니다. 팀 공통 품질과 중앙 관리가 필요해지면 에이전트를 검토합니다. |
| Production-ready: 조직 공통 운영 | Copilot Studio | 팀이 함께 쓰는 결과물을 버전 관리하고 평가·모니터링·거버넌스를 적용합니다. 지시, 스킬, 지식, 도구, 훅, 워크플로를 하나의 운영 대상에 연결합니다. |

![Copilot Chat 요약, Cowork 결과물, Copilot Studio 스킬 활용으로 이어지는 세 단계](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image2.png)

예를 들어 개인의 분기 실적 요약은 Chat로 충분할 수 있습니다. 매주 같은 형식의 영업 브리핑을 만든다면 Cowork 스킬이 적합할 수 있고, 여러 부서가 같은 정책과 품질 기준을 적용해야 한다면 Copilot Studio 에이전트로 관리하는 방안을 검토할 수 있습니다. 이는 원문의 단계 구분을 업무에 적용한 예시이지, 특정 도구가 모든 상황의 정답이라는 의미는 아닙니다.

## 1일 차: 업무 맥락과 도구 선택부터 시작하기

첫날은 실습 환경·테넌트 준비 안내에 이어 Copilot 생태계와 기본 실행 틀을 익힙니다. 난도는 원문의 분류대로 **100은 입문, 300은 고급**이며, 모듈 페이지에서 슬라이드를 확인할 수 있습니다.

| 모듈·실습 | 학습 내용 | 수준 |
|---|---|---|
| [모듈 1](https://microsoft.github.io/mcs-labs/modules/agents-workflows-making-them-real-latest/?event=architecture-bootcamp) | Microsoft Copilot 에이전트 생태계 | 100 |
| [모듈 2](https://microsoft.github.io/mcs-labs/modules/m365-copilot-latest/?event=architecture-bootcamp) · [실습 1](https://microsoft.github.io/mcs-labs/labs/copilot-chat-workiq/?event=architecture-bootcamp) | Copilot Chat와 Work IQ를 활용한 업무 요약 | 100 |
| [모듈 3](https://microsoft.github.io/mcs-labs/modules/cowork-latest/?event=architecture-bootcamp) · [실습 2](https://microsoft.github.io/mcs-labs/labs/cowork-zava-sales/?event=architecture-bootcamp) | Cowork 스킬·플러그인·코드, 영업 인사이트를 실행으로 연결 | 100~200 |
| [실습 3](https://microsoft.github.io/mcs-labs/labs/copilot-code-web-app/?event=architecture-bootcamp) | Copilot Code로 간단한 웹 앱 생성·게시 | 100 |
| [모듈 4](https://microsoft.github.io/mcs-labs/modules/copilot-harness-latest/?event=architecture-bootcamp) · [실습 4](https://microsoft.github.io/mcs-labs/labs/declarative-agent-skill-reuse/?event=architecture-bootcamp) | Copilot Chat harness의 선언형 에이전트에 Cowork 스킬 재사용 | 200 |
| [모듈 5](https://microsoft.github.io/mcs-labs/modules/standard-harness/?event=architecture-bootcamp) · [실습 5](https://microsoft.github.io/mcs-labs/labs/standard-harness-components/?event=architecture-bootcamp) | Standard harness와 구성 요소 모델 | 200 |

### 실습 1·2: 답변을 얻는 것과 일을 끝내는 것은 다릅니다

실습 1은 업로드한 보고서와 회사 정책에 근거한 업무 요약을 만듭니다. 화면에는 분기 비즈니스 검토를 위한 사전 읽기 자료와 인용이 나타납니다. 사내 교육에서는 결과의 문장 품질만 볼 것이 아니라, **어떤 자료를 근거로 삼았는지** 함께 검토하는 출발점으로 활용할 수 있습니다.

![실습 1: 근거 인용을 포함한 Copilot Chat의 분기 비즈니스 검토 요약](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image3.webp)

실습 2는 같은 영업 업무에 Copilot Chat, 영업 에이전트, Cowork를 비교해 사용합니다. 팀별 스킬을 묶은 Cowork 플러그인도 경험합니다. 질문 응답, 특정 업무 에이전트, 반복 절차 실행의 차이를 직접 확인하는 구성입니다.

![실습 2: 영업 업무 스킬을 묶은 Zava Sales Cowork 플러그인](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image4.webp)

### 실습 3·4: 개인의 결과물을 재사용 가능한 자산으로 바꾸기

실습 3은 Copilot Code로 부트캠프 실습 진행 상황을 추적하는 웹 앱을 만들고 게시한 뒤, 후속 프롬프트로 개선합니다. 코드 생성 시연에서 끝나지 않고 실제 사용 가능한 결과물로 이어지는 실습입니다.

![실습 3: Copilot Code로 만든 부트캠프 실습 진행 추적 웹 앱](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image7.webp)

실습 4는 Cowork에서 사용한 스킬을 선언형 에이전트에 업로드합니다. 원문의 예시는 호텔 운영 브리핑 스킬 ZIP 파일입니다. **반복 가능한 개인 작업을 공유 가능한 에이전트로 옮기는 연결 지점**을 보여줍니다.

![실습 4: Agent Builder에 Cowork 스킬 ZIP 파일 업로드](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image5.webp)

## 2일 차: 지식·도구·훅으로 에이전트의 행동 구성하기

둘째 날은 에이전트를 구성하는 요소와 실행 틀별 선택 기준을 깊게 다룹니다.

| 모듈·실습 | 학습 내용 | 수준 |
|---|---|---|
| [모듈 6](https://microsoft.github.io/mcs-labs/modules/harnesses-and-component-models-latest/?event=architecture-bootcamp) | Harness, 오케스트레이션, 구성 요소 모델 | 200 |
| [모듈 7](https://microsoft.github.io/mcs-labs/modules/instructions-and-skills/?event=architecture-bootcamp) · [실습 6](https://microsoft.github.io/mcs-labs/labs/instructions-skills-authoring/?event=architecture-bootcamp) | 지시와 스킬의 설계·작성 | 300 |
| [모듈 8](https://microsoft.github.io/mcs-labs/modules/knowledge-and-tools-deep-dive/?event=architecture-bootcamp) · [실습 7](https://microsoft.github.io/mcs-labs/labs/hooks-knowledge-travel-policy/?event=architecture-bootcamp) | 지식·도구·훅을 활용한 출장 정책 에이전트 | 200~300 |
| [모듈 9](https://microsoft.github.io/mcs-labs/modules/customer-conversation-harness/?event=architecture-bootcamp) · [실습 8](https://microsoft.github.io/mcs-labs/labs/customer-assist-agent/?event=architecture-bootcamp) | Customer Conversation harness | 200 |
| [모듈 10](https://microsoft.github.io/mcs-labs/modules/managed-apps/?event=architecture-bootcamp) · [실습 9](https://microsoft.github.io/mcs-labs/labs/managed-apps-build/?event=architecture-bootcamp) | Microsoft Copilot Managed Runtime의 앱 | 200 |

### 실습 6: 지시와 스킬을 함께 사용한 RFP 대응

실습 6에서는 Microsoft Copilot harness 에이전트가 제안 요청서, 즉 RFP에 응답하도록 만듭니다. 원문의 활동 추적 화면은 요청과 맞는 `rfp-response` 스킬을 불러오는 과정을 보여줍니다. 결과뿐 아니라 **필요한 스킬이 선택되었는지** 관찰할 수 있다는 점이 교육 포인트입니다.

![실습 6: RFP 요청에 맞는 스킬을 불러오는 에이전트 활동 추적](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image6.webp)

스킬 개념이 낯설다면 CAT의 [Agents Have Skills Now](https://microsoft.github.io/mcscatblog/posts/modern-mcs-agent-skills/)를 먼저 읽는 것이 원문의 권장 순서입니다.

### 실습 7: 답변과 도구 실행에 정책을 연결하기

출장 정책 실습은 세션 시작 훅으로 사용자 위치에 맞는 답변을 구성합니다. 선택 확장에서는 도구 실행 전 훅으로 예약 대상 항공사가 승인된 항공사인지 점검합니다. 화면의 예약은 **시뮬레이션 사례**이므로 실제 항공권 예약 기능이 모든 환경에서 제공된다는 의미로 해석하면 안 됩니다.

![실습 7: 출장 정책 인용과 예약 도구 실행 전 훅의 동작](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image8.webp)

도입 담당자에게 중요한 질문은 “정책 문서를 검색할 수 있는가”에서 한 걸음 더 나아갑니다. **정책에 어긋나는 도구 호출을 어디에서 검사할 것인가**까지 설계해야 합니다. 추가 배경은 [Hooks in Copilot Studio](https://microsoft.github.io/mcscatblog/posts/hooks-in-copilot-studio/)에서 확인할 수 있습니다.

### 실습 8·9: 고객 대화와 관리형 앱으로 범위 확장하기

실습 8은 주 에이전트가 특정 요청을 전문 하위 에이전트로 넘기는 고객 대응 사례입니다. 원문은 채팅과 음성 양쪽에서 테스트할 수 있다고 설명하며, 화면은 구독 취소 요청을 전문 에이전트에 라우팅하는 구성을 보여줍니다.

![실습 8: 구독 취소 요청을 전문 하위 에이전트로 연결하는 고객 대화 구성](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image9.webp)

실습 9는 Microsoft Copilot Managed Runtime에서 앱을 만드는 주제입니다. 대화형 에이전트와 앱을 구분하고, 요구하는 사용자 경험에 맞는 실행 방식을 검토하는 과정으로 볼 수 있습니다.

## 3일 차: 만들기에서 운영하기로

마지막 날은 워크플로 자동화, 에이전트 간 통합, 품질·비용·ID 관리로 이어집니다.

| 모듈·실습 | 학습 내용 | 수준 |
|---|---|---|
| [모듈 11](https://microsoft.github.io/mcs-labs/modules/workflows-latest/?event=architecture-bootcamp) · [실습 10](https://microsoft.github.io/mcs-labs/labs/workflows-autonomous/?event=architecture-bootcamp) | 워크플로 | 300 |
| [모듈 12](https://microsoft.github.io/mcs-labs/modules/agent-integration/?event=architecture-bootcamp) · [실습 11](https://microsoft.github.io/mcs-labs/labs/agent-integration-team/?event=architecture-bootcamp) | A2A를 포함한 에이전트 통합 | 200 |
| [모듈 13](https://microsoft.github.io/mcs-labs/modules/alm-and-analytics/?event=architecture-bootcamp) | ALM, 분석, 평가 | 300 |
| [모듈 14](https://microsoft.github.io/mcs-labs/modules/coding-agents/?event=architecture-bootcamp) | 코딩 에이전트의 플러그인·마이그레이션·생성 | 300 |
| [모듈 15](https://microsoft.github.io/mcs-labs/modules/ai-finops/?event=architecture-bootcamp) | AI FinOps | 200 |
| [모듈 16](https://microsoft.github.io/mcs-labs/modules/agent-identity/?event=architecture-bootcamp) | 에이전트 ID | 200 |
| [모듈 17](https://microsoft.github.io/mcs-labs/modules/copilot-agent-kit/?event=architecture-bootcamp) | Copilot Agent Kit | 200 |

### 실습 10: 자동 작성과 자동 발송 사이에 사람의 검토 넣기

워크플로는 들어온 메일을 분류하고 답장 초안을 만든 뒤, **발송 전에 사람이 검토할 때까지 기다립니다**. 자동화 여부를 단순히 켜고 끄는 대신 업무의 위험도에 맞는 검토 지점을 배치하는 예입니다.

![실습 10: Copilot 처리, 사람의 검토, 조건 분기를 거쳐 답장하는 워크플로](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image10.webp)

### 실습 11: 전문 에이전트에 무엇을 위임했는지 확인하기

운영 에이전트를 전문 에이전트와 연결하고, 실제 위임된 작업을 추적합니다. 화면에서는 Zava Operations Assistant가 재고 관련 요청을 Zava Stock & Policy Specialist에 전달합니다.

![실습 11: 재고·정책 전문 에이전트로 넘긴 작업의 활동 추적](/mwkorea/assets/images/2026-11-21-CopilotAgentsBootcamp/image11.webp)

통합 배경은 [MCP와 A2A를 통한 Microsoft Copilot harness 에이전트 호출](https://microsoft.github.io/mcscatblog/posts/call-ghcp-harness-agents-mcp-a2a/)에서, 평가 배경은 [Model Assessment를 활용한 에이전트 평가](https://microsoft.github.io/mcscatblog/posts/model-assessment/)에서 확인할 수 있습니다.

## 사내 교육을 시작하기 전 확인할 사항

온라인 자료 공개와 실습 환경의 무료 제공은 다른 이야기입니다. 원문은 **각 실습에 전제조건이 기재되어 있다**고 안내하며, 모든 실습에 동일한 라이선스나 권한이 적용된다고 설명하지 않습니다.

1. **테넌트·라이선스·환경을 먼저 준비합니다.** [부트캠프 페이지](https://microsoft.github.io/mcs-labs/events/architecture-bootcamp/)에서 각 실습의 전제조건을 읽고 참여자의 접근 가능 여부를 확인합니다. 구체적인 라이선스 SKU나 관리자 권한을 이 소개 글만으로 단정하지 않습니다.
2. **교육 자료의 최신 업데이트 날짜를 확인합니다.** 원문은 PPCC, Microsoft Ignite, Microsoft Build 등 주요 행사 이후 자료를 자주 갱신한다고 설명합니다. 교육 직전에 공개 슬라이드를 다시 내려받고 현재 UI와 실습 절차가 맞는지 점검합니다.
3. **기능별 프리뷰·GA와 제공 범위를 구분합니다.** 교육 과정에 포함되었다는 사실만으로 전 세계 모든 테넌트에 GA되었다고 판단하지 않습니다. 필요한 기능의 현재 제공 상태는 해당 실습과 공식 제품 문서에서 확인합니다.
4. **질의응답과 운영 논의를 따로 확보합니다.** 공개 일정에는 권장 Q&A 구간이 있습니다. 한국 조직에서 적용할 때는 데이터 접근, 외부 작업 실행, 사람의 검토, 비용 관리가 실제 정책과 맞는지 토론하는 시간으로 활용할 수 있습니다.
5. **절차가 맞지 않으면 이슈를 등록합니다.** 자료와 화면이 다를 경우 [mcs-labs GitHub 이슈](https://github.com/microsoft/mcs-labs/issues)로 보고하는 것이 원문의 권장 방법입니다.

교육을 운영한다면 Chat의 인용 검토, Cowork 스킬 재사용, 에이전트의 실행 추적을 같은 업무 시나리오로 연결해 보는 방식도 유용합니다. 이는 이 글의 교육 구성 제안이며, 부트캠프가 특정 기업의 보안·준법 검토를 대신한다는 뜻은 아닙니다.

## CAT의 지원을 받는 방법

원문에서 CAT는 **Copilot Acceleration Team**으로 소개되며, Microsoft Copilot 엔지니어링 조직에서 Microsoft 365 Copilot과 Copilot Studio의 도입·성공을 지원합니다. 고객 경험을 바탕으로 도구, 프로그램, 아키텍처 가이드를 제공하는 역할입니다.

관련 자료로는 [Copilot Agent Kit](https://aka.ms/copilotagentkit), [Skills for Copilot Studio](https://github.com/microsoft/skills-for-copilot-studio), [Agent Skills & Plugins Gallery](https://aka.ms/catagentskills), [Agent In A Day](https://aka.ms/agiad), [Microsoft Copilot Agents Labs](https://microsoft.github.io/mcs-labs/), [Power Platform Architecture Center](https://aka.ms/powerarchitecture), [Copilot Studio guidance](https://aka.ms/copilotstudioguidance), [Copilot Studio Samples](https://microsoft.github.io/CopilotStudioSamples/)가 있습니다.

CAT는 기존 Microsoft 계정 담당 팀을 대체하지 않습니다. 계정 팀을 기본 창구로 두고 아키텍처·설계 검토, 도입 교육, 제품 피드백 연결 등을 보완합니다. 프로젝트 지원이 필요하면 계정 팀과 논의하거나 [CAT 지원 요청](https://aka.ms/GetCAT)을 이용할 수 있습니다. 요청에는 업무 시나리오, 현재 단계, 막힌 지점을 설명하는 것이 원문의 안내입니다. 지원 요청이 모든 조직의 현장 부트캠프 제공을 보장하는 것은 아닙니다.

## 마무리: 도구보다 업무의 다음 단계를 정해 보세요

이 부트캠프의 가치는 기능 목록을 한 번에 배우는 데만 있지 않습니다. **개인에게 유용한 답변을 반복 가능한 절차로 만들고, 필요한 경우 조직이 책임지고 운영하는 에이전트로 발전시키는 판단 기준**을 제공합니다.

처음부터 3일 전체 과정을 운영하기 어렵다면, 공개된 자료에서 현재 조직의 단계에 맞는 실습을 선택할 수 있습니다. 다만 결과물을 만드는 실습과 평가·비용·ID·ALM을 다루는 운영 모듈을 분리해서 생각하지 않는 것이 중요합니다.

> 출처: [Inside the Copilot & Agents Bootcamp: Every Session and Lab, Ready for You to Run](https://microsoft.github.io/mcscatblog/posts/copilot-agents-bootcamp/) — MCSCAT Blog, The Custom Engine, 2026년 11월 21일. 자세한 내용은 원문 참조.
