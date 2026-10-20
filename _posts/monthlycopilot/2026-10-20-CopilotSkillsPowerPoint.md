---
title: "Copilot에서 스킬(Skill) 사용하기 ② — PowerPoint에서 회사 서식, 스킬로 한 번에 맞추기"
date: 2026-10-20T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - Skills
  - PowerPoint
  - 업무활용
  - 월간코파일럿
excerpt: "장표를 합칠 때마다 글꼴과 색, 표 서식을 다시 맞추고 있나요? PowerPoint의 Copilot에 회사 서식 스킬을 등록하고, 기존 자료 정돈부터 작업 기록, 새 장표 추가, 제출 전 점검까지 반복 업무에 활용하는 방법을 소개합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 고현
---

<div class="monthlycopilot-page monthlycopilot-page--adoption">
<div class="mc-issue-strip">Monthly Copilot · November 2026 · 월간 코파일럿 11월호 · Copilot Skills ②</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 11월호 ｜ Copilot 스킬 시리즈</div>
  <div class="mc-cover-title">회사 서식,<br/>매번 설명하지 마세요</div>
  <div class="mc-cover-subtitle">Copilot에서 스킬(Skill) 사용하기 ② · PowerPoint에서 회사 서식, 스킬로 한 번에 맞추기</div>
</div>

<p>내용은 다 모았는데, 발표 자료는 아직 완성되지 않았습니다. 어떤 장표는 제목이 크고, 어떤 장표는 본문 글꼴이 다릅니다. 표 머리글과 차트 색까지 맞추다 보면 마지막 서식 정리에 생각보다 많은 손이 갑니다.</p>

<p>지난 <a href="{{ '/monthlycopilot/CopilotSkillsIntro/' | relative_url }}">①편</a>에서는 스킬을 <strong>“반복해서 꺼내 쓰는 업무 설명서”</strong>로 소개했습니다. 이번에는 그 설명서에 회사 서식 기준을 담아 PowerPoint에서 활용해 보겠습니다. 매번 긴 조건을 입력하는 대신, 등록해 둔 스킬을 불러 같은 기준으로 정돈을 요청하는 방법입니다.</p>

<img src="{{ '/assets/images/20261020-copilot-skills-powerpoint/01-company-format.webp' | relative_url }}" alt="제각각인 발표 자료가 Copilot의 공통 서식 지침을 거쳐 남색 계열의 일관된 장표로 정돈되는 모습을 표현한 일러스트" width="1536" height="1024" />

<div class="mc-callout">
  <p>“제목은 회사 글꼴 28pt로, 본문은 18pt로 맞춰줘. 강조색은 회사 남색만 써줘. 표 머리글은 회색 바탕으로 해줘.”</p>
  <p>이 말을 자주 반복하고 있다면, 회사 서식 스킬을 만들 좋은 출발점입니다.</p>
</div>

<p>스킬은 서식 적용을 돕는 지침이지, 결과를 자동으로 보증하는 장치는 아닙니다. 먼저 원본의 사본에서 시험하고, 적용 뒤에는 내용과 서식이 의도대로 유지됐는지 확인하세요.</p>

<h2 class="mc-section-title">1 · PowerPoint에서 스킬 부르기</h2>

<p>PowerPoint의 Copilot 창을 열면 두 가지 방식으로 스킬을 선택할 수 있습니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>목록에서 고르기</strong></div>
    <div>요청 입력창의 <strong>+ → 기술 선택(Choose skills)</strong>을 누른 뒤 원하는 스킬을 고릅니다. 기본 제공 스킬과 내가 추가한 스킬을 확인할 수 있습니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>이름으로 부르기</strong></div>
    <div>입력창에 <strong>@스킬이름</strong>을 적고 요청을 덧붙입니다. 자주 쓰는 스킬의 이름을 알고 있다면 바로 지정할 수 있습니다.</div>
  </div>
</div>

<p>예를 들어 <code>company-format</code>이라는 스킬을 등록했다면 이렇게 요청합니다.</p>

<pre><code>@company-format 이 자료 전체를 회사 서식 기준으로 정리해줘.</code></pre>

<p class="mc-card-note">한국어 화면에서는 스킬이 ‘기술’로 표시되기도 합니다. 메뉴 이름과 제공 여부는 제품 버전 및 조직 설정에 따라 다를 수 있습니다.</p>

<div class="mc-callout">
  <p><strong>스킬과 브랜드 키트는 역할이 다릅니다.</strong></p>
  <p>서식 스킬에는 글꼴·색·표 규칙처럼 <strong>“어떻게 다듬을지”</strong>를 적습니다. 로고·템플릿 같은 디자인 자산은 <strong>브랜드 키트(Brand kit)</strong>로 관리할 수 있습니다. 브랜드 키트에서 조직의 스킬을 공유하는 방식도 지원합니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">2 · 유스케이스 ① 기존 자료를 회사 서식으로 정돈하기</h2>

<p>여러 부서의 장표를 하나로 합쳤다면, 우선 <strong>내용은 그대로 두고 서식만 정리하는 스킬</strong>부터 만들어 보세요. “깔끔하게 해줘”보다 글꼴 이름, 크기, 색상 값, 표 정렬을 구체적으로 적는 것이 좋습니다.</p>

<p>아래는 <code>company-format</code> 스킬의 <code>SKILL.md</code> 예시입니다. <strong>[회사 글꼴]</strong>과 <strong>[회사 대표색 HEX]</strong>는 실제 기준으로 바꿔 주세요.</p>

<pre><code class="language-markdown">---
name: company-format
description: &gt;-
  발표 자료를 회사 서식 기준으로 통일할 때 사용한다.
  "회사 서식으로 맞춰줘", "서식 통일해줘" 같은 요청에 적용한다.
  내용을 고치는 요청에는 사용하지 않는다.
---
# 회사 서식 정돈

## 서식 기준
- 글꼴: 제목 [회사 글꼴] 28pt 굵게, 본문 [회사 글꼴] 16~18pt
- 색상: 강조색은 [회사 대표색 HEX] 한 가지만 사용
- 제목: 왼쪽 위의 같은 위치에 배치
- 표: 머리글 연회색 바탕과 굵게, 숫자 오른쪽 정렬, 천 단위 쉼표
- 출처: 왼쪽 아래 10pt 회색

## 하지 않을 일
- 수치, 문장 내용, 장표 순서를 바꾸지 않는다.
- 출처가 없는 장표에 출처를 만들어 넣지 않는다.
- 제목이 길어 문장 수정이 필요하거나 판단이 어려운 장표는
  임의로 고치지 않고 '확인 필요'로 남긴다.

## 결과
- 바꾼 장표 목록과 '확인 필요' 장표를 마지막에 정리한다.</code></pre>

<p>핵심은 <strong>적용할 기준과 건드리지 않을 범위를 함께 적는 것</strong>입니다. 서식 정리를 요청했는데 수치나 문장이 달라지면 검토할 일이 오히려 늘어납니다. 제목을 결론형 문장으로 바꾸는 작업처럼 내용 수정이 필요한 일은 별도 요청으로 나누는 편이 안전합니다.</p>

<h2 class="mc-section-title">3 · 유스케이스 ② 한 번 해 보이고 스킬로 저장하기</h2>

<p>평소 하던 작업을 글로 설명하기 어렵다면 <strong>스킬 기록(Record Skill)</strong>을 활용할 수 있습니다. PowerPoint에서 직접 수행한 작업을 바탕으로 Copilot이 재사용할 스킬 지침의 초안을 만듭니다.</p>

<ol>
  <li>발표 자료와 Copilot 창을 열고 <strong>+ → 기술 선택 → 플러그 인 및 기술 관리(Manage plugins &amp; skills)</strong>로 이동합니다.</li>
  <li><strong>사용자 지정 스킬(Custom skills) → 스킬 추가(Add skill) → 스킬 기록(Record Skill)</strong>을 선택합니다. 기록이 자동으로 시작됩니다.</li>
  <li>표 머리글, 차트 색, 로고 위치 등을 평소처럼 정리합니다. Copilot에게 요청하거나, 장표를 직접 편집하거나, PowerPoint 리본 메뉴를 사용해도 됩니다.</li>
  <li>작업이 끝나고 원하는 변경이 실제 장표에 반영된 것을 확인한 뒤 <strong>중지(Stop)</strong>를 누릅니다.</li>
  <li>생성된 <strong>이름·설명·지침</strong>을 검토하고 필요한 부분을 수정한 다음 <strong>업로드(Upload)</strong>합니다. 업로드 완료를 확인하면 목록에서 다시 불러 쓸 수 있습니다.</li>
</ol>

<div class="mc-callout mc-callout--dark">
  <p><strong>한 번에 명확한 결과 하나, 기록은 10분 미만으로.</strong></p>
  <p>반복되는 슬라이드 서식, 표 정리, 차트 스타일, 로고 배치, 레이아웃 변경이 좋은 후보입니다. 아직 실행 중인 Copilot 작업은 기록에 포함되지 않을 수 있으므로, 변경이 화면에 나타난 뒤 기록을 멈추세요. 음성 설명과 다른 앱·창으로 전환한 뒤의 작업은 기록되지 않습니다.</p>
</div>

<p>기록을 마쳤다고 검토까지 끝난 것은 아닙니다. 다른 자료에서도 재사용할 수 있도록, 이름과 설명이 작업 목적을 잘 드러내는지, 지침에 특정 장표에만 맞는 조건이 남아 있지는 않은지 살펴보세요.</p>

<hr/>

<h2 class="mc-section-title">4 · 유스케이스 ③ 새 장표도 기존 디자인에 맞춰 추가하기</h2>

<p>자료를 다 만든 뒤 “맨 앞에 요약 한 장만 더 넣자”는 요청을 받을 때도 있습니다. 이때는 내용을 요약하는 것에 더해, <strong>기존 자료의 디자인을 확인한 뒤 같은 스타일로 추가하도록</strong> 스킬에 순서를 적어 둡니다.</p>

<pre><code class="language-markdown">---
name: add-summary-slide
description: &gt;-
  요약 장표나 결정 요청 장표를 새로 추가할 때 사용한다.
  "요약 장표 넣어줘", "결정 사항 장표 추가해줘" 같은 요청에 적용한다.
---
# 기존 디자인에 맞춘 장표 추가

1. 사용자가 요청한 내용으로 새 장표의 내용을 만든다.
2. 기존 자료의 글꼴, 색상, 제목 위치, 레이아웃을 확인한다.
3. 같은 디자인으로 새 장표를 추가한다.
4. 자료에 없는 수치나 결정 사항은 만들지 않고 '확인 필요'로 표시한다.</code></pre>

<p><code>@add-summary-slide 이 자료의 핵심을 요약한 장표를 맨 앞에 추가해줘.</code>처럼 요청할 수 있습니다. 결정 요청 장표라면 이미 결정된 내용과 앞으로 승인이 필요한 내용을 혼동하지 않았는지도 확인하세요.</p>

<h2 class="mc-section-title">5 · 유스케이스 ④ 제출 전 서식 점검하기</h2>

<p>고객에게 보낼 자료가 거의 완성됐다면, 바로 고치기보다 기준과 다른 곳부터 확인하고 싶을 수 있습니다. 이때는 <strong>수정하지 않고 점검 결과만 돌려주는 스킬</strong>을 따로 둡니다.</p>

<pre><code class="language-markdown">---
name: format-check
description: &gt;-
  발표 자료가 회사 서식 기준에 맞는지 제출 전에 점검할 때 사용한다.
  "서식 점검해줘", "제출 전에 확인해줘" 같은 요청에 적용한다.
  자료를 직접 수정하지 않는다.
---
# 회사 서식 점검

## 점검 기준
- 글꼴: 제목 [회사 글꼴] 28pt 굵게, 본문 [회사 글꼴] 16~18pt
- 색상: 강조색으로 [회사 대표색 HEX] 외의 색을 사용했는지
- 제목: 왼쪽 위의 같은 위치에 있는지
- 표: 머리글 연회색 바탕과 굵게, 숫자 오른쪽 정렬, 천 단위 쉼표
- 출처: 출처 표기가 필요한 장표에 출처가 있는지

## 결과
- 슬라이드 번호 | 항목 | 현재 상태 | 권장 수정 표로 정리한다.
- 확인할 수 없는 항목은 '확인 필요'로 표시한다.
- 장표를 직접 수정하지 않는다.</code></pre>

<p>점검 스킬에도 실제 회사 기준을 넣어야 합니다. “회사 기준에 맞는지 확인해줘”라는 말만으로 Copilot이 우리 회사의 글꼴과 색상 규칙을 알고 있다고 가정하지 마세요.</p>

<img src="{{ '/assets/images/20261020-copilot-skills-powerpoint/02-format-and-check.webp' | relative_url }}" alt="발표 자료의 서식을 정돈하는 로봇과 기준에 맞는지 점검하는 로봇을 나란히 표현한 일러스트" width="1536" height="1024" loading="lazy" />

<div class="mc-callout">
  <p><strong>정돈과 점검은 나누세요.</strong></p>
  <p><code>company-format</code>은 정해진 범위에서 서식을 바꾸고, <code>format-check</code>는 바꾸지 않은 채 검토 목록을 만듭니다. 둘을 나누면 “확인만 하고 싶었는데 장표가 바뀌는” 상황을 줄이는 데 도움이 됩니다. 회사 기준이 바뀌면 두 스킬의 기준도 함께 갱신하세요.</p>
</div>

<hr/>

<h2 class="mc-section-title">6 · 내 스킬 등록하기</h2>

<p>스킬의 내용을 준비했다면 다음 세 가지 방법 가운데 편한 방식을 선택할 수 있습니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">방법</th><th scope="col">이렇게 합니다</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">파일 업로드</th><td><strong>+ → 기술 선택 → 기술 관리(Manage skills) → 스킬 추가</strong>에서 스킬 파일을 업로드하거나 끌어다 놓습니다.</td></tr>
      <tr><th scope="row">직접 붙여넣기</th><td><strong>스킬 추가</strong> 화면의 입력 양식에 스킬 내용을 붙여넣고 <strong>추가(Add)</strong>를 선택합니다.</td></tr>
      <tr><th scope="row">OneDrive 폴더에 복사</th><td>Copilot 창의 <strong>설정(…) → 기술 관리 → 사용자 지정 스킬 → OneDrive 폴더 만들기</strong>를 선택합니다. <strong>스킬 폴더 열기</strong>로 이동해 준비한 스킬 폴더를 넣습니다.</td></tr>
    </tbody>
  </table>
</div>

<p>폴더로 준비할 때는 <strong>스킬마다 개별 폴더</strong>를 만들고 그 안에 <code>SKILL.md</code>를 둡니다. 예를 들어 첫 번째 스킬은 <code>company-format</code> 폴더 안에 저장하고, 파일 머리말의 <code>name</code>도 <code>company-format</code>으로 맞춥니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>등록 전 확인</strong></div>
    <ul>
      <li>폴더 이름과 <code>SKILL.md</code>의 <code>name</code> 값이 같아야 합니다.</li>
      <li>파일 맨 위의 <code>---</code> 사이에 <code>name</code>과 <code>description</code>을 넣습니다.</li>
      <li>개인용 사용자 지정 스킬을 ZIP으로 업로드할 때 PNG 같은 이미지 파일, PDF, 중첩 ZIP은 현재 지원되지 않습니다.</li>
    </ul>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>등록 후 확인</strong></div>
    <ul>
      <li>목록에 스킬이 나타나는지 확인하고, 사본 자료에서 호출해 봅니다.</li>
      <li>OneDrive에서 추가·수정·이름 변경을 했다면 <strong>새로 고침(Refresh)</strong>으로 반영합니다.</li>
      <li>기술 관리에서 스킬을 끄면 자동 사용이 중지되고 선택 목록에서도 숨겨집니다.</li>
    </ul>
  </div>
</div>

<p>이렇게 등록한 사용자 지정 스킬은 <strong>내 OneDrive의 스킬 폴더에 저장되는 개인용</strong>입니다. 동료에게도 자동으로 배포되는 것은 아닙니다. 팀·조직이 함께 쓰려면 브랜드 키트에서 스킬을 공유하거나, Microsoft 365 관리자가 조직 전체 또는 특정 사용자·그룹에 배포하는 방식을 검토하세요.</p>

<p class="mc-card-note">관리자 배포용 패키지는 개인용 업로드와 구성이 다릅니다. 스킬 파일 외에 앱 매니페스트와 아이콘 등을 포함해야 하므로, 아래 ‘조직 스킬 배포’ 안내의 별도 패키지 요구 사항을 확인하세요.</p>

<h2 class="mc-section-title">오늘 기억할 세 가지</h2>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>서식 기준은 스킬로</strong></div>
    <div>매번 말하던 글꼴, 색, 표 규칙을 저장해 두고 목록이나 <code>@이름</code>으로 불러 씁니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>구체적인 기준과 경계</strong></div>
    <div>“깔끔하게” 대신 숫자와 이름으로 적고, 내용·수치처럼 바꾸면 안 되는 범위도 명시합니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>정돈과 점검은 따로</strong></div>
    <div>고치는 스킬과 확인만 하는 스킬을 구분해 상황에 맞게 사용합니다.</div>
  </div>
</div>

<p>처음부터 모든 서식을 한 번에 담을 필요는 없습니다. 가장 자주 반복하는 정리 작업 하나를 스킬로 만들고, 실제 자료에 적용해 보면서 지침을 다듬어 보세요. 중요한 것은 긴 요청문을 저장하는 데 그치지 않고, <strong>우리 팀이 어떤 기준으로 자료를 만들고 검토하는지 분명히 하는 것</strong>입니다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>다음 편 예고 · Copilot Chat에서 스킬 활용하기</strong></p>
  <p>다음 편에서는 Copilot Chat에서 스킬을 불러 쓰고, 자주 하는 요청을 스킬로 저장하는 방법을 소개합니다. 메일 요약, 회의록 정리, 보고서 초안처럼 일상적으로 반복하는 업무로 활용 범위를 넓혀 보겠습니다.</p>
</div>

<h2 class="mc-section-title">참고 자료와 이용 전 확인 사항</h2>

<ul>
  <li><a href="https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills">Microsoft Support — PowerPoint의 Copilot에서 사용자 지정 스킬 사용하기</a></li>
  <li><a href="https://support.microsoft.com/en-us/powerpoint/copilot/record-skill-copilot-powerpoint">Microsoft Support — PowerPoint의 Copilot에서 스킬 기록하기</a></li>
  <li><a href="https://support.microsoft.com/en-us/powerpoint/copilot/brand-skill-support-copilot-powerpoint">Microsoft Support — PowerPoint의 Copilot용 브랜드 스킬 지원</a></li>
  <li><a href="https://support.microsoft.com/en-us/powerpoint/copilot/deploy-organization-skills-for-copilot-in-powerpoint">Microsoft Support — PowerPoint의 Copilot용 조직 스킬 배포</a></li>
  <li><a href="{{ '/monthlycopilot/CopilotSkillsIntro/' | relative_url }}">월간 코파일럿 10월호 — Copilot에서 스킬(Skill) 사용하기 ①</a></li>
</ul>

<p class="mc-card-note">실제 제공 기능·메뉴 이름·라이선스는 제품 버전과 조직 설정에 따라 다를 수 있습니다. 외부에서 받은 스킬은 지침과 포함 파일을 검토한 뒤 신뢰할 수 있는 출처의 것만 추가하세요. 본문의 SKILL.md는 설명용 예시이며, [ ] 안의 값은 각 회사 기준으로 바꿔 사용해야 합니다. 공식 자료 확인일: 2026년 10월 20일.</p>

<p class="mc-card-note">본문 이미지는 원고에 포함된 설명용 일러스트이며, 실제 제품 화면이 아닙니다.</p>

</div>
