---
title: "개발자를 위한 로우코드 에이전트 2탄: Direct Line 통합 시나리오"
date: 2025-08-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - Agent
excerpt: "Microsoft Copilot Studio의 로우코드 에이전트는 개발자가 직접 코드와 통합할 수 있는 두 가지 방법(M365 Agent SDK 또는 Direct Line)을 제공합니다. 이번 영상에서는 MDirect Line를 활용한 통합 시나리오를 중심으로 실제 구현 흐름과 샘플 코드 수정 과정을 소개합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  #actions:
  #  - label: "원문보기"
  #    url: "https://www.microsoft.com/en-us/power-platform/blog/2025/07/21/agent-costs-controls/?msockid=3535fcba82d669720766ed1c8358686d"
toc: false
toc_sticky: true
classes: wide
author: 안창주
---

# 개발자를 위한 로우코드 에이전트 2탄: Direct Line 통합 시나리오

최근 로우코드 플랫폼의 발전으로, 개발자들도 AI 에이전트를 보다 쉽게 활용할 수 있는 시대가 열렸습니다. 특히 Microsoft Copilot Studio에서 제공하는 로우코드 기반의 에이전트는 단순한 챗봇을 넘어, 실제 업무 시나리오에 맞춘 코드 레벨 통합까지 가능하게 해줍니다.

이번 영상에서는 개발자들이 가장 궁금해할 수 있는 질문,
**"로우코드 에이전트가 실제 코드와 통합될 수 있을까?"**
에 대한 해답을 제시합니다.

## 두 가지 통합 방식

Copilot Studio의 에이전트는 다음 두 가지 방식으로 코드와 통합할 수 있습니다:

1. **M365 Copilot Agent SDK**
2. **Direct Line API**

여기서는 Direct Line 기반으로 통합하는 시나리오입니다.
이건 SDK가 출시되기 전에 코드 레벨에서 통합했던 방법입니다. 이전에 AI 아바타와 연결된 에이전트도 이 방법으로 구현한 점 참고해 주세요!

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/rWxu48DG8oo?si=y6dR91r7I4CS_fJL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

이전 Azure AI 아바타와 결합된 Copilot Studio를 못 보셨다면? 아래를 참고해 주세요.

<iframe width="560" height="315" src="https://www.youtube.com/embed/QlM6QEUi_34?si=sMH6KTXdR1gpGwVy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

