---
title: "AI를 얼마나 썼나요보다 무엇을 얻었나요: Microsoft의 FinOps for AI"
date: 2026-11-20T00:00:00 KST
categories:
  - Copilot
tags:
  - FinOps
  - Microsoft365Copilot
  - CopilotStudio
  - Agent365
  - Governance
excerpt: "Microsoft Digital은 AI 비용 관리를 사용량 억제에서 업무 성과 최적화로 옮기고 있습니다. 토큰 지출 대비 가치, 계층별 비용 관리 도구, CRAFT 프롬프트 교육과 에이전트 운영 원칙을 한국 조직 관점에서 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# AI를 얼마나 썼나요보다 무엇을 얻었나요: Microsoft의 FinOps for AI

AI 도입 초기에 중요한 질문은 직원들이 얼마나 자주 쓰는지였습니다. 하지만 여러 단계를 수행하는 에이전트와 추론 작업에 소비량 기반 과금이 더해지면, 사용량 증가가 그대로 성공 지표가 되기는 어렵습니다.

Microsoft 사내 IT 조직인 Microsoft Digital은 Inside Track에서 **토큰 지출 대비 업무 가치**를 중심으로 AI 비용 관리 방식을 바꾸고 있다고 설명합니다. 사용을 일괄 차단하는 대신, 적절한 도구와 작업 범위를 선택하게 하는 접근입니다.

이 글은 2026년 11월 19일 UTC에 게시된 원문을 바탕으로 합니다. 한국 시간으로는 11월 20일이며, 제품 제공 상태와 사내 운영 사례는 원문 시점 기준입니다.

---

## 토큰 단가는 내려가도 청구액은 늘 수 있습니다

원문은 Stanford의 2025 AI Index를 인용해 GPT-3.5 수준 성능의 추론 비용이 **2022년 11월부터 2024년 10월 사이 280배 넘게 낮아졌다**고 설명합니다. 이는 특정 성능 수준의 추론 비용 비교이지 모든 고객 요금의 인하율이 아닙니다.

또한 2025년 4월 30일 Microsoft 실적 발표에서 언급된 토큰당 비용의 절반 이상 감소는 **Microsoft 자체 비용 효율**에 관한 수치입니다. 고객 청구액도 같은 비율로 줄었다는 뜻이 아닙니다.

복잡한 모델과 다단계 에이전트 작업은 더 많은 토큰을 소비합니다. 원문은 가벼운 채팅 사용자와 적극적인 에이전트 사용자 사이에 AI 사용 수준이 **10~100배** 차이 날 수 있다고 지적합니다. 인원수만으로 소비량을 예측하기 어려운 이유입니다.

![AI 비용보다 업무 성과를 강조하는 Tal Saraf](/mwkorea/assets/images/2026-11-20-FinOpsForAITokenValue/image1.png)

## 사용량 확대에서 가치 최적화로

원문은 기업의 AI 운영을 사용량 확대 중심의 tokenmaxxing, 예산·알림·상한 중심의 지출 통제, 성과 중심의 valuemaxxing이라는 흐름으로 설명합니다.

여기서 제시하는 경영 지표는 **토큰 지출 대비 수익(Return on token spend)**입니다. 개념적으로는 제공한 업무 가치를 소비한 토큰과 비교합니다. 실제 재무 운영에서는 모델별 단가 차이도 있으므로, 원문이 함께 강조하는 **업무 결과 한 건당 비용**을 추적하는 것이 중요합니다.

클라우드 FinOps에서 가져올 원칙도 명확합니다. 제한 전에 계측하고, 실행 시점에 팀·프로젝트·비용 센터를 태깅하며, 평균이 아니라 사용량이 높은 달의 변동성을 예산에 반영해야 합니다. 토큰 자체보다 완료된 결과의 비용을 판단해야 합니다.

![토큰도 인적 자본처럼 계획적으로 관리해야 한다고 설명하는 Keith Boyd](/mwkorea/assets/images/2026-11-20-FinOpsForAITokenValue/image2.png)

## 비용 제어는 한 화면에서 끝나지 않습니다

| 계층 | 원문이 소개한 관리 수단 |
|---|---|
| Microsoft 365 Cost Management | Copilot Credits 지출 정책·한도·알림, 사용자·그룹·서비스·에이전트별 소비 확인 |
| Power Platform·Copilot Studio | 환경·에이전트별 모니터링, 월간 에이전트 한도, 특정 워크로드 사용 중지 |
| Viva Insights Consumption Dashboard | 팀·서비스별 크레딧 사용과 지출 정책 한도 접근 확인 |
| Azure Cost Management·Foundry 관측 기능 | Azure AI 지출, 거의 실시간의 토큰 및 에이전트별 비용 확인 |
| Azure API Management의 AI gateway | 속도 제한·할당량, 모델 라우팅·캐싱으로 작업당 소비량 최적화 |
| Agent 365 | 원문 시점 GA인 에이전트 제어 평면. 더 상세한 재무 원격 분석은 향후 로드맵 |

Microsoft Digital은 2026년 11월부터 직원과 벤더에게 자신의 AI 사용량 및 토큰 지출을 알리고 알림을 제공하기 시작했다고 설명합니다. 이는 Microsoft 사내 사례이며, 모든 고객에게 동일한 사내 화면이 제공된다는 뜻은 아닙니다.

## 운영과 교육을 함께 설계하기

실행 단위별 계측은 앱, 워크플로, 에이전트, 사용자까지 이어져야 합니다. 확장 전에 예산, 속도 제한, 한도 도달 시 동작을 정하고, 무한 에이전트 루프나 반복 재생성처럼 가치가 낮은 소비를 구분해야 합니다.

사용자 교육에서는 아래 질문을 순서대로 적용하고, 처음 해당하는 도구에서 멈추도록 권합니다.

1. 한 번의 대화로 끝나는가? Copilot Chat의 Auto부터 사용합니다.
2. 여러 단계와 완성된 산출물이 필요한가? 작업 범위를 정해 Cowork에 위임합니다.
3. 앱 전반에서 지속적인 백그라운드 작업이 필요한가? Autopilot 같은 에이전트가 필요한지 판단합니다.
4. 팀 전체가 반복하는 절차인가? 소유자와 예산을 정하고 Copilot Studio 에이전트를 검토합니다.

원문은 Chat의 Auto를 라이선스 포함 경험으로 안내합니다. 이를 모든 에이전트·모델 사용의 무제한 무료 제공으로 확대 해석해서는 안 되며, 실제 계약과 조직 정책을 확인해야 합니다.

## CRAFT로 프롬프트의 재시도 비용 줄이기

| 요소 | 프롬프트에 명시할 내용 |
|---|---|
| Context | 꼭 필요한 배경과 자료 |
| Requirements | 범위, 분량, 어조, 제외 조건, 성공 기준 |
| Audience | 결과를 읽을 대상 |
| Format | 메일, 표, 경영진 브리핑 등 산출물 형태 |
| Task | 수행할 작업 |

예를 들어 고객 미팅을 준비해 달라고만 하기보다, **최근 60일 자료로 범위를 정하고 우선순위 5개·핵심 발언 3개·미해결 위험 3개를 한 페이지로 정리**하도록 요청하는 방식입니다. 범위와 출력 모양이 명확하면 불필요한 탐색과 재요청을 줄일 수 있습니다.

기존 자동화 일정과 워크플로를 주기적으로 점검하고, 필요 없는 실행을 중단하며, 새 에이전트를 만들기 전에 기존 것을 재사용하는 운영도 함께 필요합니다.

![FinOps for AI를 고객과 함께 발전시키는 과정이라고 설명하는 Brian Fielder](/mwkorea/assets/images/2026-11-20-FinOpsForAITokenValue/image3.png)

## 마무리

한국 조직에서도 AI 비용을 IT 부서의 청구서 문제로만 다루기보다, 현업 책임자와 함께 **어떤 결과를 얼마에 얻었는지** 논의하는 체계가 필요합니다. 계측, 예산, 사용자 교육을 함께 시작하고 업무 성과를 기준으로 조정하는 것이 이번 사례의 핵심입니다.

> 출처: [Maximizing return on token spend: How we’re approaching FinOps for AI](https://www.microsoft.com/insidetrack/blog/maximizing-return-on-token-spend-how-were-approaching-finops-for-ai/) — Microsoft Inside Track Blog
>
> 자세한 내용은 원문 참조.
