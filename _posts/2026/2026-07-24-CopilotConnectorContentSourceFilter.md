---
title: "찾던 데이터를 콕 집어: Copilot의 '콘텐츠 소스 필터'로 커넥터 검색이 쉬워진다"
date: 2026-07-24T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotConnectors
  - GraphConnectors
  - ContentSource
  - Search
  - Roadmap
excerpt: "Microsoft 365 Copilot에서 어떤 외부 데이터 소스가 연결되어 있는지 찾고, 원하는 소스만 골라 질문 범위를 좁힐 수 있게 됩니다. '콘텐츠 소스 필터'로 커넥터 소스 탐색이 한결 직관적으로 개선됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 찾던 데이터를 콕 집어: Copilot의 '콘텐츠 소스 필터'로 커넥터 검색이 쉬워진다

조직에서 Copilot 커넥터를 여러 개 연결하다 보면, 정작 사용자는 **"내가 지금 어떤 외부 데이터에 질문할 수 있는지"** 를 잘 모르는 경우가 생깁니다. Jira, ServiceNow, Confluence, 사내 위키까지 다양한 소스가 색인돼 있어도, 이를 발견하고 원하는 소스만 골라 쓰는 경험이 매끄럽지 않았죠.

이번 로드맵 항목(RM502541)은 이 문제를 해결합니다. Microsoft 365 Copilot(필요 시 채팅 추가)에서 **콘텐츠 소스 필터(Content Source filter)** 를 통해 연결된 커넥터 소스를 **더 쉽게 발견하고 선택**할 수 있도록 개선하는 기능입니다.

현재 **개발 중(In development)** 상태이며, **전 세계(Worldwide) 대상 2026년 9월 GA** 를 목표로 합니다.

---

## 무엇이 달라지나요?

- **커넥터 소스 발견성 향상**: Copilot 화면에서 조직에 연결된 외부 데이터 소스를 더 명확하게 인지할 수 있습니다.
- **콘텐츠 소스 필터 제공**: 사용자가 특정 소스(들)를 선택해 **질문·검색 범위를 그 소스로 한정**할 수 있습니다. 예를 들어 "Jira 이슈에서만 찾기"처럼 범위를 좁혀 답변의 정확도를 높이는 식입니다.
- **선택적 채팅 연동**: 채팅 경험에도 이 소스 필터를 붙여, 대화 중에도 원하는 데이터 소스만 참조하도록 조절할 수 있습니다.

## 왜 중요한가요?

- **정확도와 신뢰도**: 소스를 좁히면 Copilot이 참조하는 데이터 풀이 명확해져, 사용자가 답변의 근거를 예측하고 신뢰하기 쉬워집니다.
- **커넥터 투자 가시화**: 애써 연결해 둔 외부 데이터가 실제로 "여기 있고, 이렇게 쓸 수 있다"고 드러나야 활용률이 올라갑니다. 발견성 개선은 커넥터 투자 효과를 직접 끌어올립니다.
- **노이즈 감소**: 모든 소스를 한꺼번에 훑는 대신 필요한 소스만 지정하면, 관련성 낮은 결과가 섞여 드는 상황을 줄일 수 있습니다.

## 활용 시나리오

- **개발팀**: "Jira 커넥터에서만" 특정 릴리스의 미해결 이슈를 요약하도록 범위를 지정합니다.
- **고객지원팀**: ServiceNow 지식 문서 소스만 선택해, 표준 대응 절차 기반으로 답변을 유도합니다.
- **지식 근로자**: 사내 위키 커넥터만 지정해 정책·가이드 문서에 근거한 답변을 얻습니다.

## 도입 체크포인트

- **소스 명명 정비**: 사용자가 필터에서 소스를 골라야 하므로, 커넥터 **연결 이름을 사람이 이해하기 쉽게** 지어 두는 것이 중요합니다. "Connector1" 같은 이름은 발견성을 떨어뜨립니다.
- **권한 검증**: 소스 필터로 특정 데이터에 집중하게 되는 만큼, 항목 수준 권한이 올바르게 트리밍되는지 다시 확인하세요.
- **사용 가이드 준비**: GA(2026년 9월) 전에, 사내 사용자에게 "어떤 소스가 연결돼 있고 언제 어떤 소스를 골라 쓰면 좋은지" 안내하는 간단한 가이드를 준비해 두면 채택이 빨라집니다.
- **파일럿 검증**: 대표 커넥터 몇 개로 필터 UX와 답변 품질을 먼저 확인하고, 소스 구성·이름을 다듬는 것을 권장합니다.

---

## 마무리

Copilot의 가치는 결국 **"어떤 데이터에 근거해 답하는가"** 에서 나옵니다. 아무리 좋은 외부 데이터를 연결해도, 사용자가 그 존재를 모르거나 범위를 조절할 수 없다면 활용도는 제한적입니다. 콘텐츠 소스 필터는 사용자가 데이터의 출처를 **눈으로 확인하고 스스로 선택**하게 함으로써, 커넥터 기반 Copilot 경험을 한 단계 성숙시키는 개선입니다.

여러 커넥터를 운영 중이라면, 지금이 연결 이름과 소스 구성을 정돈하기 좋은 시점입니다.

---

> **출처**: Microsoft 365 Message Center 항목 **RM502541** — *[Copilot Extensibility] Improved discovery of Copilot connector sources in Microsoft 365 Copilot (optionally add chat) with Content Source filter(s)*
> - Message Center 아카이브: [https://mc.merill.net/message/RM502541](https://mc.merill.net/message/RM502541)
> - Microsoft 365 Roadmap: [https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=502541](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=502541)
> - 상태: 개발 중(In development) · GA 예정 2026년 9월 · Worldwide
>
> 위 내용은 Microsoft 365 로드맵/메시지 센터 정보를 바탕으로 정리한 것으로, **실제 출시 일정·기능은 변경될 수 있습니다.**
