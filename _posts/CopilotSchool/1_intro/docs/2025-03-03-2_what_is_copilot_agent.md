---
title: "Copilot 에이전트란 뭘까?"
date: 2025-03-03T00:00:00 KST
categories:
  - AgentSchool
tags:
  - AI
  - Agent
  - Copilot
excerpt: "오늘은 Copilot 에이전트란 무엇인지 같이 알아보아요!"
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  #actions:
  #  - label: "원문보기"
  #    url: "https://www.microsoft.com/en-us/microsoft-365/blog/2025/02/10/discover-the-total-economic-impact-of-microsoft-365-e3/?msockid=20f4fd7af5a86c603f7ae8f6f4df6ddb"
toc: false
toc_sticky: true
classes: wide
author: 조항우
---

안녕하세요, MW Technical Specialist 인턴 조항우입니다😊  
오늘은 Copilot 에이전트란 무엇인지 같이 알아보아요!  
<br/>
# 🚀 Copilot 에이전트란 뭘까?  

### **학습 목표:**  
Copilot이 뭔지 저번시간에 같이 공부해 보았는데요, **이번에는 AI 에이전트가 무엇인지 이해하고, 마이크로소프트의 Copilot 에이전트의 종류와 각 특징을 같이 공부**해봐요.  



## 🎯 다음 내용을 공부해봐요!  
✔️ AI 에이전트의 개념과 역할을 쉽게 이해할 수 있어요.  
✔️ Copilot 에이전트의 2가지 종류와 차이점을 명확히 구분할 수 있어요.  
✔️ Copilot 에이전트를 만드는 3가지 방식을 이해하고 자신에게 맞는 개발방식이 무엇인지 판단할 수 있어요   

---
</br>


## 🤖 AI 에이전트란?  
AI 에이전트는 **AI가 스스로 환경을 인식하고, 의사결정을 내리며, 특정 목표를 수행하는 시스템**을 의미해요.  
즉, **인간의 개입 없이도 자율적으로 행동하는 지능형 시스템**을 AI 에이전트라고 합니다.  

가장 단순한 형태의 AI 에이전트로는 한국 남성들이라면 군대에서 많이 봤을 법한, **스마트 스피커(예: KT 기가지니, Google Home, Siri)** 가 있어요.  
예를 들어, "불 꺼줘"라고 말하면:

1️⃣ **사용자의 요청을 듣고 이해** → "불을 꺼줘"라는 명령을 인식  
2️⃣ **의미를 해석하고 행동 결정** → 조명을 끄는 것이 목표임을 판단  
3️⃣ **실제 동작 실행** → 스마트홈과 연동해 조명을 끔  

하지만 AI 에이전트 기술은 이제 단순한 음성 비서에서 한 단계 더 발전하고 있어요.  
오늘날의 AI 에이전트는 단순한 명령 수행을 넘어서, NLP 그리고 컴퓨터 비전기술을 활용해 **사용자의 요구를 예측하고, 복잡한 업무를 자동화하는 수준**까지 발전하고 있습니다.  

---

## 🛠️ Copilot 에이전트란?  
Copilot 에이전트는 마이크로소프트의 **Copilot을 기반으로 동작하는 AI 에이전트**예요.  

일반적인 Copilot은 LLM(대형 언어 모델)을 활용해 **문서를 요약하거나, 질문에 답변을 제공**하는 기능을 수행하지만,  

Copilot 에이전트는 여기에서 더 나아가 **스스로 권한을 가지고 작업을 자동화하고, Microsoft 365 앱과 상호작용**할 수 있어요.  

예를 들어, 단순히 "오늘의 회의록을 요약해줘"라고 하는 것이 아니라,  
💡 "이번 주 회의록을 정리해서, 주요 액션 아이템을 포함한 요약을 작성하고 팀원들에게 이메일로 보내줘"  
같은 **더 복잡한 자동화된 작업을 수행하는 것**이 Copilot 에이전트의 역할이에요.  

❓ 그렇다면 왜 Copilot Agent가 강력할까요? 

Copilot 에이전트는 Microsoft 365, Teams, Power Platform 등의 앱과 연결되어 있기에,  기업 내의 M365를 기반으로 구축된 내부데이터에 접근하여 **더욱 강력한 AI 지원 기능을 제공**할 수 있어요. 

또한 개발자가 아니더라도, **Copilot Studio를 활용해 노코드, 로우코드 방식**으로 쉽게 자신만의 에이전트를 만들 수가 있어요 

---
</br>

# 🏗️ Copilot 에이전트의 종류  


Copilot 에이전트는 크게 **두 가지 종류**로 나눌 수 있어요. 
각각의 에이전트는 활용 목적과 개발 방식, 배포 채널이 모두 다르기 때문에, 용도와 개인의 생황에 맞게 개발하시면 돼요. 

기억하셔야할 가장 큰 차이는 이것입니다. 

{: .note }
Declarative Agent는 Copilot의 Orchestrator, Foundation Model을 사용해야하는 반면, Custom Engine Agent는 다양한 모델을 자유롭게 취사선택 가능하다!


## **1️⃣ M365 Copilot Agent (Declarative Agent)**
✅ **설명:**  
- Microsoft 365 앱(Word, Excel, Teams 등)과 연동되는 **선언형(Declarative) 방식**의 에이전트예요. 

{: .note }
**Declarative 방식이란** :  Copilot의 모델과 오케스트레이터를 사용해 에이전트들에게 "무엇을 할지" 선언하고, ACTION을 만들어주면 자동적으로 ACTION을 실행하는 방식!

> ![declarative agent](../assets/2_what_is_copilot_agent/declarative_agent.png)

✅ **개발 방식**  

| 방식           | 대상        | 내용                                                  |
|:--------------|:------------|:------------------------------------------------------|
| **Copilot Studio** | 시민개발자  | 별도의 코드 작성 없이 Copilot Studio를 활용해 **노코드로 개발**! |
| **Teams Toolkit** | 개발자      | Teams Toolkit을 활용해, **VS Code 환경**에서 코드로 직접 개발 |

- Copilot 내 에이전트 빌드에서도 Declarative 에이전트를 개발할 수 있습니다. 
- 하지만, 자신의 조직으로 배포가 용이하지 않기에 설명에서 제외되었습니다. 


✅ **특징:**  
- M365 데이터(Outlook, SharePoint 등)를 활용한 자동화 가능  
- 명령어 기반으로 작업을 수행하며 Action들을 활용해 수많은 마이크로소프트 앱을 제어하고 통합 할 수 있음  
- 추가 개발 없이 설정만으로 간단한 에이전트 구축 가능  

✅ **활용 예시:**  
- **Teams에서 회의록 자동 정리 & 액션 아이템 생성**  
- **Excel에서 특정 데이터를 정리하여 요약 제공**  
- **SharePoint에서 문서를 검색하고 메일로 자동 공유**  

---

## **2️⃣ Custom Engine Copilot Agent**  
✅ **설명:**  
-  Declarative Agent의 한계를 넘어 **외부 API, 커스텀 플러그인, 복잡한 비즈니스 로직을 포함한 Copilot을 개발하는 방식**으로. 
  
{: .note }
Custom Engine Copilot은 개발자가 **Foundation Model과 Orchestrator을 자유롭게 커스텀** 할 수 있어요 

>![Custom_Engine_Agent](../assets/2_what_is_copilot_agent/custom_engine_agent.png)

✅ **개발 방식:**  

| 방식 | 대상 | 내용 |
|:--------------|:------------|:------------------------------------------------------|
| **Copilot Studio** | 시민개발자 | 노코드·로우코드 방식으로 Azure AI Services 및 1000개 이상의 커넥터를 활용해 에이전트 커스텀 |
| **Teams Toolkit & Teams AI Library** | 개발자 | Teams Toolkit과 Teams AI Library를 활용해 **VS Code 환경**에서 코드로 직접 개발 후 통합 |
| **Microsoft 365 Agent SDK (Preview)** | 개발자 | Copilot Studio와 호환되는 Agent SDK를 활용해 추가 기능을 부여**하고 확장  |


✅ **특징:**  
- **고급 AI 기능구현 가능** → Declarative Agent보다 **더 높은 수준의 자동화와 AI 기능 추가 가능**, 복잡한 워크플로우 처리 가능.      
- **다양한 스택과의 화끈한 통합** → **Teams, Azure OpenAI, 심지어 직접 개발한 LLM이나 Orchestration** 등과 결합하여 확장된 기능을 제공할 수 있어요.  


---

✅ **활용 예시:**  
- **맞춤형 고객 지원 봇**  
  - **Teams에서 AI가 채팅을 분석하고, 자동으로 티켓을 생성하는 Help Desk Bot**을 구축하여 고객 지원을 자동화할 수 있어요.  
  - **Azure OpenAI API를 활용하여** 고객의 문의를 분석하고, 가장 적절한 솔루션을 제공하는 AI 상담 봇 개발 가능.  

- **기업 내부 데이터 기반 AI 분석 도구**  
  - **Microsoft Graph API 및 Power Automate와 연동하여** 기업 내부 문서와 데이터를 분석하고, 필요한 정보를 자동으로 추출하여 제공.  
  - Copilot Studio에서 액션을 통해 SharePoint 및 Outlook 데이터를 검색하고, 외부 LLM API를 활용하여 이를 분석하고 결과를 생성하는 에이전트 개발.

---
 

## 🛠️ Deep Dive: Copilot 에이전트의 3가지 개발방식을 파해치자!  
Copilot 에이전트를 만들기 위해 3가지 주요 방법을 선택해서 사용할 수 있어요.  

### 1️⃣ Copilot Studio 
- Copilot Studio를 사용하면 **UI 기반으로 1)Declarative와  2)Custom Engine 에이전트를 구성**할 수 있어요.  
- 코딩 없이, 개발자가 아니더라도 쉽고 편하게 **M365 내에서 자동화된 AI 에이전트를 만들기 좋은 도구**예요.  
📎 **[클릭하셔서 Copilot Studio 공식 문서를 살펴보세요!](https://learn.microsoft.com/ko-kr/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)**  

> ![alt text](../assets/2_what_is_copilot_agent/copilot_studio.png)
---

### **2️⃣ Teams Toolkit과 Teams AI Library 사용**  
- 두 스택을 활용하면, **VS Code 환경에서 1) Declarative Agent와 2) Custom Engine 에이전트를 개발**할 수 있어요  
- 개발자분께서는 해당 스택을 활용하여, 더욱 편하게 Declarative Agent를 개발하거나 Orchestrator, LLM, 액션등 모든 요소를 커스텀하여 개발하실 수 있어요 
📎 **[Teams Toolkit 공식 문서](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-fundamentals)**  

---

### **3️⃣ Microsoft 365 Agents SDK 활용**
- M 365 Agent SDK는 가장 최근에 공개된 Agent 개발 방식으로 엔터프라이즈급으로 확장 가능한 멀티채널 에이전트를 구축하기 위한 개발 프레임워크에요 
- SDK를 사용하면, Teams Toolkit과 AI Library를 사용할 떄보다 더욱 쉽게 Azure AI Foundry 같은 AI 서비스를 통합하고, 오케스트레이션 레이어를 연결해 다른 서비스와의 연결을 용이하게 합니다. 
- 주의) Microsoft 365 Agents SDK는 Public Preview 단계의 제품입니다.  
📎 **[Microsoft 365 Agents SDK 공식 문서](https://microsoft.github.io/Agents/)**  

---




## 🏁 결론  
Copilot을 활용하면 단순한 AI 챗봇이 아니라, **실제 업무를 자동화하고 생산성을 극대화하는 AI 에이전트**를 만들 수 있어요!  

Copilot 에이전트는 **두 가지 종류**로 나뉘며, 목적과 활용 방식에 따라 적절한 방식을 선택할 수 있다는것 기억해주세요.  

✅ **Declarative Agent** → 코파일럿 스튜디오에서 선언만으로 AI 자동화 기능을 쉽게 개발 가능  
✅ **Custom Engine Copilot Agent** → API, SDK 및 AI 모델을 활용해 맞춤형 에이전트 구축 가능  

또한, **Copilot 에이전트를 개발하는 방법은 3가지**가 있어요.  

🛠️ **Copilot Studio** → 노코드·로우코드로 손쉽게 AI 에이전트 개발  
🛠️ **Teams Toolkit & Teams AI Library** → VS Code 환경에서 개발 가능  
🛠️ **Microsoft 365 Agents SDK** → 가장 확장성이 뛰어나며, AI 서비스 및 M365와의 통합 기능 제공  

각 방법마다 장점이 다르므로, **자신의 필요와 개발 환경에 맞는 방법을 선택하면 됩니다.**  
긴 글 읽으시느라 수고 많으셨습니다...  
다음 시간에는 본격적으로 Copilot Studio로 직접 Agent를 개발하는 법을 알아봐요!</br> 
제가 이 글을 썼을때는 25년 설입니다!!! 새해복도 많이 받으세요:)🚀  
