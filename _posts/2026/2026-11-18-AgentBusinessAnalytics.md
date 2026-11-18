---
title: "AI 지출과 업무 가치를 한곳에: Agent 365 Business Analytics 공개 프리뷰"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent365
  - BusinessAnalytics
  - FinOps
  - VivaInsights
excerpt: "Agent 365 Business Analytics가 AI 비용·사용량·가치를 연결하는 Frontier 공개 프리뷰로 출시됩니다. 기능별 제공 일정, 접근 권한과 개인정보 보호 설정, 추정 가치 해석의 주의점을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# AI 지출과 업무 가치를 한곳에: Agent 365 Business Analytics 공개 프리뷰

AI 도입 규모가 커지면 “얼마나 썼나”와 “어떤 일에 도움이 됐나”를 함께 봐야 합니다. Microsoft는 MC1557727에서 관리 센터 비용 관리 확장과 **Agent 365 Business Analytics** 웹 앱을 발표했습니다.

새 앱은 지출 원인, 지원 업무, 다음 투자 방향을 함께 살펴보도록 설계되었습니다. 다만 전체 기능이 같은 날 GA가 되는 것은 아니며, 추정 가치도 조직이 설정한 가정에 기반한다는 점이 중요합니다.

---

## 관리 센터의 AI 비용 관리 확장

| 기능 | 원문의 제공 단계·시점 |
|---|---|
| Cowork를 포함한 Microsoft AI 총지출, 사용자·모델별 분석 | 2026년 11월 GA |
| 6,000개 이상 사용 사례 분류 및 Cowork 추정 가치 | 11월 Frontier |
| 타사 에이전트·AI 서비스 지출 및 가치 확장 | 12월 Frontier |
| 테넌트·에이전트 소비 속도 기반 비용 예측 | 11월 Frontier |
| 지출 급증·대량 활동 감지와 모델 라우팅 권고 | 11월 Frontier |
| 멀티테넌트 지출 관리 | 11월 공개 프리뷰 |
| 지출 정책 관리 위임 | 다른 관리자에게 11월, 비즈니스 리더에게 12월 Frontier |

Cowork의 사용 사례별 시간 절감 및 금전 가치 입력값을 조직에 맞게 조정할 수 있습니다.

## Business Analytics에서 볼 수 있는 내용

11월에는 라이선스 및 사용량 기반 AI 서비스의 비용을 통화와 Copilot Credits로 함께 보고, 인당 지출 상한이나 모델 구성 변경의 what-if 분석을 수행합니다.

서비스 분석은 Cowork의 출력 유형·스킬, Copilot Code, Autopilot, 에이전트, GitHub Copilot을 다룹니다. 유연한 기간과 사용자 정의 HR 속성으로 분석하며 Work IQ API는 12월 제공 일정입니다.

Cowork 사용 사례·가치는 11월, 다른 AI 서비스는 12월로 안내됩니다. Cowork 지원 시간, 만족도, 추정 가치는 시간 및 시간당 단가 가정에 영향을 받으므로 **확정된 비용 절감액과 구분**해야 합니다.

GitHub Copilot은 조직·코스트 센터·저장소·모델별 사용 및 도입과 계량 지출을 함께 볼 수 있습니다. CSV·Power BI·Microsoft Fabric으로 사용량·비용 데이터를 내보내는 기능은 11월, 관리자 전용 세션 단위 데이터는 11월 말 일정입니다.

## 누가 언제 이용할 수 있나요?

[Agent 365 Business Analytics](https://aka.ms/a365analytics)는 **2026년 11월 17일** Frontier 공개 프리뷰 배포를 시작합니다. Copilot 라이선스 50개 이상인 Frontier 테넌트부터 시작해 **12월 7일까지 전체 Frontier 테넌트**로 확장할 계획입니다.

연결된 타사 AI 플랫폼의 지출·가치 데이터 접근에는 Agent 365 및/또는 Microsoft 365 E7 라이선스가 필요합니다. 관리 센터 비용 관리 확장도 11월 17일부터 배포됩니다.

## 접근 권한과 개인정보 보호

기존 Viva Insights 역할과 최소 그룹 크기 설정은 이어집니다. Viva Insights가 없는 조직은 Global Administrator, CEO 및 그 아래 두 관리 계층에 기본 테넌트 수준 접근을 제공하고, 10명 이상 팀의 관리자는 조직 범위 인사이트 접근을 받습니다. 테넌트 수준 접근자의 비용 데이터는 관리자가 켜기 전까지 꺼져 있습니다.

관리자 계층은 기본적으로 Entra ID에서 가져오며 CSV 업로드나 MODIS로 HR 속성을 재정의할 수 있습니다. 개인 식별이 가능한 사용자 수준 데이터는 기본 꺼짐이며 Viva feature access management 정책으로 사용자·그룹별 활성화할 수 있습니다.

최소 그룹 크기보다 작은 집단의 집계 정보는 숨겨집니다. 적격 대상의 사용 사례 분류 및 Cowork 가치 계산은 기본 켜짐이고 관리자 제어 및 Cowork 분류 사용자 옵트아웃을 제공하므로 관련 별도 공지도 함께 검토해야 합니다.

## 한국 조직의 준비 사항

먼저 Entra ID 관리자 계층과 코스트 센터 등 HR 속성의 정확도를 확인하세요. 이어 보고서 열람자, 개인 식별 데이터 접근, 최소 그룹 크기, 가치 계산 가정을 재검토하면 비용 배부와 개인정보 보호를 함께 설계할 수 있습니다.

> **출처**: [MC1557727](https://mc.merill.net/message/MC1557727), Microsoft 365 Message Center Archive. [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제시되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
