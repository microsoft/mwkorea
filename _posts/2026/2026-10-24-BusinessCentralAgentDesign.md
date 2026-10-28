---
title: "Business Central 안에서 AI 에이전트 설계하기: 권한·승인·실행 추적이 먼저입니다"
date: 2026-10-24T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365BusinessCentral
  - AIDevelopmentToolkit
  - Agent
  - Governance
excerpt: "Business Central의 AI Development Toolkit은 자연어 지시로 업무 에이전트를 설계하고 샌드박스에서 시험하는 경험을 제공합니다. 권한 경계, 민감 작업 검토, 진단 로그와 Copilot 크레딧 과금, 그리고 아직 기본 제공되지 않는 자동 트리거의 한계까지 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Business Central 안에서 AI 에이전트 설계하기: 권한·승인·실행 추적이 먼저입니다

ERP의 에이전트는 답변만 잘해서는 부족합니다. 주문과 매입처럼 재무적 영향을 갖는 업무에서 여러 단계를 정확히 수행하고, 회사·환경·테넌트 경계를 지키며, 필요한 순간에는 사람의 판단을 요청해야 합니다.

RM578068은 **AI Development Toolkit for Business Central을 이용한 제품 내 에이전트 설계 경험**을 설명합니다. 원문에는 공개 미리 보기의 제약과 향후 연계 방향도 함께 적혀 있어, 현재 가능한 일과 미래 계획을 구분해서 읽어야 합니다.

---

## 내장 에이전트와 같은 실행 기반

Business Central은 Sales Order Agent와 Payables Agent 같은 내장 에이전트를 제공합니다. 전자는 자연어나 이메일 지시를 판매 문서로 바꾸고, 후자는 청구서 정보를 추출하고 구매 주문과 대조하는 업무를 돕습니다.

사용자 정의 에이전트 설계 경험은 이러한 **agent runtime의 기능을 확장해 활용**합니다. 에이전트 정의·설정·활성화·실행을 익숙한 Business Central 환경에서 수행하며 기존 보안 모델과 관리 도구를 사용합니다.

## 권한과 사람의 검토는 실행 설계의 일부

런타임은 설정 시 할당된 권한 안에서 작동하며 활동을 타임라인으로 추적할 수 있게 합니다. 실행 중 필요한 데이터를 기억해 후속 단계에서 사용하거나, 정보가 부족하면 자연어로 추가 지시를 요청할 수 있습니다.

원문은 민감한 작업에 명시적 사용자 검토와 동의가 필요하도록 하는 투명성과 통제를 강조합니다. 에이전트를 만들었다고 재무 업무를 무제한 자율 처리할 수 있다는 의미가 아닙니다.

## 샌드박스에서 설계하고 수동 작업으로 호출

설계 경험은 컨설턴트·제품 담당자·도메인 전문가·개발자·파워 사용자 등이 샌드박스에서 아이디어를 시험하도록 구성됩니다.

1. 자연어로 목표와 지시를 작성하고 다듬습니다.
2. 에이전트 프로필과 권한을 정의하고 시험합니다.
3. 수동으로 작업을 생성하고 추가 맥락 메시지를 전달합니다.
4. 실행 로그의 입력·판단 과정·출력을 검토해 지시를 개선합니다.

**중요한 제한:** 원문이 설명하는 공개 미리 보기에서는 사용자 정의 에이전트를 이메일 수신·이벤트·주기 일정으로 자동 호출하는 기본 통합이 아직 없습니다. 전문 개발자는 Toolkit API로 구현할 수 있지만, 기본 경험에서는 이메일 헤더와 본문을 작업 메시지에 넣거나 수동 호출로 시뮬레이션합니다.

## 정의 파일을 소스 관리하고 비용도 검증

에이전트 정의는 ID, 지시, 프로필, 권한 등을 담은 **JSON 파일로 가져오기·내보내기**할 수 있어 샌드박스 간 이동과 백업에 활용됩니다. 원문은 GitHub 같은 소스 관리 시스템에 저장해 변경 이력을 관리하도록 권장합니다.

사용자 정의 에이전트도 실행 단계에서 **Copilot 크레딧을 소비**합니다. 선불과 종량제 방식이 안내되어 있으며, 자연어로 쉽게 만들 수 있다는 점을 무료 실행으로 해석해서는 안 됩니다.

## MCP와 Copilot Studio 연계는 미래 방향

원문은 ERP 내부의 통제된 실행과 제품 간 상위 오케스트레이션을 의도적으로 분리한다고 설명합니다. Business Central 에이전트 역량을 향후 MCP 도구로 노출하고 Copilot Studio·Microsoft 365의 Declarative Agent에서 소비할 수 있도록 하는 방향입니다.

이는 **향후 가능성에 대한 설명**이므로 이 로드맵 항목만으로 해당 연계가 이미 일반 공급됐다고 단정할 수 없습니다.

## 일정 필드와 미리 보기 설명을 구분하세요

수집 원문은 상태가 **In development**, Preview가 **2026년 2월**, GA가 **2026년 10월**로 표시되어 있고, 본문은 설계 경험을 공개 미리 보기로 설명합니다. 날짜 필드와 본문의 표현이 일치하지 않는 부분이 있으므로 실제 도입 시 [AI Development Toolkit 문서](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/ai/ai-development-toolkit-overview)와 사용 환경의 제공 상태를 확인해야 합니다.

## 마무리

Business Central 에이전트의 핵심은 자연어 지시만이 아니라 ERP 안에서의 통제된 실행입니다. 샌드박스 검증, 최소 권한, 민감 작업 검토, JSON 버전 관리와 크레딧 측정을 함께 설계하는 것이 현실적인 출발점입니다.

> **출처**: 원문 ID [RM578068](https://mc.merill.net/message/RM578068) · [Microsoft 365 Roadmap 578068](https://www.microsoft.com/microsoft-365/roadmap?id=578068)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
