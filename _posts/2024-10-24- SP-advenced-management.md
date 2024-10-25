---
title: "SharePoint Advanced Management을 통한 GenAI 데이터 관리"
date: 2024-10-24T00:00:00 KST
categories:
  - Copilot
tags:
  - SharePoint
  - 데이터 관리
  - Microsoft 365 Copilot
  - AI
  - 보안
excerpt: "SharePoint Advanced Management을 통해 Microsoft 365 Copilot의 데이터 관리와 보안을 강화하는 방법을 알아봅니다."
header:
  overlay_image: /assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "원문 보기"
      url: "https://techcommunity.microsoft.com/t5/microsoft-365-copilot/governing-data-for-genai-with-sharepoint-advanced-management/ba-p/4249193"
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

# SharePoint Advanced Management을 통한 GenAI 데이터 관리

Microsoft 365 Copilot의 새로운 기능은 콘텐츠 생성 속도를 가속화하여 전통적인 IT 제어를 확장할 필요성을 높입니다. SharePoint Advanced Management는 데이터 거버넌스와 위생을 단순화하여 보안 태세와 Copilot 경험을 향상시키는 기능 모음입니다. 이 블로그 글에서는 민감한 데이터를 안전하게 유지하고, 과도하게 공유된 콘텐츠를 식별하며, AI 중심의 접근 제어를 활성화하고, 불필요한 콘텐츠를 쉽게 제거하는 방법을 소개합니다.
{: .notice--info}

## SharePoint Advanced Management의 새로운 기능 소개

Microsoft 365 Copilot의 새로운 기능은 콘텐츠 생성 속도를 가속화하여 전통적인 IT 제어를 확장할 필요성을 높입니다. SharePoint Advanced Management는 데이터 거버넌스와 위생을 단순화하여 보안 태세와 Copilot 경험을 향상시키는 기능 모음입니다. 이 블로그 글에서는 민감한 데이터를 안전하게 유지하고, 과도하게 공유된 콘텐츠를 식별하며, AI 중심의 접근 제어를 활성화하고, 불필요한 콘텐츠를 쉽게 제거하는 방법을 소개합니다.

## 데이터 권한 및 접근 추적

데이터 거버넌스의 핵심 원칙은 데이터 접근을 필요한 사람에게만 허용하고, 접근을 감사하여 증거와 통제를 제공하는 것입니다. 새로운 권한 상태 보고서(현재 공개 미리보기)는 SharePoint, OneDrive 및 파일 전반의 모든 사이트 권한을 한눈에 볼 수 있게 하여 테넌트 전반에서 과도하게 권한이 부여된 콘텐츠를 발견할 수 있도록 도와줍니다. 이를 통해 관리자는 Copilot 또는 검색 결과가 해당 정보에 접근할 수 있는 사용자에게만 제한되도록 보장할 수 있습니다.

![에이전트](/mwkorea/assets/images/20241024/Oversharing Baseline Report.png)
- Screenshot: permission state report

## AI 기반 의미 매칭

AI 기반 의미 매칭(현재 공개 미리보기)은 관리자가 비정형 콘텐츠를 검색하고 미리 정의된 샘플과 일치하는 패턴을 의미적으로 감지할 수 있는 강력하고 지능적인 기능입니다. 관리자는 "유사한" 문서가 있는 사이트 목록을 제공할 수 있으며, 서비스는 입력과 의미적으로 일치하는 모든 사이트를 찾아 일치하는 사이트에 대한 정책 권장 사항을 제공합니다. 이를 통해 더 빠르게 좋은 거버넌스를 달성할 수 있습니다.

![에이전트](/mwkorea/assets/images/20241024/AI driven semantic matching of sites.png)
- Screenshot: AI driven semantic matching of sites

## 사이트 소유권 정책

사이트 소유권 정책(10월 출시 예정)은 규칙 기반 정책 엔진을 사용하여 콘텐츠 소유권 관리와 관련된 시간 소모적인 작업을 자동화할 수 있습니다. 예를 들어, 최소 사이트 소유자 수를 유지하고 가장 적절하고 책임 있는 개인을 식별하는 작업을 자동화할 수 있습니다. 효과적인 콘텐츠 소유권과 책임은 접근 검토 및 콘텐츠 인증과 같은 작업에 중요하며, 이는 Copilot에 의한 의도치 않은 접근을 방지하고 과도한 공유 사례를 줄이는 데 도움이 됩니다.

![에이전트](/mwkorea/assets/images/20241024/Site Ownership Policy.png)
- Screenshot: Site ownership policy

## 제한된 콘텐츠 검색

제한된 콘텐츠 검색(11월 출시 예정)은 관리자가 선택한 데이터 사이트에 대해 검색 및 Copilot의 추론을 제한하는 정책을 구성할 수 있도록 합니다. 사이트 접근은 변경되지 않지만, Copilot 또는 조직 전체 검색에서 사이트의 콘텐츠가 노출되지 않도록 합니다.

## 결론

SharePoint Advanced Management는 Microsoft 365 Copilot의 데이터 관리와 보안을 강화하는 데 중요한 역할을 합니다. 새로운 기능을 통해 민감한 데이터를 안전하게 유지하고, 과도하게 공유된 콘텐츠를 식별하며, AI 중심의 접근 제어를 활성화하고, 불필요한 콘텐츠를 쉽게 제거할 수 있습니다. 이를 통해 조직은 데이터의 안전성을 유지하고, 완전하고 일관된 데이터를 사용할 수 있습니다.

![에이전트](/mwkorea/assets/images/20241024/Sarah_Gilbert_0-1726686554655.png)
- Screenshot: Data Access Governance report on content shared with 'Everyone except external users'

[참고자료]
- https://learn.microsoft.com/en-us/SharePoint/get-ready-copilot-sharepoint-advanced-management
