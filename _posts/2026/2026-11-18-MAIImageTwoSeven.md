---
title: "부분 수정부터 투명 배경까지: MAI Image 2.7과 Flash·Canvas"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - MAIImage
  - ImageGeneration
  - Foundry
excerpt: "MAI Image 2.7과 Flash가 이미지 생성·편집 공개 프리뷰로 제공됩니다. 부분 편집과 투명 배경, Canvas 작업 공간, 이미지 1,000장 기준 가격 및 순위의 평가 시점을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 부분 수정부터 투명 배경까지: MAI Image 2.7과 Flash·Canvas

이미지 생성 업무에서는 첫 결과물보다 그다음 수정이 더 오래 걸릴 때가 많습니다. 제품 색상만 바꾸거나 특정 사물만 이동하면서 나머지 구도를 유지하는 능력이 중요한 이유입니다.

Microsoft AI는 **MAI Image 2.7·Flash**와 Flash 기반 작업 공간 **Canvas**를 발표했습니다. 한국의 Copilot·에이전트 제작자는 이미지 작업을 도구로 연결할 때 품질뿐 아니라 반복 편집 일관성과 처리 단가를 함께 살펴볼 수 있습니다.

![MAI Image 2.7 공식 소개 이미지](/mwkorea/assets/images/2026-11-18-MAIImageTwoSeven/image1.jpg)

---

## 세밀한 편집과 투명 배경

원문은 사물의 색상·재질·위치를 바꾸면서 이미지의 다른 부분을 유지하고, 연속 편집에서도 시각적 일관성을 보존하는 점을 강조합니다.

두 모델 모두 투명 배경을 지원해 제품 이미지·로고·아이콘·삽화의 후처리 부담을 줄이는 방향입니다. 다만 특정 결과의 상표권·저작권이나 브랜드 적합성은 별도 검토가 필요합니다.

## Canvas로 만들고 다듬기

[MAI Labs Canvas](https://labs.microsoft.ai/?model=canvas)는 프롬프트나 스케치에서 시작해 다이어그램으로 발전시키고, 이미지 일부를 선택해 교체·이동·스타일 변경을 수행하는 작업 공간입니다.

Canvas는 **Image 2.7 Flash 기반**입니다. 이 발표를 Microsoft 365 Copilot 앱 안에 같은 이름의 기능이 모두 제공된다는 의미로 해석하면 안 됩니다.

## 가격과 공개 프리뷰

| 모델 | 원문의 이미지 1,000장당 대략 가격 |
|---|---|
| MAI Image 2.7 | 약 35달러 |
| MAI Image 2.7 Flash | 약 10달러 |

두 모델은 **Microsoft Foundry 공개 프리뷰**이며 MAI Labs와 fal·Genspark·OpenRouter·Vercel 등도 이용 경로로 소개합니다. 실제 비용과 성능은 구성·업무·제공처에 따라 달라질 수 있으므로 계약 가격이나 모든 해상도의 고정 단가로 보지 않는 것이 좋습니다.

## 1위라는 표현의 조건

2026년 **11월 16일 기준** AA-Image-Editing v2.1에서 Image 2.7은 **5,478표·Elo 1,215점**으로 1위이며 GPT Image 2.6 Sunburst(max)보다 **4 Elo** 높다고 발표했습니다. Arena에서는 생성 및 단일 이미지 편집에서 상위 두 연구소 중 하나라고 설명합니다.

원문의 “경쟁 모델 비용의 5분의 1”도 특정 비교 조건의 설명입니다. 시시각각 바뀌는 순위나 작은 점수 차이를 모든 작업의 압도적 우위로 확대하면 안 됩니다.

## 창작 플랫폼의 평가와 활용

Microsoft는 Adobe, Minute(Sports Illustrated), Figma Weave, Wirestock, Manus의 협업·평가 의견을 소개합니다. 원문의 파트너 로고는 다음과 같습니다.

![Adobe](/mwkorea/assets/images/2026-11-18-MAIImageTwoSeven/image2.webp)

![Minute의 Sports Illustrated](/mwkorea/assets/images/2026-11-18-MAIImageTwoSeven/image3.webp)

![Figma Weave](/mwkorea/assets/images/2026-11-18-MAIImageTwoSeven/image4.webp)

![Wirestock](/mwkorea/assets/images/2026-11-18-MAIImageTwoSeven/image5.webp)

![Manus](/mwkorea/assets/images/2026-11-18-MAIImageTwoSeven/image6.webp)

또한 MAI Image 계열은 6월 Build 이후 Bing Image Creator의 기본 모델 계열이 되었으며 사용량의 주간 복합 증가율을 **14.7%**로 보고합니다. 이것이 모든 Bing 요청이 특정 2.7 모델만 사용한다는 뜻은 아닙니다.

## 도입 체크포인트

제품 컷의 색상 수정, 다국어 캠페인 시안, 투명 배경 자산처럼 반복 작업이 많은 사례부터 품질과 편집 횟수를 측정해 보세요. 공개 프리뷰의 지원 범위와 출력 검토 절차를 확인하고, 브랜드 자산·인물·참조 이미지의 사용 권한을 별도로 관리하는 것이 좋습니다.

> **출처**: [MAI Image 2.7: Frontier quality at a fraction of the cost](https://microsoft.ai/news/introducing-mai-image-2-7/), Microsoft AI 뉴스 블로그. 자세한 내용은 원문 참조.
