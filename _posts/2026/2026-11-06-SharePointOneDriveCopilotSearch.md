---
title: "SharePoint와 OneDrive 검색이 바뀝니다: Copilot Search로 통합되는 업무 탐색"
date: 2026-11-06T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotSearch
  - SharePoint
  - OneDrive
  - Frontier
excerpt: "SharePoint Online과 웹용 OneDrive가 자연어 질문, 출처가 있는 AI 요약, 필터를 결합한 검색 경험으로 바뀝니다. Frontier 프리뷰와 일반 공급 일정, 라이선스 차이, 기존 검색 기능 점검 사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# SharePoint와 OneDrive 검색이 바뀝니다: Copilot Search로 통합되는 업무 탐색

파일 이름은 기억나지 않지만 찾고 싶은 내용은 설명할 수 있을 때가 있습니다. SharePoint와 OneDrive의 새 검색 경험은 이런 상황에서 자연어로 질문하고, 관련 결과와 출처가 있는 AI 요약을 함께 살펴보는 방향으로 바뀝니다.

Microsoft의 MC1540513 공지는 두 서비스의 검색 인터페이스를 Microsoft 365 전반의 Copilot Search 경험에 맞추겠다는 내용입니다. 다만 **공통 검색 화면을 제공한다는 것과 모든 AI 기능을 모든 사용자에게 제공한다는 것은 다릅니다.** 일부 AI 기능은 라이선스에 따라 달라집니다.

---

## 무엇이 달라지나요?

새 경험은 자연어 프롬프트, 관련 검색 결과, 출처 참조가 붙은 AI 생성 요약, 필터를 한 흐름에 결합합니다. SharePoint에서 시작하든 웹용 OneDrive에서 시작하든 비슷한 방식으로 콘텐츠를 탐색하도록 인터페이스를 통일합니다.

![SharePoint의 새로운 검색 경험](/mwkorea/assets/images/2026-11-06-SharePointOneDriveCopilotSearch/image1.png)

도입 담당자는 결과 목록을 찾는 기존 사용법뿐 아니라, 요약을 읽고 원문 출처를 확인하는 사용법도 안내하는 것이 좋습니다. AI 요약이 원문 검토 자체를 대체하는 것은 아닙니다.

![웹용 OneDrive의 새로운 검색 경험](/mwkorea/assets/images/2026-11-06-SharePointOneDriveCopilotSearch/image2.png)

## 프리뷰와 일반 공급 일정을 구분하세요

| 구분 | 전 세계 배포 일정 |
|---|---|
| Frontier Preview | 2026년 10월 중순 시작, 2027년 1월 중순 완료 예상 |
| 일반 공급(GA) | 2027년 1월 중순 시작, 2027년 4월 중순 완료 예상 |

이는 공지 시점의 예정입니다. 2026년 11월 현재 모든 조직에 GA가 완료되었다는 의미는 아닙니다.

## 기존 검색 기능을 먼저 점검하세요

대규모 배포 작업은 요구되지 않지만, Microsoft는 사용자 지정 검색 경험과 연동 기능을 테스트하도록 권장합니다. 특히 업무상 필수인 검색 기능이 새 화면에서도 가능한지 확인해야 합니다.

Frontier 프리뷰 기간에는 중요한 검색 기능을 사용할 수 없는 경우 사용자가 새 경험에서 빠져나오는 **옵트아웃**을 제공합니다. 준비 시간이 더 필요한 조직에는 테넌트 및 개별 사이트 수준에서 새 경험을 연기할 수 있는 옵션도 안내되어 있습니다. 구체적인 설정 절차는 공지에 없으며, Microsoft는 GA 전에 새 문서를 제공할 예정이라고 설명합니다.

## 도입 체크포인트

검색 운영팀은 대표적인 검색 업무와 사용자 지정 연동을 목록화하고, 사용자의 라이선스별로 어떤 AI 기능이 나타나는지 비교하는 것이 좋습니다. 헬프데스크에는 프리뷰 옵트아웃과 기존 검색 기능 차이를 안내할 준비가 필요합니다.

이번 변화의 핵심은 검색창의 외형이 아니라 **문서 찾기와 내용 이해를 하나의 경험으로 묶는 것**입니다. 전면 전환에 앞서 실제 업무 검색 시나리오를 기준으로 확인하세요.

> 출처: **MC1540513 — Microsoft SharePoint Online and OneDrive for the web: Updated search experience with Copilot Search**  
> [Message Center 원문](https://mc.merill.net/message/MC1540513) · [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)  
> 공지에 개별 Roadmap ID는 명시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
