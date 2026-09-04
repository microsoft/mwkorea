---
title: "Claude Fable 5.1이 Microsoft Copilot에 들어옵니다: Cowork와 Copilot Studio에서 오늘부터"
date: 2026-09-01T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Claude
  - Anthropic
  - CopilotCowork
  - CopilotStudio
  - WorkIQ
  - FrontierModels
excerpt: "Anthropic의 Claude Fable 5.1이 Copilot Cowork와 Copilot Studio의 프런티어 모델 목록에 추가됩니다. 장시간 실행 작업, 재무 분석, 프런트엔드 시각 코딩에 맞춰 설계됐으며, Work IQ가 사용자의 파일·회의·채팅·업무 데이터로 모델을 그라운딩합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Claude Fable 5.1이 Microsoft Copilot에 들어옵니다

Copilot에 맡기는 일이 점점 복잡해지고 있습니다. 단순 요약을 넘어 며칠에 걸친 분석, 여러 단계를 거치는 조사, 실제로 동작하는 코드 작성까지 넘어가고 있죠. 이런 작업에서는 **어떤 모델을 쓰느냐**가 결과 품질을 크게 좌우합니다.

Microsoft가 **Anthropic의 Claude Fable 5.1**을 **Copilot Cowork와 Copilot Studio**에서 사용할 수 있는 프런티어 모델(frontier models) 목록에 추가했습니다. 복잡한 작업을 AI에 위임하려는 고객에게 **선택지를 넓히는** 발표입니다.

![Claude Fable 5.1 in Microsoft Copilot](/mwkorea/assets/images/2026-09-01-ClaudeFable51InCopilot/image1.png)

---

## Fable 5.1은 어떤 모델인가

Microsoft가 밝힌 이 모델의 설계 방향은 세 가지입니다.

- **장시간 실행 작업(long-running work)**
- **재무 분석(financial analysis)**
- **프런트엔드 시각 코딩(front-end visual coding)**

작업 방식에서도 특징이 있습니다.

> **앞단에서는 더 촘촘한 계획(tighter plans up front), 뒷단에서는 더 간결한 요약(more concise summaries at the end).**

즉 작업을 시작할 때 계획을 더 꼼꼼히 세우고, 끝날 때는 결과를 군더더기 없이 정리하는 성향입니다. 여러 단계를 거치는 긴 작업에서 중요한 특성입니다. 계획이 엉성하면 중간에 방향이 어긋나고, 요약이 장황하면 결과를 확인하는 데 다시 시간이 들기 때문입니다.

---

## 모델만으로는 부족합니다 — Work IQ의 역할

이번 발표에서 눈여겨볼 부분은 모델 성능 자랑이 아니라 **맥락(context)** 에 대한 언급입니다. 원문의 표현을 옮기면 이렇습니다.

> AI에 더 많은 업무가 위임될수록, 결과의 품질은 **모델과 맥락 양쪽에** 달려 있습니다.

그래서 **Work IQ**가 Fable 5.1을 **여러분의 파일, 회의, 채팅, 비즈니스 데이터**에 그라운딩합니다. 중요한 단서가 붙어 있습니다.

**"기존 권한 범위 안에서(within your existing permissions)"**

이 구조가 만드는 차이는 이렇습니다.

| 구분 | 내용 |
|---|---|
| **그라운딩 없음** | 프롬프트만으로 추론 |
| **Work IQ 그라운딩** | **여러분의 실제 업무를 근거로 추론** |
| **결과** | 더 관련성 있고 정확한 응답 |
| **검증** | **업무 자료로 되짚어 갈 수 있는 출처(sources you can trace back)** |

모델을 바꾸는 것만으로는 "우리 회사 맥락을 아는 답"이 나오지 않습니다. Work IQ가 그 간극을 메우는 층입니다.

---

## 어디서 쓸 수 있나

Claude Fable 5.1은 **오늘부터** 자격 요건을 갖춘 사용자를 대상으로 다음 두 곳에 롤아웃됩니다.

- **Copilot Cowork**
- **Copilot Studio**

### 관리자가 알아야 할 것

> **가용성은 지역과 조직에 따라 다를 수 있습니다.**

관리자는 **Microsoft 365 관리 센터**를 통해 조직의 **접근 권한을 관리하고 가용성을 구성**할 수 있습니다.

즉 발표가 나왔다고 모든 사용자에게 자동으로 열리는 것이 아니라, **조직 설정에 따라 통제**됩니다.

---

## 도입 담당자를 위한 체크포인트

- **관리 센터에서 모델 정책부터 확인**: 조직에서 어떤 프런티어 모델을 허용할지 정책이 있다면, Fable 5.1을 그 목록에 넣을지 검토하세요. 관리 센터에서 접근 권한과 가용성을 구성할 수 있습니다.
- **지역별 가용성 확인**: 원문이 **지역(region)에 따라 다를 수 있다**고 명시합니다. 한국 테넌트에서의 실제 가용 여부를 확인해야 합니다.
- **Cowork 크레딧과 함께 보기**: Cowork에서 모델을 선택할 때 **노력 수준(effort level)** 과 함께 크레딧 소비가 결정됩니다. 새 모델을 열어 줄 때 **크레딧 사용 패턴 변화**를 함께 모니터링하는 것이 좋습니다.
- **적합한 작업 유형 안내**: 장시간 실행 작업, 재무 분석, 프런트엔드 시각 코딩에 맞춰 설계된 모델입니다. 사용자에게 **어떤 작업에 이 모델이 적합한지** 안내하면 모델 선택이 효율적으로 이뤄집니다.
- **Work IQ 그라운딩 전제 이해**: 그라운딩은 **사용자의 기존 권한 범위 안에서** 이뤄집니다. 원본 시스템 권한이 정리되어 있어야 결과도 적절해집니다.
- **출처 추적 활용**: 응답의 출처를 업무 자료로 되짚어 갈 수 있다는 점을 사용자에게 안내하세요. 특히 재무 분석처럼 **근거 확인이 필수인 작업**에서 중요합니다.

---

## 더 알아보기

Microsoft는 최신 롤아웃 정보를 다음에서 확인하라고 안내합니다.

- **Microsoft 365 Roadmap**
- **Microsoft Copilot 릴리스 노트**

모델 자체에 대해서는 **Anthropic의 Claude Fable 5.1 발표**를 참고하면 됩니다.

---

## 마무리

Copilot이 여러 프런티어 모델을 품는 방향은 이제 분명해 보입니다. 작업 성격에 따라 적합한 엔진을 고르고, **Work IQ가 그 위에 조직 맥락을 얹는** 구조입니다.

모델 선택지가 늘어난다는 것은 사용자에게 **판단할 거리가 늘어난다**는 뜻이기도 합니다. 어떤 작업에 어떤 모델을 쓸지 조직 차원의 간단한 기준을 마련해 두면, 새 모델이 추가될 때마다 혼선을 줄일 수 있습니다.

---

> **출처**
>
> - 원문 제목: *Available today: Anthropic Claude Fable 5.1 in Microsoft Copilot*
> - 링크: [https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/available-today-anthropic-claude-fable-5-1-in-microsoft-copilot/ba-p/4551974](https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/available-today-anthropic-claude-fable-5-1-in-microsoft-copilot/ba-p/4551974)
>
> 자세한 내용은 원문을 참조하세요.
