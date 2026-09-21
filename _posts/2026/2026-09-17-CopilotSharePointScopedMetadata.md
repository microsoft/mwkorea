---
title: "SharePoint 라이브러리의 열 정보까지 활용: Copilot 범위 지정 질문 개선"
date: 2026-09-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - SharePoint
  - Metadata
  - Grounding
  - Roadmap
excerpt: "Microsoft 365 Copilot이 SharePoint 라이브러리나 폴더를 첨부하거나 URL로 지정한 질문에서 열 메타데이터를 활용하도록 개선됩니다. 선택한 자료의 맥락을 더 잘 반영하는 기능으로, 원문에 남아 있는 GA 표기는 2025년 11월입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# SharePoint 라이브러리의 열 정보까지 활용: Copilot 범위 지정 질문 개선

SharePoint의 문서 라이브러리에는 파일 내용 외에도 분류나 상태를 담는 열이 있습니다. 이런 정보도 질문의 맥락에 포함된다면 자료를 해석하는 데 도움이 됩니다.

로드맵 **516044**, 수집 ID **RM516044**는 SharePoint 라이브러리 또는 폴더를 첨부하거나 URL로 지정한 경우, Microsoft 365 Copilot이 **열 메타데이터**를 활용하도록 지원한다고 설명합니다.

---

## 질문 범위를 지정했을 때의 변화

원문은 선택한 라이브러리의 추가 메타데이터를 활용해 응답의 관련성을 높이는 데 초점을 둡니다. 사용자가 라이브러리나 폴더를 첨부하거나 그 URL을 제공하는 것이 설명된 사용 방식입니다.

| 구분 | 원문이 설명한 범위 |
|---|---|
| 대상 | SharePoint 문서 라이브러리·폴더를 지정한 질문 |
| 지정 방법 | 첨부 또는 URL 제공 |
| 추가 맥락 | 선택한 라이브러리의 열 메타데이터 |

모든 SharePoint 열 형식이나 복잡한 필터 연산을 지원한다는 뜻으로 확대해석해서는 안 됩니다. 지원 열 형식, 인덱싱 요건, 상세한 질문 예시는 이 짧은 항목에 없습니다.

## 도입 담당자가 살펴볼 점

기능을 평가할 때는 팀이 실제로 사용하는 열과 값이 정리되어 있는지 먼저 살펴볼 만합니다. 자료 분류가 제각각이거나 오래된 상태 값이 남아 있다면 그 맥락도 검토해야 합니다.

이는 메타데이터 활용에 따른 운영 권고이며, 이 기능이 열을 자동으로 정비하거나 파일 권한을 변경한다는 발표는 아닙니다.

## 수집일과 출시일 구분

원문의 **GA 날짜는 2025년 11월**로 표기되어 있습니다. 이번에 처음 수집한 항목이지만 2026년 9월 신규 출시를 뜻하지 않습니다. 실제 조직의 제공 상태와 적용 범위는 별도 확인이 필요합니다.

문서의 본문뿐 아니라 조직이 붙인 정보도 업무 맥락의 일부입니다. 라이브러리의 열이 잘 관리되는 경우, 범위를 지정한 Copilot 질문을 평가할 때 함께 살펴볼 변화입니다.

---

> **출처**
>
> - 원문 ID: **RM516044** — *Microsoft Copilot (Microsoft 365): Metadata understanding support for queries scoped to SharePoint document libraries or folders*
> - 원문: [RM516044](https://mc.merill.net/message/RM516044)
> - [Microsoft 365 Roadmap 516044](https://www.microsoft.com/microsoft-365/roadmap?id=516044)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
