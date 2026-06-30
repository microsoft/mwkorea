---
title: "Researcher의 Computer Use, Microsoft가 추진 중단을 공지하다"
date: 2026-06-26T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Researcher
  - ComputerUse
  - Agent
  - Roadmap
  - Update
excerpt: "Microsoft 365 Copilot의 Researcher에서 가상 컴퓨터로 공개·로그인 필요·인터랙티브 웹 콘텐츠를 탐색하는 Computer Use 기능이 더 이상 추진되지 않습니다. Microsoft는 해당 기능을 진행하지 않기로 결정했으며, 불편에 대해 사과한다고 공지했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Researcher의 Computer Use, Microsoft가 추진 중단을 공지하다

AI 에이전트가 웹을 직접 탐색하고, 인터랙티브한 페이지를 조작하며, 그 결과를 업무 데이터와 함께 분석해 보고서를 만드는 경험은 많은 기대를 모으고 있습니다. Microsoft 365 Copilot의 **Researcher** 역시 더 깊은 조사와 풍부한 보고서 생성을 돕는 방향으로 발전해 왔습니다.

Microsoft 365 Roadmap 항목 RM511796은 원래 **Researcher with Computer Use**를 소개했습니다. 이 기능은 가상 컴퓨터를 사용해 공개 웹, 로그인이나 권한이 필요한 웹, 인터랙티브 웹 콘텐츠와 안전하게 상호작용하고, 이를 통해 더 깊은 인사이트와 풍부한 보고서를 만들 수 있도록 하는 것이 목표였습니다.

하지만 이번 로드맵 업데이트에서 Microsoft는 이 기능을 **더 이상 추진하지 않기로 결정했다**고 공지했습니다. 원문에는 “We have decided not to move forward with this. We apologize for the inconvenience.”라고 명시되어 있습니다.

---

## 무엇이 변경되었나

기존 방향은 다음과 같았습니다.

- Researcher가 **가상 컴퓨터(virtual computer)**를 사용
- 공개 웹, gated web content, interactive web content와 안전하게 상호작용
- 웹과 업무 데이터를 기반으로 더 깊은 인사이트와 풍부한 보고서 생성

하지만 현재 상태는 명확합니다.

> Microsoft는 이 기능을 진행하지 않기로 결정했습니다.

따라서 해당 Roadmap 항목을 기준으로 Researcher의 Computer Use 기능을 기다리던 조직은, 이 기능을 전제로 한 PoC나 도입 계획을 재검토해야 합니다.

---

## 왜 중요한가

Computer Use는 최근 에이전트 기술에서 매우 중요한 키워드입니다. 단순히 API를 호출하는 것을 넘어, 사람이 브라우저에서 하는 것처럼 웹 화면을 보고 조작하는 방식은 많은 업무 자동화 가능성을 열어 줍니다.

그러나 동시에 기업 환경에서는 보안·권한·감사·데이터 경계 문제가 복잡합니다. 공개 웹뿐 아니라 로그인 필요 콘텐츠나 인터랙티브 웹 콘텐츠를 다루려면, 어떤 데이터를 읽고 어떤 행동을 할 수 있는지 매우 정교한 통제가 필요합니다. 이번 중단 공지는, 이런 유형의 기능이 제품화 과정에서 높은 기준의 안정성과 신뢰를 요구한다는 점을 다시 보여 줍니다.

---

## 도입 계획에 주는 영향

- **Researcher 확장 계획 재검토**: Computer Use를 전제로 한 리서치 자동화 시나리오는 다른 방식으로 설계해야 합니다.
- **웹 자동화와 Copilot 기능을 분리해서 검토**: 웹 조작 자동화가 꼭 필요하다면, 현재 제공되는 공식 기능과 별도 자동화 도구의 경계를 명확히 해야 합니다.
- **사용자 커뮤니케이션 주의**: 내부 교육이나 PoC 자료에 이 기능을 포함했다면, "추진 중단" 상태로 업데이트해야 합니다.
- **대체 시나리오 탐색**: Researcher의 현재 제공 기능, Graph 기반 데이터 접근, 승인된 커넥터·플러그인·에이전트 확장 모델 등 공식 지원되는 경로를 우선 검토하는 것이 안전합니다.

---

## 출시 일정

| 항목 | 내용 |
|------|------|
| 기능 | Microsoft 365 Copilot Researcher의 Computer Use |
| 원래 의도 | 가상 컴퓨터로 공개·권한 필요·인터랙티브 웹 콘텐츠와 상호작용 |
| 현재 상태 | **추진 중단** |
| 로드맵 표시 일정 | Preview: 2025년 10월, GA: 2025년 11월 |

> 로드맵에는 이전 일정이 표시되어 있지만, 최신 본문에는 Microsoft가 이 기능을 진행하지 않기로 결정했다고 명시되어 있습니다.

---

## 한국 고객을 위한 체크포인트

- **PoC 문서 업데이트**: Researcher의 Computer Use를 향후 기능으로 소개한 자료가 있다면 삭제하거나 상태를 정정하세요.
- **자동화 기대치 조정**: "Copilot이 웹을 직접 조작한다"는 시나리오는 아직 제품별 지원 범위가 다르므로, 현재 사용 가능한 기능만 기준으로 설계해야 합니다.
- **보안팀과 사전 논의**: 향후 유사 기능이 다시 등장하더라도, 가상 브라우저·웹 조작·로그인 콘텐츠 접근은 보안팀의 사전 검토가 필요한 영역입니다.
- **공식 지원 경로 우선**: 업무 데이터 기반 리서치에는 Microsoft 365 Copilot, Researcher, Graph 커넥터, Copilot 확장 모델 등 공식 지원되는 경로를 우선 사용하세요.

---

## 마무리

이번 업데이트는 신기능 출시 소식은 아니지만, 도입 담당자에게는 중요한 정보입니다. 로드맵에 있던 기능도 제품화 과정에서 중단될 수 있으며, 특히 에이전트가 외부 웹과 직접 상호작용하는 영역은 높은 수준의 보안·거버넌스 검토가 필요합니다. Researcher의 Computer Use를 기다리던 조직이라면, 해당 기능을 전제로 한 계획을 멈추고 현재 제공되는 공식 기능 중심으로 시나리오를 재정리하는 것이 좋겠습니다.

---

> **출처**: Microsoft 365 Roadmap 항목 **RM511796** · [mc.merill.net/message/RM511796](https://mc.merill.net/message/RM511796) · [Microsoft 365 Roadmap에서 보기](https://www.microsoft.com/en-us/microsoft-365-roadmap?searchterms=511796)
>
> *실제 출시 일정·기능은 변경될 수 있습니다.*
