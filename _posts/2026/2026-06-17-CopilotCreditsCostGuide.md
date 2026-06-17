---
title: "Copilot Cowork 비용 관리 가이드 — Copilot Credits 비용 체계와 7월 1일 청구 전 관리자 설정"
date: 2026-06-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Cowork
  - CopilotCredits
  - WorkIQ
  - Billing
  - 비용관리
excerpt: "Copilot Cowork가 2026년 6월 16일 정식 출시(GA)되면서 7월 1일부터 Copilot Credits 기반 청구가 시작됩니다. 2계층 비용 체계와 크레딧 소비 방식, 구매 옵션, 그리고 6월 30일 전에 반드시 끝내야 하는 관리자 지출 정책 설정을 단계별 화면과 함께 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Cowork 비용 관리 가이드 — Copilot Credits 비용 체계와 7월 1일 청구 전 관리자 설정

**Copilot Cowork**가 2026년 6월 16일 전 세계 정식 출시(GA)되었습니다. Frontier 미리보기의 무료 사용 기간은 **6월 30일**에 끝나고, **7월 1일부터 실제 청구가 시작**됩니다. 이제 Cowork는 단순 기능이 아니라 **크레딧을 소비하는 클라우드 AI 워크로드**로 분류되므로, 관리자가 **지출 정책을 직접 설정**하지 않으면 예상치 못한 비용이나 서비스 중단이 발생할 수 있습니다.

이 글에서는 **Copilot Credits 비용 체계**(2계층 모델·크레딧 소비 방식·구매 옵션)와, **7월 1일 청구 시작 전에 반드시 끝내야 하는 관리자 설정**을 실제 화면과 함께 단계별로 정리합니다.

![Copilot Cowork 비용 관리 가이드 — 한국 엔터프라이즈 고객을 위한 Copilot Credits 비용 체계 및 관리자 설정 가이드](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide01.png)

> 본 글의 가격 정보는 **USD 기준이며 변경될 수 있습니다.** 관리자 설정 절차는 Microsoft Learn [사용량 기반 청구 관리 문서](https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits)를 기준으로 교차 검증했으며, 최신 가격·정책은 항상 공식 문서를 함께 확인하세요.

---

## 왜 지금 설정해야 하나 — Cowork GA와 7월 1일 청구

- **무료 사용 종료**: Frontier 미리보기 기간의 무료 크레딧 사용은 **6월 30일**까지입니다.
- **7월 1일 청구 시작**: Frontier 고객(3/30~6/16 사용분 포함)도 **7월 1일부터 동일하게 청구**가 시작됩니다.
- **워크로드로 전환**: Cowork는 이제 클라우드 AI 워크로드로 분류되어 **관리자 활성화 + 비용 정책 설정이 필수**입니다.
- **현재 지원 범위**: 사용량 기반 청구는 현재 **Copilot Cowork**와 **Work IQ API**에 적용되며, 추가 에이전트·서비스는 순차 지원됩니다.

> 설정을 마치지 않으면 7월 1일 이후 **서비스가 중단되거나 통제되지 않은 크레딧 소비**가 발생할 수 있습니다.

---

## 새 비용 체계 — 2계층 모델

Copilot Cowork 비용은 **고정 구독 + 실사용량 기반 크레딧**의 두 계층으로 구성됩니다.

| 계층 | 성격 | 포함 항목 |
|---|---|---|
| **계층 1 — 구독 라이선스** | 고정 비용 · 사용자당 월정액 | Microsoft 365 Copilot 라이선스, Copilot Chat(Word/Excel/PowerPoint/Outlook/Teams), Work IQ 컨텍스트 엔진, 사전 빌드 에이전트(Researcher·Analyst), Agent Builder |
| **계층 2 — Copilot Credits** | 변동 비용 · 실제 작업량 기반 | Cowork의 복잡한 멀티스텝 작업에 **별도 청구**, 팀이 위임한 작업량에 비례해 변동 |

> **핵심 원칙**: 계층 1 라이선스가 없으면 계층 2 Cowork에 접근할 수 없습니다. 두 계층은 상호 의존 관계입니다. 작은 팀의 가벼운 사용은 거의 0에 가깝고, 장시간 멀티 아웃풋 작업이 많을수록 의미 있는 소비가 발생합니다.

---

## 크레딧은 어떻게 소비되나 — 4가지 결정 요소

모든 태스크의 크레딧 비용은 아래 **4가지 인풋의 합**으로 계산됩니다.

- **모델(Models)** — 사용되는 AI 모델의 수준. 고성능 모델일수록 크레딧이 높아집니다.
- **컨텍스트(Context)** — 이메일·파일·회의·조직 데이터 등 검색 범위가 넓을수록 증가합니다.
- **도구(Tools)** — 이메일 전송, 문서 업데이트, 회의 예약 등 실행 횟수.
- **런타임(Runtime)** — 클라우드 오케스트레이션. 장시간 실행일수록 증가합니다.

### 태스크 유형별 예상 비용

| 유형 | 예시 작업 | 예상 크레딧 | PayGo 비용 |
|---|---|---|---|
| 경량(Light) | 주간 상태 업데이트, 간단한 요약 1개 | 100~300 | ~$1~$3 |
| 중간(Medium) | 회의 준비 문서 + Excel + 슬라이드 | 400~700 | ~$4~$7 |
| 중량(Heavy) | 6개월 데이터 분석 → 리더십 보고서 | 700+ | ~$7+ |

> PayGo 기준 **$0.01 / 크레딧**. 고성능 모델 사용 시 증가하며, 저비용 일상 작업에 특화된 **Cowork 1 모델** 출시 후 대폭 절감이 가능합니다.

---

## 크레딧 구매 옵션 3가지

조직의 사용 패턴과 예측 가능성에 따라 선택합니다.

| 옵션 | 가격 | 구매 경로 | 핵심 |
|---|---|---|---|
| **종량제(Pay-as-you-go)** | $0.01 / 크레딧 | Azure 구독 (MACC 적용) | 후불·사용한 만큼만, 선불 없음, 자동 확장. 월 비용 예측이 어렵고 대규모 사용 시 상대적 고비용 |
| **Capacity Packs** *(엔터프라이즈 권장)* | $200 / 테넌트 / 월 (25,000 크레딧) | M365 관리 센터 | 예측 가능한 월 예산, 직접 구매·확장, 초과분 자동 PayGo. 미사용분 매월 리셋(이월 불가) |
| **Pre-Purchase Plan (P3)** | 볼륨 기반 단계 할인 | Azure 구독 (MACC 적용) | 1년 선불 약정으로 **최대 비용 절감**. 사용량 과소 시 손실 리스크 |

> 청구 우선순위는 **선불(Capacity Packs / P3) → 종량제** 순서입니다. 선불 크레딧을 먼저 소진한 뒤 종량제로 자동 전환되므로, Capacity Packs를 쓰더라도 종량제 미터를 함께 켜 두면 서비스 중단을 방지할 수 있습니다.

---

## Work IQ API 별도 비용

**Work IQ API**는 타사 에이전트나 자체 개발 앱이 조직 데이터(이메일·캘린더·파일·채팅·사람 정보)를 이해하도록 돕는 API로, **동일 크레딧 풀에서 차감**됩니다. 모든 요청은 기존 M365 권한 정책을 준수해 거버넌스가 유지됩니다.

| API 유형 | 과금 | 크레딧 |
|---|---|---|
| Work IQ Tool API | 고정 | 0.1 크레딧 / API 호출 |
| Work IQ Chat API | 변동 | 시나리오 복잡도에 따라 |
| Work IQ Context API | 변동 | 시나리오 복잡도에 따라 |

시나리오별 예상 비용(Chat/Context API)은 경량 **~$0.20–$0.40**, 중간 **~$0.30–$0.75**, 중량 **~$0.50–$1.50**(호출당) 수준입니다.

> M365 기본 빌트인 에이전트(Cowork, Researcher 등)는 **추가 크레딧 없이** 기존 라이선스로 커버됩니다. Work IQ API 비용은 Copilot Studio·Foundry·타사 AI 플랫폼에서 동일 API를 호출할 때 발생합니다.

---

## 비용 관리 메뉴 위치 변경 — Copilot에서 청구 > 종량제로

기존에 **Copilot > Cowork** 하위에 있던 **Cowork 비용 관리 화면**이, 최신 Microsoft 365 관리 센터에서는 **청구(Billing) > 종량제(Pay-as-you-go)** 영역으로 **이동·통합**되었습니다. 가이드 캡처와 메뉴 위치가 다르게 보인다면 아래 경로를 확인하세요.

| 구분 | 경로 |
|---|---|
| 이전(구 메뉴) | Microsoft 365 관리 센터 → **Copilot** → **Cowork** → 비용 관리 |
| 현재(신 메뉴) | Microsoft 365 관리 센터 → **청구(Billing)** → **종량제(Pay-as-you-go)** → **서비스** 탭 → *Microsoft 365 Copilot* 행의 **정책 관리** |

**종량제** 페이지는 *"종량제 청구를 통해 서비스 사용량이 Azure 구독에 청구됩니다. 청구 정책을 생성하여 Azure 구독에 연결한 후, 서비스를 구성할 때 해당 정책을 선택하세요."* 라고 안내하며, 다음과 같이 구성됩니다.

- **탭**: 청구 정책 / 서비스
- **상단 버튼**: 비용 관리 보기(Cost management 대시보드로 이동) · 비용 예측
- **서비스 목록**: Microsoft 365 백업 · **Microsoft 365 Copilot** · 대용량 전자 메일 · Microsoft 365 SharePoint 스토리지
- 이미 정책이 연결된 서비스는 **정책 관리**, 아직 연결되지 않은 서비스는 **정책 연결**로 표시됩니다.

> 공식 문서는 현재까지 `Copilot > Cost management` 경로를 안내합니다. 본인 테넌트에 표시되는 메뉴로 진입하면 되며, 어느 경로든 도달하는 **비용 관리 대시보드와 지출 정책은 동일**합니다.

---

## [관리자] 7월 1일 전 설정 — 단계별 가이드

Microsoft 365 관리 센터에서 **Copilot → Cost management**(또는 위 **청구 > 종량제**) 경로로 진입합니다.

### 1. Cost Management 진입

**Copilot → Cost management**에서 *'6월 30일까지 요금 청구 없음'* 배너와 우측 **'13 days left'** 카드를 확인하고 **[지출 정책 설정]**을 클릭합니다.

![M365 관리 센터 Cost management 진입 — 6월 30일까지 요금 청구 없음 배너와 13 days left 카드](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide02.png)

### 2. 사용 기반 청구 활성화

*Unlock AI experiences by usage-based billing* 화면에서 대상(Copilot Cowork / Work IQ API)을 확인하고 **[시작]**을 눌러 지출 정책 구성을 시작합니다.

![사용 기반 청구 활성화 패널 — 시작 버튼](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide03.png)

### 3. 결제 방법과 범위 선택

**Capacity Packs**(25,000 크레딧/월·$200)를 선택하고 **'글로벌 크레딧 사용'** 토글을 켜면 테넌트 전체에 적용됩니다.

![지출 정책 구성 — 결제 방법(Capacity Packs)과 글로벌 크레딧 토글](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide04.png)

### 4. 발행 방식과 월 한도

**'발행 이후 방식'(권장)**을 선택합니다. 한도를 초과하면 **다음 달 1일까지 서비스가 차단**됩니다. 월별 지출 한도는 예시로 **10,000 크레딧**을 입력합니다(조직 규모·사용 패턴에 맞게 조정).

![지출 정책 구성 — 발행 방식 선택과 월 한도 입력](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide05.png)

### 5. 사용자 한도와 경고 알림

특정 사용자가 크레딧을 독점하지 않도록 **사용자당 월 1,000 크레딧** 한도를 설정하고, **경고 알림 이메일** 수신자를 등록합니다(IT 관리자 + 재무팀 권장).

![지출 정책 구성 — 사용자 한도와 경고 알림 이메일 설정](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide06.png)

### 6. All Users Policy 검토 후 활성화

정책 이름·대상·결제 방법·한도·알림을 전체 검토하고 **[활성화]**를 클릭합니다.

![All Users Policy 요약 검토 — 결제 방법, 월 한도, 사용자 한도, 경고](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide07.png)

---

## 트러블슈팅 — 활성화 오류와 Azure 리소스 그룹

활성화 시 **`copilot-credits-rg` 리소스 그룹을 찾을 수 없다**는 오류가 발생할 수 있습니다. 종량제(PAYG)는 Azure 구독에 연결되므로, 이 경우 Azure Portal에서 해당 리소스 그룹을 먼저 생성해야 합니다.

![활성화 오류 — copilot-credits-rg 리소스 그룹 미생성](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide08.png)

### Azure Portal에서 리소스 그룹 생성

**Azure Portal → 리소스 그룹 → 만들기**에서 이름은 **`copilot-credits-rg`**, 지역은 **Korea Central**(조직 데이터 상주 위치와 일치 권장)로 생성합니다.

![Azure Portal 리소스 그룹 생성 — 이름과 지역 입력](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide09.png)

리소스 그룹 목록에서 **`copilot-credits-rg`(Korea Central)**를 확인한 뒤 M365 관리 센터로 돌아가 동일 정책을 재시도합니다.

![Azure 리소스 그룹 목록에서 copilot-credits-rg 생성 확인](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide10.png)

### 활성화 성공과 최종 확인

*AI experiences enabled by usage-based billing are now available to all users* 메시지가 표시되면 성공입니다. **[구성 관리]**에서 부서별·그룹별 세부 정책을 추가할 수 있습니다.

![활성화 성공 — AI experiences enabled by usage-based billing](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide11.png)

마지막으로 **비용 관리 [구성] 탭**에서 *All Users Policy*가 활성 상태이고 설정값(월 10,000 / 사용자 1,000 / Capacity Packs + 종량제)이 맞는지 확인합니다.

![최종 확인 — 비용 관리 구성 탭의 All Users Policy](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide12.png)

---

## 주요 일정과 크레딧 공유 풀

| 일정 | 내용 |
|---|---|
| 2026.03.30 | Frontier GA — Frontier 고객 대상 정식 출시 |
| 2026.06.16 | 전 세계 GA — 정식 출시, 청구 준비 |
| 2026.06.30 | 무료 크레딧 사용 기간 마감 |
| 2026.07.01 | 지출 정책 적용 및 **실제 청구 시작** |
| 수 주 내 | **Cowork 1** 출시 — 저비용 일상 작업 특화 모델 |

크레딧은 **테넌트 전체 풀에서 공유**됩니다. 즉 **Copilot Cowork, Work IQ API, Copilot Studio, Dynamics 365 에이전트**가 동일한 크레딧 풀을 함께 소비하므로, 한도와 모니터링은 워크로드 전체를 합산해 계획해야 합니다.

---

## 관리자 액션 체크리스트

7월 1일 이전에 아래 항목을 완료하고 각 담당자에게 공유하세요.

| 항목 | 담당 |
|---|---|
| Azure 리소스 그룹 생성 | Azure 관리자 |
| M365 관리 센터 비용 관리 활성화 | 전역/청구 관리자 |
| 결제 방법 선택 및 연결 | 구매/재무팀 |
| 지출 정책 생성(All Users 기본) | IT 관리자 |
| 월별/사용자별 크레딧 한도 설정 | IT 관리자 |
| 경고 알림 이메일 수신자 등록 | IT + 재무팀 |
| Work IQ API 사용 타사 에이전트 현황 파악 | IT/개발팀 |
| 재무팀에 7월 1일 청구 시작 사전 공유 | IT 관리자 |
| Cowork 1 모델 출시 후 비용 절감 전환 검토 | IT/구매팀 |

---

## 참고 자료

- [Managing AI experiences enabled by usage-based billing — Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits) *(관리자 설정 절차 교차 검증 기준 문서)*
- [Optimize Copilot Credit costs with a pre‑purchase plan (P3) — Microsoft Learn](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/copilot-credit-p3)
- [Microsoft 365 관리자 역할 — Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles)

> 본 글의 가격은 USD 기준이며 변경될 수 있습니다. 화면의 구독·계정 정보는 데모 테넌트 값으로 일부를 블러 처리했습니다. 실제 적용 전 [공식 문서](https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits)에서 최신 가격·정책을 확인하세요.
