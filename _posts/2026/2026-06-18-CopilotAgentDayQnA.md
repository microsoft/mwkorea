---
title: "Copilot & Agent Day 현장 Q&A — 자주 나온 질문 12가지 총정리"
date: 2026-06-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - Cowork
  - Scout
  - Agent365
  - CopilotStudio
  - License
  - FAQ
excerpt: "Copilot & Agent Day 현장에서 모인 질문을 주제별로 묶어 12개 핵심 질문으로 정리했습니다. 가격·라이선스·Cowork와 Scout의 차이·Copilot Studio 배포까지 한 번에 확인하세요. 배포용 PDF도 함께 제공합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot & Agent Day 현장 Q&A — 자주 나온 질문 12가지

지난 **Copilot & Agent Day** 현장에서 참석자분들이 남겨주신 질문이 정말 많았습니다. 비슷한 질문은 하나로 합치고, **가격·라이선스·제품 비교·도입 일정·사용법** 등 주제별로 묶어 핵심 12가지로 정리했습니다.

가격이나 라이선스처럼 헷갈리기 쉬운 부분은 공식 문서와 발표 내용을 토대로 최대한 정확하게 답하려 했습니다. 현장에서 받은 질문을 그대로 살려, 같은 고민을 하셨던 분들께 도움이 되도록 구성했습니다.

> 📄 **배포용 PDF 다운로드:** [Copilot & Agent Day Q&A 12선 — PDF로 받기](/mwkorea/assets/files/2026-06-18-CopilotAgentDayQnA.pdf)

> **표기 안내** · ✅ 공개된 제품 사실 · ⚠️ 조직·계약별로 다른 항목(담당 계정팀·파트너·사내 IT 확인) · 💲 가격은 글로벌 발표 기준(국내 가격·조건은 영업/파트너 확인)

---

## 가격 · 과금

### Q1. 코파일럿/코워크는 지금 무료인가요? ✅

- **Copilot Chat은 포함, 무료.** 자격이 되는 Microsoft 365 구독(E3/E5, Business 등)이 있으면 **Microsoft 365 Copilot Chat**(웹·일부 업무 그라운딩)이 추가 비용 없이 포함됩니다.
- **풀 기능 Microsoft 365 Copilot은 유료 Add-on 라이선스**입니다(글로벌 출시가 사용자당 월 $30 💲).
- **Cowork(코워크)는 2026년 6월 정식 출시(GA)** 됐습니다. 별도 무료 제품이 아니라 **Microsoft 365 Copilot 라이선스가 있는 모든 테넌트**(tier-1 언어)에서 쓸 수 있는 기능이며, **사용량 기반(usage-based) 과금**이 적용됩니다.

> 한 줄 요약: **Copilot Chat = 자격 구독에 무료 포함 / 풀 Copilot = 유료 Add-on / Cowork = GA(정식 출시), M365 Copilot 라이선스 + 사용량 기반 과금.**

### Q2. 코워크 과금 체계는 어떻게 되나요? 교육·변화관리 프로그램은? ⚠️💲

- **Cowork는 이미 정식 출시(GA, 2026년 6월)** 됐습니다. "유료 전환"을 기다릴 필요 없이, 지금 **모든 Microsoft 365 Copilot 테넌트**(tier-1 언어)에서 사용할 수 있습니다.
- **과금은 사용량 기반(usage-based) 빌링**입니다. 관리자는 **Microsoft 365 관리 센터**에서 사용량을 확인하고 **사용자별·그룹별 한도**를 설정할 수 있으며, 소비량은 pay-as-you-go(Copilot Credits) 방식으로 측정됩니다.
- 사용 전제 조건(공식):

| # | 조건 | 내용 |
|---|---|---|
| 1 | Microsoft 365 Copilot 라이선스 | 사용자 계정에 라이선스 할당 |
| 2 | 사용량 기반 빌링 활성화 | 테넌트에 usage-based billing 설정 |
| 3 | Anthropic 모델 사용 허용 | Cowork는 Claude(Opus·Sonnet) 등 Anthropic 모델을 하위처리자(subprocessor)로 사용. 모델 선택기에 GPT 5.5도 포함 |

- 교육·변화관리는 도입 시 **담당 계정팀·파트너 또는 사내 IT와 함께 채택(Adoption) 계획을 설계**하는 것을 권장합니다. ⚠️

## 라이선스 · 사용 조건

### Q3. Cowork은 M365 Copilot 없이 별도로 쓸 수 있나요? 라이선스 구독 시 사용 가능한가요? ✅

- Cowork는 **Microsoft 365 Copilot의 기능**이므로 **M365 Copilot 라이선스가 필요**하고, **단독(standalone) 사용은 불가**합니다.
- **2026년 6월 GA**로, 이제 Frontier 등록 없이도 **모든 M365 Copilot 테넌트**에서 사용할 수 있습니다(테넌트에 사용량 기반 빌링과 Anthropic 모델 사용이 활성화되어 있어야 함). 즉 *"Copilot 라이선스가 있으면 쓸 수 있는, 사용량 기반 과금 기능"* 이 맞습니다.

## 제품 비교

### Q4. Cowork와 Scout의 차이는 무엇인가요? ✅

| 구분 | **Cowork (코워크)** | **Scout (스카우트)** |
|---|---|---|
| 성격 | 요청형(on-demand) 실행 비서 | 상시형(always-on) **Autopilot** |
| 동작 | 내가 위임 → 계획 수립 → 백그라운드 실행, **민감 작업은 내가 승인** | 매번 프롬프트하지 않아도 백그라운드에서 **자율적으로** 일정 조율·리스크 감지 |
| 위치 | Microsoft 365 Copilot 안 | 데스크톱 앱 + Teams (자체 **Entra ID**로 동작) |
| 공통점 | 둘 다 **Work IQ** 기반 | 〃 |

> 한 줄: **Cowork = 시키면 끝내는 실행 비서 / Scout = 알아서 챙기는 상시 에이전트.**

### Q5. 기존 Copilot Chat과 Cowork 도입 시 차별점은? ✅

- **Copilot Chat = "답변" 중심** — 검색·초안 작성 등 묻고 답하기.
- **Cowork = "실행" 중심** — 이메일 전송·회의 조정·문서 생성 같은 멀티스텝 작업을 *계획 → 백그라운드 실행 → 체크포인트/승인* 으로 처리합니다. 슬로건이 **"대화에서 행동으로(from conversation to action)"** 입니다.

## 도입 일정 · 로드맵

### Q6. Scout 도입일과 크레딧 계산(Credit Calculation) 공유 일정은? ⚠️

- **공개 현황:** Scout는 Microsoft가 새로 발표한 **'Autopilot'(상시 자율 에이전트)** 범주의 첫 제품으로, 현재 **Frontier 프로그램의 실험적(experimental) 프리뷰**(일부 고객 private preview)입니다. **공식 GA 일정은 미발표**입니다.
- **설치 요건(공식):** Frontier 등록 + Intune 정책 구성 + opt-in 동의 + **GitHub Copilot 라이선스**가 있으면 데스크톱 환경을 설치할 수 있습니다. (설치 안내: `learn.microsoft.com/microsoft-scout`)
- 구체적인 **도입 시점과 크레딧 산정·공유 일정은 조직·계약별로 다릅니다** → 담당 계정팀·파트너 또는 사내 IT로 확인하세요. ⚠️

### Q7. 클로드코드 같은 코딩 어시스턴트 도입 계획이 있나요? 있다면 언제쯤? ⚠️

- **제품 차원:** GitHub Copilot 계열로 이미 제공됩니다.
  - **Copilot 코딩 에이전트** — GitHub 이슈를 맡기면 코드 작성·PR 생성까지 자동 (GA)
  - **GitHub Copilot 앱** — 에이전트 네이티브 데스크톱 (기술 프리뷰)
  - **Copilot CLI** — 터미널 환경
  - **Copilot SDK** — 직접 도구 제작용 (GA)
- 'Claude Code'식 **터미널형 자율 코더**에 가장 가까운 조합은 **Copilot CLI + 코딩 에이전트**입니다.
- 조직 내 사내 도입 계획·시점은 ⚠️ 별도 결정 사항으로, 담당팀 확인이 필요합니다.

## 교육 · 매뉴얼 · 채널

### Q8. Copilot 라이선스 취득 교육과정 등 정보가 궁금합니다. ✅

- 별도의 'Copilot 라이선스 자격시험'은 없지만, **Microsoft Learn**(`learn.microsoft.com`)의 역할별 학습 경로와 **Copilot 채택 허브**(`adoption.microsoft.com`)에서 **무료로** 학습할 수 있습니다.
- Copilot Studio·에이전트 등 주제별 학습 모듈과 실습 콘텐츠가 제공됩니다.

### Q9. Copilot의 다양한 메뉴·기능에 대한 상세 매뉴얼이 있나요? ✅

- 네. **Microsoft Learn**(`learn.microsoft.com/copilot`, `/microsoft-365/copilot`)의 기능별 문서, **`support.microsoft.com`** 사용 가이드, **Copilot 채택 허브**의 시나리오별 안내가 있습니다.

### Q10. M365를 넘어 Agent 365 생태계를 한눈에 볼 공식 채널이 있나요? ✅

- 네. **공식 제품 페이지:** `microsoft.com/microsoft-agent-365`, **문서 허브:** `learn.microsoft.com/microsoft-agent-365/overview`.
- Agent 365는 조직 내 모든 에이전트를 **관측·거버넌스·보안**(Entra Agent ID + Defender + Purview + Intune)하는 **'에이전트용 컨트롤 플레인'** 입니다. (Ignite 2025에서 발표, 이후 일반 공급(GA))
- 업데이트는 **Microsoft 365 로드맵**(`microsoft.com/microsoft-365/roadmap`)과 Tech Community 블로그에서 추적할 수 있습니다.

## 사용법 · 기술

### Q11. 컨텍스트가 꽉 차 대화가 끊길 때, 새 채팅에서 이어가는 가장 좋은 방법은? ✅

- **① 핸드오프 요약:** 끊기기 전에 *"지금까지 내용을 요약해줘"* → 그 요약을 새 채팅 첫 메시지로 붙여넣기.
- **② 맥락 외부화:** 중요한 배경·결정사항은 **파일/메모로 저장**하고 새 대화에 첨부·그라운딩 소스로 연결.
- **③ 반복 업무는 저장:** 자주 쓰는 흐름은 에이전트/프롬프트로 저장해 재사용.
- **④ 상시 에이전트 활용:** Scout·Cowork처럼 **Work IQ로 맥락을 지속 보관**하는 에이전트는 세션이 바뀌어도 맥락 유지에 유리합니다.

> 핵심: 맥락을 "대화창"이 아니라 **"파일·요약·에이전트 메모리"** 에 두세요.

### Q12. Copilot Studio 에이전트를 Teams 앱스토어에 특정 그룹 대상으로 배포할 수 있나요? ✅

- **네, 가능합니다.** Copilot Studio에서 Teams 채널로 게시하면 Teams 앱으로 등록되고, **Teams 관리 센터의 앱 설정/권한 정책(app setup & permission policies)** 으로 **특정 사용자·보안 그룹**에만 노출·배포할 수 있습니다.
- 또한 게시 시 **'공유 사용자(shared users)'** 에게만 'Built with Power Platform' 섹션에 노출하거나, **Microsoft 365 관리 센터의 에이전트 승인·배포** 흐름으로 대상 그룹을 제어합니다.
- 즉, 전사 일괄이 아닌 **그룹 단위 타깃 배포**를 지원합니다.

---

## 마무리

현장에서 주신 **"에이전트 실습 시간을 늘리고 세션을 더 자주 열어달라"** 는 의견도 잘 받았습니다. 다음 회차 기획에 반영하겠습니다. 🙌

위 12개 질문은 [배포용 PDF](/mwkorea/assets/files/2026-06-18-CopilotAgentDayQnA.pdf)로도 정리해 두었으니, 팀에 공유하거나 인쇄해 활용하세요.

> 본문은 Microsoft 공식 블로그와 [Microsoft Learn](https://learn.microsoft.com) 문서를 토대로 정리했습니다. 프리뷰 단계 제품의 가격·일정·기능은 변경될 수 있으니, 도입 의사결정 시 공식 페이지와 담당 영업/파트너를 통해 최종 확인하시기 바랍니다.
