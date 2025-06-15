---
title: "Copilot Chat Pay-as-you-Go 환경구성 가이드"
date: 2025-06-05T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
excerpt: "M365 Copilot 환경에서 선언형 에이전트를 사용하기 위한 설정과 과금 정책에 대해 다루고 있습니다. M365 Copilot 라이센스가 없는 사용자도 선언형 에이전트를 활용할 수 있도록 테넌트 기반 설정이 필요하며, 이를 통해 메시지 소모에 따른 과금 정책을 설정할 수 있습니다. 이 글에서는 Microsoft 365 관리자 센터와 Power Platform 관리자 센터에서 설정할 수 있는 청구 정책의 차이점과 설정 방법을 상세히 설명합니다. 또한, 각 청구 정책의 적용 단위와 과금 대상 서비스에 대해 비교하고, 선언형 에이전트를 무료 사용자에게 배포할 때 발생할 수 있는 문제점과 해결 방법을 제시합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  #actions:
  #  - label: "원문보기"
  #    url: "https://techcommunity.microsoft.com/blog/microsoft_365blog/sharing-the-vision-microsoft-365-community-conference-keynotes-now-available/4416368"
toc: false
toc_sticky: true
classes: wide
author: 최치원
---

# Copilot Chat Pay-as-you-Go 환경구성 

## 목적 

M365 Copilot License가 없는 사용자 (무료 사용자라 지칭)가 Agent Builder, Copilot Studio로 개발,배포된 선언형 Agent(Declarative Agent)를 이용하기 위해서는 몇가지 
테넌트 기반 설정이 필요합니다. 

과금 설정이 되어있지 않을 경우, **선언형 Agent 이용이 불가**하기에, 설정을 하지 않았을 때 발생하는 문제점과 분리과금 정책, Power platform admin center에서 환경설정에 연결한 과금 정책(Billing plan)과의 차이점에 대해 기술합니다. 

## 청구 정책(Billing Policy) 종류 

Copilot Agent를 운영하기 위해서는 2가지 종류의 청구 정책에 대해 이해가 필요합니다. 

1. Microsoft 365 관리자 센터에서 설정되는 청구 정책 (Microsoft 365 Copilot Chat) 
2. Power platform 관리자 센터에서 설정되는 청구 정책 (Azure Subscription/Microsoft 365 copilot Chat) 
{: .notice}

두 청구 정책 모두 사용한 만큼 과금이 되는 종량제 서비스(Pay-as-you-Go)를 위해 Azure Subscription을 연결한다는 것에서는 같은 컨셉이지만, 과금이 되는 대상에서 차이가 있습니다. 

|청구 정책 유형|과금 서비스|정책 적용 단위|비고|
|---|---|---|---|
|Microsoft 관리자센터 <br>M365 Copilot Chat|선언형 Agent|유저, 그룹 단위|**권장** 그룹별 별도 청구 정책 구성 가능|
|PowerPlatform 관리자센터 <br>Azure Subscription|커스텀 엔진 에이전트를 포함한 <br>Power platform 서비스 전체|환경 단위|과금 대상 서비스 조정 가능|
|PowerPlatform 관리자센터 <br>M365 Copilot Chat|선언형 Agent|환경 단위|1개의 정책만 구성 가능|

MAC(Microsoft 365 관리자센터)에서 설정할 수 있는 청구 정책의 경우, M365 Copilot license를 보유하지 않은 사용자가 **"선언형 Agent를 이용"** 하면서 메시지 소모(과금)가 발생하는 상황에서 청구되는 Azure Subscription을 지정하는 설정입니다. (Agent builder, Copilot Studio 모두 해당) 

**중요!** <br>
이곳에서는 복수개의 청구정책을 설정할 수 있으며, 각 정책마다 각기 다른 그룹, Azure subscription을 연결할 수 있어 부서별, 계열사별 분리 과금을 구성, 운영할 수 있습니다. 현재는 Power platform에서는 해당 기능을 제공하고 있지 않기에 분리 과금을 고려한다면 반드시 MAC에서 청구정책을 구성하여야 합니다. 
{: .notice--info}

Power Platform에서 설정하는 청구정책의 경우 Copilot Studio에서 개발 배포되는 Custom Engine Agent를 포함한 여러 Power Platform의 서비스 (Automate, Page, Apps, Dataverse 등)에 대해 종량제 과금을 환경(Environment) 단위로 적용 가능 

- 참고 링크#1 [Microsoft 365 Copilot chat 종량제 개요 Microsoft 365 Copilot](https://learn.microsoft.com/ko-kr/copilot/microsoft-365/pay-as-you-go/overview)
- 참고 링크#2 [종량제 플랜 설정 - Power Platform](https://learn.microsoft.com/ko-kr/power-platform/admin/pay-as-you-go-set-up?tabs=new)

## M365 Copilot chat 청구 정책을 만들지 않을 경우 발생하는 문제 

Custom Engine Agent만 이용하는 경우에는 Microsoft 365 Copilot Chat 청구 정책을 구성하지 않아도 문제가 없으나, 선언형 Agent를 활용 또는 일반 임직원, 시민 개발자 대상 Agent builder를 통한 no-code 기반 Agent 확산을 고려한다면 메시지 팩과 무관하게 Copilot Chat 청구 정책은 반드시 활성화가 필요합니다. 

**중요!** <br>
메시지팩을 구매하여 Copilot studio 환경에 메시지팩이 적용되더라도 선언형 Agent에 대해서는 청구 정책이 없을 경우 Agent는 동작하지 않음 
{: .notice--info}

청구 정책이 아직 생성/적용 되지 않은 상태에서 선언형 Agent를 무료사용자에게 배포할 경우, 아래와 같이 무료사용자들은 웹서치만 적용된 Agent가 아닌 모든 선언형 Agent에 대해서 공란으로 답변을 받게 된다. 

![image](/mwkorea/assets/images/20250605/image.png)  

---

## M365 Copilot chat 청구 정책 구성하기 (MAC vs Power Platform 관리자센터)  

선언형 Agent를 이용하기 위해서는 청구정책이 반드시 필요하며, 이를 구성할 수 있는 곳은 MAC(M365 관리자 센터) 또는 Power Platform 관리자센터 2군데가 존재한다.  <br>
둘 중 한곳에만 생성을 하면 이후 무료사용자들이 선언형 Agent를 이용할 수 있지만, MAC에서 구성하는 것을 권장한다.  <br>
Power Platform에서 구성을 할 경우, Microsoft 365 Copilot Chat 청구 정책은 1개만 생성 할 수 있기에 이와 연결되는 Azure Subscription도 1개로 제한된다.  <br>
따라서, 조직별 또는 하나의 테넌트에 여러 계열사가 소속된 경우 Azure subscription 단위로 분리 과금이 불가하다. 

![image](/mwkorea/assets/images/20250605/image2.png)  

---

반면, Microsoft 365 admin center에서 Copilot chat 청구 정책을 구성할 경우, 복수의 정책을 생성하여 Copilot chat에 연결할 수 있으며, 각각의 정책에 서로 다른 대상 그룹과 Azure 구독을 지정할 수 있어 부서별/계열사별 선언형 Agent 비용관리를 Azure 구독 단위로 설정하여 관리할 수 있다. 

![image](/mwkorea/assets/images/20250605/image3.png)  

---

이에, 본 문서에는 M365 관리센터에서 청구 정책을 연결하는 방법에 대해서만 기술한다. 

M365 관리자센터에서 청구 정책을 구성하기 전, 아래 작업을 사전에 완료한다. 

- Copilot chat에 연결한 Azure 구독 및 리소스 그룹 생성 
- Copilot Chat 청구 정책에 적용 받을 사용자 또는 그룹 선정 및 생성 

그룹에 속한 사용자들이 선언형 Agent를 이용할 경우, 해당 그룹과 연결된 청구 정책에 따라 Azure 구독으로 과금이 발생. 

- 청구 정책에 이용할 수 있는 그룹 
  - Microsoft 365 Group: 지원 
  - Security Group: 지원 
  - Distribution Group: 미지원 

준비가 완료되는 M365 관리자 센터로 이동 **[Copilot] – [청구 및 사용량]**으로 이동 후, **[+ 청구 정책 추가]**를 선택합니다. 

![image](/mwkorea/assets/images/20250605/image4.png)   

---

이후 이름, Azure 구독, 리소스 그룹 및 지역을 지정합니다.  
이 때 관리자는 연결 하려는 Azure 구독과 리소스 그룹에 대해 소유자 또는 기여자 역할이 있어야 합니다. 

![image](/mwkorea/assets/images/20250605/image5.png)  

---

청구 정책을 적용 받을 사용자, 그룹을 지정합니다.  <br>
모든 사용자를 선택할 경우 테넌트 내 모든 사용자들이 과금 기능이 포함된 선언적 에이전트를 이용할 수 있습니다.  <br>
그룹은 보안그룹, M365 그룹만 이용가능합니다. 

![image](/mwkorea/assets/images/20250605/image6.png)    

---

정보를 최종 확인하고 청구 정책을 생성합니다. 

![image](/mwkorea/assets/images/20250605/image7.png)    

---

생성이 완료되면, **[종량제 서비스]**로 이동, **[Microsoft 365 Copilot chat]**을 클릭합니다. 

![image](/mwkorea/assets/images/20250605/image8.png)    

---

Copilot chat에 연결할 정책을 지정합니다.  <br>
2025년 6월 5일 기준, 1개의 정책만 추가 저장이 되므로, 복수의 정책을 Copilot chat에 연결이 필요한 경우 하나씩 체크박스를 클릭하여 추가 저장합니다.  <br>
해당 설정이 완료되면 약 2-3시간 이후부터 무료사용자들도 선언형 Agent에 메시지 과금 기능(액션, 그라운딩 데이터 참조)을 이용할 수 있습니다. 

![image](/mwkorea/assets/images/20250605/image9.png)    

---

## Appendix. 청구정책에 속한 유저와 속하지 않은 유저간의 이용할 수 있는 기능차이 

![image](/mwkorea/assets/images/20250605/image11.png)    

---

## Appendix. SharePoint Agent 청구 정책 활성화 

SharePoint Agent의 경우 Microsoft 365 Copilot chat 청구 정책이 아닌, MAC에서 **[조직 설정] – [종량제 서비스] – [청구]** 에 있는 SharePoint Agent 설정을 통해 청구 정책을 활성화 해야 한다. 2025년 6월 5일 기준, 해당 설정은 조직별로 분류할 수 없이 테넌트 전체 사용자가 이용할 수 있도록 활성화가 되어있으므로 조직별 분산 과금, 하나의 테넌트에 복수의 계열사가 있는 경우에는 사용이 제한 된다. 

- 참고 링크: [Microsoft 365의 SharePoint 에이전트에 대한 사용량 기반 가격 책정](https://techcommunity.microsoft.com/blog/spblog/consumption-based-pricing-for-sharepoint-agents/4389591)

![image](/mwkorea/assets/images/20250605/image10.png)  
