---
title: "검색 결과가 달라진다: Copilot 커넥터 콘텐츠의 '리치 엔티티' 표현"
date: 2026-07-24T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotConnectors
  - GraphConnectors
  - Search
  - Extensibility
  - Roadmap
excerpt: "ServiceNow, Jira 같은 외부 시스템을 연결하는 Copilot 커넥터의 검색 결과가 단순 링크에서 벗어나, 핵심 필드를 담은 '리치 엔티티' 카드로 표현됩니다. 2026년 9월 GA 예정인 이 변화가 사내 검색·Copilot 경험을 어떻게 바꾸는지 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 검색 결과가 달라진다: Copilot 커넥터 콘텐츠의 '리치 엔티티' 표현

사내 데이터를 Microsoft 365 Copilot과 Microsoft Search로 끌어오는 통로가 바로 **Copilot 커넥터(구 Microsoft Graph 커넥터)** 입니다. ServiceNow 티켓, Jira 이슈, Confluence 문서, 사내 위키처럼 SharePoint 밖에 흩어진 데이터를 색인해, 사용자가 한곳에서 검색하고 Copilot이 답변의 근거로 활용하도록 해 줍니다.

그런데 지금까지 커넥터로 들어온 결과는 대체로 **제목과 링크 위주의 밋밋한 형태**로 표시되는 경우가 많았습니다. 이번 로드맵 항목(RM502533)은 이 지점을 개선합니다. 커넥터 콘텐츠가 검색 결과에서 **리치 엔티티(rich entity)** 형태, 즉 핵심 속성을 담은 구조화된 카드로 표현되도록 하는 변화입니다.

이 기능은 현재 **개발 중(In development)** 상태이며, **전 세계(Worldwide) 대상 2026년 9월 GA(정식 출시)** 를 목표로 하고 있습니다.

---

## 무엇이 달라지나요?

핵심은 "링크 한 줄"에서 "정보가 담긴 카드"로의 전환입니다.

- 기존: 커넥터 결과가 제목·URL 중심의 단순 링크로 노출
- 변경: 항목의 **주요 필드와 메타데이터**(예: 상태, 담당자, 우선순위, 갱신일 등)를 함께 보여주는 **리치 엔티티 표현**

즉, ServiceNow 인시던트를 검색했을 때 티켓 번호·상태·우선순위 같은 핵심 정보가 결과 화면에서 바로 보이고, Jira 이슈라면 이슈 키·담당자·상태가 한눈에 드러나는 식입니다. 사용자는 링크를 열어 보기 전에 그 항목이 내가 찾던 것인지 **더 빠르게 판단**할 수 있습니다.

## 왜 중요한가요?

- **탐색 시간 단축**: 결과 카드에서 핵심 정보를 바로 확인하므로, 원본을 일일이 클릭해 확인하는 수고가 줄어듭니다.
- **Copilot 답변 품질과 연결**: 커넥터 콘텐츠가 구조화되어 표현될수록, 사용자가 근거 자료를 신뢰하고 활용하기 쉬워집니다. 검색 UX 개선은 결국 Copilot이 인용하는 외부 데이터의 **가시성과 신뢰도**를 높이는 방향입니다.
- **일관된 검색 경험**: SharePoint·Exchange 등 1차 데이터와 외부 커넥터 데이터가 시각적으로 더 균질하게 표현되어, 사용자가 출처를 가리지 않고 통합 검색을 활용하게 됩니다.

## 활용 시나리오

- **IT 서비스데스크**: 직원이 사내 검색에서 인시던트 번호를 입력하면, 티켓 상태·우선순위가 담긴 카드가 바로 표시되어 현황 파악이 빨라집니다.
- **개발/프로젝트 팀**: Jira·Azure DevOps 이슈를 검색할 때 담당자·상태를 카드에서 확인해 컨텍스트 전환 없이 흐름을 유지합니다.
- **지식 관리**: 사내 위키·문서 커넥터 결과가 요약 필드와 함께 노출되어, 최신 문서를 골라내기 쉬워집니다.

## 도입 체크포인트

- **커넥터 구성 점검**: 리치 엔티티 표현의 품질은 커넥터가 색인한 **속성(스키마)과 매핑 품질**에 크게 좌우됩니다. 어떤 필드를 검색·표시 가능하도록 설정했는지 미리 정비해 두세요.
- **의미 레이블(semantic labels)**: 제목, 작성자, 날짜, URL 등 표준 속성을 커넥터의 의미 레이블에 정확히 매핑해 두면 리치 표현의 효과가 커집니다.
- **권한 트리밍 확인**: 외부 데이터가 더 눈에 잘 띄게 표시되는 만큼, 항목 수준 접근 권한(ACL)이 올바르게 반영되는지 반드시 검증하세요.
- **단계적 롤아웃**: GA가 2026년 9월로 예정된 만큼, 그 전에 파일럿 커넥터로 표현 결과를 확인하고 사내 검색 가이드를 업데이트하기에 좋은 시점입니다.

---

## 마무리

이번 변화는 화려한 신기능이라기보다, **외부 데이터를 사내 검색과 Copilot에 제대로 녹여내는 기반을 다지는** 개선에 가깝습니다. 커넥터로 아무리 많은 데이터를 끌어와도 결과가 밋밋하면 사용자가 외면하기 마련입니다. 리치 엔티티 표현은 그 "마지막 1미터"를 좁혀, 커넥터 투자 대비 체감 가치를 끌어올리는 방향입니다.

커넥터를 이미 운영 중이라면 지금이 스키마와 속성 매핑을 재점검할 타이밍입니다.

---

> **출처**: Microsoft 365 Message Center 항목 **RM502533** — *[Copilot Extensibility][Search UX] Rich entity representation for connectors in Search results*
> - Message Center 아카이브: [https://mc.merill.net/message/RM502533](https://mc.merill.net/message/RM502533)
> - Microsoft 365 Roadmap: [https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=502533](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=502533)
> - 상태: 개발 중(In development) · GA 예정 2026년 9월 · Worldwide
>
> 위 내용은 Microsoft 365 로드맵/메시지 센터 정보를 바탕으로 정리한 것으로, **실제 출시 일정·기능은 변경될 수 있습니다.**
