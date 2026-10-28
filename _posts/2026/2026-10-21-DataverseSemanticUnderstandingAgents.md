---
title: "Dataverse를 업무 언어로 이해하는 에이전트: 스키마를 넘어 의미 정보를 활용합니다"
date: 2026-10-21T00:00:00 KST
categories:
  - Copilot
tags:
  - Dataverse
  - SemanticUnderstanding
  - PowerApps
  - Agents
excerpt: "Dataverse의 뷰·폼·메타데이터에서 의미 정보를 추출해 에이전트가 업무 데이터를 이해하도록 지원하는 기능이 로드맵에 등록됐습니다. 메이커는 생성된 정보를 확인하고 용어집으로 보완하며, 조직·신호 유형·테이블 수준에서 사용을 제어할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Dataverse를 업무 언어로 이해하는 에이전트: 스키마를 넘어 의미 정보를 활용합니다

데이터베이스의 열 이름을 아는 것과 회사가 그 데이터를 어떤 뜻으로 사용하는지 이해하는 것은 다릅니다. 에이전트가 업무 질문에 답하려면 테이블 구조뿐 아니라 업무 용어와 맥락이 필요합니다.

Microsoft Dataverse의 Roadmap 577185는 **agentic use를 위한 semantic data understanding**을 소개합니다. 이미 환경에 정의된 뷰·폼·메타데이터에서 의미 지식을 추출해 수동 구성을 줄이는 것이 목표입니다.

---

## 기존 앱 구성을 의미 정보의 재료로 활용합니다

원문은 Dataverse 환경의 뷰, 폼과 메타데이터를 자동 활용한다고 설명합니다. 별도 스키마 매핑이나 사용자 지정 쿼리 논리에 의존하는 구성을 줄여, 데이터의 기술적 명칭과 실제 업무 의미 사이의 차이를 좁히려는 방향입니다.

다만 원문의 “수일의 수작업에서 거의 없는 수준으로”라는 설정 노력 감소 표현은 제품이 지향하는 설명입니다. **검증된 도입 소요 시간이나 모든 환경에서 재현되는 성능 수치로 받아들이면 안 됩니다.**

## 메이커가 확인하고 보완할 수 있습니다

Power Apps maker portal에서 엔터티별로 생성된 의미 지식을 확인할 수 있으며, 이름·설명·예시 질문이 포함된다고 안내합니다.

이해가 부족한 부분을 찾아내고, 내장 용어집으로 도메인 전용 용어를 보완하는 것도 핵심입니다. 예를 들어 사내에서만 쓰는 계약 단계나 고객 분류 용어를 설명하는 방식으로 활용할 수 있습니다. 이 예시는 적용 아이디어이며 원문에 제시된 기본 항목은 아닙니다.

## 의미 신호도 거버넌스 대상입니다

원문은 semantic signals를 **조직 수준, 개별 신호 유형 수준, 테이블 수준**에서 활성화하거나 비활성화할 수 있다고 설명합니다. 에이전트 품질뿐 아니라 개인정보와 컴플라이언스 요구를 고려해 참여 범위를 정할 수 있도록 설계한 것입니다.

의미 정보가 추가되어도 데이터 권한이 불필요해지는 것은 아닙니다. 도입 담당자는 어떤 테이블이 참여하는지, 생성된 설명이 실제 업무 의미와 맞는지 함께 검토하는 것이 좋습니다.

## 일정과 현재 상태

수집 시점 로드맵은 **In development**이며, 프리뷰 목표는 **2026년 6월**, GA 목표는 **2026년 11월**입니다. 대상은 Web, Worldwide Standard Multi-Tenant입니다. 이 날짜는 계획이며, 현재 모든 환경의 사용 가능 여부를 확인한 결과는 아닙니다.

## 마무리

이번 기능의 방향은 에이전트마다 데이터 구조를 일일이 설명하는 부담을 줄이고, 이미 운영 중인 업무 앱의 맥락을 재사용하는 것입니다. 메이커에게는 자동 생성된 의미 정보를 검토하고 보완하는 역할이 더 중요해집니다.

> **출처**: [RM577185 — Microsoft Dataverse: Enable semantic data understanding for agentic use](https://mc.merill.net/message/RM577185) · [Microsoft 365 Roadmap 577185](https://www.microsoft.com/microsoft-365/roadmap?id=577185). 실제 출시 일정·기능은 변경될 수 있습니다.
