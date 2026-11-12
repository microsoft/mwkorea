---
title: "Copilot 답변의 근거를 직접 고른다: 콘텐츠 소스 필터로 검색 범위 좁히기"
date: 2026-11-11T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotChat
  - GraphConnectors
  - Grounding
excerpt: "Microsoft 365 Copilot Chat에서 프롬프트마다 답변의 근거가 될 콘텐츠 소스를 선택할 수 있게 됩니다. 필터의 적용 범위와 권한 경계, 커넥터 운영자가 준비할 사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 답변의 근거를 직접 고른다: 콘텐츠 소스 필터로 검색 범위 좁히기

회사 문서와 외부 업무 시스템이 Copilot에 연결되면 질문할 수 있는 범위는 넓어집니다. 반대로 이번 답변은 특정 시스템의 정보만 근거로 삼았으면 하는 순간도 생깁니다.

MC1548004는 Microsoft 365 Copilot Chat의 **콘텐츠 소스 필터**를 소개합니다. 사용자가 프롬프트에 사용할 소스를 선택하면 Copilot은 선택한 소스에서 정보를 검색하고 답변의 근거를 구성합니다.

---

## 프롬프트에서 하나 이상의 소스를 선택

Copilot Chat 입력 영역에 소스 선택 컨트롤이 나타납니다. 사용자는 제공되는 콘텐츠 소스 중 하나 이상을 선택해 해당 질문의 검색·그라운딩 범위를 제한할 수 있습니다.

![Copilot Chat의 콘텐츠 소스 선택 메뉴](/mwkorea/assets/images/2026-11-11-CopilotChatContentSourceFilters/image1.png)

표시되는 소스는 테넌트에서 활성화되어 사용자에게 제공되는 소스에 따라 달라집니다. 원문은 **Graph connectors와 federated connectors**를 포함한 Microsoft 365 및 외부 콘텐츠 소스를 설명합니다.

예를 들어 특정 업무 시스템만 근거로 현황을 확인하려는 경우, 해당 소스가 실제 선택 목록에 제공된다면 이를 선택해 질문의 범위를 좁힐 수 있습니다. 이는 활용 예시이며 모든 테넌트에 동일한 시스템이 기본 제공된다는 뜻은 아닙니다.

## 필터는 접근 권한을 바꾸지 않습니다

소스 선택은 **어디서 찾을지**를 정하는 기능이지 **무엇에 접근할 수 있는지**를 확장하는 기능이 아닙니다. 기존 데이터 접근 권한, 컴플라이언스 경계, 테넌트 데이터 처리 방식은 유지됩니다.

| 상황 | 동작 |
|---|---|
| 소스 선택 | 현재 프롬프트의 검색·그라운딩을 선택 소스로 제한 |
| 소스를 선택하지 않음 | 기존 기본 오케스트레이션으로 사용 가능한 소스 활용 |
| 답변의 출처 표시 | 선택한 소스를 반영한 인용 제공 |
| 다음 세션 | 소스 선택이 세션 간 유지되지 않음 |

원문은 소스 선택이 **현재 프롬프트에만 적용**된다고 명시합니다. 한 번 선택하면 이후 모든 질문의 기본값이 된다고 가정하지 말고, 질문별 선택 상태를 확인하는 것이 좋습니다.

## 대상과 일정

대상은 **Microsoft 365 Copilot 라이선스가 있는 사용자**입니다. 기능은 기본 활성화되며 별도의 필수 관리자 조치는 없습니다.

전 세계 일반 공급(GA)은 **2026년 11월 중순 시작 및 완료 예정**으로 안내되어 있습니다. 공개 공지의 플랫폼 표기는 Web입니다. 다른 클라이언트까지 동일한 시점에 제공된다고 확대 해석하지 않는 편이 안전합니다.

이 글의 날짜는 피드 발행 시각인 2026년 11월 10일 23:58:34 UTC를 한국 표준시로 환산한 11월 11일 기준입니다.

## 커넥터 운영자가 점검할 두 가지

첫째, 게시된 Graph 커넥터의 **표시 이름을 사용자가 알아보기 쉽게 정리**하세요. 이 이름이 소스 선택 경험에 표시됩니다.

둘째, **커넥터 상태와 검색 권한**을 점검하세요. 오류 상태이거나 게시되지 않은 커넥터는 목록에 나타나지 않습니다. 사용자가 소스를 찾지 못할 때 단순한 화면 문제로 보기 전에 게시 상태와 접근 권한을 확인해야 합니다.

사용 방법은 [Copilot Chat 응답의 소스 제어 및 검토](https://support.microsoft.com/microsoft-365-copilot/control-review-sources-copilot-chat)에서 확인할 수 있습니다.

## 마무리

이번 업데이트는 연결된 데이터가 많아질수록 중요해지는 질문을 해결합니다. “Copilot이 무엇을 참고했는가”를 답변 뒤에만 확인하는 대신, 질문할 때부터 필요한 콘텐츠 범위를 직접 지정할 수 있습니다.

> 출처: [MC1548004 — Microsoft 365 Copilot Chat: Filter responses by content source](https://mc.merill.net/message/MC1548004)  
> [Microsoft 365 Roadmap 502541](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&searchterms=502541)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
