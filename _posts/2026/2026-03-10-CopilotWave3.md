---
title: "Copilot Wave 3 상세 안내: Copilot Cowork, 멀티모델 인텔리전스, Agent 365"
date: 2026-03-10T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - Agent
excerpt: "2026년 3월 9일 Microsoft가 발표한 Copilot Wave 3는 Copilot Cowork, 앱 내 실행형 Copilot, 채팅 기반 에이전트, 멀티모델 인텔리전스, Agent 365, 그리고 Microsoft 365 E7까지 포함하며, AI를 업무 보조에서 실제 실행 단계로 확장합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
  actions:
    - label: "원문보기"
      url: "https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/powering-frontier-transformation-with-copilot-and-agents/"
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Wave 3 상세 안내: Copilot Cowork, 멀티모델 인텔리전스, Agent 365

Microsoft는 2026년 3월 9일, **Microsoft 365 Copilot Wave 3**를 발표했습니다. 이번 발표의 핵심은 분명합니다. Copilot이 이제 단순히 답변을 생성하는 도구를 넘어, **실제 업무를 계획하고 실행하며, 여러 앱과 데이터를 넘나들며 결과를 만들어내는 실행형 AI**로 진화하고 있다는 점입니다.

이번 Wave 3는 단일 기능 업데이트가 아니라, 다음과 같은 큰 축의 변화를 포함합니다.

- **Copilot Cowork**를 통한 장시간·다단계 업무 위임
- **Word, Excel, PowerPoint, Outlook 안에서 동작하는 실행형 Copilot**
- **Copilot Chat 중심의 에이전트 경험 확대**
- **Claude와 OpenAI 모델을 함께 활용하는 멀티모델 인텔리전스**
- **조직 차원의 에이전트 운영·보안·거버넌스를 위한 Agent 365**
- **생산성, AI, 보안을 통합한 Microsoft 365 E7 출시**

아래에서 이번 발표를 항목별로 자세히 정리해보겠습니다.

<figure style="margin: 1.4rem 0 1.8rem;">
  <img src="https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2026/03/Copilot_Excel_Agent_v2_1920.png" alt="Microsoft 365 Copilot Wave 3 대표 이미지" />
  <figcaption style="font-size: 0.92rem; color: #6b7280; margin-top: 0.55rem;">출처: Microsoft 365 Blog, Powering Frontier Transformation with Copilot and agents</figcaption>
</figure>

---

## 이번 발표를 한 문장으로 요약하면

**Wave 3는 Copilot을 "질문에 답하는 AI"에서 "일을 실제로 진행시키는 AI"로 전환하는 업데이트**입니다.

기존의 Copilot이 이메일 초안, 문서 요약, 회의 정리처럼 사용자의 생산성을 높이는 데 강점이 있었다면, 이번 Wave 3는 그 다음 단계인 **업무 실행(execution)** 에 초점을 둡니다. 사용자가 결과를 지시하면 Copilot이 필요한 자료를 찾고, 작업 계획을 세우고, 앱 안에서 산출물을 만들고, 필요 시 승인 지점을 제공하면서 실제 업무를 진행시키는 방식입니다.

Microsoft는 이를 위해 **Work IQ** 기반의 컨텍스트 이해와, **엔터프라이즈 보안 및 거버넌스**, 그리고 **멀티모델 전략**을 함께 전면에 내세웠습니다.

---

## 1. Copilot Cowork: 장시간 실행형 업무 위임의 시작

이번 발표에서 가장 상징적인 기능은 **Copilot Cowork**입니다. Microsoft는 Anthropic과의 협력을 통해 Claude Cowork를 구동하는 기술을 Microsoft 365 Copilot 안으로 가져왔고, 이를 기반으로 **장시간 실행되는 다단계 업무를 Copilot에 위임**할 수 있게 했습니다.

Copilot Cowork의 핵심은 다음과 같습니다.

- 사용자가 원하는 **결과 중심의 지시**를 내리면 Copilot이 작업을 단계별 계획으로 전환
- 이메일, 회의, 채팅, 파일, 조직 데이터 등 Microsoft 365 전반의 문맥을 활용해 업무를 진행
- 실행 과정에서 **진행 상태를 보여주고**, 사용자가 중간에 수정, 승인, 일시 중지 가능
- 단일 프롬프트 응답이 아니라 **몇 분 또는 몇 시간에 걸쳐 이어지는 업무 흐름** 지원

Microsoft가 소개한 대표 시나리오는 다음과 같습니다.

- **캘린더 정리**: 우선순위에 맞게 회의를 재조정하고 집중 시간을 확보
- **미팅 패킷 준비**: 브리핑 문서, 분석 자료, 발표 자료, 후속 메일까지 연결된 산출물 생성
- **기업 리서치**: 웹 자료와 업무 데이터를 기반으로 조사 메모, 요약, Excel 자료 정리
- **출시 계획 수립**: 경쟁 분석, 가치 제안서, 고객 발표 자료, 마일스톤 초안 작성

중요한 점은, Cowork가 완전히 블랙박스로 동작하는 것이 아니라는 점입니다. Microsoft는 **observable, transparent, controllable**한 실행 경험을 강조하고 있으며, 사용자는 필요한 시점에 개입할 수 있습니다.

현재 Copilot Cowork는 **일부 고객 대상 Research Preview**로 테스트 중이며, **2026년 3월 말부터 Frontier program을 통해 더 넓게 제공**될 예정입니다.

<figure style="margin: 1.4rem 0 1.8rem;">
  <video controls preload="metadata" poster="https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/3245650-Copilot-Cowork_tbmnl_en-us?wid=1280" style="width: 100%; border-radius: 18px; box-shadow: 0 14px 30px rgba(15, 23, 42, 0.12);">
    <source src="https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/3245650-Copilot-Cowork-0x1080-6439k" type="video/mp4" />
  </video>
  <figcaption style="font-size: 0.92rem; color: #6b7280; margin-top: 0.55rem;">공식 Copilot Cowork 소개 영상</figcaption>
</figure>

---

## 2. Word, Excel, PowerPoint, Outlook 안으로 들어온 실행형 Copilot

Wave 3의 두 번째 핵심 변화는 Copilot이 앱 바깥에서 초안을 던져주는 방식이 아니라, **Word, Excel, PowerPoint, Outlook 안에서 실제 작업물을 직접 다듬고 완성하는 방식**으로 진화했다는 점입니다.

Microsoft는 미리보기 단계에서 이 경험을 "Agent Mode"라고 불렀지만, 이제는 별도 모드가 아니라 **Copilot의 기본 동작 방식 자체가 바뀌고 있다**고 설명합니다.

앱별로 보면 다음과 같은 변화가 있습니다.

- **Word**: 기존 문서를 더 완성도 높은 초안으로 재구성하고, 조직 문맥을 반영해 수정
- **Excel**: 실제 수식과 구조를 반영한 스프레드시트 개선 및 분석 보조
- **PowerPoint**: 조직의 레이아웃, 오브젝트 스타일, 브랜드 키트까지 이해한 발표자료 작성
- **Outlook**: 메일 초안 생성뿐 아니라 실제 대화 흐름과 최근 문맥을 반영한 수정 및 정교화

<div style="margin: 1.4rem 0 1.8rem;">
  <iframe src="https://demos.microsoft.com/Microsoft/play/5875/march-moment-agent-apps#/0/0" title="Microsoft PowerPoint Agent demo" style="border: 0; width: 100%; min-height: 440px; border-radius: 18px; box-shadow: 0 14px 30px rgba(15, 23, 42, 0.12); background: #fff;" loading="lazy" sandbox="allow-same-origin allow-scripts allow-popups allow-forms"></iframe>
  <div style="font-size: 0.92rem; color: #6b7280; margin-top: 0.55rem;">출처: Microsoft 공식 데모, PowerPoint Agent 경험</div>
</div>

이 경험의 장점은 분명합니다.

- 작업이 **앱 안에서 그대로 이뤄지기 때문에 검토와 수정이 쉬움**
- 결과물이 로컬에 흩어지는 대신 **OneDrive와 SharePoint에 저장**되어 협업 및 통제 용이
- 기존의 **권한, 민감도 레이블, 보존 정책, 감사 정책**을 그대로 적용 가능

배포 현황은 다음과 같습니다.

- **Excel과 Word는 일반 공급(GA)**
- **PowerPoint와 Outlook은 향후 수개월 내 순차 롤아웃**

---

## 3. Copilot Chat이 업무 시작점이 된다: Agents in Chat

모든 일이 문서에서 시작되지는 않습니다. 실제 업무는 종종 "이거 정리해줘", "회의 하나 잡아줘", "이 내용을 발표자료로 만들어줘" 같은 대화형 요청에서 시작됩니다. Microsoft는 이 점을 반영해 **Copilot Chat을 채팅 기반 생성과 실행의 진입점**으로 확장하고 있습니다.

Wave 3에서 Copilot Chat은 다음 역할을 맡습니다.

- 대화에서 바로 **문서, 스프레드시트, 프레젠테이션 생성**
- 회의 일정 조율, 팀 메일 작성 등 **공통 업무 액션 수행**
- Word, Excel, PowerPoint, Outlook용 **내장 에이전트**와 연결
- Apps SDK, MCP Apps 같은 **개방형 표준 기반 앱과 에이전트 경험** 수용

이 구조는 Copilot을 단순 챗봇이 아니라 **업무 허브**로 바꿉니다. Microsoft는 Dynamics 365, Power Apps, Adobe, Monday.com, Figma 등 다양한 경험이 Copilot Chat 안으로 들어와 실제 작업 맥락에서 연결될 수 있다고 설명합니다.

또한 조직 내부에서는 다음 두 축으로 에이전트 확장이 가능해집니다.

- 현업 사용자는 **Agent Builder**로 일상 업무용 에이전트를 손쉽게 생성
- IT 및 비즈니스 리더는 **Copilot Studio**로 온보딩, 구매, 프로세스 자동화 등 더 복잡한 업무 프로세스 에이전트를 설계

현재 공개된 배포 정보는 다음과 같습니다.

- **Excel, Word, PowerPoint Agents는 Copilot Chat에서 GA로 롤아웃 중**
- **Schedule from chat**와 **custom instructions**는 현재 사용 가능
- **Send email from chat**은 올해 봄부터 광범위하게 롤아웃 예정

---

## 4. 멀티모델 인텔리전스: Claude와 OpenAI를 함께 활용하는 Copilot

Wave 3에서 Microsoft가 강하게 내세운 또 하나의 메시지는 **모델 선택의 유연성**입니다. 조직 입장에서 특정 단일 모델 공급자에 종속되는 것은 리스크가 될 수 있고, 사용자 입장에서는 어떤 모델을 써야 하는지 매번 고민하는 것 자체가 마찰이 됩니다.

Microsoft 365 Copilot은 이 문제를 **멀티모델 인텔리전스**로 해결하려고 합니다.

- Copilot이 작업에 맞는 모델을 **자동으로 선택**
- 사용자는 모델 이름보다 **업무 결과**에 집중 가능
- 최신 OpenAI 모델과 함께 **Claude가 mainline chat in Copilot에 Frontier program 형태로 제공**
- 모든 모델 사용은 **엔터프라이즈 컨텍스트, 보안, 거버넌스** 안에서 이루어짐

이 전략의 의미는 큽니다. 앞으로 Copilot은 "어떤 모델 기반이냐"보다, **업무 문맥을 얼마나 잘 이해하고 신뢰할 수 있게 실행하느냐**로 차별화하려는 방향이 더 강해질 것으로 보입니다.

---

## 5. Agent 365: 에이전트 시대를 위한 관리·보안·거버넌스 컨트롤 플레인

Copilot과 에이전트가 확산될수록 조직에는 새로운 과제가 생깁니다. "누가 어떤 에이전트를 만들었는가", "어떤 데이터에 접근하는가", "어떤 행동을 수행했는가", "규정 준수 상태는 어떤가" 같은 질문에 답할 수 있어야 합니다.

이를 위해 Microsoft는 **Agent 365**를 발표했습니다.

Agent 365는 에이전트를 위한 **컨트롤 플레인(control plane)** 으로, IT와 보안팀이 조직 전반의 에이전트를 한곳에서 관찰, 보호, 관리, 거버넌스할 수 있도록 설계됐습니다. Microsoft는 이를 기존 사용자 관리와 유사한 방식으로 운영할 수 있도록 하겠다고 설명합니다.

즉, 에이전트를 별도의 예외 시스템으로 다루는 것이 아니라 다음과 같은 기존 Microsoft 보안 체계와 연결하는 접근입니다.

- **Microsoft Admin Center** 기반 관리 경험
- **Microsoft Defender** 기반 보안 가시성
- **Microsoft Entra** 기반 신원 및 접근 통제
- **Microsoft Purview** 기반 거버넌스 및 규정 준수

Agent 365는 **2026년 5월 1일 GA**, 가격은 **사용자당 월 15달러**로 발표됐습니다.

<div style="margin: 1.4rem 0 1.8rem;">
  <iframe src="https://demos.microsoft.com/Microsoft/play/5890/agent-365#/0/0" title="Agent 365 demo" style="border: 0; width: 100%; min-height: 440px; border-radius: 18px; box-shadow: 0 14px 30px rgba(15, 23, 42, 0.12); background: #fff;" loading="lazy" sandbox="allow-same-origin allow-scripts allow-popups allow-forms"></iframe>
  <div style="font-size: 0.92rem; color: #6b7280; margin-top: 0.55rem;">출처: Microsoft 공식 데모, Agent 365 관리 경험</div>
</div>

---

## 6. Microsoft 365 E7: 생산성, AI, 보안을 하나로 묶은 Frontier Suite

이번 발표는 기능만이 아니라, 이를 기업이 어떻게 구매하고 운영할지까지 포함하고 있습니다. Microsoft는 **Microsoft 365 E7: The Frontier Suite**를 새롭게 소개했습니다.

Microsoft의 설명에 따르면 E7은 다음 요소를 하나의 묶음으로 제공합니다.

- **Microsoft 365 Copilot**
- **Agent 365**
- **Microsoft Entra Suite**
- **Microsoft 365 E5**와 고급 Defender, Entra, Intune, Purview 보안 기능

이 패키지는 단순 라이선스 번들이 아니라, **사용자 생산성 + 에이전트 운영 + 보안·거버넌스**를 하나의 운영 모델로 제시한다는 점에서 의미가 있습니다.

Microsoft 365 E7은 **2026년 5월 1일 구매 가능**, 가격은 **사용자당 월 99달러**로 안내됐습니다.

<figure style="margin: 1.4rem 0 1.8rem;">
  <img src="https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2026/03/202603-Horizon-Licensing_v6.jpg" alt="Microsoft 365 E7 Frontier Suite 구성 및 가격표" />
  <figcaption style="font-size: 0.92rem; color: #6b7280; margin-top: 0.55rem;">출처: Microsoft 365 Blog, Microsoft 365 E7: The Frontier Suite 구성표</figcaption>
</figure>

---

## 이번 발표에서 특히 주목해야 할 포인트

이번 Copilot Wave 3는 기능 수가 많아서 복잡해 보이지만, 실제로는 세 가지 변화로 정리할 수 있습니다.

### 1. Copilot이 "생성"에서 "실행"으로 이동한다

이제 Copilot은 문장을 잘 쓰는 도구를 넘어, **계획을 세우고 결과물을 끝까지 밀어붙이는 실행 파트너**로 발전하고 있습니다.

### 2. 업무 맥락이 훨씬 더 중요해진다

Wave 3 전반에는 **Work IQ**가 핵심 기반으로 깔려 있습니다. 파일 몇 개를 참고하는 수준이 아니라, 이메일, 회의, 채팅, 문서 관계, 조직 문맥까지 활용해 더 정확하고 실무적인 결과를 내는 방향입니다.

### 3. AI 확산의 핵심은 결국 신뢰다

Microsoft는 이번 발표에서 거의 모든 기능에 대해 **보안, 가시성, 승인, 감사, 정책 적용**을 함께 언급했습니다. 이는 앞으로 AI 도입의 성공 여부가 "모델 성능"만이 아니라, **조직이 안심하고 확산할 수 있는 운영 체계**에 달려 있음을 보여줍니다.

---

## 조직이 지금 준비하면 좋은 항목

Copilot Wave 3를 본격적으로 활용하려면, 기능 이해보다 먼저 **도입 우선순위와 운영 기준**을 정리하는 것이 좋습니다.

- **우선 시나리오 선정**: 회의 준비, 리서치, 일정 조정, 제안서 작성처럼 반복적이면서 문맥 의존도가 높은 업무부터 선정
- **데이터 거버넌스 점검**: SharePoint, OneDrive, Teams, Outlook의 권한 구조와 민감도 레이블 상태 확인
- **에이전트 운영 기준 수립**: 어떤 부서가 어떤 에이전트를 만들고 사용할 수 있는지 정책 정의
- **Frontier program 검토**: Cowork 및 멀티모델 경험을 조기에 검증하려면 참여 여부 확인
- **보안·관리 조직 협업**: Copilot 도입을 생산성 프로젝트가 아니라 보안·거버넌스 프로젝트와 함께 설계

특히 이번 발표는 현업 사용자만의 변화가 아니라, **IT 관리자, 보안팀, Copilot Center of Excellence, 업무 혁신 담당자**가 함께 준비해야 하는 단계로 넘어갔다는 신호로 보는 것이 맞습니다.

---

## 마무리

2026년 3월 9일 발표된 Copilot Wave 3는 Microsoft 365 Copilot이 본격적으로 **실행형 AI 플랫폼**으로 진입했음을 보여주는 업데이트입니다. Copilot Cowork는 장시간 업무 위임을 가능하게 하고, Word·Excel·PowerPoint·Outlook 안의 Copilot은 실제 산출물 제작 흐름을 바꾸며, Agents in Chat은 대화에서 바로 실행으로 이어지는 경험을 강화합니다. 여기에 멀티모델 전략, Agent 365, Microsoft 365 E7까지 더해지면서 Microsoft는 단순한 AI 기능 추가가 아니라 **조직 전체의 업무 운영 모델**을 새롭게 제시하고 있습니다.

앞으로 중요한 것은 "Copilot을 써볼까"가 아니라, **우리 조직의 어떤 업무를 Copilot과 에이전트에게 어떻게 위임하고, 어떤 통제 체계 안에서 확장할 것인가**가 될 것입니다.

---

## 참고 자료

- [Powering Frontier Transformation with Copilot and agents](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/powering-frontier-transformation-with-copilot-and-agents/)
- [Copilot Cowork: A new way of getting work done](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/)
- [Frontier program](https://adoption.microsoft.com/en-us/copilot/frontier-program/)
- [Microsoft Frontier Transformation digital event](http://aka.ms/MicrosoftFrontierTransformation2026)
