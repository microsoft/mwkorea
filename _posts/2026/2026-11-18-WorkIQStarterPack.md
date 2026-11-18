---
title: "빈 데모 테넌트를 살아 있는 업무 공간으로: Work IQ Starter Pack"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - CopilotStudio
  - CopilotCowork
  - Dynamics365
  - Developer
excerpt: "Work IQ Starter Pack은 가상의 회사 데이터로 Microsoft 365와 Dynamics 365 데모 환경을 구성하는 오픈 소스 프로젝트입니다. 선택 가능한 콘텐츠 팩과 네 가지 실습, 운영 테넌트 사용 금지 및 필수 권한을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 빈 데모 테넌트를 살아 있는 업무 공간으로: Work IQ Starter Pack

Copilot 데모를 준비하다 보면 기능보다 데이터가 먼저 막힙니다. 요약할 이메일, 회의 대화 기록, 에이전트가 추론할 문서와 업무 레코드가 없으면 실제 업무처럼 연결된 장면을 보여 주기 어렵습니다.

Microsoft가 공개한 **Starter Pack for Work IQ**는 데모·개발 테넌트에 일관된 가상 사용자와 콘텐츠를 배포하는 PowerShell 스크립트 모음입니다. 실제 고객 자료를 쓰지 않고도 Copilot Chat·Cowork·Copilot Studio에서 조직 지식과 업무 데이터를 연결하는 흐름을 실습할 수 있습니다.

---

## 하나의 가상 회사를 여러 서비스에 구성

데이터는 가상의 제약회사 **Caldova Pharmaceuticals**를 중심으로 연결됩니다. Exchange Online, SharePoint Online, Teams, Dynamics 365 Sales·Customer Service·Finance and Operations에서 같은 제품·공급업체·고객·사람을 참조합니다.

| 역할 | 가상 사용자 | 직책 |
|---|---|---|
| 마케팅 | Serena Ribeiro | Market Research Analyst |
| 재무 | Babak Shammas | Financial Reconciliation Lead |
| 보안·거버넌스 | Cassandra Dunn | Compliance Manager |
| 재무·구매 | Charlotte Waltson | VP Procurement |
| 영업 | David Power | Sales Director |

기존 데모 사용자를 이 다섯 역할에 매핑할 수도 있습니다. 설치 프로그램은 Entra ID에서 사용자를 찾아 콘텐츠의 이름과 이메일 주소를 바꿉니다.

![가상 제품 ALLER의 출시 일정에 관한 이메일 예시](/mwkorea/assets/images/2026-11-18-WorkIQStarterPack/image1.webp)

## 필요한 콘텐츠 팩만 선택

설치 스크립트 하나와 정리 스크립트 하나가 Microsoft 365 및 Dynamics 365 콘텐츠를 처리합니다. 최소 한 팩을 선택해야 하지만 Dynamics 팩만 독립적으로 설치할 수도 있습니다.

**Microsoft 365 팩**은 PnP PowerShell과 Microsoft Graph를 사용해 Teams 팀·채널·대화·회의 기록, 사용자 사서함 이메일, SharePoint 파일·목록 항목을 구성합니다.

![연결된 가상 업무 맥락을 보여 주는 Teams 대화](/mwkorea/assets/images/2026-11-18-WorkIQStarterPack/image2.webp)

**Sales 및 Customer Service 팩**은 Caldova Field Engagement 관리형 솔루션과 사용자 정의 Power App을 배포합니다. Dataverse에는 잠재 고객, 거래처·연락처, 가격표·제품, 영업 기회, 견적·주문·송장, 사례, 이메일, Field Engagement 레코드가 생성됩니다. 거래처에 연결된 SharePoint 문서는 선택 사항입니다.

**Finance and Operations 팩**은 기존 F&O 환경에 데모 고객, 출시 제품, 판매 주문을 만듭니다. 다른 팩과 독립적으로 선택할 수 있으며, F&O 환경 자체를 새로 제공한다는 뜻은 아닙니다.

![Finance and Operations의 가상 제품 데이터 예시](/mwkorea/assets/images/2026-11-18-WorkIQStarterPack/image3.webp)

## 네 가지 독립 실습

각 실습에는 시나리오, 전제조건, 안내형 단계, 결과 확인 항목이 있으며 원하는 실습부터 시작할 수 있습니다.

| 실습 | 구현 내용 | 예상 시간 |
|---|---|---|
| 1. 조직 지식 탐색 | Copilot Chat으로 ALLER 출시 준비 브리핑 작성. 이메일·Teams·문서·회의 기록을 출처와 함께 통합하며 별도 에이전트 불필요 | 15~20분 |
| 2. 지능형 조사 | Copilot Studio 오케스트레이터가 Work IQ MCP로 근거를 검색하고 게시·연결된 전문 에이전트 2개를 조율해 공급업체 송장 이의 검토 패킷 초안 생성 | 90~120분 |
| 3. 인사이트에서 실행으로 | Cowork 사용자 정의 스킬로 공급업체를 조사하고 사용자 확인 후 역량 검토 회의 생성 | 60~75분 |
| 4. 업무 데이터 통합 | Copilot Studio의 읽기 전용 에이전트로 고객 Meridian Health Alliance의 영업·서비스·Field Engagement·M365 및 선택적 F&O 맥락 통합 | 60~90분 |

실습 1~3은 Microsoft 365 콘텐츠 팩이 필요합니다. 실습 4는 Dynamics 365 콘텐츠도 필요하며 F&O 부분에는 해당 팩이 추가로 필요합니다. 실습 4의 **Work IQ Business apps는 원문 시점 프리뷰**입니다.

## 운영 테넌트에는 절대 설치하지 마세요

이 프로젝트는 **데모·개발 테넌트 전용**입니다. 설치에는 Global Administrator 계정이 필요하고, 데모 사용자에게 Office와 Copilot 라이선스를 할당합니다.

사용자·팀·SharePoint 사이트 생성, 사서함에 이메일 직접 기록, Teams 채널 메시지 가져오기, 문서 업로드, Dynamics 365 업무 데이터 쓰기가 수행될 수 있습니다. 실제 업무가 있는 운영 테넌트에서 시험할 도구가 아닙니다.

인물·회사·제품·문서·대화·업무 레코드는 모두 허구입니다. 의료·재무·규제·상업적 의사결정의 근거로 사용해서는 안 됩니다.

## 시작하기와 공식 데모

[Work-IQ-Starter-Pack GitHub 저장소](https://github.com/microsoft/Work-IQ-Starter-Pack)에서 현재 설치 전제조건과 안내를 확인한 뒤 격리된 데모 환경에 필요한 팩을 배포하세요. 한국 조직의 메이커 교육에서는 공통 데이터와 결과 확인 항목을 활용해 교육생마다 다른 업무 자료를 준비하는 부담을 줄일 수 있습니다.

{% include video id="HdAQtYuHz7Q" provider="youtube" %}

이 글은 원문 발표 내용을 정리한 것이며, 후속 버전의 설치 요구사항이나 지원 범위가 그대로라는 의미는 아닙니다.

> **출처**: [Introducing the Starter Pack for Work IQ](https://devblogs.microsoft.com/microsoft365dev/introducing-the-starter-pack-for-work-iq/), Microsoft 365 Developer Blog. 자세한 내용은 원문 참조.
