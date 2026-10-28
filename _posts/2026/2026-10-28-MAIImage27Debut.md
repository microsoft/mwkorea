---
title: "MAI Image 2.7 프리뷰: 이미지 편집의 승부처는 디테일 제어"
date: 2026-10-28T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - MAIImage
  - ImageEditing
  - GenerativeAI
excerpt: "Microsoft AI가 이미지 편집 모델 MAI Image 2.7을 프리뷰로 공개했습니다. 평가된 10개 활용 사례와 7개 편집 동작에서 이전 버전을 개선했으며, 텍스트 기반 이미지 생성은 후속 제공 예정으로 구분해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# MAI Image 2.7 프리뷰: 이미지 편집의 승부처는 디테일 제어

업무에서 이미지를 활용할 때는 완전히 새 그림을 만드는 것보다 기존 자산의 일부를 정확히 바꾸는 일이 더 까다롭습니다. 제품은 유지하면서 배경만 바꾸거나, 조명을 바꾸되 물체와 그림자의 관계가 어색해지지 않도록 해야 하기 때문입니다.

Microsoft AI는 **이미지 편집 모델 MAI Image 2.7을 프리뷰로 공개**하며 이런 제어 능력의 개선을 강조했습니다. Copilot과 에이전트를 활용하는 국내 독자에게는 시각 자료 제작 도구의 발전으로 볼 만하지만, 이 발표를 Microsoft 365 Copilot에 즉시 기본 탑재되었다는 의미로 해석해서는 안 됩니다.

![Microsoft AI가 MAI Image 2.7 발표에 사용한 대표 이미지](/mwkorea/assets/images/2026-10-28-MAIImage27Debut/image1.webp)

---

## 무엇을 더 잘 편집하나요?

원문은 장면 전체의 스타일과 조명을 바꾸고, 이미지 속 텍스트·기호를 주변과 어울리도록 수정하며, 기존 자산을 복원·개선하는 능력을 설명합니다. 물체, 조명, 환경이 어떻게 함께 작동해야 하는지 이해해야 하는 편집이 핵심입니다.

예를 들어 제품을 새로운 환경에 배치하거나, 장면의 분위기를 바꾸거나, 전체 구도를 유지하면서 개별 물체를 수정하는 작업입니다. 단순히 “더 예쁜 이미지”보다 **편집 의도를 얼마나 정밀하게 반영하는가**에 초점이 있습니다.

## 평가 수치가 말하는 것과 말하지 않는 것

| 항목 | 발표 시점 Microsoft AI의 설명 |
|---|---|
| Arena Edit | 3위, 연구 조직 기준 Microsoft AI 2위 |
| Artificial Analysis 이미지 편집 리더보드 | 2위 |
| 이전 2.6 대비 | 평가된 10개 활용 사례와 7개 편집 동작 모두 개선 |
| 특히 강조한 영역 | 개선·복원, 추론 기반 편집, 장면·스타일, 텍스트·기호 편집 |
| 장면·스타일 범주 | 차상위 모델보다 24 Elo 앞선 점수 |

위 수치는 **원문 발표 시점의 평가 결과**입니다. 리더보드 순위는 변할 수 있고, 24 Elo 차이를 성공률 24%포인트나 모든 업무의 품질 차이로 바꾸어 읽어서는 안 됩니다. 또한 “모든 활용 사례 개선”은 해당 평가에 포함된 범위를 뜻합니다.

원문 제목은 GPT Image 2.5 Flare와의 비교를 내세우지만, 본문은 위 순위와 범주별 수치를 중심으로 설명합니다. 공개되지 않은 개별 점수나 비용 비교를 추가로 가정하지 않는 것이 정확합니다.

## 지금은 이미지 편집부터, 생성은 후속 제공

출시 단계는 **Preview**이며 먼저 편집 기능을 제공합니다. **텍스트에서 이미지를 생성하는 text-to-image는 곧 제공 예정**이라고 설명되어 있어, 현재 편집 제공과 분리해 이해해야 합니다.

원문은 [Arena](https://arena.ai/leaderboard/image/text-to-image), [Artificial Analysis](https://artificialanalysis.ai/?category=image#image-editing), [MAI Playground](https://playground.microsoft.ai/?model=mai-image-2-6)를 체험 경로로 연결합니다. 다만 발표 본문의 Playground 링크에는 여전히 `model=mai-image-2-6`이 들어 있습니다. 원문 링크를 그대로 제공하되, 접속 후 실제 선택된 모델 버전을 확인하세요. 확인되지 않은 2.7 주소를 임의로 만들지는 않았습니다.

## 한국의 콘텐츠·에이전트 담당자를 위한 체크포인트

브랜드 자료를 편집한다면 배경·조명 변경 후에도 제품 형태와 로고가 보존되는지, 한글 문구와 기호가 정확한지, 복원 과정에서 없던 디테일이 생기지 않는지부터 확인하는 것이 좋습니다. 이는 도입 시 권장 검증 항목이며, 원문이 한글 정확도나 브랜드 보존을 보장한 것은 아닙니다.

이번 글에는 가격, 기업용 배포 지역, SLA, Microsoft 365 Copilot 연동 일정이 제시되어 있지 않습니다. 따라서 제작 파이프라인이나 에이전트에 적용할 때는 정식 제공 경로와 데이터 처리 조건을 별도로 확인해야 합니다.

## 마무리

MAI Image 2.7의 메시지는 “이미지를 새로 만드는 능력”만이 아니라 **이미 있는 자산을 의도대로 고치는 능력**입니다. 프리뷰에서는 실제 업무 자산과 유사한 비민감 샘플로 편집 품질을 검증하고, 향후 text-to-image 제공과 기업용 통합 여부는 별도 발표로 확인하는 접근이 적절합니다.

> **출처**: [MAI Image 2.7 debuts above GPT Image 2.5 Flare on Artificial Analysis and #3 on Arena](https://microsoft.ai/news/mai-image-2-7-debut/) — Microsoft AI 뉴스 블로그. **자세한 내용은 원문 참조**.
