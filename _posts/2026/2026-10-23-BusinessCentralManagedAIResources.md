---
title: "Business Central Copilot 확장, AI 인프라를 직접 운영하지 않아도 됩니다"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - BusinessCentral
  - AzureOpenAI
  - Copilot
  - Development
excerpt: "Business Central의 Copilot 개발 도구는 Microsoft 관리형 AI 리소스를 기본 경로로 제시합니다. 자체 Azure OpenAI 구독과의 차이, 소비량 청구, 인증 API 변경과 제공 일정을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Business Central Copilot 확장, AI 인프라를 직접 운영하지 않아도 됩니다

ERP에 Copilot 기능을 추가할 때 모델 호출 코드만큼 부담스러운 일이 AI 인프라 운영입니다. 고객마다 Azure OpenAI 구독을 준비하고, 용량과 장애 대응, 청구 체계를 관리해야 하기 때문입니다.

Roadmap RM577820은 **Business Central 개발 도구가 제공하는 Microsoft 관리형 AI 리소스**를 기본·권장 방식으로 설명합니다. 고객과 파트너가 별도 인프라 관리보다 업무 기능 개발에 집중하도록 하는 접근입니다.

---

## 관리형 AI 리소스로 달라지는 것

Microsoft가 관리하는 Azure OpenAI 리소스를 이용하면 업데이트, 모니터링, 유지보수 부담을 줄일 수 있습니다. 원문은 확장, 스로틀링, 부하 분산과 장애 대응을 통한 안정성, 유해 콘텐츠 보호와 데이터 상주 요구사항을 고려한 거버넌스도 장점으로 제시합니다.

고객 입장에서는 여러 ISV의 AI 확장을 사용하더라도 Business Central을 통한 **AI 소비량 추적과 청구 경험을 통합**할 수 있다는 점이 중요합니다. 다만 이것이 무료 사용이나 무제한 사용을 의미하지는 않습니다.

## 자체 구독을 선택해야 하는 경우

관리형 리소스에 없는 특정 모델이나 미세 조정 모델이 필요하면 자체 Azure OpenAI 구독도 사용할 수 있습니다. 이 경우 배포, 유지보수, 확장, 보안과 고객 대상 AI 비용 청구는 게시자 책임입니다.

관리형 AI 소비 과금은 앱 게시자의 기존 Marketplace 수익화 경로를 대체하지 않습니다. 앱의 지식재산 가치에 대한 수익화와 AI 리소스 소비 비용을 구분해 설계해야 합니다.

## 개발자가 확인할 인증 API

원문은 AI Module의 `AzureOpenAI` codeunit에서 관리형 리소스 인증에 `SetManagedResourceAuthorization`을 사용하던 예제를 소개하면서, **2026 release wave 1부터 자체 구독 정보가 필요 없는 새 `SetManagedResources` 시그니처를 사용하라**고 안내합니다.

자체 구독 인증은 `SetAuthorization` 경로입니다. 과거 예제를 그대로 복사하기보다 설치된 Business Central 버전에 맞춰 [AI 리소스 개발 문서](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/ai-dev-tools-resources)의 메서드와 과금 조건을 확인하는 편이 안전합니다.

## 일정과 도입 체크포인트

수집 시점 Roadmap 상태는 **In development**, 표기된 프리뷰 시점은 **2025년 6월**, GA 목표는 **2027년 4월**입니다. 과거 프리뷰 날짜와 향후 GA 목표가 함께 있으므로, 이미 전 고객에게 GA로 제공된 기능으로 해석하면 안 됩니다.

한국 파트너라면 필요한 모델, 데이터 상주 조건, 고객별 비용 배분과 장애 대응 책임을 먼저 비교해 보세요. 관리형 리소스는 운영을 단순화하는 선택이지, 앱 품질 검증과 고객 계약 검토를 생략하는 수단은 아닙니다.

> **출처**: [RM577820 — Business Central Copilot 확장용 AI 리소스](https://mc.merill.net/message/RM577820) · [Microsoft 365 Roadmap 577820](https://www.microsoft.com/microsoft-365/roadmap?id=577820). 실제 출시 일정·기능은 변경될 수 있습니다.
