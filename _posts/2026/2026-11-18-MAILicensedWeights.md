---
title: "모델도 우리 환경에서 통제하기: MAI Licensed Weights의 의미"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - LicensedWeights
  - CustomModels
  - Azure
excerpt: "MAI Licensed Weights는 조직의 Azure 환경에 모델을 배포·조정하고 접근과 업그레이드를 통제하는 제공 방식을 예고합니다. 고객별 맞춤 평가 수치와 데이터 사용 조건, 아직 공개되지 않은 도입 조건을 구분합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 모델도 우리 환경에서 통제하기: MAI Licensed Weights의 의미

회사의 지식과 업무 흐름을 모델에 반영할수록 “어디서 실행하고 누가 접근하며 언제 바뀌는가”가 중요해집니다. Microsoft AI가 발표한 **MAI Licensed Weights**는 이러한 통제권을 강조합니다.

핵심은 Microsoft AI 모델을 조직의 Azure 환경에 배포하고 자체 지식으로 조정하는 것입니다. Copilot·에이전트를 자사 서비스에 내장하려는 기업에는 흥미로운 선택지이지만, 즉시 누구나 가중치를 내려받는 공개 모델 발표는 아닙니다.

![MAI Licensed Weights 공식 소개 이미지](/mwkorea/assets/images/2026-11-18-MAILicensedWeights/image1.jpg)

---

## 조직이 통제하는 범위

원문은 조직이 배포 방식, 접근자, 업그레이드 시점을 통제하고 자체 지식·전문성을 반영할 수 있다고 설명합니다.

데이터와 조정 결과는 고객에게 남으며, Microsoft가 이를 자사 모델 학습에 사용하는 것은 **고객의 명시적 동의가 있을 때만**이라고 명시합니다. 이 설명을 Azure 밖 임의 배포 권리나 모든 데이터 처리 조건의 면제로 확대해서는 안 됩니다.

## 고객 사례는 무엇을 보여 주나요?

| 고객 | 원문의 과제·결과 |
|---|---|
| AT&T | 맞춤 Code 2 Flash·Code 2로 5G 네트워크 분석. 표준 과제에서 GPT-6.1 Sol보다 높은 성능을 약 50분의 1 비용으로 달성 |
| Woven by Toyota | 과거 MISRA 코딩 표준 수정으로 조정한 Code 2 Flash. 기존 모델이 사람 개입을 요구한 사례 중 44%에서 병합 가능한 수정 생성, 비용 10분의 1 미만 |
| Alaska Airlines | Code 2 Flash 조정 후 항공기 정비 보고서 분류 정확도 81.2%에서 91.1%로 개선 |

Woven의 **44%는 전체 코드 수정 성공률이 아니라 기존 모델의 사람 개입 사례라는 부분집합**에 대한 수치입니다. Alaska의 개선은 약 9.9%포인트이며 “정확도가 10%가 되었다”는 뜻이 아닙니다.

모두 고객별 과제·모델 구성·평가 방식에 따른 결과입니다. 특히 항공 정비 등 고위험 분야의 최종 판단 책임은 자격을 갖춘 직원에게 남습니다.

## 언제 어떻게 시작하나요?

원문은 **Frontier Company 협업을 통해 제공 예정**이라고 안내하며 Microsoft 담당 계정 팀에 문의하도록 합니다. 공개 셀프서비스 GA나 구체적인 일반 가격표는 제시하지 않습니다.

지원 지역, 배포 용량, 모델별 라이선스 범위, 업데이트 책임과 서비스 수준도 이 글만으로 확정할 수 없습니다.

## 한국 조직의 검토 질문

도입 검토에서는 모델 접근·배포 통제뿐 아니라 조정 데이터 권한, 평가 데이터 분리, 업그레이드 전 회귀 평가, 운영 비용과 지원 책임을 함께 정의하는 것이 좋습니다.

“가중치를 통제한다”와 “오픈 소스다”는 다릅니다. 구체적인 사용·수정·재배포 권리는 계약으로 확인해야 하며, 원문은 자유 재배포를 약속하지 않습니다.

> **출처**: [MAI Licensed Weights: Frontier performance you control](https://microsoft.ai/news/introducing-mai-licensed-weights/), Microsoft AI 뉴스 블로그. 자세한 내용은 원문 참조.
