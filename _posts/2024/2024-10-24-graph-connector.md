---
title: "Microsoft Graph Connectors 업데이트: Copilot의 지식을 확장하는 방법"
date: 2024-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft Graph
  - Copilot
  - 데이터 통합
  - Microsoft 365
excerpt: "Microsoft Graph Connectors를 통해 Copilot의 지식을 확장하고, 외부 데이터를 Microsoft 365 환경에 통합하는 방법에 대해 알아보세요."
header:
  overlay_image: /assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "원문 보기"
      url: "https://techcommunity.microsoft.com/t5/microsoft-365-copilot/microsoft-graph-connectors-update-expand-copilot-s-knowledge/ba-p/4243648"
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

# Microsoft Graph Connectors 업데이트: Copilot의 지식을 확장하는 방법

Microsoft Graph Connectors는 외부 데이터를 Microsoft Graph에 통합하여 Microsoft 365 환경 전반에서 검색 가능하게 합니다. 이번 업데이트를 통해 각 테넌트는 추가 비용 없이 5천만 개의 외부 데이터 항목을 인덱싱할 수 있게 되었습니다. 이로 인해 Microsoft 365 Copilot의 응답이 더 많은 작업 콘텐츠와 맥락에 기반할 수 있게 됩니다.
{: .notice--info}

![에이전트](/mwkorea/assets/images/20241024/copilot_graph-connectors-infographic.png)

## Microsoft Graph Connectors란 무엇인가?

Microsoft Graph Connectors는 조직이 외부 소스의 데이터를 Microsoft Graph에 통합하여 Microsoft 365 환경 전반에서 검색 가능하게 하는 도구입니다. 이를 통해 사용자는 Word 문서, PowerPoint 프레젠테이션 등 다양한 Microsoft 365 콘텐츠와 외부 콘텐츠를 통합된 경험으로 즐길 수 있습니다.

## 이번 업데이트의 주요 내용

이번 업데이트를 통해 Microsoft 365 및 Office 365 구독자는 추가 비용 없이 각 테넌트당 5천만 개의 외부 데이터 항목을 인덱싱할 수 있게 되었습니다. 이로 인해 라이선스당 인덱스 할당량이 제거되었으며, 추가 할당량에 대한 추가 비용도 없어졌습니다.

## 데이터 보안 및 접근 제어

Microsoft Graph Connectors를 구현할 때, 기존의 접근 제어 목록을 Microsoft 365 및 Entra ID의 객체에 매핑하여 올바른 권한을 가진 사용자만 콘텐츠에 접근할 수 있도록 합니다. 이를 통해 조직은 중앙 집중식 데이터 접근을 안전하게 유지할 수 있습니다.

## 변화의 이유

이전에는 특정 라이선스를 통해 내장된 할당량을 가지거나 추가 할당량을 구매해야 했습니다. 그러나 많은 조직이 Microsoft 365 Copilot의 잠재력을 최대한 활용하기 위해 더 많은 외부 데이터를 Microsoft Graph에 인덱싱하는 것이 중요하다고 인식하고 있습니다. 이번 변화는 고객 피드백에 직접 응답하여 데이터 용량을 늘리기 위한 우리의 헌신을 반영합니다.

## 조직에 미치는 영향

이번 변화로 인해 조직은 엄청난 양의 외부 데이터를 Microsoft Graph에 통합할 수 있게 되었습니다. 추가된 데이터 소스의 각 레코드는 "항목"으로 간주되며, Microsoft 365 Copilot의 응답에서 고유한 인용으로 검색 가능하게 됩니다.