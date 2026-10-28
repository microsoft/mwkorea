---
title: "CRM의 업무 언어를 이해하는 Sales Agent: semantic model의 역할"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - SalesAgent
  - SemanticModel
  - Dataverse
  - Salesforce
  - Copilot
excerpt: "Sales Agent의 semantic model은 CRM 테이블·필드·관계와 용어를 연결해 복잡한 업무 질문의 맥락을 보강합니다. Dynamics 365와 Salesforce 관리자의 구성 경로, 프리뷰·GA 일정을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# CRM의 업무 언어를 이해하는 Sales Agent: semantic model의 역할

사람은 “주요 거래처의 진행 중인 기회”라는 말을 자연스럽게 이해하지만, CRM에서는 여러 테이블과 필드·관계를 연결해야 답할 수 있습니다. 조직별 용어가 다르면 더 어려워집니다.

Roadmap RM573294는 **Sales Agent가 CRM의 구조와 의미를 이해하도록 돕는 semantic model**을 소개합니다. 답변 때 참조할 메타데이터 맥락을 연결하는 기능입니다.

---

## 어떤 정보를 연결하나요?

모델은 CRM 테이블·객체, 필드와 설명, 데이터 형식, 관계, 뷰, 선택 목록 값과 용어집을 연결해 표현합니다. Sales Agent는 질문에 답할 때 이 맥락을 검색할 수 있습니다.

목표는 업무 용어를 더 잘 해석하고, 서로 관련된 CRM 레코드에 걸친 복잡한 질문을 이해하도록 돕는 것입니다. 잘못된 메타데이터를 자동으로 모두 수정한다는 설명은 아닙니다.

## Dynamics 365 관리자의 구성

원문은 **Power Apps Maker Portal**에서 semantic model을 활성화하고 Sales Agent가 사용할 데이터 범위와 신호를 구성한다고 설명합니다. 기반 데이터, 뷰, 메타데이터와 관계를 설정할 수 있습니다.

따라서 테이블·필드 설명과 관계 정의가 실제 업무 의미를 반영하는지 점검하는 일이 중요합니다.

## Salesforce는 어떻게 다른가요?

Salesforce 고객의 모델은 기존 Sales agent 설정 또는 Power Apps Maker Portal의 **테이블·용어집 구성**을 바탕으로 합니다. Salesforce 관리자는 Maker Portal에서 관계와 뷰 같은 추가 Salesforce 신호를 구성할 수 있다고 안내합니다.

두 CRM의 설정 경로가 완전히 같다고 단순화하지 말고 현재 연결 방식과 데이터 범위를 확인해야 합니다.

## 도입 체크포인트와 일정

[semantic model 개요](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/semantic-model-overview)를 바탕으로 용어집, 관계와 뷰를 검토하고, 여러 테이블을 연결하는 대표 질문으로 답변을 비교해 보세요. 접근 권한과 데이터 품질 검토는 별도로 유지해야 합니다.

수집 시점 상태는 **In development**, 프리뷰 **2026년 10월**, GA 목표 **2026년 11월**입니다. 모델이 문맥 이해를 돕더라도 모든 답변이 정확해진다는 보장은 아닙니다.

> **출처**: [RM573294 — Sales agent semantic model](https://mc.merill.net/message/RM573294) · [Microsoft 365 Roadmap 573294](https://www.microsoft.com/microsoft-365/roadmap?id=573294). 실제 출시 일정·기능은 변경될 수 있습니다.
