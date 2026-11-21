---
title: "Copilot Studio 비용을 API로 들여다보기: Copilot Credits Reporting API 공개 프리뷰"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - PowerPlatform
  - CopilotCredits
  - API
  - CostManagement
excerpt: "Copilot Studio의 크레딧 사용량을 Power Platform API로 조회하는 Reporting API가 공개 프리뷰로 제공됩니다. 리소스·환경·사용자·기능별 사용량을 파악하고 크레딧 할당과 함께 운영하는 방법을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 비용을 API로 들여다보기: Copilot Credits Reporting API 공개 프리뷰

에이전트 운영이 늘어나면 “총 크레딧을 얼마나 썼는가”를 넘어 “어느 환경과 기능에서 사용량이 발생했는가”가 중요해집니다. 부서별 활용이 늘어날수록 이 정보를 반복적으로 확인할 방법도 필요합니다.

Microsoft는 MC1558020을 통해 **Copilot Credits Reporting API의 공개 프리뷰**를 알렸습니다. Power Platform API로 Copilot Studio 크레딧 사용량에 접근할 수 있게 하는 기능입니다.

---

## 무엇을 조회할 수 있나요?

새 API 메서드는 다음 구분으로 사용량을 파악할 수 있도록 안내돼 있습니다.

| 조회 관점 | 운영에서 확인할 질문의 예 |
|---|---|
| 리소스 | 어떤 리소스에서 크레딧이 소비되는가? |
| 환경 | 개발·검증·운영 환경 중 어디에 사용량이 집중되는가? |
| 사용자 | 사용자별 사용 패턴이 어떻게 다른가? |
| 기능 | 어떤 기능에서 소비가 발생하는가? |

오른쪽 질문은 활용을 설명하기 위한 예시입니다. 실제 응답 필드, 집계 구간, 조회 조건은 [원문이 연결한 API 사용 안내](https://aka.ms/22552Link1)를 확인해야 합니다.

## 사용량 조회와 크레딧 할당은 구분하세요

이번 보고서는 **읽기 전용**입니다. 조회 API를 호출한다고 크레딧 할당량이나 에이전트 설정이 자동 변경되는 것은 아닙니다.

Microsoft는 이 보고서를 Power Platform API의 [크레딧 할당 기능](https://aka.ms/22552Link2)과 함께 활용할 수 있다고 설명합니다. 운영 흐름으로 풀면 먼저 사용량을 파악하고, 그 결과를 근거로 리소스와 환경의 용량 배분을 검토하는 방식입니다. 조회와 변경을 분리하면 비용 관리 절차의 책임도 더 명확해집니다.

## 도입 전에 확인할 사항

이 공지는 기능 인지를 위한 안내이며 **필수 관리자 작업은 없습니다.** 또한 원문 시점에 공개 프리뷰이므로 정식 공급이 완료된 API로 표현해서는 안 됩니다.

API 연동을 검토하는 개발자와 관리자는 공식 문서에서 인증 방식, 필요한 권한, 엔드포인트, 응답 스키마와 제한을 확인해야 합니다. 이번 메시지 본문에는 해당 세부사항이나 실제 호출 예제가 제시돼 있지 않으므로, 임의의 URL·권한 이름·조회 주기를 전제로 구현하지 않는 것이 중요합니다.

국내 조직에서는 먼저 소규모 환경에서 보고서와 기존 관리 화면의 수치를 비교하고, 집계 기준을 확인한 뒤 내부 비용 대시보드에 연계하는 접근을 권합니다. 이는 도입 제안이지 원문이 보장한 실시간 대시보드 기능은 아닙니다.

## 관련 문서와 마무리

원문은 [GitHub Copilot harness 기반 에이전트 비용 관리](https://aka.ms/22552Link3)와 [Copilot Studio 크레딧 및 용량 관리](https://aka.ms/22552Link4) 문서도 함께 제공합니다.

이번 프리뷰의 가치는 비용 통제 자체를 자동화한다는 데 있지 않습니다. **사용량을 프로그램으로 확인할 수 있는 관측 수단**이 생겼다는 점이 핵심입니다. 보고서 조회, 원인 분석, 할당 검토를 분리해 운영하면 에이전트 확대에 따른 비용을 더 체계적으로 설명할 수 있습니다.

> **출처**: [MC1558020 — Power Platform admin center - Reporting API for Copilot Credits (preview)](https://mc.merill.net/message/MC1558020)
>
> **Microsoft 365 Roadmap**: [공식 로드맵](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 명시되지 않았습니다.
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
