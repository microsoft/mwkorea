---
title: "Copilot Cowork 비용 관리 가이드 — Copilot Credits 지출 정책 설정 (엔터프라이즈 관리자용)"
date: 2026-06-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Cowork
  - CopilotCredits
  - Billing
  - 비용관리
  - WorkIQ
excerpt: "Copilot Cowork와 Work IQ API의 사용량 기반 과금(Copilot Credits)을 안전하게 통제하는 방법을 정리했습니다. 결제 방법 선택부터 조직·사용자 월별 한도, 경고 알림, 부서별 정책까지 Microsoft 365 관리 센터에서 지출 정책을 설정하는 전 과정을 공식 문서와 교차 검증해 단계별로 안내합니다. 또한 비용 관리 메뉴가 '청구 > 종량제'로 이동된 변경 사항도 함께 다룹니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Cowork 비용 관리 가이드 — Copilot Credits 지출 정책 설정

Microsoft 365 Copilot이 **고정 라이선스**를 넘어 **사용량 기반 과금(usage-based billing)** 으로 확장되고 있습니다. 그 중심에 있는 것이 바로 **Copilot Credits** 입니다. **Copilot Cowork** 와 **Work IQ API** 같은 AI 경험은 이제 크레딧을 소비하며 동작하고, 관리자는 이 크레딧을 **조직 차원에서 할당·제한·모니터링** 해야 합니다.

이 글은 엔터프라이즈 관리자가 Microsoft 365 관리 센터에서 **지출 정책(Spending policy)** 을 설정하는 전 과정을, Microsoft 공식 문서와 **교차 검증**하여 단계별로 정리한 가이드입니다.

![Copilot Cowork 비용 관리 가이드 — 엔터프라이즈 관리자를 위한 Copilot Credits 정책 구성 가이드](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide01.png)

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
  <strong>이 글의 한 줄 요약</strong><br/>
  설정을 하지 않으면 크레딧이 <strong>통제 없이 소모</strong>될 수 있습니다. <strong>결제 방법 → 조직 월별 한도 → 사용자별 한도 → 경고 알림</strong> 순서로 기본 지출 정책을 먼저 만들고, 이후 부서별 정책으로 세분화하세요.
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f0fdf4; border: 1px solid #bbf7d0; color: #065f46;">
  📘 <strong>공식 문서(참조 및 교차 검증 기준)</strong><br/>
  본 가이드의 모든 절차와 수치는 아래 Microsoft Learn 문서를 기준으로 검증했습니다.<br/>
  <a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits">Managing AI experiences enabled by usage-based billing — Microsoft Learn</a>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fffbeb; border: 1px solid #fde68a; color: #78350f;">
  ⚠️ <strong>적용 범위</strong><br/>
  사용량 기반 과금(Copilot Credits)은 현재 <strong>Copilot Cowork</strong> 와 <strong>Work IQ API</strong> 에만 적용됩니다. Microsoft는 더 많은 에이전트·서비스를 이 경험으로 편입할 예정입니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #dc2626; background: #fef2f2;">🚨 [중요] 비용 관리 메뉴가 이동되었습니다</h2>

기존에 **Copilot 메뉴 하위(Copilot > Cowork)** 에 있던 **에이전트 비용 관련 화면**이, 최신 Microsoft 365 관리 센터에서는 **청구(Billing) > 종량제(Pay-as-you-go)** 영역으로 **이동·통합**되었습니다. 가이드용 캡처와 메뉴 위치가 다르게 보인다면 아래 경로를 확인하세요.

![Copilot > Cowork 관리 페이지에 표시된 평가 기간 만료 경고와 지출 정책 설정 안내](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide03.png)
*▲ Copilot > Cowork 관리 페이지의 평가 기간 만료("13 days left") 경고와 "지출 정책 설정" 진입 버튼*

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #fef2f2; border: 1px solid #fecaca; color: #7f1d1d;">
    <strong>❌ 이전 경로 (구 메뉴)</strong><br/>
    <span style="font-size: 0.95em;">Microsoft 365 관리 센터 → <strong>Copilot</strong> → <strong>Cowork</strong> → 비용 관리</span>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #ecfdf5; border: 1px solid #a7f3d0; color: #065f46;">
    <strong>✅ 현재 경로 (신 메뉴)</strong><br/>
    <span style="font-size: 0.95em;">Microsoft 365 관리 센터 → <strong>청구(Billing)</strong> → <strong>종량제(Pay-as-you-go)</strong> → <strong>서비스</strong> 탭 → <em>Microsoft 365 Copilot</em> 행의 <strong>정책 관리</strong> (또는 상단 <strong>비용 관리 보기</strong>)</span>
  </div>
</div>

**종량제** 페이지는 *"종량제 청구를 통해 서비스 사용량이 Azure 구독에 청구됩니다. 청구 정책을 생성하여 Azure 구독에 연결한 후, 서비스를 구성할 때 해당 정책을 선택하세요."* 라고 안내하며, 다음 요소로 구성됩니다.

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  <ul style="margin: 0; padding-left: 1.2rem;">
    <li><strong>탭</strong>: <strong>청구 정책</strong> / <strong>서비스</strong></li>
    <li><strong>상단 버튼</strong>: <strong>비용 관리 보기</strong>(Cost management 대시보드로 이동) · <strong>비용 예측</strong></li>
    <li><strong>서비스 목록</strong>: Microsoft 365 백업 · <strong>Microsoft 365 Copilot</strong> · 대용량 전자 메일 · Microsoft 365 SharePoint 스토리지</li>
    <li>이미 정책이 연결된 서비스는 <strong>정책 관리</strong>, 아직 연결되지 않은 서비스는 <strong>정책 연결</strong> 로 표시됩니다.</li>
  </ul>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 0.9rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
  📌 <strong>참고</strong> — 공식 문서는 현재까지 <code>Copilot &gt; Cost Management</code> 경로를 안내하고 있습니다. 실제 화면에서는 위 <strong>청구 &gt; 종량제</strong> 진입점으로 롤아웃되는 중이므로, <strong>본인 테넌트에 표시되는 메뉴</strong>를 기준으로 진입하면 됩니다. 어느 경로로 들어가든 도달하는 <strong>Cost Management 대시보드</strong>와 지출 정책은 동일합니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">왜 지금 설정해야 하는가 — 핵심 변경 사항</h2>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  <ol style="margin: 0; padding-left: 1.2rem; line-height: 1.9;">
    <li><strong>평가 기간 종료 안내</strong> — 무료 평가판 기간이 끝나면 설정이 없는 경우 Cowork 접근이 제한될 수 있습니다. 관리 센터에 <em>"13 days left"</em> 같은 <strong>설정 마감 배너</strong>가 표시됩니다.</li>
    <li><strong>새 비용 모델 도입</strong> — AI 크레딧(Copilot Credits) <strong>소비 기반 과금</strong>으로 전환됩니다.</li>
    <li><strong>지출 정책이 필수</strong> — 조직 월별 한도·사용자별 한도·경고 알림을 관리자가 직접 설정합니다.</li>
    <li><strong>결제 방법 연결</strong> — 선불(Capacity Packs / P3) 또는 종량제(PAYG, Azure 구독)를 정책에 연결합니다.</li>
    <li><strong>정책 미설정 시 위험</strong> — 정책이 없으면 크레딧이 <strong>통제 없이 소모</strong>될 수 있으므로, 마감 전 설정 완료를 권장합니다.</li>
  </ol>
</div>

![핵심 변경 사항 5가지 요약 — 기존 방식 종료, 새 비용 모델, 지출 정책 필수, 결제 방법 연결, 정책 발효](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide02.png)
*▲ 핵심 변경 사항 — 왜 지금 설정해야 하는가*

<div style="margin: 1rem 0 1.4rem; padding: 0.9rem 1.1rem; border-radius: 14px; background: #fffbeb; border: 1px solid #fde68a; color: #78350f;">
  📌 <strong>교차 검증 노트 — "6월 30일" 마감은?</strong><br/>
  공식 문서에는 전사 공통의 "6/30 마감"이 명시되어 있지 않습니다. 화면의 <em>"13 days left" / "6월 30일까지 설정"</em> 배너는 <strong>해당 테넌트의 평가 기간 만료일</strong>을 반영하는 안내입니다. <strong>본인 조직 화면에 표시되는 날짜</strong>를 기준으로 일정을 잡으세요.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">먼저 이해하기 — 결제 방법(Billing method)</h2>

Copilot Credits의 결제 방법은 **"선불이냐 종량제냐"의 양자택일이 아닙니다.** 선불 크레딧을 먼저 소진하고, 그 다음 종량제로 자동 전환되는 **계층(layered) 구조**입니다.

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  <strong>크레딧 소진(청구) 순서</strong><br/>
  <div style="margin-top: 0.6rem; font-size: 0.97em;">
    1️⃣ <strong>Capacity Packs</strong> (선불) &nbsp;→&nbsp; 2️⃣ <strong>P3 선불 크레딧</strong>(Pre-Purchase Plan) &nbsp;→&nbsp; 3️⃣ <strong>Pay-as-you-go</strong>(종량제)
  </div>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #ecfdf5; border: 1px solid #a7f3d0; color: #065f46;">
    <strong>💳 Capacity Packs (선불)</strong><br/>
    <span style="font-size: 0.95em;">선불로 구매한 용량 팩. 감지되면 기본 결제 방법으로 설정됩니다. 소진 이후 서비스가 끊기지 않도록 <strong>종량제 미터를 함께 활성화</strong>하는 것을 권장합니다.</span>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
    <strong>🎟️ Pre-Purchase Plan (P3)</strong><br/>
    <span style="font-size: 0.95em;">연간 선불 크레딧으로 <strong>할인율</strong>이 적용됩니다. 종량제 위에 얹어지는 구조이며, 선불분 소진 후 자동으로 종량제로 이어집니다.</span>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #fefce8; border: 1px solid #fde68a; color: #78350f;">
    <strong>📊 Pay-as-you-go (종량제)</strong><br/>
    <span style="font-size: 0.95em;">사용한 만큼 <strong>Azure 구독</strong>으로 청구됩니다. 선불 크레딧이 없거나 모두 소진된 이후의 기본 청구 방식입니다.</span>
  </div>
</div>

![Capacity Packs 결제 방법 상세 설정 화면 — 빌링 방식 확인과 구독 연결 토글](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide06.png)
*▲ Capacity Packs 결제 방법 상세 — 선불 용량 팩 확인과 종량제(구독) 연결 토글*

<div style="margin: 1rem 0 1.4rem; padding: 0.9rem 1.1rem; border-radius: 14px; background: #fef2f2; border: 1px solid #fecaca; color: #7f1d1d;">
  ⚠️ <strong>한 번 정하면 못 바꿉니다</strong><br/>
  지출 정책에 <strong>결제 방법을 설정해 정책을 생성하면, 이후 해당 정책의 결제 방법은 변경할 수 없습니다.</strong> 변경하려면 정책을 삭제하고 새로 만들어야 합니다. 결제 방법 선택에 특히 신중하세요.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">사전 준비 — 필요한 관리자 역할</h2>

공식 문서 기준으로 작업별 **최소 권한 역할**은 다음과 같습니다. (Microsoft는 최소 권한 원칙을 권장하며, 전역 관리자는 비상 시로 제한할 것을 권고합니다.)

| 작업 | 필요 역할 |
| --- | --- |
| **결제 방법** 추가·선택·변경, 정책에 결제 방법 설정 | 전역 관리자(Global), **청구 관리자(Billing)** |
| **지출 정책 생성**, 한도·알림 관리, 비용 관리 대시보드 조회 | **AI 관리자(AI admin)**, **라이선스 관리자(License)** |

> AI 관리자·라이선스 관리자는 결제 방법은 설정·수정할 수 없습니다. 결제 방법까지 다루려면 전역 또는 청구 관리자 권한이 필요합니다.

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">단계별 설정 — 기본 지출 정책 만들기</h2>

관리 센터에서 위 **비용 관리(Cost Management)** 화면에 진입한 뒤, **시작(Get Started)** 을 눌러 *"조직의 기본 지출 정책 활성화"* 마법사를 시작합니다.

![비용 관리 화면의 두 긴급 배너 — 6월 30일까지 설정 요구와 정책 7월 1일 발효 안내, 시작 버튼](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide04.png)
*▲ 비용 관리 진입 — 설정 마감 배너와 "시작" 버튼으로 지출 정책 마법사 진입*

### Step 1 — 결제 방법 & 월별 지출 정책 선택

<div style="margin: 0.8rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  <ol style="margin: 0; padding-left: 1.2rem; line-height: 1.9;">
    <li><strong>결제 방법(Billing method)</strong> 선택 — 조직의 기본 구독/결제 방법을 지정합니다. (선불 용량 팩이 감지되면 기본값으로 설정됩니다.)</li>
    <li><strong>월별 지출 한도</strong> 선택:
      <ul style="margin: 0.3rem 0 0; padding-left: 1.1rem;">
        <li><strong>월별 지출 제한 안 함</strong> — 무제한 소모. <span style="color:#b91c1c;"><strong>권장하지 않음.</strong></span></li>
        <li><strong>월별 지출 제한</strong> — 매월 사용 가능한 크레딧 상한 설정. <span style="color:#15803d;"><strong>권장.</strong></span></li>
      </ul>
    </li>
  </ol>
</div>

![Step 1 결제 방법 및 월별 지출 정책 선택 화면 — Capacity Packs와 월별 지출 제한 옵션](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide05.png)
*▲ Step 1 — 결제 방법(Capacity Packs)과 월별 지출 제한 옵션 선택. 수치는 테넌트 예시값입니다.*

### Step 2 — 조직 월별 크레딧 한도 설정

**월별 지출 제한**을 선택하면 조직 전체가 매월 사용할 수 있는 크레딧 상한을 입력합니다. 한도를 초과하면 **그 달의 남은 기간 동안 에이전트·서비스 접근이 차단**되고, 매월 1일에 크레딧이 초기화됩니다.

<div style="margin: 0.8rem 0 1.2rem; padding: 0.9rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
  💡 <strong>예시값</strong> — 약 100명 규모 기준 <strong>10,000 크레딧/월</strong>로 시작. (조직 규모·사용 패턴에 따라 조정하세요. 본 수치는 예시입니다.)
</div>

![Step 2 조직 월별 크레딧 한도 설정 화면 — 월별 예산 입력과 한도 초과 시 차단 안내](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide07.png)
*▲ Step 2 — 조직 월별 크레딧 한도 입력(예시 10,000)과 한도 초과 시 서비스 차단 안내*

### Step 3 — 사용자별 월별 크레딧 한도 (선택, 강력 권장)

특정 사용자가 조직 크레딧을 혼자 소진하는 것을 막기 위해, **사용자별 월 한도**를 설정합니다. 선택 사항이지만 **반드시 검토·설정**하는 것을 권장합니다.

<div style="margin: 0.8rem 0 1.2rem; padding: 0.9rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
  💡 <strong>예시값</strong> — 사용자당 <strong>1,000 크레딧/월</strong>. (일반적으로 조직 한도의 10~20% 수준을 권장.)
</div>

![Step 3 사용자별 월별 크레딧 한도 설정 화면 — 개인 소비 제한값 입력](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide08.png)
*▲ Step 3 — 사용자별 월 한도(예시 1,000)로 한 사람의 과소비 방지*

### Step 4 — 경고 알림(Define alerts) 설정

임계값에 도달하면 지정한 수신자에게 **이메일 알림**을 보냅니다. 임계값 도달 시점부터 시작해 **매주** 발송되며, 월 초기화 또는 한도 조정 시 멈춥니다. (로그인한 관리자 이메일이 기본 입력됩니다.)

<div style="margin: 0.8rem 0 1.2rem; padding: 0.9rem 1.1rem; border-radius: 14px; background: #fffbeb; border: 1px solid #fde68a; color: #78350f;">
  📌 <strong>교차 검증 노트 — 임계값은 한도보다 작아야 합니다</strong><br/>
  알림 임계값은 <strong>월별 한도 이내</strong>로 설정해야 의미가 있습니다. 예를 들어 조직 한도가 10,000 크레딧이라면 임계값은 <strong>80%인 8,000 크레딧</strong> 정도가 적절합니다. (한도보다 큰 값을 넣으면 알림이 동작하지 않습니다.) 사용자별 한도를 설정한 경우, 사용자가 <strong>한도의 70%</strong>에 도달할 때의 알림도 함께 설정할 수 있습니다.
</div>

![Step 4 경고 알림 설정 화면 — Define alerts 토글, 수신자 이메일, 임계값 입력](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide09.png)
*▲ Step 4 — Define alerts 활성화, 알림 수신자 이메일과 임계값 설정 (임계값은 한도 이내로)*

### 활성화 & 구성 확인

기본 설정은 **조직 전체·모든 사용자**를 대상으로 합니다. 그룹·서비스 단위로 좁히려면 활성화 전에 **설정 사용자 지정(Customize setup configuration)** 을 선택합니다. 준비가 되면 **활성화(Activate)** 를 누르고, 이어서 **구성 관리(Manage Configuration)** 로 이동해 **구성(Configuration)** 탭에서 *All Users Policy* 가 생성되었는지 확인합니다.

![활성화 성공 화면 — AI experiences enabled by usage-based billing 메시지와 구성 관리 버튼](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide12.png)
*▲ 활성화 성공 — "AI experiences enabled by usage-based billing are now available to all users"*

![설정 완료 확인 화면 — 구성 탭의 All Users Policy 생성 완료 배너](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide14.png)
*▲ 구성 탭 — "설정이 완료되었습니다!" 와 All Users Policy 생성 확인*

![All Users Policy 최종 설정값 검토 — 적용 대상, 에이전트, 결제, 월별·사용자 한도, 알림](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide15.png)
*▲ All Users Policy 최종 설정값 — 적용 대상 · 에이전트(Cowork + Work IQ API) · 결제 · 한도 · 알림*

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">종량제(PAYG)를 쓴다면 — Azure 구독 연결</h2>

종량제로 청구하려면 **Azure 구독**을 결제 방법으로 연결합니다. 기존 구독을 선택하거나, 구독이 없으면 관리 센터에서 새로 만들 수 있습니다.

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  <ul style="margin: 0; padding-left: 1.2rem; line-height: 1.85;">
    <li><strong>기존 구독 사용</strong> — 청구 계정에 연결된 구독 목록에서 선택합니다. 구독 이름 위에 마우스를 올리면 구독 ID를 볼 수 있습니다.</li>
    <li><strong>새 구독 생성</strong> — 구독 드롭다운에서 <strong>새로 만들기</strong>를 선택합니다. (이 방식으로 만들려면 <strong>전역 관리자</strong> 권한 필요.)</li>
    <li><strong>P3 선불 크레딧</strong> — 구독에 <em>"X prepaid credits available"</em> 라벨이 보이면 P3 선불 플랜이 연결된 것으로, 선불분을 먼저 쓰고 소진 후 종량제로 이어집니다.</li>
  </ul>
</div>

![Azure 포털에서 리소스 그룹 생성 화면 — 이름과 지역 입력](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide10.png)
*▲ (선택) Azure 리소스 그룹 생성 — 이름과 지역(예: Korea Central) 입력*

![Azure 리소스 그룹 검토 및 생성 화면 — 구독·이름·지역 확인](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide11.png)
*▲ 리소스 그룹 검토 및 생성 (화면의 구독명·계정 정보는 CONTOSO 데모 테넌트 값)*

<div style="margin: 1rem 0 1.4rem; padding: 0.9rem 1.1rem; border-radius: 14px; background: #fffbeb; border: 1px solid #fde68a; color: #78350f;">
  📌 <strong>교차 검증 노트 — "리소스 그룹 생성"은 필수 단계가 아닙니다</strong><br/>
  공식 문서에서 종량제 연결의 필수 요소는 <strong>Azure 구독(Subscription)</strong> 연결입니다. 일부 가이드 캡처에 보이는 <code>copilot-credits-rg</code> 같은 <strong>리소스 그룹 생성</strong>은 문서상 필수 단계로 명시되어 있지 않습니다. 다만 관련 Azure 리소스를 모아 <strong>비용을 분리·추적</strong>하려는 조직 운영 관점에서는 전용 리소스 그룹을 두는 것이 유용할 수 있습니다. (예: <em>Korea Central</em> 리전, 데이터 상주 위치와 일치 권장.)
</div>

![Azure 리소스 그룹 목록에서 copilot-credits-rg 생성 확인](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide13.png)
*▲ 리소스 그룹 목록에서 생성된 copilot-credits-rg(Korea Central) 확인*

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">부서별 세분화 — 추가 지출 정책 만들기</h2>

기본 **All Users** 정책 외에, 그룹·부서별로 별도 한도와 결제 방법을 둘 수 있습니다. **+지출 정책 추가**를 누르고 다음 탭을 차례로 완료합니다.

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  <ol style="margin: 0; padding-left: 1.2rem; line-height: 1.9;">
    <li><strong>범위(사용자·그룹)</strong> — 정책 이름을 정하고 적용 대상 그룹을 선택합니다. 특정 사용자는 <strong>보안 그룹</strong>을 통해서만 지정할 수 있습니다.</li>
    <li><strong>한도 및 알림</strong> — 기본 정책과 동일하게 월별 한도·사용자 한도·알림을 설정합니다. (정책은 항상 선불 크레딧을 먼저 사용합니다.)</li>
    <li><strong>에이전트·서비스 선택</strong> — 이 정책이 접근할 수 있는 서비스를 선택합니다. <em>"신규 서비스·에이전트 자동 포함"</em> 토글이 기본 켜져 있어, 향후 추가되는 서비스가 자동 편입됩니다(필요 시 끄기).</li>
    <li><strong>결제 방법 선택</strong> — 전역/청구 관리자는 정책별로 결제 방법을 다르게 지정해 <strong>부서별 청구</strong>를 구현할 수 있습니다.</li>
    <li><strong>검토 및 생성</strong> — 내용을 확인하고 <strong>지출 정책 만들기</strong>를 선택하면, 범위 내 사용자에게 즉시 적용됩니다.</li>
  </ol>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">사용량 모니터링 & 거버넌스</h2>

**비용 관리(Cost Management)** 대시보드에서 소비 현황을 추적합니다.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
    <strong>📈 개요(Overview) 탭</strong><br/>
    <span style="font-size: 0.95em;">총 크레딧 사용량, 선불 용량 팩 사용량, 종량제(P3 포함) 사용량, 활성 사용자 수, 선불↔종량제 소비 추세를 한눈에 확인합니다. <strong>Top Actions</strong> 에서 크레딧 요청 확인·지출 정책 관리로 바로 이동할 수 있습니다.</span>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #ecfdf5; border: 1px solid #a7f3d0; color: #065f46;">
    <strong>📊 소비(Consumption) 탭</strong><br/>
    <span style="font-size: 0.95em;"><strong>사용자 / 그룹 / 에이전트·서비스</strong> 별로 크레딧 사용량·세션 수·마지막 활동일을 비교합니다. Cowork·Work IQ API 같은 서비스별 사용량을 확인해 정책·한도를 조정합니다.</span>
  </div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 0.9rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  🙋 <strong>크레딧 요청 관리</strong> — 최초 사용이나 한도 증액이 필요한 사용자는 <strong>크레딧 요청</strong>을 제출할 수 있습니다. 관리자는 <em>View requests</em> 에서 요청을 검토하고, 정책에 사용자 추가·새 정책 생성·한도 조정·오프라인 분류용 내보내기로 대응합니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #16a34a; background: #f0fdf4;">모범 사례 — 엔터프라이즈 비용 관리</h2>

![엔터프라이즈 Cowork 비용 관리 모범 사례 — 크레딧 계획, 정책 구성 원칙, 모니터링과 거버넌스](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide16.png)
*▲ 모범 사례 한눈에 보기 — 크레딧 계획 · 정책 구성 원칙 · 모니터링 & 거버넌스*

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
    <strong>💰 크레딧 계획</strong>
    <ul style="margin: 0.5rem 0 0; padding-left: 1.1rem; font-size: 0.94em; line-height: 1.7;">
      <li>파일럿은 작게 시작 후 사용 패턴을 보고 증액</li>
      <li>전사 산정: <strong>사용자 수 × 평균 사용량</strong> 기준</li>
      <li>초기에는 낮게 설정하고 점진적으로 상향</li>
    </ul>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
    <strong>⚙️ 정책 구성 원칙</strong>
    <ul style="margin: 0.5rem 0 0; padding-left: 1.1rem; font-size: 0.94em; line-height: 1.7;">
      <li>조직 한도 ≈ 사용자 수 × 예상 사용량 × <strong>1.2배 버퍼</strong></li>
      <li>사용자 한도 = 조직 한도의 <strong>10~20%</strong></li>
      <li>알림 임계값 = 조직 한도의 <strong>80%</strong></li>
      <li>부서별 정책은 기본 정책 후 단계적 적용</li>
    </ul>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
    <strong>📋 모니터링 & 거버넌스</strong>
    <ul style="margin: 0.5rem 0 0; padding-left: 1.1rem; font-size: 0.94em; line-height: 1.7;">
      <li>월 1회 소비(Consumption) 탭 검토</li>
      <li>분기별 크레딧 한도 재검토·조정</li>
      <li>알림 수신자에 <strong>IT 관리자 + 비용 담당자</strong> 포함</li>
      <li>종량제 사용 시 Azure 비용 관리와 연계 모니터링</li>
    </ul>
  </div>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">설정 완료 체크리스트</h2>

![6월 30일 전 완료 체크리스트 — 필수·권장·선택 항목](/mwkorea/assets/images/2026-06-17-CopilotCreditsCostGuide/slide17.png)
*▲ 마감 전 완료 체크리스트 — 필수 · 권장 · 선택 항목*

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  <table style="width:100%; border-collapse: collapse; font-size: 0.95em;">
    <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:6px 8px; white-space:nowrap;"><strong style="color:#b91c1c;">필수</strong></td><td style="padding:6px 8px;">관리 센터 <strong>청구 &gt; 종량제</strong>(또는 Copilot &gt; 비용 관리) 진입</td></tr>
    <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:6px 8px;"><strong style="color:#b91c1c;">필수</strong></td><td style="padding:6px 8px;"><strong>시작</strong> 클릭 → 지출 정책 활성화 마법사 진입</td></tr>
    <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:6px 8px;"><strong style="color:#b91c1c;">필수</strong></td><td style="padding:6px 8px;">결제 방법 선택: Capacity Packs / P3(선불) 또는 PAYG(Azure 구독)</td></tr>
    <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:6px 8px;"><strong style="color:#b91c1c;">필수</strong></td><td style="padding:6px 8px;">조직 월별 크레딧 한도 입력(무제한 비권장)</td></tr>
    <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:6px 8px;"><strong style="color:#15803d;">권장</strong></td><td style="padding:6px 8px;">사용자별 월 한도 활성화 및 값 입력(조직 한도의 10~20%)</td></tr>
    <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:6px 8px;"><strong style="color:#15803d;">권장</strong></td><td style="padding:6px 8px;">경고 알림 활성화 → 수신자 이메일 + 임계값(한도의 80%) 설정</td></tr>
    <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:6px 8px;"><strong style="color:#15803d;">권장</strong></td><td style="padding:6px 8px;"><strong>활성화</strong> 후 <strong>구성</strong> 탭에서 All Users Policy 확인</td></tr>
    <tr style="border-bottom:1px solid #e2e8f0;"><td style="padding:6px 8px;"><strong style="color:#2563eb;">선택</strong></td><td style="padding:6px 8px;">PAYG 사용 시 전용 리소스 그룹으로 비용 분리·추적</td></tr>
    <tr><td style="padding:6px 8px;"><strong style="color:#2563eb;">선택</strong></td><td style="padding:6px 8px;">부서별 세분화 정책 추가 및 소비 탭 모니터링 일정 수립</td></tr>
  </table>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #64748b; background: #f8fafc;">참고 자료</h2>

- 📘 [Managing AI experiences enabled by usage-based billing — Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits) *(본 가이드의 교차 검증 기준 문서)*
- 🎟️ [Optimize Copilot Credit costs with a pre‑purchase plan (P3) — Microsoft Learn](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/copilot-credit-p3)
- 🔐 [Microsoft 365 관리자 역할 정보 — Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles)

> 본 글의 절차와 수치는 작성 시점(2026년 6월) 기준이며, 제품 UI와 메뉴 위치는 롤아웃 단계에 따라 다르게 보일 수 있습니다. 항상 본인 테넌트의 관리 센터 화면과 공식 문서를 함께 확인하세요.
