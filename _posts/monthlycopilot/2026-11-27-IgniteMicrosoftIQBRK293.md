---
title: "Ignite Microsoft IQ | 같은 질문인데, 왜 보고서 숫자가 다를까요?"
date: 2026-11-27T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - MicrosoftIQ
  - BusinessPlugins
  - Ignite
  - 월간코파일럿
excerpt: "Ignite 2026 BRK293의 고객 지원·법무 시연으로, Microsoft IQ가 팀의 공식 자료와 업무 절차를 여러 에이전트가 참고할 수 있게 하는 방법을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · December 2026 · 월간 코파일럿 12월호 · Microsoft IQ</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Microsoft Ignite 2026 ｜ BRK293</div>
  <div class="mc-cover-title">같은 질문인데,<br/>왜 보고서 숫자가 다를까요?</div>
  <div class="mc-cover-subtitle">Microsoft IQ로 에이전트에 우리 회사의 업무 기준을 알려 주는 법</div>
</div>

<p>재무팀 세 사람이 Copilot에 같은 일을 부탁했습니다. “이번 분기 실적이 계획과 얼마나 달랐는지 보고서를 만들어 줘.” 돌아온 보고서는 세 개였고, 숫자도 제각각이었습니다. Ignite 2026의 <strong>BRK293</strong>에서 소개한 사례입니다. 질문은 같았지만 각 에이전트가 참고한 파일, 도구, 정책 버전이 달랐습니다. 이런 경우 프롬프트를 더 자세히 쓰기 전에, <strong>어떤 자료를 공식 기준으로 삼을지</strong>부터 정해야 합니다.</p>

<p><a href="https://www.youtube.com/watch?v=Ca44w1lUxog&amp;t=245s">세 사람이 다른 결과를 받은 이유 보기 (04:05) →</a></p>

<h2 class="mc-section-title">1 · 재무팀의 업무 기준을 한 번 정리해 여러 에이전트에서 씁니다</h2>

<p><strong>Microsoft IQ</strong>는 에이전트가 회사의 자료와 업무 기준을 찾아 쓸 수 있게 묶어 주는 플랫폼입니다. 업무 문서와 대화는 <strong>Work IQ</strong>, 승인된 지표 정의와 운영 데이터는 <strong>Fabric IQ</strong>, 정책 문서처럼 선별한 사내 지식은 <strong>Foundry IQ</strong>, 최신 외부 정보는 <strong>Web IQ</strong>에서 연결하는 방식입니다. 필요한 경우 외부 업무 시스템의 자료도 연결할 수 있습니다.</p>

<p><strong>Business Plugin</strong>은 이렇게 연결한 자료 중 특정 업무에 필요한 출처, 스킬, 도구와 각각을 언제 써야 하는지에 대한 지침을 담은 <strong>업무 플레이북</strong>입니다. 예를 들어 재무팀은 어떤 자료를 확정 실적으로 보고, 어떤 산식으로 계획 대비 차이를 계산하는지 정리할 수 있습니다. 새 에이전트를 만들 때마다 그 기준을 다시 설명하는 대신, 팀에서 관리하는 플레이북을 참고하게 하는 겁니다.</p>

<h2 class="mc-section-title">2 · 질문이 들어오면 플레이북에서 필요한 부분만 찾습니다</h2>

<p>사용자가 플러그인 이름을 외울 필요는 없습니다. 세션에서 소개한 방식은 질문이 들어오면 활성화된 플러그인에서 <strong>사용자가 접근할 수 있는 관련 항목</strong>을 찾고, 관련도가 높은 자료와 사용 지침을 에이전트에 전달하는 것이었습니다. 매번 플레이북 전체를 읽히는 방식과 다릅니다.</p>

<p>고객 지원 데모에서는 “긴급 장애(P1)가 나면 어떻게 대응해야 하나요?”라고 묻자 공식 체크리스트를 안내했습니다. 승인되지 않은 거래에 대한 이의 제기는 누가 승인해야 하는지 묻자, 같은 <strong>Customer Support</strong> 플레이북에서 해당 승인자를 찾아 줬습니다. 두 질문에 같은 문서를 돌려준 게 아니라, <strong>질문에 맞는 절차를 공식 자료에서 골라</strong> 답한 겁니다.</p>

<p><a href="https://www.youtube.com/watch?v=Ca44w1lUxog&amp;t=1379s">고객 지원 플레이북 시연 보기 (22:59) →</a></p>

<h2 class="mc-section-title">3 · 법무 데모: 답변에 ‘누가 승인해야 하는지’가 나왔습니다</h2>

<p>“50만 달러짜리 계약에 제가 직접 서명해도 되나요?” 시연에서 Copilot Chat은 법무 플레이북을 참고해 본인이 직접 서명하면 안 된다고 안내하고, 필요한 승인자와 정책 문서 링크를 제시했습니다. 이는 <strong>시연에 쓰인 회사의 정책</strong>에 따른 답입니다. Copilot이 서명 권한을 부여하거나 승인을 대신한 것은 아닙니다.</p>

<p>이런 답을 믿고 쓰려면 플레이북 자체도 관리해야 합니다. 세션에서는 편집·관리하는 사람(<strong>Curator</strong>)과 자신의 접근 권한 안에서 이용하는 사람(<strong>User</strong>)을 구분했습니다. <strong>Promoted</strong>는 소유자가 추천한 상태이고, <strong>Certified</strong>는 관리자가 검토해 인증한 상태입니다. 인증된 플러그인은 대상 그룹에 개인별 수락 없이 활성화할 수 있지만, 원본 문서에 없던 접근 권한이 새로 생기는 건 아닙니다.</p>

<p><a href="https://www.youtube.com/watch?v=Ca44w1lUxog&amp;t=2051s">계약 서명 권한 시연 보기 (34:11) →</a></p>

<h2 class="mc-section-title">4 · 우리 팀에서는 헷갈리는 질문 하나부터</h2>

<p>같은 팀에서 “최신 양식이 뭐예요?” 또는 “이 건은 누가 승인하나요?”라는 질문이 반복된다면 좋은 출발점입니다. 질문 하나를 골라 <strong>업무 책임자 한 명, 플레이북 하나</strong>로 시험해 보세요.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>업무 책임자 · 공식 기준 정하기</strong></div>
    <div>최신 정책과 양식의 원본을 고르고, 서로 다른 버전이 나오면 무엇을 우선할지 정합니다. 정책이 바뀌면 플레이북을 누가 갱신할지도 정해 둡니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>관리자 · 대상과 권한 확인하기</strong></div>
    <div>먼저 필요한 팀에만 적용하고, 문서를 볼 수 없는 사용자에게 답변으로 그 내용이 드러나지 않는지 확인합니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>팀 · 적용 전후 비교하기</strong></div>
    <div>같은 질문을 여러 방식으로 묻고, 최신 정책을 인용한 답변의 비율과 사람이 근거를 다시 찾는 데 걸린 시간을 비교합니다.</div>
  </div>
</div>

<p>처음 재무팀 사례로 돌아가 보면, 세 보고서의 문장까지 똑같을 필요는 없습니다. 중요한 건 같은 기준으로 계산했는지, 다른 숫자가 나왔다면 <strong>어떤 자료와 산식에서 차이가 났는지</strong> 확인할 수 있는가입니다.</p>

<p><a class="btn btn--primary" href="https://ignite.microsoft.com/en-US/sessions/BRK293">Ignite 공식 세션 보기 →</a></p>
<p class="mc-card-note">참고: <a href="https://www.youtube.com/watch?v=Ca44w1lUxog">BRK293 전체 녹화</a> · <a href="https://azure.microsoft.com/en-us/blog/introducing-the-new-microsoft-iq-putting-your-organizations-intelligence-to-work-in-every-agent/">Microsoft IQ 공식 발표</a> · <a href="https://news.microsoft.com/events/ignite/2026/book-of-news/">Ignite 2026 Book of News</a>. 세션에서 소개한 새 Business Plugin 기능은 발표 당시 Frontier 프로그램으로 안내됐습니다. 실제로 시험하기 전에 조직의 사용 가능 여부를 확인하세요.</p>
</div>
