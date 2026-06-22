---
title: "Copilot 크레딧, 누가 얼마나 쓰고 있을까? Viva Insights에 'AI 지출·사용' 분석이 들어옵니다"
date: 2026-06-20T00:00:00 KST
categories:
  - Copilot
tags:
  - VivaInsights
  - CopilotAnalytics
  - Cowork
  - WorkIQ
  - AISpend
  - CopilotCredit
  - Governance
excerpt: "팀·그룹 단위로 Copilot 크레딧(AI 지출) 사용량을 볼 수 있는 분석 기능이 Viva Insights에 추가됩니다. 이번 릴리스의 대상 서비스는 Cowork와 Work IQ API이며, 2026년 6월 GA 예정입니다. 누가 볼 수 있고, 어떤 전제 조건이 필요한지 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 크레딧, 누가 얼마나 쓰고 있을까? Viva Insights에 'AI 지출·사용' 분석이 들어옵니다

Copilot과 에이전트를 도입하면 자연스럽게 따라오는 질문이 있습니다. **"그래서 우리 조직이 AI에 얼마를 쓰고 있는가?"** 사용량 기반(소비형) 과금이 늘어나면서, IT·재무·현업 리더 모두 *어느 팀이 어떤 서비스를 얼마나 사용하는지*를 투명하게 보고 싶어 합니다.

Microsoft 365 메시지 센터에 등록된 새 로드맵 항목(RM566302)은 바로 이 지점을 겨냥합니다. **Copilot 크레딧 사용량, 즉 'AI 지출(AI spend)'을 그룹·팀 단위로 들여다볼 수 있는 분석 기능이 Viva Insights에 추가**됩니다.

이번 포스팅에서는 무엇이 새로 생기는지, 누가 볼 수 있는지, 사용하려면 어떤 전제 조건이 필요한지를 한국 IT 담당자·도입 검토자 관점에서 정리해 드립니다.

---

## 무엇이 새로워지나요?

핵심은 한 줄입니다.

> **그룹·팀 단위의 AI 지출(Copilot 크레딧 사용량) 인사이트가 Viva Insights에 대시보드 형태로, 그리고 Advanced insights 안에서 제공됩니다.**

지금까지 AI 사용 비용은 주로 관리자가 관리 센터의 청구·비용 관리 화면에서 확인하는 영역이었습니다. 이번 변경으로 그 사용량 데이터가 **Viva Insights의 분석 경험 안으로 들어와**, 조직·팀 맥락에서 "어디에서 소비가 발생하는지"를 더 쉽게 파악할 수 있게 됩니다.

이번 릴리스에서 분석 대상이 되는 서비스는 다음 두 가지입니다.

- **Cowork**
- **Work IQ API**

두 서비스 모두 사용량 기반 과금(usage-based billing)으로 동작하는 영역으로, 이번 인사이트는 이들의 **크레딧 소비 현황**을 그룹·팀 수준으로 집계해 보여 줍니다.

---

## 어디에서 볼 수 있나요?

이번 인사이트는 두 가지 경로로 제공됩니다.

| 제공 경로 | 형태 | 대상 |
|---|---|---|
| **Viva Insights 대시보드** | 사용량 기반 비용 인사이트 대시보드 | 직속 부하 5명 이상을 둔 관리자(범위 제한 접근), Insights 분석가, 전역 관리자(Global Administrator) |
| **Advanced insights** | 동일 인사이트 | Insights 분석가, 전역 관리자 |

대시보드 경험은 **기본값으로 활성화(enabled by default)** 되어, 별도 설정 없이도 즉시 사용량 기반 비용 인사이트에 접근할 수 있도록 제공됩니다.

> 참고로, 관리자가 보는 대시보드는 **직속 부하 5명 이상을 둔 관리자에게 범위 제한(scoped) 접근**으로 열립니다. 즉, 자신의 조직 범위 안에서의 사용량을 보는 구조입니다.

---

## 이번 릴리스의 범위와 한계

도입을 검토할 때 꼭 짚어야 할 부분이 있습니다. **이번 릴리스에는 포함되지 않는 것**입니다.

- **테넌트 전체 데이터에 대한 리더(leader) 접근은 이번 릴리스 범위에서 제외**됩니다.

즉, 조직 전체를 가로지르는 전사 단위의 리더십 뷰는 이번 출시에 포함되지 않으며, 제공은 그룹·팀 단위 인사이트와 위 표의 대상(관리자·분석가·전역 관리자) 중심으로 이루어집니다.

---

## 사용 전 반드시 확인할 전제 조건

사용자가 **Cowork** 또는 **Work IQ API**를 사용할 수 있으려면, 그리고 그 사용량 인사이트가 의미를 가지려면 한 가지 전제 조건이 충족되어야 합니다.

> **테넌트에 Microsoft 365 관리 센터의 비용 관리(Cost Management)를 통한 사용량 기반 과금(usage-based billing)이 설정되어 있어야 합니다.**

따라서 도입 순서는 다음과 같이 정리할 수 있습니다.

1. Microsoft 365 관리 센터 → **비용 관리(Cost Management)** 에서 사용량 기반 과금 설정
2. 대상 사용자가 **Cowork / Work IQ API** 사용
3. 발생한 크레딧 사용량이 **Viva Insights 대시보드 / Advanced insights**에 집계되어 표시

---

## 한국 조직을 위한 도입 관점 체크포인트

- **AI 비용의 가시성 확보**: 사용량 기반 과금이 늘어나는 환경에서, "누가·어느 팀이·어떤 서비스를 얼마나 쓰는가"를 분석 화면으로 확인할 수 있다는 점은 거버넌스와 비용 최적화의 출발점입니다.
- **기본 활성화에 대한 사전 안내**: 대시보드가 기본값으로 켜진 상태로 제공되므로, 관리자·분석가에게 어떤 데이터가 어떤 범위로 보이는지 사전에 커뮤니케이션해 두는 것이 좋습니다.
- **접근 범위 정리**: 관리자는 5명 이상 직속 부하 기준의 범위 제한 접근, 분석가·전역 관리자는 Advanced insights 접근 등 **역할별로 보이는 범위가 다릅니다.** 내부 권한 정책과 함께 점검하세요.
- **전제 조건 선행**: 비용 관리(Cost Management) 기반의 사용량 기반 과금 설정이 선행되지 않으면 인사이트가 채워지지 않습니다. 재무·IT 협업으로 과금 설정을 먼저 마무리하는 것을 권장합니다.
- **전사 리더 뷰는 추후**: 테넌트 전체에 대한 리더 접근은 이번 범위에 없으므로, 전사 단위 리포팅이 필요하다면 후속 업데이트 일정을 별도로 추적하는 것이 좋습니다.

---

## 출시 일정

| 항목 | 내용 |
|---|---|
| 로드맵 ID | 566302 |
| 대상 제품 | Microsoft 365 Roadmap · Microsoft Copilot (Microsoft 365) · Microsoft Viva |
| 대상 서비스 | Cowork, Work IQ API |
| 일반 공급(GA) | **2026년 6월** |

---

## 마무리

Copilot과 에이전트가 업무에 깊이 스며들수록, "얼마나 쓰는가"를 보는 일은 선택이 아니라 운영의 기본이 됩니다. 이번 Viva Insights의 AI 지출·사용 인사이트는 **Cowork와 Work IQ API의 크레딧 사용량을 팀·그룹 단위로 가시화**하여, 한국 조직이 AI 투자 대비 활용도를 점검하고 비용을 합리적으로 관리하는 데 좋은 출발점이 되어 줄 것입니다.

도입을 검토 중이라면, 먼저 비용 관리(Cost Management) 기반의 사용량 기반 과금 설정을 점검하고, 관리자·분석가의 접근 범위를 정리해 두시길 권합니다.

---

> **출처**
>
> - Microsoft 365 메시지 센터 / 로드맵 항목 **RM566302** — [https://mc.merill.net/message/RM566302](https://mc.merill.net/message/RM566302)
> - Microsoft 365 Roadmap (Feature ID 566302) — [https://www.microsoft.com/en-us/microsoft-365-roadmap?searchterms=566302](https://www.microsoft.com/en-us/microsoft-365-roadmap?searchterms=566302)
>
> *본 글은 Microsoft 365 메시지 센터/로드맵 정보를 바탕으로 작성되었습니다. 실제 출시 일정·기능은 변경될 수 있습니다.*
