---
title: '데이터로 예방하고, AI로 선제 대응하다 — AI XYZ 팀의 Credit Risk Guardian'
date: 2026-06-16T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - Agent
  - PowerAutomate
  - AIBuilder
  - 고객사례
  - 월간코파일럿
excerpt: 'AI Tour Agenthon in Seoul 2026 로우코드 부문 2위 AI XYZ 팀은, 별도 개발 인력 없이 M365와 Copilot만으로 신용 리스크를 조기에 포착하는 「Credit Risk Guardian」을 만들어 업무 시간 83% 절감과 ROI 10배를 달성했습니다.'
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 김현지
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · July 2026 · 월간 코파일럿 7월호 · Customer Case · Agenthon</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Customer Case ｜ AI Tour Agenthon in Seoul 2026</div>
  <div class="mc-cover-title">데이터로 예방하고,<br/>AI로 선제 대응하다</div>
  <div class="mc-cover-subtitle">AI Tour Agenthon in Seoul 2026 — 코파일럿이 보여준 가능성</div>
</div>

<img src="/mwkorea/assets/images/20260616-aixyz/hero.png" alt="AI XYZ 팀의 Credit Risk Guardian 소개 이미지" />

<p>정유·에너지 업계에서 신용 리스크 관리는 단순한 재무 업무를 넘어, 회사의 손익을 좌우하는 핵심 과제입니다. 거래처 한 곳의 부실이 곧바로 큰 손실로 이어질 수 있고, 업종마다 위험이 드러나는 방식도 제각각이라 담당자의 경험과 직관에 의존하기엔 한계가 분명하죠. 매일 수십 곳의 거래처 정보를 일일이 들여다보는 일도 결코 만만치 않습니다.</p>

<p>이번 7월호에서는 바로 이 오래된 숙제를, 익숙한 도구로 새롭게 풀어낸 팀의 이야기를 소개합니다. <strong>AI Tour Agenthon in Seoul 2026</strong> 로우코드 부문에서 2위를 차지한 <strong>AI XYZ 팀</strong>은, 여신 담당자의 일상에 가장 가까이 다가가는 방식으로 답을 찾았습니다. 이들이 만든 <strong>「Credit Risk Guardian」</strong>은 업종별 특화 신용 리스크를 조기에 포착해 담당자에게 경보를 보내주는 에이전트로, 거래처 정보 수집부터 위험 분석, 등급 판정, 알림, 조치 기록까지 <strong>여신 업무 전 과정을 6단계로 자동화</strong>했습니다.</p>

<p>특히 주목할 점은 <strong>별도의 개발 인력이나 외부 솔루션 없이, 모두에게 익숙한 M365와 Copilot만으로 구축</strong>했다는 사실입니다. SharePoint, Power Automate, AI Builder, Teams처럼 이미 사내에 자리 잡은 도구들을 활용하여 Agent를 개발했고, 도입 후 <strong>업무 시간 83% 절감</strong>과 <strong>ROI 10배</strong>라는 성과를 만들어냈죠. AI가 분석하고 사람이 결정하는 <strong>Human-in-the-Loop</strong> 구조로 신뢰성까지 챙긴 점도 인상적입니다.</p>

<div class="mc-callout mc-card--blue">
  <div class="mc-card-title">Article Summary</div>
  <div>이번 호에서는 AI XYZ 팀이 어떤 문제의식에서 출발했는지, 6단계 자동화 흐름은 어떻게 설계됐는지 그 전 과정과 인사이트를 자세히 풀어봅니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">01 · 왜 지금, 이 에이전트인가 — 매일 2시간의 수동 검색</h2>

<p>여신 담당자의 하루는 검색창에서 시작됩니다. 담당자별 매일 50개가 넘는 거래처에 대해 공시 자료, 주가 흐름 등을 일일이 수기로 확인하는 일이 일상이었죠. 보기에는 단순한 반복 업무 같지만, 그 안에는 회사의 자산을 지키는 무거운 책임이 담겨 있습니다. 그러나 이 방식에는 네 가지 구조적인 한계가 있었습니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--red">
    <div class="mc-card-title">비효율적 수동 검색</div>
    <div>담당자별로 하루 평균 2시간 이상 이 검색에만 쓰이며, 본업인 분석과 판단에 쓸 시간을 잠식했습니다.</div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title">판단 오류 및 신호 누락</div>
    <div>정보량은 갈수록 늘고 담당자별 역량 편차는 존재하는 상황. 정작 중요한 위험 신호가 묻혀버리는 일이 적지 않았습니다.</div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title">위험 대응 지연</div>
    <div>위험을 감지하더라도 보고와 결재 절차를 거치다 보면 평균 1~2일이 소요됐고, 그사이 상황은 더 악화되곤 했습니다.</div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title">지식 자산 유실</div>
    <div>담당자가 바뀌면 그동안 쌓아온 분석 이력과 판단 근거가 함께 사라져, 업무 연속성에 공백이 생겼습니다.</div>
  </div>
</div>

<div class="mc-callout mc-card--blue">
  <div class="mc-card-title">AI XYZ 팀의 답</div>
  <div>"AI is eXpanding Your Zone." — 담당자의 업무 영역을 넓히고, 매일 반복되는 수작업을 AI가 대신한다. 사람은 그 시간을 아껴 진짜 중요한 판단과 결정에 집중한다. 단순한 자동화 도구가 아닌, <strong>담당자의 동료</strong>를 만들겠다는 발상이 출발점이었습니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">02 · 한 장으로 보는 6단계 End-to-End 자동화</h2>

<p>Credit Risk Guardian의 가장 큰 특징은 어느 한 지점만 자동화한 것이 아니라, <strong>데이터 수집부터 조치 기록까지 여신 업무 전 과정을 6단계로 끊김 없이 연결</strong>했다는 점입니다. 매일 오전 8시, 누구도 버튼을 누르지 않아도 에이전트가 알아서 하루 일과를 시작합니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title">STEP 01 · 거래처 정보 수집</div>
    <div>SharePoint 마스터 조회<br/><strong>➜ 기준 정보 일원화</strong></div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title">STEP 02 · 공개 정보 자동 수집</div>
    <div>Power Automate<br/><strong>➜ 수동 검색 0건</strong></div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title">STEP 03 · AI 위험 분석</div>
    <div>GPT-5 · AI Builder<br/><strong>➜ 분석 시간 83% ↓</strong></div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title">STEP 04 · 위험 등급 판정</div>
    <div>HIGH / MED / LOW 자동 분류<br/><strong>➜ 객관적 평가</strong></div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title">STEP 05 · Teams/메일 경보</div>
    <div>Adaptive Cards · 즉시 알림<br/><strong>➜ 당일 조치 완료</strong></div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title">STEP 06 · 조치 &amp; 기록</div>
    <div>SharePoint Audit Log<br/><strong>➜ 감사 추적 100%</strong></div>
  </div>
</div>

<p>각 단계는 독립적으로 작동하지 않습니다. SharePoint에 정리된 거래처 마스터 정보가 공개 정보 수집의 기준이 되고, 수집된 정보는 GPT-5와 AI Builder를 거쳐 위험 등급으로 정제됩니다. 그렇게 도출된 결과가 Teams와 메일을 통해 담당자에게 닿고, 담당자의 조치는 다시 SharePoint에 자동 기록되어 다음 분석의 자산이 됩니다. <strong>데이터가 사람을 거치지 않고도 알아서 흐르는 구조</strong>, 이것이 6단계 자동화의 핵심입니다.</p>

<hr/>

<h2 class="mc-section-title">03 · Human-in-the-Loop — AI는 제안하고, 사람이 결정한다</h2>

<p>Credit Risk Guardian이 단순한 알림 봇과 결정적으로 다른 지점이 바로 여기에 있습니다. AI Builder와 GPT 기반 프롬프트는 각 공개 정보의 문맥을 감성 분석하고, 업종별 지표를 반영해 HIGH/MED/LOW 위험 등급을 자동으로 부여합니다. 여기까지는 AI의 영역이죠.</p>

<p>그러나 <strong>한도 축소와 같이 거래처에 직접 영향을 미치는 고위험 의사결정은, 반드시 사람의 손을 거치도록</strong> 설계됐습니다. 담당자는 메일 속 '한도 축소 메일 작성하기' 버튼을 눌러 AI가 작성한 초안을 검토하고, 필요하다면 수정한 뒤에야 발송합니다. AI는 무거운 자료 정리를, 사람은 책임 있는 판단을 — 각자 가장 잘하는 일에 집중하는 구조입니다.</p>

<p>종합 리스크 판정은 공개 정보 유입 전 '보통'에서 유입 후 '높음'으로 자동 상향되며, 판단 근거·핵심 관리 포인트·권고 사항까지 에이전트가 보고서로 자동 완성합니다.</p>

<hr/>

<h2 class="mc-section-title">04 · 숫자로 증명된 임팩트</h2>

<p>도입 효과는 명확하게 측정됩니다. 단순히 "편해졌다"는 정성적 평가가 아니라, <strong>시간·비용·성과 모두에서 정량적 변화</strong>가 확인됩니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--green">
    <div class="mc-card-title">83%</div>
    <div>업무 시간 절감<br/>2시간 → 20분</div>
  </div>
  <div class="mc-card mc-card--green">
    <div class="mc-card-title">수십억원</div>
    <div>연간 손실 예방<br/>조기 차단 효과</div>
  </div>
  <div class="mc-card mc-card--green">
    <div class="mc-card-title">10배</div>
    <div>투자 대비 효과(ROI)<br/>M365 활용, 추가 비용 Zero</div>
  </div>
</div>

<p>특히 <strong>ROI 10배는 기존에 사용하던 M365 라이선스와 연계하여 구현</strong>한 결과라는 점에서 의미가 큽니다. 새로운 솔루션 도입 비용도, 별도 개발 조직도 없이, 이미 가진 도구를 잘 엮는 것만으로도 이 정도 성과가 가능하다는 사실을 보여준 셈이죠.</p>

<p><strong>기존 업무와 비교하면 변화의 폭이 더욱 뚜렷합니다.</strong></p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>항목</th><th>Before</th><th>After</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>업무 처리 시간</strong></td><td>담당자별 2시간 / 매일 50+ 거래처 수동 검색</td><td>20분 이내 / 자동 분석 (83% ↓)</td></tr>
      <tr><td><strong>정확도 &amp; 신뢰성</strong></td><td>정보 과부하로 중요 신호 누락·오판</td><td>GPT 신뢰도 점수 공개 · 7개 지표 교차 검증</td></tr>
      <tr><td><strong>위험 대응 속도</strong></td><td>보고서·결재 대기 1~2일 지연</td><td>Teams 실시간 경보 · 당일 조치</td></tr>
      <tr><td><strong>지식 관리</strong></td><td>담당자 교체 시 노하우·이력 유실</td><td>SharePoint 자동 저장 · 감사 추적 100%</td></tr>
    </tbody>
  </table>
</div>

<div class="mc-callout mc-callout--dark">
  익숙한 M365와 Copilot, 그리고 Human-in-the-Loop 설계만으로도 현장의 오랜 숙제는 풀립니다. AI XYZ 팀의 Credit Risk Guardian은 "거창한 새 솔루션"이 아니라 "이미 가진 도구를 제대로 엮는 일"에서 출발했습니다. 우리 팀의 반복 업무 한 가지도, 같은 방식으로 다시 설계해 볼 수 있지 않을까요?
</div>

</div>
