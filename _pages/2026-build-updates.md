---
title: "2026년 Microsoft Build 주요 업데이트"
layout: single
permalink: /hidden/2026-build-updates/
sitemap: false
excerpt: "2026년 6월 2~3일 열린 Microsoft Build에서 발표된 주요 소식을 정리해 전해드립니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 김현지
---

<div class="monthlycopilot-page monthlycopilot-page--tour">
<div style="background: #eef1f4; padding: 1.5rem; border-radius: 8px;">

<div style="background: #000; padding: 1.5rem; text-align: center;">
  <img src="/assets/images/20260605-build/build-title.png" alt="제목: BUILD" width="180" />
</div>
<div style="background: #0078d4; color: #fff; padding: 0.7rem 1rem; font-weight: 700;">
  2026년 Build 주요 업데이트
</div>

<div style="padding: 0 0.5rem;">

안녕하세요.

2026년 **Microsoft Build**에서 발표된 주요 소식을 정리해 전해드립니다.

**Microsoft Build**는 전 세계 개발자가 함께하는 마이크로소프트의 대표 연례 기술 행사로, 올해는 6월 2~3일 미국 샌프란시스코 현장과 온라인에서 열렸습니다. 차세대 AI 애플리케이션을 만들고 배포하고 확장하는 새로운 방향을 한자리에서 제시했습니다.

라이브를 놓치셨더라도 걱정하지 마세요. 주요 발표 내용은 아래에서 정리해 드렸으며, 전체 세션은 [Build 다시보기](https://build.microsoft.com/)를 통해 확인하실 수 있습니다.

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.35rem 0.85rem; border-left: 4px solid #0067b8;">AI 에이전트 플랫폼의 진화</h2>

<div class="mc-cover-kicker" style="margin-bottom: 0.8rem;">Frontier Development</div>

소프트웨어 개발이 큰 전환점을 맞고 있습니다. AI 에이전트는 단순히 거드는 도구를 넘어, 복잡한 일을 스스로 오랫동안 수행하는 **장기 실행(long-running)** 시스템으로 발전하고 있습니다. 개발자가 이런 에이전트를 오래 살아남는 경쟁력 있는 솔루션으로 키워 내려면, 디지털 동료로서 AI 에이전트 맥락을 포함한 지능(Intelligence)과 신뢰성(Trust)을 갖춰야 합니다.

이번 Build에서 Microsoft는 AI 중심 컴퓨팅을 위한 인프라와 에코시스템, 디바이스, 에이전트 플랫폼 및 도구, 모델은 물론, 모델을 넘어 도메인 특화된 추론(Reasoning) 역량을 강화하는 다양한 방안까지 폭넓게 선보였습니다.

**Microsoft Agent Platform Stack**은 AI를 만들고(build), 연결하고(connect), 실행하고(run), 관리하는(govern) 전 과정을 아우르는 시스템으로, 여러 에이전트가 한 팀처럼 협력해 실제 업무를 처리하도록 도와줍니다. 여기에 풍부한 업무 컨텍스트에 대한 데이터와 기업용 보안, 끊임없는 개선이 함께 제공됩니다.

<p style="text-align: center; margin: 1.2rem 0;">
  <img src="/assets/images/20260605-build/agent-platform-stack.png" alt="Microsoft Agent Platform Stack" style="max-width: 561px; width: 100%; height: auto;" />
</p>

- **GitHub Copilot app** — GitHub Copilot을 데스크톱 앱으로 새롭게 선보였습니다(현재 프리뷰). 아이디어나 기존 이슈, PR에서 작업을 시작해 여러 에이전트를 동시에 돌릴 수 있고, 코드 리뷰부터 CI, 병합(merge)까지 하나의 흐름으로 이어집니다. 각 작업은 git worktree 단위로 분리돼 서로 섞이지 않으며, 실제 실행은 Copilot이 맡되 모든 과정은 개발자가 직접 통제합니다.

- **Microsoft IQ** — 에이전트에 세상의 지식과 기업 내부 지식을 함께 연결해 주는 새로운 컨텍스트 계층으로, 오늘부터 GitHub Copilot, Microsoft Foundry, Copilot Studio에서 정식 제공됩니다. 모델 성능이 서로 비슷해지는 지금, 기업의 경쟁력은 더 이상 ‘좋은 AI를 쓸 수 있느냐’가 아니라 구성원이 일하는 방식과 사내 곳곳에 흩어진 지식을 하나로 모아 에이전트에 연결하는 능력에서 갈립니다.

- **Work IQ** — 에이전트가 ‘업무 맥락’을 이해하도록 돕는 지능(Intelligence) 계층입니다. Microsoft 365와 사내 시스템, 외부 소스에 흩어진 사람·이메일·문서·회의, 그리고 이들 사이의 연결 관계까지 파악해 실제로 일이 어떻게 돌아가는지를 읽어 냅니다. 이 정보를 코드에서 바로 활용할 수 있는 **Work IQ API**는 6월 16일 정식 출시됩니다.

- **Fabric IQ** — 매출 및 재고처럼 표로 정리된 정형 데이터를 에이전트가 일관되게 해석하도록, 공통의 의미 체계(시맨틱 계층)를 제공합니다.

- **Foundry IQ** — 위 요소들을 하나로 묶어, 사내 지식과 실시간 웹을 넘나들며 필요한 정보를 찾아 답을 구성하는 검색 및 추론(retrieval) 과정을 담당합니다.

- **Web IQ** — 이번에 새롭게 공개된 기능으로, 에이전트를 실시간 웹 정보에 가장 빠르게 연결합니다. AI에 최적화된 웹 검색 엔진으로 특정 모델에 얽매이지 않고(model-agnostic) MCP를 기본 지원하며, 콘텐츠 제공자(퍼블리셔)를 존중하는 방식으로 설계됐습니다. 동급 최고 수준보다 2.3배 빠르게 정보를 찾아 줍니다.

- **Rayfin** — 애플리케이션의 백엔드를 코드 안에서 바로 정의하고 Microsoft Fabric에 곧장 배포할 수 있는 오픈소스 SDK이자 CLI입니다. 엔터프라이즈급 보안과 확장성을 갖춰, 인프라를 따로 구성하지 않고도 GitHub 워크플로우만으로 프로토타입에서 실제 서비스까지 빠르게 끌어올릴 수 있습니다. 여기에 **Replit**과 협력해, 코딩 에이전트가 만든 프로토타입을 처음부터 거버넌스가 적용된 엔터프라이즈 환경으로 곧바로 옮길 수 있는 길도 마련했습니다.

- **Microsoft Foundry** — 에이전트를 더 쉽게 만들고 운영할 수 있도록 여러 기능을 새로 더했습니다. 먼저 인프라를 직접 관리할 필요 없이 에이전트를 배포 및 운영하는 **Hosted Agents**를 선보였고, **Fireworks AI**와 협력해 모델 학습과 파인튜닝(fine-tuning)을 Foundry의 거버넌스/운영 체계 안에서 그대로 수행할 수 있게 했습니다. 이 모든 과정은 **Foundry Control Plane** 한곳에서 관리되어, 모델·에이전트·인프라를 함께 다루면서 보안과 규정 준수, 비용까지 한눈에 통제할 수 있습니다. 또한 어떤 프레임워크에서도 쓸 수 있는 개방형 신뢰 체계도 공개했는데, 정책에 따라 안전성을 자동 점검하는 **ASSERT**와 에이전트의 동작을 어디서 어떻게 통제할지 표준화한 **Agent Control Specification** 두 오픈소스가 그 기반입니다.

- **Azure HorizonDB** — 까다로운 대규모 서비스까지 안정적으로 받쳐 주는 새로운 데이터베이스입니다. 초저지연(ultra-low latency) PostgreSQL을 기반으로 읽기 부하를 빠르게 분산하고(read scale-out) AI 기능을 내장했으며 Azure와 긴밀히 연동돼, 규모와 상관없이 미션 크리티컬 서비스를 든든하게 운영할 수 있습니다. VS Code의 GitHub Copilot, 데이터베이스 안에서 바로 쓰는 AI 모델, 고급 벡터 인덱싱(vector indexing)과 시맨틱(semantic) 검색까지 지원해 앱 개발 속도도 끌어올려 줍니다.

- **Agent 365 SDK** — 보안과 기업 요건을 갖춘 에이전트를 더 쉽게 만들 수 있도록 정식 출시됐습니다. 개발 단계에서부터 모니터링(observability)·접근 제어·규정 준수가 자동으로 적용되며, 어떤 AI 플랫폼에서 만든 에이전트라도 규정을 지키면서 Agent 365와 자연스럽게 연결할 수 있습니다.

- **Agent 365** — Entra·Defender·Purview를 하나의 관리 체계로 묶어, 데스크톱에서 도는 로컬 에이전트까지 포함한 모든 에이전트를 한곳에서 관찰하고 통제하고 보호할 수 있습니다. 그동안 보이지 않던 관리·보안의 사각지대를 없애 줍니다. **A365 Agent Registry**는 새로운 탐지 신호로 회사 곳곳에서 몰래 쓰이는 ‘관리되지 않는 에이전트’를 찾아내고, Defender·Entra·Intune·Purview가 함께 정책을 적용하고 위험을 잡아내며 민감 데이터를 지킵니다. 또 Windows에서 도는 에이전트를 위한 기본 보호 장치로 에이전트용 Windows 365와 **Microsoft Execution Container(MXC)**를 제공해, 로컬 에이전트가 처음부터 끝까지 안전하게 동작하도록 합니다. 덕분에 속도를 늦추지 않으면서도 빠르게 늘어나는 에이전트를 안전하게 관리할 수 있습니다.

- **MDASH (코드네임)** — 100개가 넘는 전문 AI 에이전트를 여러 모델로 함께 돌려 보안을 점검하는 시스템입니다. 주요 프로그래밍 언어로 작성된 코드 전반에서 취약점을 찾아내고, 단순히 의심되는 부분을 짚는 데 그치지 않고 실제로 악용이 가능한지까지 검증해 줍니다. 그 결과는 Defender 포털에서 바로 확인할 수 있어, 개발팀과 보안팀이 한층 탄탄하게 대비할 수 있습니다.

에이전트 시대에는 클라우드든 디바이스든 어디서나 똑같이 작동하는 인텔리전스 플랫폼이 필요합니다. 개발자에게 가장 중요한 건 강력한 에이전트를 만드는 동시에 주도권을 스스로 가지고 있는 것입니다. 툴이 준비되기를 기다리기보다, 바로 작업을 시작하고 몇 시간이 아니라 몇 분 안에 새로운 시도를 해볼 수 있는 환경이 핵심입니다.

- **Surface RTX Spark** — 오래 이어지는 모델 학습, 에이전트 기반 AI 파이프라인, 로컬 파인튜닝(fine-tuning)처럼 묵직한 작업을 위해 만든 개발자용 디바이스입니다. NVIDIA N1X Arm SoC를 기반으로 100W의 낮은 전력에서도 최대 1페타플롭(petaflop)의 AI 연산 성능과 128GB 통합 메모리를 제공해, 시끄러운 외부 GPU 서버 없이 책상 위에서 700억(70B) 규모의 모델까지 직접 돌릴 수 있습니다. GPU를 그대로 활용하는(GPU 패스스루) CUDA 지원 WSL 2가 미리 설정돼 있고, VS Code와 GitHub Copilot 등 주요 개발 도구도 기본 탑재됐습니다. 올해 하반기 출시 예정입니다.

- **Microsoft Execution Containers(MXC)** — OS 차원에서도 Microsoft는 Windows를 에이전트를 구축하고 실행하기에 가장 좋은 환경으로 만들고 있으며, 여기에는 OpenClaw도 포함됩니다. MXC는 SDK가 오늘 공개되고 Process·Session 컨테이너가 Windows Insider Program을 통해 프리뷰로 제공됩니다. 개발자와 IT 관리자는 이를 통해 에이전트를 위한 다양한 엔터프라이즈급 샌드박스 환경을 선택할 수 있으며, 격리(containment)는 운영체제 자체에서 직접 적용됩니다. 요구사항을 한 번만 정의하면, 에이전트가 실행되는 모든 곳에 Windows가 이를 적용합니다.

- **OpenClaw on Windows** — OpenClaw라는 기술이 이미 Windows에 적용되어 있어서, 운영체제(OS)가 정해둔 보안 범위 안에서 여러 단계를 거치는 작업(워크플로우)을 자동으로 실행할 수 있습니다.

- **NVIDIA OpenShell** — 선언형 에이전트 정책을 Windows의 MXC 기반 격리에 매핑하며, 샌드박싱, 파일 시스템 권한, 네트워크 정책, 자격 증명 처리, 추론(inference)까지 포괄합니다. 이를 통해 개발자에게는 개방형 런타임을, IT 부서에는 디바이스·가상 머신·클라우드 환경 전반에 걸친 일관된 가시성과 통제력을 제공합니다.

- **확장되는 협력** — NVIDIA와 OpenClaw 외에도 Windows는 OpenAI, Hermes, AMD 등 업계 선도 기업들과 협력하여, 구축 중인 격리 기술이 개발자의 실제 요구를 충족하도록 하고 있습니다.

- **Microsoft Scout** (Frontier Preview) — Microsoft가 처음 선보이는 ‘오토파일럿(autopilot)’ 개념의 데스크톱에서 실행되는 에이전트로, 항상 켜져 있는 상태에서 사용자를 대신해 스스로 업무를 처리하는 새로운 유형의 AI입니다. 백그라운드에서 지속적으로 작동하면서 여러 앱과 시스템에 걸친 업무 흐름을 이해하고, 매번 지시하지 않아도 필요한 일을 알아서 챙깁니다. 또한 매일 사용하는 Microsoft 365 앱에 자연스럽게 통합되어, 클라우드·데스크톱·웹 환경을 넘나들며 Teams, Outlook, OneDrive, SharePoint는 물론 채팅·이메일·일정·연락처 등 업무에 필요한 데이터와 연결됩니다.

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.35rem 0.85rem; border-left: 4px solid #0067b8;">AI 지능의 확장</h2>

<div class="mc-cover-kicker" style="margin-bottom: 0.8rem;">Frontier Opportunities</div>

모델 측면에서는, Microsoft AI Superintelligence Team이 자체 개발한 최신 세대 모델들을 새롭게 공개했습니다.

- **MAI-Thinking-1** — Microsoft AI가 내놓은 첫 텍스트·추론·코딩 모델입니다. 350억 개의 활성 파라미터와 128K 길이의 컨텍스트를 갖췄고, 적은 비용으로도 높은 성능을 내도록 설계됐습니다. 여러 단계로 이어지는 복잡한 지시 수행, 긴 맥락을 따라가는 추론, 코드 생성에 특히 강하며 빠르고 안정적으로 동작합니다. 현재 Microsoft Foundry에서 프라이빗 프리뷰로 사용해 보실 수 있습니다.

- **MAI-Image-2.5** — 글로 설명하면 이미지를 만들어 주고(text-to-image), 기존 이미지를 새로운 이미지로 바꿔 주는(image-to-image) 기능을 모두 갖춘 Microsoft의 첫 이미지 모델입니다. 머릿속 아이디어를 곧바로 시각화하거나 기존 결과물을 다듬을 때 유용해, 다양한 개발 작업에 폭넓게 쓸 수 있습니다.

- **MAI 모델 제품군 확장** — 이 외에도 여러 모델이 새로 합류했습니다. **MAI-Transcribe-1.5**는 업계 최고 수준의 음성 인식 정확도에, 사람·제품명 같은 고유 명칭을 더 정확히 알아듣는 기능(entity biasing)을 더했고 실시간 스트리밍도 곧 지원합니다. **MAI-Voice-2**는 10개 이상의 언어를 새로 지원하며 다양한 목소리를 제공합니다. **MAI-Code-1**은 Flash와 Pro 두 가지로 나와 GitHub Copilot과 VS Code에 최적화돼 있습니다. 이들 멀티모달 모델은 지금 Microsoft Foundry와 MAI Playground에서 바로 써 보실 수 있습니다.

- **Frontier Tuning** — 회사의 데이터와 업무 방식을 학습 재료로 삼아, 규정을 지키는 범위 안에서 강화학습(reinforcement learning)으로 AI를 그 회사에 꼭 맞게 길들이는 새로운 방식입니다. 현재 전담 엔지니어(Forward Deployed Engineer)를 통해 프라이빗 프리뷰로 제공되며, Microsoft Copilot Studio와 Microsoft Foundry에서도 곧 만나보실 수 있습니다.

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.35rem 0.85rem; border-left: 4px solid #0067b8;">차세대 혁신</h2>

<div class="mc-cover-kicker" style="margin-bottom: 0.8rem;">New Frontiers</div>

장기 실행 에이전트가 소프트웨어 개발과 개발자의 역할을 바꿔 놓았듯, 이제 새로운 에이전트가 연구개발(R&D)과 과학자가 일하는 방식까지 바꾸기 시작했습니다.

- **Microsoft Discovery** — 오늘 정식 출시됐습니다. Foundry와 GitHub Copilot을 기반으로, 연구자가 가설을 세우고 실험하고 결과를 분석하는 연구의 전 과정을 에이전트가 돕는 플랫폼입니다. 실제로 광산기업 BHP는 이를 활용해 구리 추출(copper-leaching) 공정을 몇 년이 아닌 몇 달 만에 찾아내고 있고, Syensqo는 반도체 냉각 연구를, GSK는 신약 개발을 앞당기고 있습니다. 더 많은 연구자가 부담 없이 쓸 수 있도록, 개인 PC에 직접 설치해 사용하는 무료 버전도 함께 제공됩니다.

- **Majorana 2** — 차세대 양자 프로세서로, 양자 컴퓨터를 실제 규모로 키우는 데 한 걸음 더 다가선 성과입니다. 이전 세대인 Majorana 1보다 큐비트 안정성을 1,000배 높였고, 소재를 알루미늄에서 납으로 바꾼 새로운 구조를 적용했습니다. 덕분에 신용카드보다 작은 칩 하나에 큐비트 100만 개를 담을 수 있는 길이 열렸습니다.

<hr/>

<div style="background: #f6f8fa; padding: 1.2rem; border-radius: 8px; margin-top: 1.4rem;">

<h2 style="margin-top: 0; padding: 0.35rem 0.85rem; border-left: 4px solid #0067b8;">더 알아보기</h2>

- **발표 내용 한눈에 보기** — [Microsoft Build 라이브 블로그](https://aka.ms/microsoft-build-2026-live-blog)와 [공식 Microsoft 블로그](https://aka.ms/AA10pe80)에서 이번에 발표된 모든 소식을 확인하세요.
- **원하는 방식으로 세션 보기** — 주요 세션을 [라이브와 다시보기](https://build.microsoft.com/)로 시청하고, [세션 카탈로그](https://aka.ms/MSBuildSessions)에서 필요한 주제를 골라 보세요.
- **한 걸음 더 배우기** — 행사 자료와 새로 추가된 자격증을 살펴보고, [Microsoft AI Skills Fest](https://aka.ms/aiskillsfest)에서 역량을 한층 더 키워 보세요.
- **터미널에서 직접 써 보기** — GitHub Copilot CLI와 [Microsoft Build CLI](https://aka.ms/MS_Build_FY26_Github)로 터미널에서 바로 Build를 경험해 보세요.

</div>

감사합니다.

</div>
</div>
</div>
