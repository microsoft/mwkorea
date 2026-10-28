---
title: "MAI Cyber 1.1 Flash: MDASH 취약점 스캔 비용 18% 절감의 의미"
date: 2026-10-28T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - MAICyber
  - MDASH
  - Security
  - Agent
excerpt: "MAI Cyber 1.1 Flash는 MDASH 내부 평가에서 이전 모델과 비슷한 성능을 유지하며 스캔당 비용을 18% 줄였습니다. 범용 Copilot 업데이트가 아닌 검증된 MDASH 고객 대상의 보안 특화 모델이며, 접근 조건과 평가 범위를 구분해 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# MAI Cyber 1.1 Flash: MDASH 취약점 스캔 비용 18% 절감의 의미

보안 에이전트의 효율은 모델 하나의 성능표만으로 설명하기 어렵습니다. 어떤 보안 데이터와 도구를 쓰고, 작업을 어떻게 나누며, 유용한 발견을 얻기까지 시스템 전체가 얼마나 많은 일을 하는지가 함께 중요합니다.

Microsoft AI는 **MAI Cyber 1.1 Flash**를 발표하며, MDASH 취약점 스캔 내부 평가에서 기존 MAI Cyber 1 Flash와 **비슷한 성능을 유지하면서 스캔당 비용을 18% 줄였다**고 설명했습니다. 국내 Copilot·에이전트 담당자에게는 범용 모델 교체보다 특화 모델과 실행 체계를 함께 최적화한 사례로 읽을 만합니다.

![Microsoft AI가 MAI Cyber 1.1 Flash 발표에 사용한 대표 이미지](/mwkorea/assets/images/2026-10-28-MAICyber11FlashMDASH/image1.webp)

---

## 모델과 MDASH 실행 체계를 함께 봐야 합니다

앞선 MAI Cyber 1 Flash는 특화 보안 모델, Microsoft의 보안 데이터, **MDASH harness**를 결합한 접근이었습니다. 여기서 harness는 모델이 취약점 탐색 업무를 수행하도록 연결하는 실행 체계로 이해할 수 있습니다.

1.1 Flash는 모델이 직접 맡는 작업을 늘려, 전체 MDASH 시스템이 유용한 결과를 더 낮은 비용으로 찾도록 설계한 후속 모델입니다. 원문은 모델 단독 가격보다 **전체 취약점 발견 시스템의 효율**을 강조합니다.

## 18%라는 수치의 정확한 범위

비용 비교는 Microsoft의 **내부 MDASH 취약점 스캔 평가 세트**에서 이루어졌습니다. 해당 평가에서 스캔당 완료 비용이 18% 낮아졌으며, 성능은 MAI Cyber 1 Flash와 유사하다는 설명입니다.

이는 고객 청구 금액이 일괄 18% 인하되었다거나, 모든 코드베이스에서 취약점을 18% 더 찾는다는 의미가 아닙니다. 제목은 더 적은 토큰 사용을 강조하지만, 본문에는 토큰 감소율이나 절대 토큰 수가 별도로 제시되어 있지 않습니다.

실제 도입에서는 비용뿐 아니라 유효한 발견 수, 검토 부담, 기존 보안 업무와의 연결성을 함께 비교하는 것이 좋습니다. 이 항목들은 도입 담당자를 위한 권장 평가 기준이며, 발표에 나온 추가 측정 결과는 아닙니다.

## 기존 고객의 이용 추세도 공개

| 지표 | Microsoft AI 발표 내용 |
|---|---|
| MAI Cyber 1 Flash 프로필 첫 사용 이후 | 후속 스캔 약 10회 중 9회에서 OpenAI 전용 프로필보다 MAI 프로필 선택 |
| 전체 MDASH 스캔에서 MAI Cyber 비중 | 거의 50% |
| 이용 규모 | 수백 고객의 수천 건 규모 스캔 |

약 90%라는 수치는 첫 MAI 프로필 스캔 이후의 **후속 스캔 선택 비중**입니다. 모든 신규 고객의 선택률, 탐지 정확도, 시장 점유율과는 다릅니다. 또한 이 이용 추세는 기존 MAI Cyber 활용을 설명하는 수치이지, 새 1.1 모델만의 장기 사용 결과가 아닙니다.

## 누가 사용할 수 있고 어떻게 시작하나요?

MAI Cyber 1.1 Flash는 **검증된 MDASH 고객**에게 MDASH를 통해 제공됩니다. 명확한 이용 정책과 지속적인 모니터링 등 책임 있는 사용을 위한 보호 조치가 적용됩니다. 일반 Copilot 사용자가 바로 선택하는 범용 채팅 모델로 발표된 것은 아닙니다.

기존 고객은 새 스캔을 시작할 때 **MAI Cyber 1.1 Flash 프로필**을 선택합니다. 원문은 [MDASH와 Foundry 통합의 필요한 모델 배포 문서](https://learn.microsoft.com/en-us/security-exposure-management/mdash-foundry-integration#deploy-the-required-models)로 연결하므로, 자신의 환경에 필요한 배포 조건도 확인해야 합니다.

신규 사용자는 [MDASH 접근 신청 양식](https://forms.cloud.microsoft/pages/responsepage.aspx?id=v4j5cvGGr0GRqy180BHbR5n91RGSMY5MoMjm9pNflCtUODBFQ0NKTllWTkRWRTY3TU0zQkg5S1JXSiQlQCN0PWcu&route=shorturl)으로 접근을 요청할 수 있습니다. 모델의 상세 정보는 원문이 연결한 [MAI Cyber 1.1 Flash 모델 카드](https://microsoft.ai/pdf/MAI-Cyber-1.1-Flash%20ORA%20Model%20Card.pdf)를 참고하세요. 신청이 자동 승인된다는 안내는 없습니다.

## 한국 조직의 도입 관점

에이전트 기반 보안 점검에서는 허가받은 시스템과 코드만 대상으로 삼고, 발견된 문제의 확인·수정 책임을 명확히 해야 합니다. 원문이 말하는 비용 효율을 검증하려면 실제 승인된 업무 범위에서 동일 조건의 스캔을 비교하는 것이 적절합니다.

이번 발표는 Microsoft 365 Copilot이나 Security Copilot에 기본 포함된다는 내용도, 일반 고객 대상 GA 전환을 별도로 선언한 내용도 아닙니다. **MDASH를 통한 제한된 고객 제공**이라는 범위를 지키면서, 보안 특화 모델과 실행 체계를 함께 개선한 사례로 이해하는 것이 핵심입니다.

> **출처**: [MAI Cyber 1.1 Flash: Sharper findings and fewer tokens inside MDASH](https://microsoft.ai/news/mai-cyber-1-1-flash/) — Microsoft AI 뉴스 블로그. **자세한 내용은 원문 참조**.
