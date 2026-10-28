---
title: "영수증 양식도 자연어로: Copilot Cowork와 Commerce Receipt designer"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCowork
  - Dynamics365Commerce
  - ReceiptDesigner
  - Agent
excerpt: "Copilot Cowork에서 Commerce 영수증 양식을 생성·수정·번역·검사하는 스킬이 예고되었습니다. 구조 검사와 실제 출력·바코드·법적 검증의 차이, 권한과 원본 보존 조건을 짚습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 영수증 양식도 자연어로: Copilot Cowork와 Commerce Receipt designer

매장 영수증은 짧지만 바꾸기 까다로운 양식입니다. 문구 번역, 필드 위치와 폭, 바코드와 필수 표시 사항이 얽혀 있어 작은 수정도 실제 출력 확인이 필요합니다.

Roadmap RM577405는 **Copilot Cowork의 Commerce receipt format designer 스킬**을 소개합니다. Dynamics 365 Commerce headquarters의 설정을 바탕으로 Store Commerce POS용 영수증 양식을 다룹니다.

---

## 생성·수정·번역을 자연어로

사용자는 현대적인 Receipt designer의 구조화된 표현을 가진 기존 양식에서 출발해 새 형식을 만들거나 기존 대상을 수정할 수 있습니다. 헤더·상세 행·푸터 내용, 필드 위치와 정렬, 지원되는 서식을 바꿀 수 있습니다.

정적 레이블을 번역하거나 사용자 제공 문구를 추가할 때 동적 필드는 보존합니다. 누락된 업무 정보는 임의로 만들어 넣지 않고 식별하는 방향으로 설명됩니다.

## 변경하지 않고 검사할 수도 있습니다

구조·배치 검사로 겹침, 폭 위반과 잘림 위험을 찾아 수정 방향을 받을 수 있습니다. 저장 후에는 구성을 다시 읽어 요청한 변경이 반영됐는지 확인합니다.

원본에서 새 양식을 생성하는 경우 원본은 보존됩니다. 작업 전에 원본과 대상이 모호하면 사용자가 이를 해소하고 결과를 검토해야 합니다.

## 자동 검사가 보장하지 않는 것

**구조 검사는 실제 외관, 바코드 스캔 가능 여부, 실행 시 값, 법적·세무적 적합성을 보장하지 않습니다.** Receipt designer에서 레이아웃을 확인하고 실제 운영 전 적절한 테스트 인쇄를 해야 합니다.

영수증 프로필이나 프린터에 양식을 연결하는 일, 거래를 인쇄·재인쇄하는 일은 별도의 설정·운영 흐름입니다. 양식을 만들었다고 POS 배포와 출력 검증까지 끝나는 것은 아닙니다.

## 권한과 제공 일정

권한이 있는 Copilot Cowork 사용자에게 스킬이 자동 제공되는 방향이며, Commerce 관리자는 headquarters 접근 권한과 원본의 현대적 구조 표현을 준비해야 합니다.

수집 시점은 **In development**, 프리뷰 **2026년 10월**, GA 목표 **2026년 12월**입니다. 한국 리테일 조직이라면 번역 편의성뿐 아니라 국내 영수증 필수 항목과 실제 장비 출력 검증을 함께 준비해야 합니다.

> **출처**: [RM577405 — Commerce receipt formats with Copilot Cowork](https://mc.merill.net/message/RM577405) · [Microsoft 365 Roadmap 577405](https://www.microsoft.com/microsoft-365/roadmap?id=577405). 실제 출시 일정·기능은 변경될 수 있습니다.
