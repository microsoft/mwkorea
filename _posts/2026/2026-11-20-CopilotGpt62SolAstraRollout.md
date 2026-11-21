---
title: "Copilot에 GPT-6.2 Sol·Astra 추가: 앱별 제공 단계와 과금 조건 한눈에 보기"
date: 2026-11-20T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - GPT62Sol
  - GPT62Astra
  - CopilotStudio
  - Cowork
  - Frontier
  - Governance
excerpt: "Microsoft Copilot의 지원 경험에 GPT-6.2 Sol과 Astra가 순차 추가됩니다. Cowork·Copilot Studio의 사용량 기반 과금과 Office 앱·Chat의 구독 및 Frontier 조건, Astra의 OpenAI 하위 처리자 설정을 구분해 설명합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot에 GPT-6.2 Sol·Astra 추가: 앱별 제공 단계와 과금 조건 한눈에 보기

Copilot의 모델 선택지가 늘어날 때는 모델 이름만 확인해서는 충분하지 않습니다. 같은 모델이라도 어떤 앱에서 쓰는지에 따라 정식 제공 여부와 과금·관리 설정이 다를 수 있기 때문입니다.

Message Center 공지 MC1560916은 **GPT-6.2 Sol과 GPT-6.2 Astra를 Copilot 경험에 순차 도입**한다고 안내합니다. 한국 시간으로 공지 RSS 발행일은 2026년 11월 20일이며, 원문 페이지는 11월 19일로 표시됩니다. 아래 내용은 해당 공지 시점의 제공 조건을 기준으로 합니다.

---

## 모델·앱별 제공 조건

| 모델 | 경험 | 공지 기준 제공 단계 | 라이선스·과금 조건 |
|---|---|---|---|
| GPT-6.2 Sol | Cowork, Copilot Studio | GA 순차 배포 | USL 할당 및 UBB 활성화 |
| GPT-6.2 Astra | Cowork, Copilot Studio | GA 순차 배포 | USL 할당 및 UBB 활성화 |
| GPT-6.2 Sol | Word, Excel, PowerPoint, Chat | GA 순차 배포 | Microsoft 365 Copilot USL에 포함, 사용 한도 적용 |
| GPT-6.2 Astra | Word, Excel, PowerPoint, Chat | Frontier 순차 배포 | USL, Frontier 등록, UBB 활성화 |

**USL은 사용자 구독 라이선스, UBB는 사용량 기반 과금**을 뜻합니다. 특히 Sol이 Word·Excel·PowerPoint·Chat의 구독에 포함된다는 설명을 Cowork나 Copilot Studio에도 그대로 적용하면 안 됩니다.

공지에는 Sol의 사용 한도가 있다고 명시되어 있습니다. 대부분의 사용자가 일상 업무에서 한도에 도달하지 않도록 설계되었다고 설명하지만, **구체적인 횟수나 기간별 한도 수치는 제공하지 않습니다.** 무제한 사용으로 안내해서는 안 됩니다.

## Astra는 OpenAI 하위 처리자 설정 확인이 필요

원문에 따르면 **모든 지원 경험에서 GPT-6.2 Astra에 접근하려면 OpenAI subprocessor가 활성화되어 있어야 합니다.** 비활성화된 조직에서는 Astra를 사용할 수 없습니다.

이 설정의 범위를 정확히 이해하는 것이 중요합니다.

- 제어 대상은 **OpenAI가 하위 처리자로서 직접 운영하는 OpenAI 모델**입니다.
- **Microsoft가 운영하는 Azure OpenAI의 OpenAI 모델은 이 설정의 영향을 받지 않으며**, 해당 설정과 관계없이 Copilot에서 계속 제공됩니다.

즉, OpenAI 하위 처리자를 끄는 것을 “Copilot의 모든 OpenAI 모델을 끈다”라고 설명하면 부정확합니다. 자세한 범위는 [OpenAI as a subprocessor in Microsoft Online Services](https://learn.microsoft.com/microsoft-365/copilot/openai-subprocessor)에서 확인할 수 있습니다.

## 사용자는 어떻게 접근하나요?

적용 가능한 라이선스와 구성 요건을 충족한 사용자는 지원 Copilot 경험의 **모델 선택기**에서 새 모델을 선택할 수 있습니다. 해당 사용자에게는 모델이 기본 활성화됩니다.

다만 공지는 **순차 배포 중**이라고 설명할 뿐, 테넌트별 도착 시각이나 전체 완료일을 제시하지 않습니다. 모델이 바로 보이지 않는다고 해서 설정 오류로 단정하지 말고, 라이선스·프로그램·과금 설정과 배포 상태를 함께 확인해야 합니다.

## 관리자와 지원팀 체크포인트

1. Astra를 제공하려면 OpenAI 하위 처리자 설정을 조직의 데이터 처리 정책과 함께 검토합니다.
2. Cowork·Copilot Studio와 Office 앱·Chat의 과금 조건을 구분해 사용자에게 안내합니다.
3. Astra의 Office 앱·Chat 제공은 Frontier라는 점을 교육 자료에 표시합니다.
4. 헬프데스크에 사용 한도 알림이 나타날 수 있음을 알리고 대응 안내를 준비합니다.
5. 내부 AI 사용 지침과 모델 선택 안내를 업데이트합니다.

접근을 원하는 조직에 공지가 별도 필수 조치를 요구하지 않는다는 설명은, 필요한 라이선스나 구성 조건이 없어도 쓸 수 있다는 의미는 아닙니다.

## 마무리

이번 공지는 선택지 확대에 관한 안내이지, 모델별 품질·속도·정확도 비교 결과를 제공하는 발표는 아닙니다. 도입 시에는 확인되지 않은 성능 차이를 단정하기보다 **제공 단계, 비용, 데이터 처리 조건**을 먼저 정리하는 것이 좋습니다.

> **출처:** Message Center **MC1560916**, [Microsoft Copilot: GPT-6.2 Sol and Astra rolling out](https://mc.merill.net/message/MC1560916). [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap)에서 관련 업데이트를 확인할 수 있습니다. 이 공지에는 개별 Roadmap ID가 명시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
