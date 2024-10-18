---
title: "Intune Endpoint Privilege Management의 신규 승인된 권한 상승 기능 소개"
date: 2024-10-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - 에이전트
  - AI 어시스턴트
  - 개인 비서
excerpt: "2024년 3월 릴리즈된 Intune Endpoint Privilege Management에 새롭게 추가된 승인된 권한 상승 기능에 대해 소개해드리겠습니다."
header:
  overlay_image: /assets/images/unsplash-image-11.jpg
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "원문 보기"
      url: "https://techcommunity.microsoft.com/t5/microsoft-intune-blog/endpoint-privilege-management-adds-support-approved-elevations/ba-p/4101196/"
toc: false
toc_sticky: true
classes: wide
author: 이지연
---

# Intune Endpoint Privilege Management의 신규 승인된 권한 상승 기능 소개

2024년 3월 릴리즈된 Intune Endpoint Privilege Management에 새롭게 추가된 승인된 권한 상승 기능에 대해 소개해드리겠습니다.
[원문보기](https://techcommunity.microsoft.com/t5/microsoft-intune-blog/endpoint-privilege-management-adds-support-approved-elevations/ba-p/4101196/)
{: .notice--info}

기존에는 IT 전문가들이 환경에서 가장 많이 사용되는 애플리케이션에 대한 권한 상승 규칙을 생성했습니다. 그러나 최종 사용자가 규칙이 없는 애플리케이션에 대한 권한 상승을 요청할 때는 자동으로 거부되었습니다. 이로 인해 최종 사용자는 도움말 데스크 티켓을 제출해야 했습니다. 이제는 승인된 권한 상승 기능을 통해 더 간단한 솔루션을 제공할 수 있습니다.

승인된 권한 상승 기능은 사용자가 특정 애플리케이션이나 작업에 대해 임시 관리자 권한을 요청할 수 있도록 하여 워크플로우를 간소화하면서도 강력한 보안 태세를 유지합니다. Windows 표준 사용자는 기존 권한 상승 규칙이 없는 애플리케이션에 대해 승인을 요청할 수 있습니다. Intune 관리자는 케이스별로 권한 상승 요청을 검토하고 승인 또는 거부할 수 있습니다.

일반적으로 Endpoint Privilege Management는 표준 사용자가 애플리케이션 설치나 장치 드라이버 업데이트와 같은 작업을 수행할 수 있도록 합니다. IT 관리자에게는 표준 사용자를 관리하면서도 Zero Trust 프레임워크를 유지하는 데 도움이 됩니다. 이 기능은 또한 보고 기능을 제공하여 조직 내 권한 상승에 대한 가시성을 제공합니다.

## 작동 방식

표준 사용자가 권한 상승이 필요한 작업을 수행할 때, 이제 애플리케이션의 컨텍스트 메뉴에서 직접 지원 승인을 요청할 수 있습니다. 최종 사용자는 요청에 대한 비즈니스 정당성을 제공해야 합니다. 필요할 경우, 사용자는 애플리케이션을 마우스 오른쪽 버튼으로 클릭하고 "승인된 액세스로 실행"을 선택할 수 있습니다. 그런 다음 비즈니스 정당성을 제출하고 신원을 확인한 후 요청을 제출합니다. 요청은 IT 관리자에게 전송되며, 관리자는 제공된 비즈니스 정당성을 기반으로 권한 상승을 승인하거나 거부할 수 있습니다. 승인이 되면 사용자는 다음 24시간 동안 권한 상승 작업을 수행할 수 있습니다.

![img1](/mwkorea/assets/images/20241018/img1.png)
 
승인된 권한 상승 기능은 Microsoft Intune 관리 센터 내에서 관리되며, IT 전문가가 하나의 콘솔에서 엔드포인트와 권한을 관리할 수 있도록 합니다. 권한 상승 요청 속성에는 애플리케이션 이름, 사용자 세부 정보 및 제공된 비즈니스 정당성이 포함됩니다.

![img2](/mwkorea/assets/images/20241018/img2.png)
 
요청은 제공된 비즈니스 정당성에 따라 등급을 승인하거나 거부할 수 있는 IT 관리자에게 전송됩니다.Intune 관리자는 요청을 승인할지 또는 거부할지 결정하여 사용자에게 24시간 동안 애플리케이션에 대한 높은 액세스 권한을 제공할 수 있습니다.

Endpoint Privilege Management는 표준 사용자가 관리자 권한이 필요한 작업을 수행할 수 있도록 하여 생산성을 유지하면서도 보안을 강화하는 데 중점을 둡니다. 이 기능을 통해 IT 관리자와 최종 사용자는 더 효율적이고 안전한 환경에서 작업할 수 있습니다.


## 참고

### Microsoft Endpoint Privilege Management 란?

Microsoft Endpoint Privilege Management는 Microsoft Intune Suite의 중요한 기능 중 하나입니다. Microsoft Endpoint Privilege Management는 사용자에게 최소 권한 원칙을 적용하면서도 필요한 경우 권한을 일시적으로 상승시킬 수 있는 기능을 제공합니다. 이를 통해 사용자는 필요한 작업을 수행할 수 있으며, IT 관리자는 보안 위험을 최소화할 수 있습니다.

이 솔루션의 주요 기능 중 하나는 **승인된 권한 상승**입니다. 사용자가 특정 애플리케이션이나 작업에 대해 관리자 권한이 필요할 때, 권한 상승 요청을 제출할 수 있습니다. 이 요청은 IT 관리자에게 전송되며, 관리자는 이를 검토하고 승인 또는 거부할 수 있습니다. 승인된 요청은 일정 기간 동안 유효하며, 사용자는 해당 기간 동안 필요한 작업을 수행할 수 있습니다.

또한, Microsoft Endpoint Privilege Management는 **자동화된 승인 프로세스**를 제공합니다. 이를 통해 권한 상승 요청이 신속하게 처리되며, IT 관리자의 업무 부담을 줄일 수 있습니다. 모든 권한 상승 요청과 승인/거부 내역은 기록되어 추적 및 감사가 가능하며, 이를 통해 보안 사고 발생 시 원인을 파악하고 대응할 수 있습니다.

이 솔루션은 **Zero Trust 보안 모델**을 지원합니다. Zero Trust 모델은 모든 사용자와 장치를 신뢰하지 않고, 모든 접근 요청을 검증하는 보안 접근 방식입니다. Microsoft Endpoint Privilege Management는 이 모델을 통해 조직의 보안을 강화하고, 불필요한 권한 부여를 방지합니다.

마지막으로, Microsoft Endpoint Privilege Management는 **사용자 경험을 개선**합니다. 사용자는 필요한 권한을 신속하게 얻을 수 있으며, IT 관리자는 보안 정책을 준수하면서도 사용자에게 원활한 작업 환경을 제공할 수 있습니다.

이와 같은 기능을 통해 Microsoft Endpoint Privilege Management는 조직의 보안을 강화하고, IT 관리의 효율성을 높이는 데 중요한 역할을 합니다. 

