---
title: "여러 테넌트의 에이전트와 AI 비용을 한곳에서: Microsoft 365 멀티테넌트 관리"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - MultiTenant
  - Agent365
  - Governance
  - FinOps
  - Microsoft365
excerpt: "Microsoft 365 관리 센터의 All tenants가 테넌트 전환과 에이전트·설정·AI 비용 관리를 연결합니다. GA인 테넌트 전환과 공개 프리뷰인 관리 기능, GDAP 기반 권한 경계를 구분해 설명합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 여러 테넌트의 에이전트와 AI 비용을 한곳에서: Microsoft 365 멀티테넌트 관리

자회사·지역·사업부별 테넌트를 운영하거나 여러 고객을 지원하는 조직은 같은 설정과 배포를 반복하기 쉽습니다. Copilot과 에이전트가 늘면 사용 허용 범위와 AI 비용까지 관리 대상이 확대됩니다.

Microsoft는 관리 센터의 **All tenants**에서 적격 연결 테넌트를 통합 관리하는 기능을 발표했습니다. 중앙 가시성과 작업을 제공하지만 각 테넌트의 권한 경계를 없애는 것은 아닙니다.

![Microsoft 365 멀티테넌트 관리 원문 대표 화면](/mwkorea/assets/images/2026-11-18-MultiTenantAgentManagement/image1.png)

---

## 테넌트 전환은 GA, 나머지 핵심 기능은 공개 프리뷰

| 기능 | 원문 발표 시점 상태 |
|---|---|
| 로그아웃·재로그인 없는 권한 보유 테넌트 전환 | GA |
| 멀티테넌트 에이전트 관리 | 공개 프리뷰 |
| Desired-state configuration | 공개 프리뷰 |
| 멀티테넌트 AI 비용 관리 | 공개 프리뷰 |

지원 범위는 테넌트 자격, 라이선스, 관리자 역할, 지역, 순차 배포 상태에 따라 달라질 수 있습니다.

## 접근 경계: GDAP와 위임 역할

파트너의 접근은 Partner Center의 **Granular Delegated Admin Privileges(GDAP)** 관계에 의해 관리됩니다. 기업은 **Microsoft Entra Tenant Governance**에서 GDAP 기반 거버넌스 관계를 설정합니다.

이 관계와 위임 역할이 접근 가능한 테넌트와 수행 가능한 작업을 결정합니다. 중앙 화면에 연결했다고 모든 관리 권한이 생기거나 테넌트가 병합되는 것은 아닙니다.

![권한이 있는 테넌트 사이의 전환 관련 원문 화면](/mwkorea/assets/images/2026-11-18-MultiTenantAgentManagement/image2.png)

## 에이전트 배포와 거버넌스를 반복 가능한 작업으로

All tenants에서 지원 에이전트의 교차 테넌트 인벤토리를 보고 승인된 에이전트를 선택한 테넌트에 설치할 수 있습니다. 위임 권한 범위에서 가용성·설정·권한을 관리하고 필요하면 차단할 수 있습니다.

Agent 365를 통해 위험 및 활동 정보를 확인하고, 테넌트별 데이터·도구 접근과 보안 정책·사용량을 비교하는 흐름도 제공됩니다.

![교차 테넌트 에이전트 관리 관련 원문 화면](/mwkorea/assets/images/2026-11-18-MultiTenantAgentManagement/image3.png)

![에이전트별 테넌트 설정과 접근 관련 원문 화면](/mwkorea/assets/images/2026-11-18-MultiTenantAgentManagement/image4.png)

## 원하는 구성과 실제 구성의 차이를 관리

Desired-state configuration은 Microsoft 권장 기준선 또는 지원되는 테넌트 전체 설정으로 만든 사용자 정의 기준선을 적용합니다. 이후 실제 설정이 기준선에서 벗어나는 **구성 드리프트**를 모니터링하고 수정할 수 있습니다.

지역·사업부별 의도된 차이를 고려해 기준선을 설계하는 것이 중요합니다. 모든 차이를 오류로 간주하거나 조직 예외를 없애는 도구로 사용하기보다, 표준과 예외를 명시하는 관리 절차에 연결하는 편이 좋습니다.

![구성 기준선과 드리프트 관리 관련 원문 화면](/mwkorea/assets/images/2026-11-18-MultiTenantAgentManagement/image5.png)

## AI 비용과 지출 정책의 재사용

AI 비용 관리 프리뷰는 지원 테넌트의 소비 정보를 모아서 보고 개별 테넌트로 내려가 분석하도록 합니다. 재사용 가능한 지출 정책 템플릿을 적격 테넌트에 적용해 정책을 매번 다시 만들지 않도록 지원합니다.

지출 정보, 정책 한도, 크레딧 요청을 함께 살펴 고객·사업부별 비용 문제를 일찍 발견하는 것이 목적입니다. 테넌트 간 비용 통합 조회가 청구 계정 병합을 의미하는 것은 아닙니다.

![교차 테넌트 AI 소비와 비용 관리 관련 원문 화면](/mwkorea/assets/images/2026-11-18-MultiTenantAgentManagement/image6.png)

## 시작하기와 공식 데모

먼저 [Microsoft 365 관리 센터](https://admin.cloud.microsoft/)의 All tenants에서 연결 관계와 위임 역할을 확인하세요. 파트너는 Partner Center의 활성 관계를, 기업은 [Tenant Governance 거버넌스 관계](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/governance-relationships)를 점검해야 합니다.

아래는 원문에 포함된 실제 멀티테넌트 관리 데모입니다.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.34%; overflow: hidden;"><iframe src="https://medius.microsoft.com/Embed/video-nc/43dcafae-9c6b-4f3d-8fb2-beb73199aa45?r=1065904920792" title="Multi-Tenant Management" allowfullscreen allow="fullscreen; picture-in-picture" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" sandbox="allow-scripts allow-same-origin allow-forms"></iframe></div>

한국의 그룹사 IT나 MSP에는 반복 작업을 줄일 기회이지만, 첫 적용 범위는 위임 권한과 테넌트별 예외가 명확한 곳으로 좁혀 검증하는 것이 적절합니다.

> **출처**: [Multi-tenant management: Tenants, agents, and AI spend in one place](https://techcommunity.microsoft.com/t5/microsoft-365-blog/multi-tenant-management-tenants-agents-and-ai-spend-in-one-place/ba-p/4573372), TechCommunity Microsoft 365 Blog. 자세한 내용은 원문 참조.
