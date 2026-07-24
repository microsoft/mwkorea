---
title: "GitHub Copilot과 Excel을 위한 MAI 모델: 제품 스택 안에서 '힐 클라이밍'으로 키운 효율 모델"
date: 2026-07-24T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftAI
  - MAI
  - GitHubCopilot
  - Excel
  - AgenticModels
  - HillClimbing
excerpt: "Microsoft AI가 GitHub Copilot과 Excel에 특화된 MAI 모델 사례를 공개했습니다. GitHub Copilot 하니스에서 후속 학습한 MAI-Code-1-Flash를 출발점으로 Excel 평가에서 '힐 클라이밍'해, 더 작고 효율적이면서 GPT-5.6에 준하는 품질의 특화 모델을 만들었습니다. 모델·하니스·에이전트·제품 평가를 아우르는 전체 스택 접근이 핵심입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# GitHub Copilot과 Excel을 위한 MAI 모델: 제품 스택 안에서 '힐 클라이밍'으로 키운 효율 모델

에이전트 제품의 품질은 결국 그 아래에서 돌아가는 모델에 크게 좌우됩니다. 그런데 가장 크고 비싼 최신 모델만이 답일까요? Microsoft AI는 이 질문에 "제품 스택 전체를 활용하면 더 작고 효율적인 모델로도 같은 일을 해낼 수 있다"고 답합니다.

Microsoft AI가 GitHub Copilot과 Excel에 특화된 **MAI 모델** 사례를 공개했습니다. 6월 Build에서 소개한 **힐 클라이밍 머신(hill-climbing machine)** — 데이터·모델·하니스(harness)를 통합한 플라이휠 — 을 실제 제품에 적용한 첫 결과입니다.

> **한 줄 요약**
> GitHub Copilot 하니스에서 후속 학습한 MAI-Code-1-Flash를 출발 체크포인트로 삼아 Excel 평가에서 힐 클라이밍한 결과, 더 작고 효율적이면서도 가장 흔한 작업에서 GPT-5.6에 준하는 품질의 특화 모델 두 개를 만들었습니다.

![MAI-Code-1-Flash를 출발점으로 Excel 평가에서 힐 클라이밍하는 과정을 보여주는 도표](/mwkorea/assets/images/2026-07-24-MAIHillClimbingGithubCopilotExcel/image1.png)

---

## 더 좋은 모델, 더 적은 파라미터, 더 적은 토큰

이번 발표의 핵심 메시지는 "더 큰 모델"이 아니라 **더 효율적인 모델**입니다. 라이브 제품 배포에서 Excel에 투입된 MAI 모델은 가장 흔한 작업에서 GPT-5.6과 대등한 품질을 보이면서도 비용 효율이 더 높았습니다.

## MAI-Code-1-Flash in GitHub Copilot

6월 GitHub Copilot에 MAI-Code-1-Flash를 출시한 이후, 수백만 명의 개발자가 일상 업무에 사용하고 있으며 유사한 크기의 다른 모델들을 능가하는 성과를 보이고 있습니다.

- VS Code에서 GPT-5.4 Mini·Claude Haiku 4.5 대비 **코드 수락률(code accept rate)이 약 10% 높음**
- 개발자가 여러 날에 걸쳐 다시 사용할 확률이 GPT-5.4 Mini 대비 **6%**, Claude Haiku 4.5 대비 **11%** 높음
- GPT-5.4 mini·Claude Haiku 4.5 대비 **중앙값 토큰 사용량이 10% 낮으면서도** 사용자 주도 턴(turn)은 더 많음

즉, 더 적은 토큰으로 더 자주 쓰이는 모델이라는 의미입니다.

## Excel에 투입된 MAI 모델

Excel은 중요한 시험대였습니다. MAI-Code-1-Flash에 담긴 역량이 **학습된 도메인을 넘어 전이(transfer)될 수 있는가**, 즉 에이전틱 코딩에서 에이전틱 지식 노동으로 옮겨갈 수 있는가를 확인하는 자리였기 때문입니다.

이를 위해 MAI-Code-1-Flash 체크포인트를 **Excel 강화학습(reinforcement learning) 환경**에서 추가로 학습시켜, 스프레드시트의 도구와 지식 워크플로를 익히게 했습니다. 그 결과 Excel 워크플로를 능숙하게 다루면서도 더 효율적이고 실행 비용이 낮은 모델이 만들어졌습니다.

프로덕션 트래픽의 사용자 피드백에 따르면 Excel의 MAI 모델은 가장 흔한 작업에서 GPT-5.6과 대등한 품질입니다. 여기에 더해 이 더 작고 효율적인 모델은 최신 세대 가속기만 요구하는 대신 **Nvidia H100과 A100급 GPU 모두에서 서빙**할 수 있어, Microsoft 입장에서 배포 비용을 크게 낮춥니다.

## 제품 스택 안에서 에이전틱 모델을 학습시키다

이 결과들은 더 넓은 전략을 가리킵니다. **모델, 그 모델을 실행하는 하니스, 에이전트, 제품별 평가**라는 전체 제품 스택에 접근할 수 있기 때문에, 이전에는 더 크고 비싼 모델이 처리하던 작업을 효율적이고 강력한 모델로 힐 클라이밍하며 학습시킬 수 있다는 것입니다.

GitHub Copilot과 Excel을 넘어, Microsoft는 이 힐 클라이밍 접근을 **Copilot Chat, Outlook, PowerPoint** 등 Microsoft의 에이전틱 제품군 전반으로 확장하고 있습니다.

## Copilot·에이전트 관점에서의 시사점

- **모델은 곧 비용이자 품질**: 같은 작업을 더 작은 모델로 처리하면 응답 속도·서빙 비용·확장성이 함께 개선됩니다.
- **도메인 전이 가능성**: 코딩용으로 학습한 모델이 Excel 지식 노동으로 전이됐다는 점은, 특화 에이전트 모델이 여러 제품으로 퍼질 수 있음을 시사합니다.
- **제품에 내장된 평가의 중요성**: 제품별 실사용 평가(product-specific evaluations)가 모델 개선의 나침반 역할을 합니다.
- **하드웨어 유연성**: 최신 가속기에만 묶이지 않는 모델은 도입·확장 관점에서 실질적 이점이 큽니다.

## 마무리

이번 사례는 "가장 큰 모델을 쓰는 것"이 아니라 "제품 스택 전체를 활용해 딱 맞는 효율 모델을 키우는 것"이 Copilot·에이전트 품질을 끌어올리는 또 다른 길임을 보여줍니다. GitHub Copilot과 Excel에서 시작된 이 접근이 Copilot Chat·Outlook·PowerPoint로 확산되는 과정을 지켜볼 만합니다.

---

> **원문**: [Hill-Climbing MAI models for GitHub Copilot and Excel (Microsoft AI Blog)](https://microsoft.ai/news/hill-climbing-mai-models-for-github-copilot-and-excel/)
>
> 자세한 내용은 원문을 참조하세요.
