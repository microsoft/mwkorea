---
title: "Microsoft 365 Copilot Chat vs 직원 셀프서비스 에이전트, 언제 무엇을 써야 할까"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - EmployeeSelfServiceAgent
  - WorkIQ
  - CopilotStudio
  - EmployeeExperience
  - AIGovernance
excerpt: "Microsoft 사내 IT 부서가 생산성용 Microsoft 365 Copilot Chat과 HR·IT 지원용 Employee Self-Service Agent를 어떻게 구분해 운영하는지 소개합니다. 여러 AI 경험을 도입하는 조직을 위한 설계 원칙을 담고 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Microsoft 365 Copilot Chat vs 직원 셀프서비스 에이전트, 언제 무엇을 써야 할까

조직에 AI 기반 업무 지원 도구를 하나둘 늘려가다 보면 반드시 마주치는 질문이 있습니다. "이 요청에는 어떤 에이전트를 써야 하지?" Microsoft 사내 IT 부서(Microsoft Digital)도 같은 고민을 했고, Inside Track 블로그를 통해 그 해법을 공유했습니다.

핵심은 하나의 범용 챗봇에 모든 것을 몰아넣는 대신, **생산성 업무용 Microsoft 365 Copilot Chat**과 **직원 지원용 Employee Self-Service Agent**를 명확히 분리해 "하나의 정문(front door)"처럼 운영하는 것입니다. 여러 AI 에이전트를 함께 운영해야 하는 한국의 IT·HR 담당자에게 실질적인 설계 지침이 될 만한 내용입니다.

---

## 생산성과 직원 지원을 분리하기

Microsoft 365 Copilot Chat은 **생산성 업무**를 위한 도구입니다. 파일, 이메일, Teams 대화, 회의 데이터, 웹 정보 등 직원이 접근 가능한 업무 콘텐츠를 바탕으로 추론합니다.

- "어제 회의에서 어떤 결정을 내렸지?"
- "이 두 제안서를 비교해 줘"
- "프로젝트 기획서 초안 작성을 도와줘"

반면 HR·IT 지원처럼 **승인된 정책, 지원 기록, 기기 정보, 위치 기반 정보**에 의존하고, 때로는 케이스 개설이나 요청 제출 같은 **실제 조치**로 이어져야 하는 영역은 접근 방식이 다릅니다. Microsoft는 이를 **Employee Self-Service Agent**로 처리합니다.

- "자격 증명(credential) 문제를 해결하도록 도와줘"
- "HR 티켓을 열어줘"
- "고장난 장비에 대한 시설 요청은 어떻게 제출하나요?"

| 구분 | Microsoft 365 Copilot Chat | Employee Self-Service Agent |
|---|---|---|
| 지원 시스템 연결 | 아니오 | 예 (지원 대상 서비스 전체) |
| 작업 완료 | 예 (생산성 시나리오) | 예 (업무 지원 요청) |
| 개인화 | 예 (Work IQ 기반) | 예 (직무·기기 정보·위치 기반) |
| OneDrive/메일/Teams/회의 정보 접근 | 예 | 아니오 (설계상 의도적 제한) |
| 외부 웹사이트 접근 | 예 | 아니오 (설계상 의도적 제한) |

두 경험은 같은 플랫폼을 공유하지만 역할이 다릅니다. 선택 기준은 직원의 의도, 답변에 필요한 소스, 그리고 비즈니스 프로세스·워크플로 연결 필요 여부입니다.

---

## 각 경험을 용도에 맞게 개인화하기

생산성 업무에서는 "폭넓음"이 가치입니다. Copilot Chat은 Microsoft 365 업무 맥락과 외부 정보를 함께 활용해 요약·비교·조사·작성·추론을 지원합니다. 이는 Microsoft가 **Work IQ**라고 부르는 기능으로, 직원 개인의 업무 데이터를 활용하는 방식입니다.

반면 직원 지원에서는 "폭넓음"보다 "권위(authority)"가 중요합니다. Employee Self-Service Agent는 HR, 기술 지원, 사내 캠퍼스 서비스에 특화된 **Microsoft 관리 소스**만 사용해, 답변이 확립된 정책·지원 프로세스와 일치하도록 합니다. 또한 기기 정보나 위치 같은 업무 신호를 활용해 올바른 정책·지원 경로·서비스로 안내합니다.

흥미로운 점은 이 에이전트가 **아키텍처 수준에서도 계속 진화 중**이라는 것입니다. Employee Self-Service Agent는 Microsoft 365 Copilot 오케스트레이터·런타임 위에서 네이티브로 동작하는 **선언적(declarative) 에이전트**로 재구축되고 있습니다. 플랫폼 "옆"이 아니라 플랫폼 "위"에서 직접 빌드함으로써, 최신 Copilot 지원 모델과 함께 최신 상태를 유지하고, Copilot 네이티브 추론으로 응답하며, 더 빠르게 반응하고, 예측 가능한 작업을 위한 결정론적(deterministic) 워크플로와 자연스러운 대화를 위한 생성형 지능을 함께 결합하면서도 플랫폼 개선 사항을 자동으로 상속받습니다.

조직이 유사한 경험을 설계할 때는 **소스 경계와 맥락 신호를 미리 정의**해야 합니다. 각 서비스 영역에 대한 승인된 시스템을 식별하고, 콘텐츠를 최신 상태로 유지할 담당자를 지정하고, 정확한 응답에 필요한 맥락만 사용하는 것이 핵심입니다.

---

## 올바른 경험을 쉽게 찾도록 만들기

아무리 좋은 AI 경험도 직원이 어디서 시작해야 할지 모르면 마찰이 생깁니다. Microsoft에서는 Employee Self-Service Agent를 Copilot 환경 안에서 바로 접근할 수 있도록 배치했습니다. 직원은 Copilot 사이드바에 이 에이전트를 고정해두고, 다른 인터페이스를 열지 않고도 일반 생산성 지원에서 업무 지원으로 손쉽게 전환할 수 있습니다.

조직도 같은 원칙을 적용해야 합니다: 직원이 이미 일하는 곳에 전문화된 에이전트를 배치하고, 그것이 해결하는 문제를 기준으로 설명하며, 간단한 판단 규칙을 제공하세요. 직원은 내부 아키텍처를 이해할 필요가 없습니다. 눈앞의 작업을 위해 어디로 가야 하는지만 알면 됩니다.

---

## 피드백으로 라우팅과 답변 개선하기

여러 AI 경험이 관련된 질문을 함께 다룰 수 있을 때, 피드백 루프는 특히 중요해집니다. Microsoft 직원들은 Employee Self-Service Agent의 응답에 즉시 평점을 매기고 코멘트를 남길 수 있으며, 이 입력은 누락된 지식, 불명확한 안내, 라우팅 문제, 제대로 동작하지 않는 작업을 찾아내는 데 쓰입니다.

이 피드백은 만족도 점수라기보다 **운영 신호**로 봐야 합니다. 직원이 어디서 어려움을 겪는지, 어떤 지식 소스를 개선해야 하는지, 경험 간 라우팅을 어떻게 더 명확히 할 수 있는지를 드러내 줍니다.

---

## 핵심 요약

- **직원의 의도에서 시작하라**: AI 경험이나 아키텍처를 고르기 전에 생산성 업무와 업무 지원 요청을 분리하라
- **권위 있는 소스를 정의하라**: 승인된 HR·IT·업무 정보가 담긴 시스템을 식별하고 콘텐츠 최신화 담당자를 지정하라
- **지원을 조치로 연결하라**: 답변만으로 부족할 때 요청 생성·지원 연결·워크플로 완료가 가능하도록 전문 에이전트를 설계하라
- **목적에 맞게 개인화하라**: 직원의 결과를 직접 개선하는 업무·기기·조직·위치 맥락만 사용하라
- **찾기 쉽게 만들어라**: 직원이 이미 일하는 곳에 전문 에이전트를 배치하고 해결하는 문제 기준으로 설명하라
- **피드백 루프를 구축하라**: 평점과 코멘트로 지식 격차, 라우팅 문제, 서비스 개선 기회를 찾아라

---

## 더 알아보기

- [Employee Self-Service Agent 개요 (Microsoft Learn)](https://learn.microsoft.com/en-us/microsoft-365/copilot/employee-self-service/overview?OCID=InsideTrack_Product_10942)
- [적합한 Copilot 고르는 법 (Inside Track)](https://www.microsoft.com/insidetrack/blog/picking-the-right-copilot-for-the-job-tips-from-our-experience-at-microsoft/)
- [Employee Self-Service Agent로 직원 서비스 가속화하기 (Inside Track)](https://www.microsoft.com/insidetrack/blog/accelerating-employee-services-at-microsoft-with-the-employee-self-service-agent/)
- [엔터프라이즈 규모 배포 블루프린트 (Inside Track)](https://www.microsoft.com/insidetrack/blog/deploying-the-employee-self-service-agent-our-blueprint-for-enterprise-scale-success/)
- [Microsoft Copilot Studio로 엔터프라이즈 AI 확장성 확보하기 (Inside Track)](https://www.microsoft.com/insidetrack/blog/unlocking-enterprise-ai-extensibility-at-microsoft-with-microsoft-copilot-studio)

---

> **출처**: [Choosing the right AI experience for employee productivity and support (Microsoft Inside Track Blog, 2026-10-01)](https://www.microsoft.com/insidetrack/blog/choosing-the-right-ai-experience-for-employee-productivity-and-support/) · 자세한 내용은 원문 참조
