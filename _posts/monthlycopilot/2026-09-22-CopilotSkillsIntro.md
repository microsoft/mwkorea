---
title: "Copilot에서 스킬(Skill) 사용하기 ① — 매번 설명하지 말고, 업무 방식을 저장하세요"
date: 2026-09-22T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - Skills
  - CopilotStudio
  - 업무활용
  - 월간코파일럿
excerpt: "보고서를 요청할 때마다 같은 조건을 반복하고 있나요? 스킬은 업무 처리 방법을 저장해 다시 쓰는 설명서입니다. SKILL.md의 구조부터 좋은 description을 쓰는 법, 첫 스킬을 설계하는 여섯 가지 질문까지 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 고현
---

<div class="monthlycopilot-page monthlycopilot-page--adoption">
<div class="mc-issue-strip">Monthly Copilot · October 2026 · 월간 코파일럿 10월호 · Copilot Skills ①</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 10월호 ｜ Copilot 스킬 시리즈</div>
  <div class="mc-cover-title">매번 설명하지 말고,<br/>업무 방식을 저장하세요</div>
  <div class="mc-cover-subtitle">Copilot에서 스킬(Skill) 사용하기 ① · 개념과 설계부터</div>
</div>

<img src="/mwkorea/assets/images/20260922-copilot-skills/01-cover.webp" alt="SKILL.md 문서를 중심으로 문서·표·발표 자료 등 여러 업무가 연결되는 모습을 표현한 일러스트" width="1536" height="1024" />

<h2 class="mc-section-title">이런 적 있으신가요</h2>

<p>Copilot에게 보고서를 요청할 때마다 이런 말을 덧붙이지 않으셨나요?</p>

<div class="mc-callout">
  <p>“결론부터 써줘. 없는 숫자는 추측하지 말고 '확인 필요'로 표시해줘. 의사결정 요청은 마지막에 넣어줘.”</p>
</div>

<p>같은 설명을 매번 반복하고, 빠뜨리면 결과물이 달라집니다. 이 반복을 줄여 주는 장치가 <strong>스킬(Skill)</strong>입니다. 이번 글에서는 등록 버튼을 누르는 방법보다 먼저, 스킬이 무엇이고 어떤 내용을 담아야 하는지 알아보겠습니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-skills/02-repeatable-work.webp" alt="매번 요청 조건을 입력하는 모습과 공통 업무 지침을 활용하는 모습을 대비한 일러스트" width="1536" height="1024" loading="lazy" />

<hr/>

<h2 class="mc-section-title">1 · Copilot만의 개념이 아닙니다</h2>

<p>스킬은 Copilot만의 전용 개념이 아니라, 여러 AI 도구에서 활용하는 방식입니다. 출발점은 같습니다. <strong>모델을 다시 학습시키지 않고, 업무를 수행하는 방법을 알려 주는 것</strong>입니다.</p>

<p>Microsoft는 에이전트 스킬을 지침, 스크립트, 참고 자료 등을 묶어 전문 지식과 작업 능력을 제공하는 재사용 가능한 패키지로 설명합니다. 필요한 작업에서 해당 지침을 불러오는 방식이므로, 모든 업무 설명을 매번 대화창에 붙여 넣을 필요가 줄어듭니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">구분</th><th scope="col">내용</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">형태</th><td>사람이 읽고 수정할 수 있는 지침 문서. 필요에 따라 참고 자료나 보조 파일을 함께 구성합니다.</td></tr>
      <tr><th scope="row">동작</th><td>사용자의 요청과 스킬의 설명을 바탕으로, 필요한 작업에서 지침을 불러옵니다.</td></tr>
      <tr><th scope="row">장점</th><td>모델을 재학습시키지 않고 지침을 수정해 업무 절차와 결과물 기준을 바꿀 수 있습니다.</td></tr>
    </tbody>
  </table>
</div>

<p>Copilot Studio의 GitHub Copilot 하네스 기반 에이전트도 이 방식을 지원합니다. 스킬은 도구나 지식과 함께 작동할 수 있습니다. 예를 들어 <strong>도구가 외부 서비스에 연결하는 수단</strong>이라면, <strong>스킬은 그 도구를 어떤 순서와 기준으로 사용할지 알려 주는 업무 지침</strong>입니다.</p>

<h2 class="mc-section-title">2 · 한 문장으로 말하면, 업무 설명서</h2>

<p>신입 사원에게 업무를 인수인계할 때 만드는 문서를 떠올리면 됩니다. 어떤 순서로 처리하는지, 결과물은 어떤 모양인지, 빠지면 안 되는 항목은 무엇인지를 적어 두는 문서입니다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>스킬은 업무 방법을 알려 주는 것이지, 권한을 부여하는 것이 아닙니다.</strong></p>
  <p>스킬 파일을 추가하는 것만으로 새로운 시스템이나 데이터에 접근할 수 있는 것은 아닙니다. 실제 접근 범위는 해당 제품의 사용자·에이전트 권한, 연결된 도구의 인증 방식과 조직 정책에 따릅니다.</p>
</div>

<p>또한 지침을 저장한다고 결과의 정확성이 자동으로 보장되는 것은 아닙니다. 반복되는 업무의 기준을 분명히 하고, 결과를 같은 기준으로 검토하기 쉬워지는 데 의미가 있습니다.</p>

<hr/>

<h2 class="mc-section-title">3 · 그때그때 하는 요청과 무엇이 다른가요?</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">구분</th><th scope="col">요청(프롬프트)</th><th scope="col">스킬</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">형태</th><td>대화창에 입력하는 요청과 조건</td><td>파일이나 패키지로 저장한 작업 지침</td></tr>
      <tr><th scope="row">재사용</th><td>새 대화에서 같은 조건을 다시 전달해야 할 수 있음</td><td>지원되는 환경에 등록해 반복 활용</td></tr>
      <tr><th scope="row">호출</th><td>사용자가 필요한 요청을 직접 입력</td><td>지원되는 실행 환경이 요청과 설명(description)을 보고 적합한 스킬을 선택</td></tr>
    </tbody>
  </table>
</div>

<p>요청문이 <strong>“이번 주문 내용”</strong>이라면, 스킬은 <strong>“매번 꺼내 쓰는 조리법”</strong>입니다. 대화 기록이 사라진다는 뜻은 아닙니다. 저장된 대화와 별개로, 반복해서 적용할 업무 지침을 독립적으로 관리한다는 차이입니다.</p>

<p>주간보고 작성, 회의록 정리처럼 반복되고 형식이 정해진 일에 먼저 적용해 보세요. 한 번뿐인 간단한 요청이라면 굳이 스킬로 만들지 않아도 됩니다.</p>

<h2 class="mc-section-title">4 · 스킬은 어떻게 생겼나요?</h2>

<p>스킬 패키지의 중심에는 <code>SKILL.md</code> 파일이 있습니다. 별도 폴더에 이 파일을 두고, 필요한 템플릿이나 참고 자료를 함께 구성할 수 있습니다. 파일은 크게 두 부분으로 나뉩니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>① 머리말 · 스킬의 이름표</strong></div>
    <div>문서 맨 위의 <code>---</code> 사이에 이름(<code>name</code>)과 설명(<code>description</code>)을 적습니다. 실행 환경이 “이 스킬은 언제 필요한가?”를 판단하는 단서입니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>② 본문 · 일하는 방법</strong></div>
    <div>작업 순서, 결과물의 모양, 검토 기준, 하지 말아야 할 일을 Markdown으로 작성합니다. 필요하면 보조 파일을 언제 참고할지도 적습니다.</div>
  </div>
</div>

<p>Copilot Studio에서는 지침을 담은 Markdown 파일이나, <code>SKILL.md</code>와 스크립트·템플릿·참고 문서를 포함하는 ZIP 패키지를 추가할 수 있습니다. 제품마다 지원하는 파일 형식과 등록 경로가 다르므로, 하나의 설치 방법이 모든 Copilot에 동일하게 적용된다고 생각하지 않는 것이 좋습니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-skills/03-skill-package.webp" alt="SKILL.md 파일과 보조 자료를 폴더 안에 구성하는 방식을 표현한 일러스트" width="1536" height="1024" loading="lazy" />

<hr/>

<h2 class="mc-section-title">5 · 가장 많이 막히는 지점은 설명(description)입니다</h2>

<p>스킬의 설명은 단순한 소개 문구가 아닙니다. <strong>사용자의 어떤 요청에 이 스킬을 꺼내야 하는지</strong> 알려 주는 단서입니다. 설명이 모호하면 적절한 상황에 선택되기 어렵습니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>아쉬운 설명</strong></div>
    <div>“보고서를 잘 만들어 주고 필요한 업무를 처리한다.”</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>더 구체적인 설명</strong></div>
    <div>“프로젝트 현황으로 주간보고를 작성하거나, 이번 주 진행 상황 정리를 요청할 때 사용한다.”</div>
  </div>
</div>

<p>요령은 <strong>사용자가 실제로 요청할 법한 문장</strong>을 넣는 것입니다. “주간보고를 작성해 줘”, “이번 주 프로젝트 현황을 정리해 줘”처럼 업무 상황을 구체화하세요. 여기에 이 스킬이 맡지 않을 일까지 적어 두면 범위가 더 명확해집니다.</p>

<h2 class="mc-section-title">6 · 처음 만들 때는 여섯 줄부터</h2>

<p>파일 편집기부터 열 필요는 없습니다. 반복하는 업무 하나를 고르고, 아래 여섯 질문에 한 줄씩 답해 보세요.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">질문</th><th scope="col">예시 · 주간보고</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">언제 쓰는가</th><td>“이번 주 프로젝트 현황을 정리해 줘”라고 요청할 때</td></tr>
      <tr><th scope="row">어떤 자료를 받는가</th><td>프로젝트 현황표, 보고 기준일과 기간</td></tr>
      <tr><th scope="row">무엇을 만드는가</th><td>정해진 순서로 구성된 주간보고 문서</td></tr>
      <tr><th scope="row">어디까지 맡기는가</th><td>보고서 작성까지. 메일 발송이나 일정 변경은 제외</td></tr>
      <tr><th scope="row">무엇을 금지하는가</th><td>없는 수치·날짜·지연 원인을 추측하지 않기</td></tr>
      <tr><th scope="row">빈칸은 어떻게 하는가</th><td>필수 조건은 사용자에게 질문하고, 확인되지 않은 값은 '확인 필요'로 표시</td></tr>
    </tbody>
  </table>
</div>

<p>이 여섯 줄에 작업 순서와 검토 기준을 덧붙이면 <code>SKILL.md</code>의 뼈대가 됩니다. 처음에는 업무 하나를 좁게 정의하고, 실제 요청으로 시험하면서 설명과 지침을 다듬는 편이 좋습니다.</p>

<hr/>

<h2 class="mc-section-title">오늘 기억할 세 가지</h2>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>업무 설명서</strong></div>
    <div>스킬은 AI에게 우리 업무의 처리 방법과 결과물 기준을 알려 줍니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>반복해서 재사용</strong></div>
    <div>매번 입력하던 공통 조건을 파일로 관리하고 지원되는 환경에서 다시 씁니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>구체적인 설명</strong></div>
    <div>description에는 실제 요청 문장과 적용할 업무 상황을 적습니다.</div>
  </div>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>다음 편 예고 · PowerPoint에서 스킬 활용하기</strong></p>
  <p>이번 편은 Copilot 스킬 시리즈의 첫 번째 글입니다. 다음 편에서는 PowerPoint에서 스킬을 선택하고 등록하는 방법, 그리고 회사 템플릿 기준에 맞춰 발표 자료를 정리하는 방법을 소개하겠습니다.</p>
</div>

<h2 class="mc-section-title">참고 자료와 이용 전 확인 사항</h2>

<ul>
  <li><a href="https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/skills-overview">Microsoft Learn — 에이전트 스킬 개요</a></li>
  <li><a href="https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/skills-add-existing">Microsoft Learn — 기존 스킬 추가와 지원 파일 형식</a></li>
  <li><a href="https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-customize">Microsoft Learn — Copilot Cowork의 스킬 사용자 지정</a></li>
</ul>

<p class="mc-card-note">이 글은 스킬의 개념과 설계 방법을 소개합니다. 실제 제공 기능·등록 방법·라이선스는 제품과 조직 설정에 따라 다릅니다. Copilot Studio의 GitHub Copilot 하네스 기반 에이전트는 빌드·테스트·실행 등에 Copilot Credits를 사용할 수 있습니다. 외부 스킬은 지침과 포함 파일을 검토한 뒤 신뢰할 수 있는 출처에서만 추가하세요. 공식 자료 확인일: 2026년 9월 22일.</p>

<p class="mc-card-note">본문 이미지는 원고에 포함된 설명용 일러스트이며, 실제 제품 화면이 아닙니다.</p>

</div>
