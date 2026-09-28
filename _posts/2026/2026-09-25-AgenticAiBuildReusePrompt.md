---
title: "에이전트를 만들기 전에 세 갈래로 나누세요: Microsoft의 Build, Reuse, Prompt"
date: 2026-09-25T00:00:00 KST
categories:
  - Copilot
tags:
  - AgenticAI
  - Microsoft365Copilot
  - Agent365
  - Cowork
  - Governance
  - Adoption
excerpt: "Microsoft 유럽 현장팀은 모든 AI 아이디어를 새 에이전트 개발로 연결하지 않았습니다. Build·Reuse·Prompt로 적합한 경로를 고르고, 초기부터 거버넌스와 운영 배포 절차를 안내한 도입 경험을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트를 만들기 전에 세 갈래로 나누세요: Microsoft의 Build, Reuse, Prompt

직원들이 AI 에이전트 아이디어를 쏟아내기 시작했다면 다음 과제는 무엇일까요? Microsoft Inside Track은 유럽 남부 현장팀의 경험을 통해, 도입의 중심이 사용 독려에서 **적합한 문제 선택, 신뢰, 운영 거버넌스**로 이동하고 있다고 설명합니다.

Microsoft는 20만 명이 넘는 조직에 Copilot을 확산하면서 데이터 품질과 거버넌스, 지속적인 변화 관리가 기반이라는 점을 배웠습니다. 에이전트가 여러 단계를 수행하고 결과를 가져오는 경험이 늘자, 매번 좋은 프롬프트를 작성하도록 교육하는 것만으로는 충분하지 않았습니다.

이 글은 Microsoft 내부의 도입 경험입니다. 원문에 등장하는 Cowork·Scout 등의 사내 활용을 특정 제품의 고객 대상 GA 발표나 전 지역 출시 안내로 읽어서는 안 됩니다.

---

## 프롬프트 교육에서 업무 위임으로 바뀌었습니다

초기 Copilot 도입에는 직원이 무엇을 어떻게 질문해야 할지 모르는 **프롬프트 격차**가 있었습니다. 반면 원문이 묘사한 에이전트 경험은 맥락을 유지하고 여러 단계를 수행하며, 제안만이 아니라 완료된 작업을 돌려주는 방향입니다.

Cowork와 Scout를 일상 업무에 활용한 사례는 동료 사이에서 확산되었습니다. 신뢰하는 동료가 반복 업무를 처리한 결과를 보여주면 다른 직원이 자기 업무에 적용할 아이디어를 얻는 방식입니다. 변화 관리팀의 역할도 사용을 밀어붙이는 것보다 이런 실험이 안전하게 확산될 조건을 만드는 쪽으로 바뀌었습니다.

## Build, Reuse, or Prompt로 먼저 분류합니다

Microsoft Europe South와 스페인의 Customer and Partner Solutions 팀 파일럿은 도구 교육부터 시작하지 않았습니다. 직원이 자신의 프로세스를 돌아보고 반복적·수작업·판단 중심 업무를 찾도록 도왔습니다.

그다음 모든 아이디어에 “정말 새로운 에이전트가 필요한가?”를 물었습니다.

| 경로 | 판단 방향 |
|---|---|
| **Build** | 기존 기능으로 해결하기 어렵고 새 에이전트가 실제 추가 가치를 만드는 문제 |
| **Reuse** | 다른 팀의 기존 솔루션이나 Cowork·Scout·GitHub Copilot 등의 경험을 활용할 수 있는 문제 |
| **Prompt** | 더 적절한 프롬프트나 기존 Copilot 기능으로 해결할 수 있는 문제 |

세 경로는 개발량을 늘리기 위한 분류가 아닙니다. **중복 개발을 줄이고 소유권을 분명히 하며 필요한 곳에만 구축 노력을 쓰기 위한 원칙**입니다. 경우에 따라 자동화 전에 프로세스 자체를 개선해야 합니다.

## 아이디어 수보다 평가의 충실도가 중요합니다

원문은 기존 에이전트 사용 현황, 기술적 실현 가능성, 해당 역할의 준비도, 가치 측정, 데이터·보안 조건을 함께 검토했다고 설명합니다. 좋은 아이디어가 기술팀에서만 나오는 것도 아니었습니다. 실제 업무에 가까운 직원이 불필요한 반복과 마찰을 발견했습니다.

한국 조직의 워크숍에도 같은 원칙을 적용할 수 있습니다. 아이디어 개수만 세기보다 담당 업무, 현재의 불편, 기존 도구로 가능한지, 필요한 데이터와 승인 주체를 함께 적도록 하는 방식입니다. 이 양식은 사례를 응용한 제안이며 Microsoft가 지정한 필수 서식은 아닙니다.

## 거버넌스를 마지막 심사가 아니라 초기 안내로

Microsoft 내부에서 승인된 채널로 에이전트를 게시하기 위해 거치는 절차로 원문은 다음을 열거합니다.

1. **Service Tree 등록**
2. **Security Development Lifecycle 및 Secure Future Initiative 검증**
3. **개인정보 평가**
4. **접근성 점검**
5. **Responsible AI 검토**

이는 Microsoft의 내부 운영 절차이며 고객 조직이 똑같은 이름의 시스템을 갖춰야 한다는 뜻은 아닙니다. 핵심은 개발이 끝난 뒤에 요구사항을 알리는 대신, 첫 만남부터 운영 배포에 이르는 경로를 보여줬다는 점입니다.

![방법론·거버넌스·협업의 중요성을 설명한 Microsoft Spain의 Doris Gomes](/mwkorea/assets/images/2026-09-25-AgenticAiBuildReusePrompt/image1.png)

요구사항이 일찍 보이면 직원은 실험 결과를 실제 운영에 연결하는 방법을 이해할 수 있습니다. 보안·개인정보·접근성 심사가 불확실한 장애물이 아니라, 잘 만드는 과정의 일부가 됩니다.

## Agent 365로 확산되는 에이전트를 파악합니다

원문은 Microsoft 테넌트의 여러 환경에 있는 에이전트를 모니터링하는 관리 계층으로 **Agent 365**를 사용한다고 설명합니다. 현장에서 만들어지는 에이전트가 보이지 않는 자산으로 늘어나지 않도록, 발견 가능성과 보안, 책임 소재를 유지하려는 접근입니다.

다만 이 사례는 모든 외부 환경과 임의의 에이전트를 아무 설정 없이 자동 관리한다는 보장이 아닙니다. 자체 조직에서는 관리 대상과 등록·모니터링 범위를 확인해야 합니다.

## 성과는 에이전트 수가 아니라 일의 변화입니다

다음 단계의 측정 대상은 마찰 감소, 업무 소요시간 단축, 후속 조치 개선, 더 가치 있는 활동에 쓸 시간입니다. 원문은 이 관점을 제시하지만 정량적인 개선율을 발표하지는 않습니다.

![조직의 업무 개선과 확산 경험을 설명한 Microsoft Spain의 Paco Salcedo](/mwkorea/assets/images/2026-09-25-AgenticAiBuildReusePrompt/image2.png)

예로 등장하는 **MSX-IQ**는 Microsoft 영업팀을 위한 내부 AI 도우미로, 영업 파이프라인과 대화하는 경험을 여러 국가에서 사용한다고 설명합니다. 이는 제품 목록을 늘리는 것보다 좋은 도구, 거버넌스, 지원을 함께 제공했을 때 확산이 가능하다는 사례입니다.

새 에이전트를 만드는 능력과 만들지 않아도 되는 문제를 구분하는 능력은 함께 필요합니다. 도입 프로그램을 설계한다면 Build·Reuse·Prompt 판단부터 시작하고, 운영 승인과 성과 측정을 같은 흐름에 넣어 보세요.

> 출처: [From the field: How agentic AI is reshaping adoption at Microsoft](https://www.microsoft.com/insidetrack/blog/from-the-field-how-agentic-ai-is-reshaping-adoption-at-microsoft/) — Microsoft Inside Track Blog, 원문 발행 2026년 9월 24일(UTC), 한국 시간 9월 25일.  
> 자세한 내용은 원문 참조.
