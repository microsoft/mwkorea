---
layout: single
title: "우리 데이터, 안전한가요? — Copilot 도입 전 꼭 짚어야 할 보안 이야기"
permalink: /hidden/copilot-security/
author_profile: true
sitemap: false
search: false
excerpt: "Microsoft 365 Copilot 도입 전에 고객이 가장 많이 묻는 보안 질문과 안전하고 효율적인 도입을 위한 준비 항목을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 안영택
---

<style>
.page__content .security-meta {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.55rem 1rem;
  margin-top: 0.9rem;
  color: #64748b;
  font-size: 0.88rem;
}
.page__content .security-hero-art {
  display: block;
  width: min(220px, 70vw);
  height: auto;
  margin: 1.15rem auto 0;
}
.page__content .security-faq {
  display: grid;
  grid-template-columns: 52px minmax(0, 1fr);
  gap: 1rem;
  align-items: start;
  margin: 1rem 0;
}
.page__content .security-q-badge {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 12px;
  background: var(--mc-accent);
  color: #fff;
  font-weight: 800;
}
.page__content .security-question {
  margin-bottom: 0.35rem;
  color: #111827;
  font-size: 1.05rem;
  font-weight: 800;
}
.page__content .security-answer-tag {
  margin-right: 0.35rem;
  color: #166534;
  font-weight: 800;
}
.page__content .security-step {
  display: grid;
  grid-template-columns: 110px minmax(0, 1fr);
  gap: 1.25rem;
  align-items: center;
}
.page__content .security-step-art {
  display: block;
  width: 88px;
  height: 88px;
  margin: 0 auto;
}
.page__content .security-step-number {
  color: var(--mc-accent-ink);
  font-size: 0.82rem;
  font-weight: 900;
  letter-spacing: 0.08em;
}
.page__content .security-bigquote {
  margin: 1.4rem 0;
  padding: 1.5rem 1rem;
  border: 1px solid var(--mc-accent-border);
  border-radius: 18px;
  background: linear-gradient(135deg, var(--mc-accent-soft), #fff 62%, var(--mc-accent-mist));
  color: #111827;
  text-align: center;
  box-shadow: var(--mc-shadow);
}
.page__content .security-bigquote p {
  margin: 0.25rem 0 0;
  font-size: 1.35rem;
  font-weight: 900;
}
@media (max-width: 640px) {
  .page__content .security-faq,
  .page__content .security-step {
    grid-template-columns: 1fr;
  }
  .page__content .security-q-badge {
    width: 42px;
    height: 42px;
  }
}
</style>

<div class="monthlycopilot-page monthlycopilot-page--security">
<div class="mc-issue-strip">Monthly Copilot · Security</div>

<div class="mc-cover">
  <div class="mc-cover-title">“우리 데이터,<br/><span style="color:var(--mc-accent);">안전한가요?</span>”</div>
  <div class="mc-cover-subtitle">Copilot 도입 전 꼭 짚어야 할 보안 이야기</div>
  <div class="security-meta">
    <span><strong>주제</strong> Microsoft 365 Copilot</span>
    <span><strong>읽는 시간</strong> 약 6분</span>
    <span><strong>카테고리</strong> 보안 · 거버넌스</span>
  </div>
  <svg class="security-hero-art" viewBox="0 0 230 230" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="데이터를 감싸는 신뢰의 방패">
    <circle cx="115" cy="115" r="108" fill="var(--mc-accent-soft)"/>
    <path d="M115 35 L180 60 V120 C180 160 150 185 115 198 C80 185 50 160 50 120 V60 Z" fill="var(--mc-accent)"/>
    <path d="M115 49 L168 69 V120 C168 152 144 173 115 184 C86 173 62 152 62 120 V69 Z" fill="#fff"/>
    <rect x="86" y="92" width="58" height="13" rx="4" fill="var(--mc-accent)"/>
    <rect x="86" y="111" width="58" height="13" rx="4" fill="#f59e0b"/>
    <rect x="86" y="130" width="58" height="13" rx="4" fill="#0078d4"/>
    <circle cx="100" cy="73" r="4.5" fill="#111827"/>
    <circle cx="130" cy="73" r="4.5" fill="#111827"/>
    <path d="M101 82 Q115 92 129 82" stroke="#111827" stroke-width="3" stroke-linecap="round" fill="none"/>
    <circle cx="160" cy="150" r="22" fill="#16a34a"/>
    <path d="M150 150 l7 7 l13 -15" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  </svg>
</div>

<div class="mc-callout">
  <p>Microsoft 365 Copilot을 검토하는 거의 모든 조직이 가장 먼저 던지는 질문은 똑같습니다. <strong>“그래서, 우리 회사 데이터는 안전한가요?”</strong> 이번 호에서는 고객이 가장 많이 묻는 보안 질문에 답하고, 안전하면서도 효율적으로 Copilot을 도입하기 위한 준비 항목을 정리합니다.</p>
</div>

<h3>준비된 데이터를 감싸는 ‘신뢰의 보호막’</h3>

<p>Copilot 도입을 망설이게 하는 건 대부분 ‘기능’이 아니라 ‘보안’입니다. 좋은 소식은, 이 질문들 대부분은 <strong>이미 명확한 답</strong>이 있다는 것입니다. Copilot은 새로운 보안 모델을 들고 오는 것이 아니라, 여러분이 <strong>이미 운영 중인 Microsoft 365의 보안·규정 약속 위에서</strong> 동작하기 때문입니다.</p>

<p>이 글은 세 부분으로 구성됩니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue"><strong>① 고객이 가장 많이 묻는 보안 FAQ</strong></div>
  <div class="mc-card mc-card--teal"><strong>② 도입 전에 짚어야 할 3단계 준비</strong></div>
  <div class="mc-card mc-card--purple"><strong>③ 한 줄 결론</strong></div>
</div>

<hr/>

<div class="mc-cover-kicker">Part 1 · Frequently Asked</div>
<h2 class="mc-section-title">가장 많이 받는 보안 질문 5가지</h2>

<div class="mc-card security-faq">
  <div class="security-q-badge">Q1</div>
  <div>
    <div class="security-question">우리 회사 데이터로 AI 모델을 학습시키나요?</div>
    <p><span class="security-answer-tag">아니요.</span>사용자의 프롬프트, Copilot의 응답, 그리고 Microsoft Graph 데이터는 기반 LLM(대규모 언어 모델)을 학습시키는 데 사용되지 않습니다. Copilot 관련 고객 데이터는 Microsoft 365의 데이터 거주 약속과 테넌트 격리 원칙에 따라 보호됩니다. 일부 처리는 Microsoft 365 및 Azure 인프라의 적절한 서비스 위치에서 수행될 수 있으나, 고객 데이터가 다른 고객이나 외부 서비스와 공유되거나 기반 모델 학습에 사용되지는 않습니다.</p>
  </div>
</div>

<div class="mc-card security-faq">
  <div class="security-q-badge">Q2</div>
  <div>
    <div class="security-question">Copilot은 어떤 데이터에 접근하나요?</div>
    <p>이메일·문서·채팅·일정 등 Microsoft Graph 안의 Microsoft 365 데이터에 접근할 수 있습니다. 다만 가장 중요한 원칙이 하나 있습니다 — <strong>사용자가 이미 접근 권한을 가진 데이터만 참조합니다.</strong> 권한이 없는 데이터는 Copilot도 볼 수 없습니다. 이 원칙이 뒤에 나올 ‘과잉 공유’ 이야기의 핵심입니다.</p>
  </div>
</div>

<div class="mc-card security-faq">
  <div class="security-q-badge">Q3</div>
  <div>
    <div class="security-question">데이터는 어디서 처리되고, 어디에 저장되나요?</div>
    <p>Copilot 요청의 처리는 Microsoft 365 서비스와 Azure 인프라에서 이뤄지고, 고객 데이터는 Microsoft 365 데이터 거주 약속에 따라 해당 테넌트의 데이터 지역(geography) 내에 저장됩니다. 기능별 지원 범위와 일부 모델·서비스 예외는 최신 Microsoft Learn 문서를 기준으로 확인하는 것이 좋습니다. Copilot은 별도의 새 저장소를 만들지 않고, 기존 Microsoft 365 데이터 구조와 권한 모델을 활용합니다.</p>
  </div>
</div>

<div class="mc-card security-faq">
  <div class="security-q-badge">Q4</div>
  <div>
    <div class="security-question">데이터 거주 · 암호화 · 테넌트 격리는요?</div>
    <p><strong>데이터 거주:</strong> Microsoft 365의 데이터 거주 정책을 그대로 따릅니다. Advanced Data Residency / Multi-Geo, EU Data Boundary도 지원합니다(일부 모델 예외).<br/>
    <strong>암호화:</strong> 저장 시·전송 시 모두 암호화됩니다(Microsoft 365 표준 암호화).<br/>
    <strong>테넌트 격리:</strong> 각 고객 테넌트는 논리적으로 분리되어 다른 조직 데이터와 섞이지 않습니다. 접근은 Microsoft Entra ID 인증과 권한 기반으로 통제됩니다.</p>
  </div>
</div>

<div class="mc-card security-faq">
  <div class="security-q-badge">Q5</div>
  <div>
    <div class="security-question">규정 준수와 데이터 관리는 어떻게 하나요?</div>
    <p>Copilot은 Microsoft 365의 규정 준수 체계를 그대로 따릅니다. Audit(감사 로그), eDiscovery, Data Lifecycle(보존·삭제)을 비롯한 Microsoft Purview 기능을 모두 활용할 수 있고, GDPR·ISO 27001 등 글로벌 규정 기준을 충족합니다.</p>
  </div>
</div>

<div class="mc-callout mc-card--green">
  <strong>💡 한 줄 요약 —</strong> Copilot은 추가적인 보안 약속을 새로 요구하지 않습니다. 기존 Microsoft 365의 보안·규정 약속 위에서 그대로 동작합니다.
</div>

<hr/>

<div class="mc-cover-kicker">Part 2 · Get Ready</div>
<h2 class="mc-section-title">그렇다면 무엇을 준비해야 할까요 — 3단계</h2>

<p>보안 질문에 답이 명확하다고 해서 “아무 준비 없이 켜도 된다”는 뜻은 아닙니다. Copilot을 안전하고 효율적으로 도입하려면 데이터를 미리 정돈해 두는 것이 좋습니다. 핵심은 다음 <strong>3단계</strong>입니다.</p>

<div class="mc-card security-step">
  <svg class="security-step-art" viewBox="0 0 88 88" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="과잉 공유 교정">
    <rect x="10" y="30" width="50" height="38" rx="6" fill="#f59e0b"/>
    <path d="M10 36 v-5 a6 6 0 0 1 6 -6 h14 l6 7 h-26 z" fill="#f59e0b"/>
    <rect x="48" y="14" width="20" height="26" rx="3" fill="#fff" stroke="#64748b" stroke-width="2" transform="rotate(12 58 27)"/>
    <rect x="58" y="22" width="20" height="26" rx="3" fill="#fff" stroke="#64748b" stroke-width="2" transform="rotate(-8 68 35)"/>
    <circle cx="34" cy="50" r="13" fill="none" stroke="var(--mc-accent)" stroke-width="4"/>
    <line x1="43" y1="59" x2="56" y2="72" stroke="var(--mc-accent)" stroke-width="5" stroke-linecap="round"/>
  </svg>
  <div>
    <div class="security-step-number">STEP 1</div>
    <h3>과잉 공유(Oversharing) 교정</h3>
    <p>가장 중요한 원칙은 단순합니다. <strong>Copilot은 새로운 권한을 만들지 않습니다.</strong> 대신 조직에 이미 존재하던 ‘과잉 공유’를 검색과 AI를 통해 더 쉽게 드러냅니다. 예전에는 깊숙이 묻혀 찾기 어려웠던 파일도, 사용자가 접근 권한을 갖고 있다면 Copilot 답변의 근거로 표면화될 수 있습니다.</p>
    <p>원인은 익숙합니다 — 조직 전체에 열린 공유, 방치된 상속 권한, 분류되지 않은 파일. 이를 통제하는 도구는 네 가지입니다.</p>
  </div>
</div>

<div class="mc-table-wrap">
<table>
  <thead>
    <tr><th>도구</th><th>역할</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>SAM<br/>(SharePoint Advanced Management)</td>
      <td>검색 결과 노출과 사이트 접근 범위 제한 (<strong>RCD·RAC 권장</strong>)<br/>
        · 방법 #1 — <a href="https://learn.microsoft.com/en-us/microsoftsearch/semantic-index-for-copilot#excluding-sharepoint-online-sites">SharePoint 검색 인덱싱 제외</a><br/>
        · 방법 #2 — <a href="https://learn.microsoft.com/ko-kr/sharepoint/restricted-sharepoint-search">제한된 SharePoint 검색 (RSS)</a><br/>
        · 방법 #3 — <a href="https://learn.microsoft.com/ko-kr/sharepoint/restricted-content-discovery">제한된 콘텐츠 검색 (RCD/SAM)</a><br/>
        · 방법 #4 — <a href="https://learn.microsoft.com/ko-kr/sharepoint/restricted-access-control">제한된 액세스 제어 (RAC/SAM)</a></td>
    </tr>
    <tr><td>컨테이너 레이블<br/>(MIP 민감도 레이블)</td><td>사이트·그룹 비공개 강제, 콘텐츠와 함께 이동</td></tr>
    <tr><td>DLP for Copilot</td><td>민감 프롬프트·레이블 콘텐츠를 응답에서 제외</td></tr>
    <tr><td>DSPM</td><td>과잉 공유 자동 식별·교정·모니터링</td></tr>
  </tbody>
</table>
</div>

<div class="mc-callout mc-card--amber">
  ⚠️ 제한된 SharePoint 검색 기능(RSS)은 <strong>향후 지원 종료 예정</strong>이므로 SAM의 RCD·RAC을 활용하세요.
</div>

<div class="mc-callout mc-card--amber">
  🔎 SharePoint Online의 <strong>‘외부 사용자를 제외한 모든 사용자(EEEU)’ 공유 범위</strong>도 반드시 점검해야 합니다. EEEU로 공유된 문서는 조직 내 다수가 접근할 수 있어 Copilot이 의도치 않게 민감 정보를 활용할 수 있습니다. <a href="https://learn.microsoft.com/ko-kr/powershell/module/microsoft.online.sharepoint.powershell/set-spotenant?view=sharepoint-ps#-showeveryoneexceptexternalusersclaim">신규 공유에서 EEEU를 숨기는 설정</a>은 신규 공유에만 적용되므로, 기존 EEEU 공유 사이트·문서는 별도로 검토·정리해야 합니다.
</div>

<div class="mc-callout mc-card--blue">
  <strong>🎁 참고 —</strong> 2025년 1월부터 SharePoint Advanced Management(SAM)는 Microsoft 365 Copilot 라이선스에 <strong>무료로 포함</strong>됩니다. 제한된 검색·콘텐츠 검색·액세스 제어 등을 추가 비용 없이 활용할 수 있습니다.
</div>

<div class="mc-card security-step">
  <svg class="security-step-art" viewBox="0 0 88 88" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="가드레일 구성">
    <rect x="14" y="40" width="60" height="10" rx="5" fill="var(--mc-accent)"/>
    <rect x="18" y="48" width="8" height="26" rx="3" fill="var(--mc-accent)"/>
    <rect x="62" y="48" width="8" height="26" rx="3" fill="var(--mc-accent)"/>
    <rect x="36" y="48" width="8" height="26" rx="3" fill="var(--mc-accent)"/>
    <rect x="34" y="14" width="20" height="16" rx="4" fill="#16a34a"/>
    <path d="M37 14 v-4 a7 7 0 0 1 14 0 v4" fill="none" stroke="#16a34a" stroke-width="4"/>
    <circle cx="44" cy="21" r="2.6" fill="#fff"/>
  </svg>
  <div>
    <div class="security-step-number">STEP 2</div>
    <h3>가드레일 구성 (런타임 보호)</h3>
    <p>데이터를 정돈했다면, 이제 <strong>실시간으로 작동하는 가드레일</strong>을 세웁니다.</p>
    <ul>
      <li><strong>DLP for Copilot (프롬프트):</strong> 신용카드 번호 같은 민감정보(SIT)가 프롬프트에 감지되면, Copilot이 요청을 처리하기 전에 차단합니다. Work·Web 환경 모두에서 동일하게 동작합니다.</li>
      <li><strong>DLP for Copilot (민감도 레이블):</strong> Copilot과 에이전트는 사용자의 기존 권한과 문서 보호 설정을 따릅니다. DLP 정책으로 민감정보나 특정 레이블 콘텐츠가 응답·외부 공유·메일 반출에 부적절하게 사용되지 않도록 제어할 수 있습니다.</li>
    </ul>
  </div>
</div>

<div class="mc-card security-step">
  <svg class="security-step-art" viewBox="0 0 88 88" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="모니터링과 규정 준수">
    <circle cx="44" cy="44" r="30" fill="none" stroke="#64748b" stroke-width="3"/>
    <circle cx="44" cy="44" r="18" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="3 4"/>
    <path d="M44 44 L44 16 A28 28 0 0 1 68 30 Z" fill="var(--mc-accent-soft)"/>
    <line x1="44" y1="44" x2="66" y2="28" stroke="var(--mc-accent)" stroke-width="4" stroke-linecap="round"/>
    <circle cx="44" cy="44" r="5" fill="var(--mc-accent)"/>
    <circle cx="64" cy="60" r="4" fill="#16a34a"/>
    <circle cx="26" cy="58" r="4" fill="#f59e0b"/>
  </svg>
  <div>
    <div class="security-step-number">STEP 3</div>
    <h3>모니터링 · 규정 준수</h3>
    <p>마지막은 <strong>‘보이게 만들기’</strong>입니다.</p>
    <ul>
      <li><strong>DSPM:</strong> 조직 전체의 AI 앱·에이전트 수, 고위험 에이전트 현황(High/Medium/Low), Oversharing·Exfiltration 같은 민감 상호작용을 한 대시보드에서 봅니다.</li>
      <li><strong>Activity Explorer:</strong> 누가, 언제, 어떤 AI 앱으로 무엇을 했는지 — 권한이 있으면 프롬프트·응답 텍스트까지 — 세부 추적합니다.</li>
      <li><strong>Audit · eDiscovery · Communication Compliance:</strong> 상세 동작 로그와 프롬프트 내용을 검사하고, EU AI Act 등 규정 준수 평가(Compliance Manager)와 위험 행동 기반 동적 차단(Insider Risk·조건부 액세스)까지 연결합니다.</li>
    </ul>
  </div>
</div>

<hr/>

<div class="mc-cover-kicker">Part 3 · Takeaway</div>
<h2 class="mc-section-title">한 줄로 정리하면</h2>

<h3>한 눈에 보는 요약 — 보안 FAQ와 도입 3단계</h3>
<p>세 단계를 한 문장씩으로 줄이면 이렇습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue" style="text-align:center;">
    <div class="mc-card-title"><strong>1</strong></div>
    <div><strong>보안 원칙 확인</strong></div>
    <div class="mc-card-note">고객 데이터는 기반 모델 학습에 사용되지 않으며, 기존 권한·암호화·테넌트 격리 원칙을 따릅니다.</div>
  </div>
  <div class="mc-card mc-card--teal" style="text-align:center;">
    <div class="mc-card-title"><strong>2</strong></div>
    <div><strong>공유·접근 정리</strong></div>
    <div class="mc-card-note">SAM, 민감도 레이블, DLP로 과잉 공유를 줄이고 민감 콘텐츠의 부적절한 사용을 통제합니다.</div>
  </div>
  <div class="mc-card mc-card--purple" style="text-align:center;">
    <div class="mc-card-title"><strong>3</strong></div>
    <div><strong>모니터링·단계 도입</strong></div>
    <div class="mc-card-note">DSPM, Audit, eDiscovery로 가시성과 규정 준수 기반을 확보한 뒤 단계적으로 확장합니다.</div>
  </div>
</div>

<div class="security-bigquote">
  <div style="color:var(--mc-accent); font-size:1.8rem; font-weight:900;">&ldquo;</div>
  <p>준비된 데이터 위에서<br/>Copilot은 안전합니다.</p>
</div>

<p>보안은 Copilot 도입의 걸림돌이 아니라, 오히려 <strong>데이터 거버넌스를 한 단계 끌어올리는 좋은 계기</strong>가 될 수 있습니다. 질문에 답이 있고, 준비할 항목이 분명하다면 — 남은 건 시작하는 것뿐입니다.</p>

<div class="mc-callout mc-callout--dark" style="text-align:center;">
  이 기사는 Microsoft Learn의 ‘Data, Privacy, and Security for Microsoft 365 Copilot’ 및 Microsoft 365 Copilot 보안·도입 가이드를 바탕으로 정리했습니다.<br/>
  © Monthly Copilot · Security
</div>

</div>