---
title: "Ignite Copilot Studio | AI가 보고서를 써도, 발송은 사람이 승인합니다"
date: 2026-11-27T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - CopilotStudio
  - Ignite
  - Workflow
  - 월간코파일럿
excerpt: "Ignite 2026 BRK267의 금융 데모로, Copilot Studio에서 에이전트에 분석을 맡기고 고객 메일 발송에는 사람의 승인을 두는 방법을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · December 2026 · 월간 코파일럿 12월호 · Copilot Studio</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Microsoft Ignite 2026 ｜ BRK267</div>
  <div class="mc-cover-title">AI가 보고서를 써도,<br/>발송은 사람이 승인합니다</div>
  <div class="mc-cover-subtitle">에이전트, 워크플로우, 앱으로 설계하는 업무</div>
</div>

<p>고객의 포트폴리오를 검토한다고 해 보죠. 보유 종목을 조회하고, 펀드 안에 어떤 종목이 들어 있는지 확인하고, 사내 투자 기준에 어긋나는 부분을 설명해야 합니다. AI가 이 일을 도와줄 수 있다면, 어디까지 맡겨도 될까요? Ignite 2026의 Copilot Studio 세션 <strong>BRK267</strong>은 보고서를 쓰는 일과 고객에게 보내는 일을 나누는 데서 출발했습니다.</p>

<h2 class="mc-section-title">1 · 펀드 속 종목까지 찾아도, 메일은 바로 보내지 않습니다</h2>

<p>시연에서는 Copilot Cowork에 금융 분석 에이전트를 만들어 달라고 요청했습니다. 에이전트는 고객관리시스템(CRM)에서 보유 내역을 가져오고, Morningstar에 연결해 직접 보유한 종목뿐 아니라 펀드를 통해 간접 보유한 종목까지 확인했습니다. 사내 투자 지침을 참고해 특정 종목의 비중이 회사의 10% 상한을 넘었다고 짚었고, 팀에서 쓰던 이메일 템플릿으로 보고서 초안을 작성했습니다.</p>

<p>눈여겨볼 부분은 그다음입니다. <strong>“승인 없이 보내지 마세요”라고 에이전트에 지시하는 것으로 끝내지 않았습니다.</strong> 별도의 워크플로우가 담당자에게 승인을 요청하고, 승인된 경우에만 발송 단계로 넘어가도록 구성했습니다. 발송 여부를 결정하는 건 AI의 판단이 아니라 워크플로우가 확인한 승인 결과입니다.</p>

<p><a href="https://www.youtube.com/watch?v=F1uiehsuwAU&amp;t=1002s">고객 이메일 승인 워크플로우 보기 (16:42) →</a></p>

<h2 class="mc-section-title">2 · 업무를 세 가지로 나누면 설계가 쉬워집니다</h2>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>에이전트 · 조사와 초안</strong></div>
    <div>어떤 자료를 더 확인해야 할지 판단하고, 발견한 위험의 근거를 정리합니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>워크플로우 · 반드시 지킬 절차</strong></div>
    <div>승인을 요청하고 결과에 따라 분기합니다. 승인되지 않으면 발송하지 않습니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>앱 · 사람이 일하는 화면</strong></div>
    <div>예를 들어 담당자가 초안과 근거를 나란히 보고 검토 의견을 남기는 화면을 만들 수 있습니다.</div>
  </div>
</div>

<p>세 가지를 한곳에서 만들 수 있다는 게 이번 업데이트의 핵심입니다. Microsoft는 <strong>Apps in Copilot Studio</strong>의 정식 출시(GA)와 11월 순차 배포를 발표했습니다. 시연에 나온 <strong>Copilot Cowork나 Copilot Code에서 자연어로 에이전트와 워크플로우를 만드는 기능</strong>은 발표 시점에 공개 미리 보기였습니다.</p>

<h2 class="mc-section-title">3 · 같은 모델이어도 실행 방식이 다르면 결과가 달라집니다</h2>

<p>에이전트가 여러 자료를 조사하려면 어떤 도구를 쓸지 정하고, 호출에 실패했을 때 다시 시도하거나 다른 경로를 찾아야 합니다. 이 실행 과정을 맡는 것이 <strong>하네스(harness)</strong>입니다. Microsoft는 BRK267에서 Claude Sonnet 4.6과 평가 과제를 그대로 두고, 표준 하네스와 새 Microsoft Copilot 하네스를 비교한 내부 평가를 공개했습니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">평가 항목</th><th scope="col">표준 하네스</th><th scope="col">Microsoft Copilot 하네스</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">코드 분석</th><td>40.6%</td><td>88.1% (+47.5%p)</td></tr>
      <tr><th scope="row">대화당 입력 토큰</th><td>47,800개</td><td>26,500개 (약 45% 감소)</td></tr>
    </tbody>
  </table>
</div>

<p>이 수치는 발표에서 사용한 평가 과제의 결과입니다. 특히 약 45%는 <strong>입력 토큰 감소율</strong>이지, 전체 운영 비용이 45% 줄었다는 뜻은 아닙니다.</p>

<h2 class="mc-section-title">4 · 배포 전에는 답변뿐 아니라 ‘하지 말아야 할 일’도 테스트합니다</h2>

<p>세션의 <strong>Evaluate</strong> 데모에서 모델별 실행 비용 추정치는 회당 약 0.40~2.00달러였지만, 기본 ‘일반 품질’ 채점 결과에는 뚜렷한 차이가 없었습니다. 이 수치는 데모 추정치이지 실제 요금이 아닙니다. 점수가 비슷하다면 두 모델의 품질이 같다고 보기 전에 채점 기준과 답변을 살펴봐야 합니다. 금융 데모라면 ‘문장이 자연스러운가’보다 ‘펀드 안의 간접 보유분까지 반영했는가’, ‘사내 한도 초과를 근거와 함께 설명했는가’가 더 유용한 기준입니다. <strong>승인이 거절됐을 때 메일이 나가지 않는지</strong>는 워크플로우에서 별도로 확인할 항목입니다.</p>

<div class="mc-callout">
  <p><strong>팀에서는 매주 반복하는 업무 하나부터 나눠 보세요.</strong></p>
  <p>AI가 자료를 모으고 초안을 쓸 구간, 반드시 지켜야 할 절차, 사람이 근거를 확인하고 결정할 순간을 각각 표시해 보세요. 처음부터 업무 전체를 맡기는 것보다, 어떤 결정은 사람에게 남길지 정하는 편이 좋은 출발점입니다.</p>
</div>

<p><a class="btn btn--primary" href="https://ignite.microsoft.com/en-US/sessions/BRK267">Ignite 공식 세션 보기 →</a></p>
<p class="mc-card-note">참고: <a href="https://www.youtube.com/watch?v=F1uiehsuwAU">BRK267 전체 녹화</a> · <a href="https://www.microsoft.com/en-us/copilot/blog/copilot-studio/build-and-manage-business-processes-with-microsoft-copilot-studio/">Microsoft Copilot Studio 공식 발표</a></p>
</div>
