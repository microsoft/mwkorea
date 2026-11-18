---
title: "보안 에이전트를 더 자주 실행하기: MAI Cyber 2 Flash의 성능과 비용"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - MAICyber
  - Security
  - MDASH
excerpt: "MAI Cyber 2 Flash는 100만 토큰 맥락과 낮은 작업당 비용을 강조하는 보안 특화 모델입니다. 평가에서 제외한 과제와 비용 산정 조건, Microsoft 보안 제품 전용 제공 일정을 구분해 설명합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 보안 에이전트를 더 자주 실행하기: MAI Cyber 2 Flash의 성능과 비용

취약점 탐색과 수정 권고, 위협 조사를 상시 수행하려면 모델 품질만큼 반복 실행 비용이 중요합니다. Microsoft AI는 보안 데이터와 전문성을 바탕으로 **MAI Cyber 2 Flash**를 발표했습니다.

Copilot·보안 에이전트 도입 담당자가 볼 핵심은 긴 맥락과 비용 효율, 그리고 실제 이용 경로입니다. 일반 개발자가 임의 API로 바로 호출할 수 있는 공개 모델 발표와는 다릅니다.

![MAI Cyber 2 Flash 공식 소개 이미지](/mwkorea/assets/images/2026-11-18-MAICyberTwoFlash/image1.webp)

---

## 성능과 맥락 길이

맥락 창은 **100만 토큰**으로 Cyber 1.1 Flash의 네 배입니다. 복잡한 다단계 조사에서 더 넓은 코드 맥락을 분석하는 방향입니다.

| 평가 | 원문의 결과 |
|---|---|
| CyberGym-E2E | Cyber 2 Flash 92.3%, GPT-6 Astra 91.5% |
| WebExploitBench | Cyber 2 Flash 40.4%, GPT-5.6 Cyber 38.4% |
| CyberGym-E2E 작업당 비용 | GPT-6 Astra의 2% 미만 |

CyberGym 비교는 GPT-6 Astra의 **절반 추론 예산**, WebExploitBench는 GPT-5.6 Cyber와 **같은 추론 예산**을 사용했습니다. Microsoft Perception 초기 평가에서도 조사 에이전트 및 보안 탐지 작성에서 선도 모델과 유사한 성능을 제시합니다.

Insight Enterprises의 MAI Cyber 고객 평가에는 약 **20% 토큰 효율 개선**이 보고됩니다. 각주가 제시한 비교군은 GPT-5.4·GPT-5.3 Codex·GPT-5.4 Mini이며, 이를 Cyber 2 Flash만의 보편적 개선율로 보면 안 됩니다.

## 평가 무결성과 비용 조건

원문은 CyberGym-E2E 905개 과제 중 **92개**가 일부 학습 데이터와 동일한 오픈 소스 프로젝트·취약점 보고서에 기반했음을 공개합니다. 참조 정답은 학습에 사용하지 않았지만 보수적으로 모든 모델에서 해당 과제를 빼고 **813개** 결과를 보고했습니다.

비용 비교는 입력·캐시 입력·출력 토큰을 모두 합산한 오프라인 평가입니다.

| 모델 | 입력 / 캐시 입력 / 출력, 100만 토큰당 |
|---|---|
| MAI Cyber 2 Flash | 0.10 / 0.01 / 0.50달러 |
| GPT-6 Astra Azure OpenAI Global | 10 / 1 / 50달러 |

이는 평가용 정가 가정이며 고객의 실제 보안 제품 청구액이 아닙니다.

또한 GPT-6 Cyber와의 비교 결과는 아직 제공하지 않습니다. 제한된 고객 제공과 에이전트·도구 평가의 추가 안전조치가 이유로 설명되며 향후 공개 예정입니다.

## 언제 어디에서 쓰나요?

Cyber 2 Flash는 **Microsoft 보안 제품 전용**으로 제공됩니다. Codename MDASH에서는 적격 고객의 MAI 프로필 기존 모델을 **2026년 12월 중순부터 자동 교체**할 예정입니다.

일반 Foundry 공개 API나 모든 Copilot 제품의 모델 선택기 제공을 발표한 것은 아닙니다. 실제 사용할 수 있는지는 해당 보안 제품의 자격과 배포 상태를 확인해야 합니다.

## 한국 조직의 도입 관점

평가 대상과 비슷한 업무인지, 조사 결과를 검토할 담당자가 있는지, 어떤 자산과 코드에 접근하는지부터 확인하는 것이 좋습니다. 모델의 높은 벤치마크 점수가 취약점 누락·오탐·잘못된 수정의 부재를 보장하지는 않습니다.

보안 자동화의 경제성은 모델 토큰 비용뿐 아니라 검토 인력, 후속 수정, 재검증을 함께 고려해야 합니다.

> **출처**: [MAI Cyber 2 Flash: Leading security. Lower cost](https://microsoft.ai/news/introducing-mai-cyber-2-flash/), Microsoft AI 뉴스 블로그. 자세한 내용은 원문 참조.
