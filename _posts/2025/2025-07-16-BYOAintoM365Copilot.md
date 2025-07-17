---
title: "커스텀 엔진 에이전트가 GA 되었습니다! BYOA!!"
date: 2025-07-16T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
excerpt: "Microsoft 365 Copilot에서 커스텀 엔진 에이전트가 공식적으로 지원되어, 조직이나 개발자가 자신만의 AI 에이전트를 업무 흐름에 직접 통합할 수 있게 되었습니다. 개발자는 다양한 플랫폼과 도구(Azure AI Foundry, Visual Studio 등)를 활용해 맞춤형 에이전트를 만들고, 비동기 작업, 외부 시스템 연동, 엔터프라이즈급 보안 및 관리 기능을 그대로 적용할 수 있습니다. 이제 누구나 Microsoft 365 Agents Toolkit과 SDK를 사용해 손쉽게 에이전트를 개발·배포할 수 있으며, Agent Store를 통해 조직 내에서 안전하게 관리할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "원문보기"
      url: "https://devblogs.microsoft.com/microsoft365dev/bring-your-own-agents-into-microsoft-365-copilot/"
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

# Microsoft 365 Copilot에 나만의 에이전트 가져오기  

## 커스텀 엔진 에이전트 일반 제공—직접 만든 AI를 업무 흐름에 통합하세요

Microsoft 365 Copilot은 사람들이 AI와 상호작용하는 방식을 재정의하고 있습니다—에이전트의 직관적이고 자연스러운 인터페이스, 즉 ‘AI를 위한 UI’로 업무 흐름에 직접 내장되고 있습니다.

Copilot이 직장에서 AI의 인터페이스가 되면서, 고객들은 자체 솔루션으로 Copilot의 기능을 확장하고자 하는 수요가 점점 커지고 있습니다. 많은 고객들이 커스텀 에이전트를 만들고자 하거나, 이미 Microsoft 365 생태계 외부에서 동작하는 에이전트를 구축해왔습니다—파인튜닝된 모델, 커스텀 로직, 오케스트레이터, 도구, 지식 소스, 또는 다른 시스템과의 복잡한 통합을 활용하여 말이죠. **오늘, 우리는 이 에이전트들을 Microsoft 365 Copilot에 가져올 수 있도록 지원합니다. Microsoft 365 Copilot에서 [커스텀 엔진 에이전트](https://aka.ms/BYOA-Blog-docscea)의 일반 제공(General Availability)을 발표하게 되어 기쁩니다.**

개발자가 어디서, 어떻게 에이전트를 만들었든—Copilot Studio, Azure AI Foundry, Visual Studio, 기타 AI 플랫폼 등—이제 Microsoft 365 Copilot에 원활하고 네이티브한 경험으로 가져올 수 있습니다. 이 통합은 개발자에게 에이전트의 동작, 데이터 접근, 사용자 상호작용에 대한 완전한 제어권을 제공하여, Microsoft 365 생태계 전반에서 일관성, 보안, 적응성을 보장합니다.

![image](/mwkorea/assets/images/20250716/image01.png)  

**LexisNexis Protege 커스텀 엔진 에이전트**  
커스텀 엔진 에이전트가 LexisNexis Protégé™를 Microsoft 365 Copilot에서 구현합니다.

## 완전한 유연성으로 에이전트 구축

처음부터 시작하든, 기존 솔루션을 확장하든, 로직, 데이터 접근, 사용자 상호작용을 완전히 제어하면서 개발자는 다음을 할 수 있습니다:

- 특정 비즈니스 프로세스에 맞는 **커스텀 워크플로우와 로직을 코드로 정의**
- **자체 오케스트레이션 및 모델**(예: Azure AI Foundry, Hugging Face 등에서 가져온 독점 또는 파인튜닝된 LLM) 사용
- **외부 API 및 시스템과 통합**하여 복잡한 작업 자동화, 실시간 데이터 검색, Copilot의 기본 기능을 넘어선 확장성 제공
- 장기 실행 작업 및 사전 알림 등 **비동기 패턴 구현**으로, 에이전트가 백그라운드에서 동작하는 동안 사용자의 생산성 유지
- **Microsoft 365 Copilot, Teams, 기타 채널 전반**에 엔터프라이즈급 보안 및 컴플라이언스와 함께 배포
- 조직 정책 및 규제 요건에 부합하는 **보안 및 컴플라이언스 제어 강화**

## Microsoft 365 Agents Toolkit 및 SDK로 커스텀 에이전트 개발 가속화

개발자는 Visual Studio와 Visual Studio Code에서 제공되는 [Microsoft 365 Agents Toolkit](https://aka.ms/BYOA-M365AgentsToolkit)을 통해 더 빠르게 Microsoft 365 Copilot용 커스텀 엔진 에이전트를 만들 수 있습니다. 이 툴킷은 내장된 스캐폴딩, 디버깅 도구, 테스트, [Microsoft 365 Agents SDK](https://aka.ms/BYOA-M365AgentsSDK-Docs)와의 원활한 통합으로 커스텀 에이전트 구축 과정을 간소화합니다.

![image](/mwkorea/assets/images/20250716/image02.png)  

에이전트가 게시되면, 즉시 Agent Store에서 검색 가능해지며, Microsoft 365 Copilot, Teams 등 사용자가 일하는 곳 어디서든 바로 사용할 수 있습니다.

Azure AI Foundry 모델로 커스텀 엔진 에이전트를 쉽게 만들고, Toolkit과 SDK로 Microsoft 365 Copilot에 게시하는 방법을 확인해보세요.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yTJ9-CWwHXQ?si=5JUqyBZZDg1PwvaU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 비동기 시나리오 패턴 지원 도입

Microsoft 365 Copilot의 에이전트에 새로운 네이티브 패턴을 도입하여, 개발자가 비동기적으로 동작하는 커스텀 에이전트를 구축할 수 있도록 지원합니다—더 풍부하고 유연한 사용자 경험을 제공합니다. 기존의 동기식 상호작용과 달리, 이 패턴은 에이전트가 백그라운드에서 계속 작업하거나 필요할 때 사용자를 능동적으로 참여시킬 수 있게 합니다.

비동기 시나리오 패턴을 통해 커스텀 에이전트는 이제 다음을 할 수 있습니다:

- **후속 메시지**: 커스텀 에이전트가 데이터 분석이나 보고서 생성 등 백그라운드 처리를 수행하는 동안, 사용자는 Copilot 인터페이스의 다른 부분에서 계속 작업할 수 있습니다. 예를 들어, 사용자가 노트북 교체 주문을 요청하면, 에이전트가 백그라운드에서 이를 처리하여 워크플로우를 방해하지 않습니다.
- **장기 실행 작업**: 에이전트가 확장된 작업을 비동기적으로 관리하여, 사용자가 작업을 시작하고 완료 알림을 받을 수 있습니다. 예를 들어, 에이전트가 SharePoint 사이트의 모든 문서에 워터마크를 추가하는 동안 사용자는 다른 업무를 계속할 수 있습니다.
- **사전 알림**: 에이전트가 사용자 프롬프트 없이도 적시에 알림을 보내, 예를 들어 면접 피드백 입력을 상기시키는 등, 사용자가 중요한 작업을 놓치지 않도록 도와줍니다.

## Microsoft Teams 및 Microsoft 365 Copilot과의 원활한 통합

커스텀 엔진 에이전트의 경험은 Microsoft 365 Copilot의 네이티브 일부처럼 느껴지도록 설계되었습니다. Agent Store에서 승인 및 게시되면, 별도의 설치 없이 즉시 사용자에게 제공됩니다. Microsoft Teams, Microsoft 365 Copilot 웹 또는 데스크톱 앱 어디에서든, 사용자는 Copilot Chat 및 사이드바에서 에이전트를 직접 검색, 실행, 상호작용할 수 있습니다.

![image](/mwkorea/assets/images/20250716/image03.png)  

**M365 Copilot Agent Store**  
Agent Store는 모든 에이전트를 하나의 직관적인 경험으로 모읍니다.

에이전트는 친근한 환영 메시지와 시작을 돕는 추천 프롬프트를 제공하여, 첫 상호작용부터 직관적이고 Copilot-네이티브한 경험을 제공합니다. 사용자는 에이전트 설명을 둘러보고, 즐겨찾는 에이전트를 설치하거나, 업무 흐름 내에서 빠르게 접근할 수 있도록 고정할 수 있습니다.

![image](/mwkorea/assets/images/20250716/image04.png)  

**Asana 이미지**  
커스텀 엔진 에이전트로 Asana를 Copilot과 Teams에서 네이티브하게 사용할 수 있습니다.

현재 SAP Joule, LexisNexis Protégé, Meltwater, Asana 등 파트너들이 Microsoft 365 Copilot용 커스텀 에이전트를 Agent Store에 출시하고 있습니다. 이 에이전트들은 파트너의 에이전트 활용 사례에 맞는 맞춤형 기능을 M365 Copilot의 업무 흐름에 제공합니다. 앞으로 더 많은 파트너의 에이전트가 추가될 예정입니다.

![image](/mwkorea/assets/images/20250716/image05.png)  

**SAP Joule 커스텀 엔진 에이전트**  
SAP Joule은 커스텀 엔진 에이전트를 통해 Microsoft 365 Copilot과 원활하게 연결됩니다.

## 엔터프라이즈급 제어—다른 Copilot 에이전트와 동일하게

커스텀 엔진 에이전트는 Microsoft 365 Copilot의 다른 에이전트와 동일한 관리 및 거버넌스 모델을 따르므로, IT 관리자는 안전하게 확장할 수 있는 신뢰와 제어권을 가집니다. Microsoft 365 관리 센터를 통해 관리자는 다음을 할 수 있습니다:

- 조직 전체에서 Agent Store의 에이전트 승인 또는 차단으로 사용 가능 여부 관리
- 보안 그룹 및 역할 기반 권한을 사용하여 접근 제어
- 데이터 접근 정책을 정의하여 에이전트가 승인된 소스와만 상호작용하도록 보장
- 내장된 보고 및 분석 기능으로 사용 현황과 성능 모니터링
- 조직 정책 및 규제 요건에 따른 컴플라이언스 강제
- 이러한 기능을 통해 커스텀 엔진 에이전트도 다른 Copilot 네이티브 경험과 동일한 엄격함, 유연성, 보안으로 배포 및 관리할 수 있습니다.

## 지금 바로 Microsoft 365 Copilot용 에이전트로 코드 변환!

커스텀 엔진 에이전트가 이제 일반 제공됨에 따라, 개발자와 조직은 AI가 업무 흐름에 어떻게 적용될지 직접 설계할 수 있습니다. 커스텀 로직과 모델부터 안전하고 확장 가능한 배포까지, 팀이 고유한 요구와 업무 방식을 반영하는 에이전트를 Microsoft 365 Copilot 내에서 직접 구축할 수 있습니다.

시작하려면 Visual Studio 및 Visual Studio Code용 Microsoft 365 Agents Toolkit을 [다운로드](https://aka.ms/BYOA-M365AgentsToolkit)하고, 몇 분 만에 첫 번째 에이전트를 Microsoft 365 Copilot에 가져오세요. 다음 리소스를 참고하실 수 있습니다:

- 커스텀 엔진 에이전트에 대해 더 알아보기:  
  [개발자 문서](https://aka.ms/BYOA-Blog-docscea)
- 단계별 튜토리얼 따라하기:  
  [M365 Agents SDK와 Semantic Kernel로 나만의 에이전트 만들기](https://aka.ms/BYOA-L300Labs)
- 영상으로 보기:  
  [Azure AI Foundry 에이전트를 Microsoft 365 Copilot 및 그 이상으로 가져오기](https://aka.ms/BYOA-L300DemoATK-allchannels)
  [M365 Agents SDK로 Microsoft 365 Copilot용 에이전트 만들기](https://aka.ms/BYOA-L300DemoASDK)

여러분이 Microsoft 365 Copilot에 어떤 멋진 에이전트를 가져올지 기대하겠습니다.

---

**원문 블로그**
https://devblogs.microsoft.com/microsoft365dev/bring-your-own-agents-into-microsoft-365-copilot/
