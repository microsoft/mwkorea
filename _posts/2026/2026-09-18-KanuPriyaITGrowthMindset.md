---
title: "코드 작성 이후까지 책임지는 엔지니어링: Kanu Priya의 Copilot 에이전트 개발 사례"
date: 2026-09-18T00:00:00 KST
categories:
  - Copilot
tags:
  - InsideTrack
  - MicrosoftDigital
  - CopilotStudio
  - AIAgents
  - EmployeeExperience
excerpt: "Microsoft Digital 엔지니어 Kanu Priya의 경력 이야기는 직원의 장치 관리와 구매 경험을 AI 에이전트로 개선하는 사례로 이어집니다. 기술 학습뿐 아니라 문제 이해부터 운영과 지속 개선까지 책임지는 개발 방식이 핵심입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 코드 작성 이후까지 책임지는 엔지니어링: Kanu Priya의 Copilot 에이전트 개발 사례

에이전트를 만드는 일은 대화 화면을 구현하는 것으로 끝나지 않습니다. 직원이 어떤 문제를 겪는지 이해하고, 실제 운영에서 잘 작동하는지 살피며, 출시 뒤에도 개선해야 합니다.

Microsoft Inside Track은 사내 IT 조직인 **Microsoft Digital**의 소프트웨어 엔지니어 **Kanu Priya**를 소개합니다. 성장 과정과 경력을 다룬 인물 이야기이지만, 직원용 장치 관리·구매 에이전트의 개발 경험은 Copilot 도입 담당자와 메이커에게도 참고할 만합니다.

---

## 새로운 기술을 배우는 것 이상의 변화

Priya는 인도 펀자브의 인구 약 1,500명인 Nangal-Shama에서 자랐습니다. 주변에서 여성의 엔지니어 진로가 흔하지 않았지만 가족과 교사의 격려를 받아 컴퓨터 과학·공학을 공부했고, Publicis Sapient와 Expedia Group에서 여러 산업과 대규모 서비스의 개발을 경험했습니다.

2021년 Microsoft Digital에 합류한 뒤에는 Java·Python 중심의 배경에서 .NET과 C#을 배웠습니다. 자산 관리와 ServiceNow 개발을 거쳐 최근에는 원문이 Azure AI Foundry와 Copilot Studio로 설명하는 에이전트 개발에도 참여했습니다.

![Microsoft Digital 소프트웨어 엔지니어 Kanu Priya](/mwkorea/assets/images/2026-09-18-KanuPriyaITGrowthMindset/image1.png)

원문이 강조하는 변화는 기술 스택만이 아닙니다. 고객 문제를 이해하고, 솔루션을 전달하고, 프로덕션 상태를 관찰하며, 출시 이후 경험까지 개선하는 책임의 범위입니다.

## 직원 장치 정보 에이전트가 해결한 문제

Priya는 **Employee Device Information agent** 개발에 기여했습니다. Microsoft 직원이 주요 장치를 관리하고 잘못된 장치 정보나 할당을 수정하는 셀프서비스 경험입니다.

장치 정보가 틀리거나 수정하기 어렵다면 직원과 지원팀 모두 불필요한 확인 작업을 반복하게 됩니다. 원문은 이전에 사람의 개입이 필요했던 일을 자동화해 **지원팀과 BPO 조직의 수작업 노력을 70% 줄였다**고 보고합니다.

이 숫자는 해당 내부 사례에서 보고한 결과입니다. 측정 기간과 산식의 상세 내용은 이 인물 소개 글에 없으므로, 모든 장치 관리 에이전트나 고객 조직에 같은 효과가 보장된다고 일반화해서는 안 됩니다.

## 장치 선택과 구매를 대화로 연결

Priya는 구매 경험 에이전트의 초기 버전에도 참여했습니다. 직원이 구매 가능한 장치를 탐색하고 옵션을 비교하며, 직원 유형과 회사 요구사항을 바탕으로 추천을 이해하도록 돕는 기능입니다.

| 경험 | 원문에 소개된 역할 |
|---|---|
| 장치 정보 관리 | 주요 장치 확인, 부정확한 정보와 할당 수정 |
| 구매 경험 | 장치 탐색, 옵션 비교, 추천 이해, 대화형 선택 |
| 차세대 다중 에이전트 | 장치 선택·구매 흐름을 Microsoft 365의 Copilot 경험으로 연결하는 개발 작업 |

원문은 Copilot Studio를 이용해 장치 질문과 요청을 빠르게 처리하는 에이전트를 출시한 경험을 소개합니다. 반면 차세대 다중 에이전트 경험은 **현재 진행 중인 개발**로 설명합니다. 모든 고객에게 해당 솔루션이 이미 출시됐다는 발표가 아닙니다.

## AI 도입팀이 참고할 개발 방식

이 사례에서 가져갈 점은 특정 에이전트 이름보다 **문제에서 출발하는 방법**입니다. 직원이 자주 확인하는 정보, 지원팀에 반복해서 들어오는 수정 요청, 여러 화면을 오가야 하는 선택 과정을 먼저 살펴볼 수 있습니다.

또한 원문은 요구사항과 명세부터 코드·배포까지 소프트웨어 개발 과정 자체에서도 AI를 활용하고 있다고 설명합니다. 업무용 에이전트를 만드는 일과 개발 과정에서 AI를 사용하는 일은 연결되어 있지만, 각각의 결과를 구분해 평가하는 것이 좋습니다.

실무에서는 개발 완료와 운영 완료를 같은 것으로 보지 않는 접근이 필요합니다. 에이전트를 출시한 뒤에도 지원 요청과 사용자 피드백을 확인하고, 잘못된 데이터나 실패하는 흐름을 개선할 책임자를 정해 두는 것이 도움이 됩니다. 이는 사례에서 도출한 운영 제안입니다.

## 성장의 경험을 다른 사람의 기회로

원문은 Priya가 멘토와 동료의 지원을 경력 성장의 중요한 요소로 꼽고, 고향의 젊은 여성들에게 새로운 진로의 본보기가 된 이야기도 담습니다.

Copilot·에이전트 개발에서는 새로운 도구를 배우는 능력뿐 아니라 함께 배우고 운영 문제를 해결하는 문화도 중요합니다. 이 사례는 기능을 빠르게 만드는 것과 장기적으로 책임 있게 운영하는 일을 함께 생각하게 합니다.

---

> **출처**
>
> - Microsoft Inside Track: [Building a career in IT with a growth mindset: Kanu Priya’s Microsoft journey](https://www.microsoft.com/insidetrack/blog/building-a-career-in-it-with-a-growth-mindset-kanu-priyas-microsoft-journey/)
> - 관련 사례: [Employee Device Information agent](https://www.microsoft.com/insidetrack/blog/meet-eddie-our-agent-for-putting-new-pcs-in-the-hands-of-our-employees/)
>
> 자세한 내용은 원문 참조. 성과 수치는 Microsoft 내부 사례의 보고이며 일반적인 성능 보장을 뜻하지 않습니다.
