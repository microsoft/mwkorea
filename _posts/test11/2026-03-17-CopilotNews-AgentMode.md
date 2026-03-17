---
title: "코파일럿 뉴우쓰: Agent Mode, 이제 AI가 문서 안에서 같이 일합니다"
date: 2026-03-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - AI
  - Agent Mode
  - Microsoft 365 Copilot
  - Word
  - Excel
  - PowerPoint
excerpt: "Word, Excel, PowerPoint에서 Copilot이 직접 편집하고 이어서 일하는 Agent Mode를 소개합니다. Chat 기반 Agents와의 차이, 앱별 활용 장면, 바로 써볼 수 있는 실전 프롬프트 9개까지 담았습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<style>
.cn-wrap { max-width: 860px; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color: #1a1a2e; }

/* 커버 */
.cn-hero { background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); border-radius: 20px; padding: 2.8rem 2.2rem; margin-bottom: 2rem; color: #fff; position: relative; overflow: hidden; }
.cn-hero::before { content: ''; position: absolute; top: -40px; right: -40px; width: 220px; height: 220px; background: radial-gradient(circle, rgba(99,102,241,0.35) 0%, transparent 70%); border-radius: 50%; }
.cn-hero-badge { display: inline-block; background: linear-gradient(90deg, #6366f1, #8b5cf6); color: #fff; font-size: 0.7rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; padding: 0.3rem 0.85rem; border-radius: 999px; margin-bottom: 1rem; }
.cn-hero-title { font-size: 2rem; font-weight: 900; line-height: 1.25; margin-bottom: 0.6rem; }
.cn-hero-sub { font-size: 1rem; color: #c7d2fe; line-height: 1.7; }
.cn-hero-quote { margin-top: 1.2rem; border-left: 3px solid #818cf8; padding-left: 1rem; color: #e0e7ff; font-style: italic; font-size: 0.95rem; }

/* 리드 박스 */
.cn-lead { background: linear-gradient(135deg, #eff6ff 0%, #f5f3ff 100%); border: 1px solid #c7d2fe; border-radius: 16px; padding: 1.2rem 1.4rem; margin-bottom: 1.6rem; }
.cn-lead-label { font-weight: 900; color: #4338ca; font-size: 0.8rem; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.4rem; }
.cn-lead-text { color: #374151; line-height: 1.8; font-size: 0.97rem; }

/* 섹션 헤더 */
.cn-section-h { display: flex; align-items: center; gap: 0.6rem; margin: 2rem 0 0.85rem; padding: 0.6rem 1rem; border-radius: 10px; font-size: 1.1rem; font-weight: 900; }
.cn-section-h.blue   { background: #eff6ff; border-left: 5px solid #2563eb; color: #1e3a8a; }
.cn-section-h.green  { background: #f0fdf4; border-left: 5px solid #16a34a; color: #14532d; }
.cn-section-h.teal   { background: #f0fdfa; border-left: 5px solid #0d9488; color: #134e4a; }
.cn-section-h.cyan   { background: #ecfeff; border-left: 5px solid #0891b2; color: #164e63; }
.cn-section-h.violet { background: #f5f3ff; border-left: 5px solid #7c3aed; color: #3b0764; }
.cn-section-h.orange { background: #fff7ed; border-left: 5px solid #ea580c; color: #7c2d12; }
.cn-section-h.indigo { background: #eef2ff; border-left: 5px solid #4f46e5; color: #312e81; }

/* 카드 그리드 */
.cn-grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 1rem 0 1.4rem; }
.cn-grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin: 1rem 0 1.4rem; }
@media (max-width: 640px) { .cn-grid-3 { grid-template-columns: 1fr; } .cn-grid-2 { grid-template-columns: 1fr; } }
.cn-card { border-radius: 14px; padding: 1rem 1.05rem; }
.cn-card-title { font-weight: 800; margin-bottom: 0.35rem; font-size: 0.9rem; }
.cn-card-body { font-size: 0.88rem; line-height: 1.65; }
.cn-card.blue   { background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a; }
.cn-card.cyan   { background: #ecfeff; border: 1px solid #99f6e4; color: #115e59; }
.cn-card.violet { background: #f5f3ff; border: 1px solid #ddd6fe; color: #4c1d95; }
.cn-card.green  { background: #f0fdf4; border: 1px solid #86efac; color: #166534; }
.cn-card.red    { background: #fef2f2; border: 1px solid #fecaca; color: #991b1b; }
.cn-card.amber  { background: #fffbeb; border: 1px solid #fde68a; color: #92400e; }
.cn-card.slate  { background: #f8fafc; border: 1px solid #cbd5e1; color: #1e293b; }
.cn-card.orange { background: #fff7ed; border: 1px solid #fdba74; color: #c2410c; }

/* 비교 테이블 */
.cn-table { width: 100%; border-collapse: collapse; border-radius: 14px; overflow: hidden; margin: 1rem 0 1.5rem; font-size: 0.9rem; }
.cn-table thead tr { background: #1e1b4b; color: #f9fafb; }
.cn-table thead th { padding: 0.85rem 1rem; text-align: left; }
.cn-table tbody tr:nth-child(odd)  { background: #f8fafc; }
.cn-table tbody tr:nth-child(even) { background: #fff; }
.cn-table td { padding: 0.8rem 1rem; border-bottom: 1px solid #e5e7eb; vertical-align: top; color: #1f2937; }
.cn-table td:first-child { font-weight: 700; }

/* 인용/강조 박스 */
.cn-tip { border-radius: 14px; padding: 1rem 1.2rem; margin: 1rem 0 1.4rem; }
.cn-tip.blue   { background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8; }
.cn-tip.dark   { background: #1e1b4b; color: #e0e7ff; }
.cn-tip.amber  { background: #fffbeb; border: 1px solid #fcd34d; color: #78350f; }
.cn-tip.teal   { background: #f0fdfa; border: 1px solid #5eead4; color: #115e59; }

/* 프롬프트 카드 */
.cn-prompt { background: #f8fafc; border: 1px solid #dbe4f0; border-radius: 14px; padding: 1rem 1.1rem; margin: 0.8rem 0; }
.cn-prompt-label { font-weight: 800; color: #1e40af; margin-bottom: 0.4rem; font-size: 0.9rem; }
.cn-prompt-text { background: #fff; border: 1px dashed #93c5fd; border-radius: 8px; padding: 0.75rem 1rem; font-size: 0.88rem; line-height: 1.75; color: #1f2937; margin: 0.5rem 0; }
.cn-prompt-tip { color: #64748b; font-size: 0.83rem; margin-top: 0.45rem; }

/* 체크리스트 */
.cn-checklist { list-style: none; padding: 0; margin: 0.6rem 0 1rem; }
.cn-checklist li { padding: 0.45rem 0; padding-left: 1.6rem; position: relative; color: #374151; font-size: 0.93rem; }
.cn-checklist li::before { content: '✅'; position: absolute; left: 0; }

/* 구분선 */
.cn-divider { border: none; border-top: 2px dashed #e2e8f0; margin: 1.8rem 0; }

/* 마무리 CTA */
.cn-cta { background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%); border-radius: 18px; padding: 1.8rem 1.6rem; color: #f9fafb; margin-top: 2rem; }
.cn-cta-title { font-weight: 900; font-size: 1.05rem; margin-bottom: 0.6rem; color: #c7d2fe; letter-spacing: 0.06em; text-transform: uppercase; }
.cn-cta-items { line-height: 2; font-size: 0.95rem; }
.cn-cta-note { margin-top: 0.9rem; color: #a5b4fc; font-size: 0.88rem; line-height: 1.7; }

/* 섹션 서브헤더 */
.cn-sub-h { font-weight: 800; color: #1f2937; margin: 1rem 0 0.5rem; font-size: 0.95rem; }
</style>

<div class="cn-wrap">

<!-- ===== 커버 ===== -->
<div class="cn-hero">
  <div class="cn-hero-badge">🤖 Copilot New Feature · March 2026</div>
  <div class="cn-hero-title">이제 Copilot은<br/>'도구'가 아니라 '동료'입니다</div>
  <div class="cn-hero-sub">From AI Assistant to AI Doer<br/>Agent Mode로 바뀌는 일하는 방식을 소개합니다.</div>
  <div class="cn-hero-quote">"Agent Mode는 '말로 지시하는 AI'가 아니라<br/>'같이 문서를 고치는 AI'입니다."</div>
</div>

<!-- ===== 리드 ===== -->
<div class="cn-lead">
  <div class="cn-lead-label">이번 호 핵심 요약</div>
  <div class="cn-lead-text">이번 달 코파일럿 뉴우쓰에서는 Microsoft 365 Copilot의 새로운 진화, <strong>Agent Mode</strong>를 집중 소개합니다. Copilot은 이제 단순히 "물어보면 답해주는 AI"를 넘어, Word·Excel·PowerPoint 안에서 <strong>직접 편집하고 이어서 일하는 협업 파트너</strong>로 진화하고 있습니다. Agent Mode와 Chat 기반 Agents의 차이, 앱별 활용 장면, 바로 써볼 수 있는 실전 프롬프트 9개까지 이 한 편에 모두 담았습니다.</div>
</div>

<!-- ===== Agent Mode란? ===== -->
<div class="cn-section-h blue">✨ Agent Mode란 무엇인가요?</div>

<p>Agent Mode는 Word, Excel, PowerPoint 앱 안에서 Copilot이 실제 문서(Canvas) 위에서 여러 단계를 스스로 계획하고 실행하며 사람과 협업하듯 작업을 이어가는 새로운 방식입니다.</p>

<div class="cn-grid-3">
  <div class="cn-card blue">
    <div class="cn-card-title">👉 실제 문서(Canvas) 위에서</div>
    <div class="cn-card-body">Word, Excel, PowerPoint 앱 안에서 결과물을 바로 다룹니다.</div>
  </div>
  <div class="cn-card cyan">
    <div class="cn-card-title">👉 여러 단계를 스스로 계획·실행</div>
    <div class="cn-card-body">계획–편집–반복 작업을 한 흐름으로 이어갑니다.</div>
  </div>
  <div class="cn-card violet">
    <div class="cn-card-title">👉 사람과 협업하듯 이어가는 방식</div>
    <div class="cn-card-body">단순 응답이 아니라 함께 완성해 가는 협업형 작업입니다.</div>
  </div>
</div>

<!-- 비교 테이블 -->
<div style="overflow-x: auto;">
<table class="cn-table">
  <thead>
    <tr>
      <th>구분</th>
      <th>Agent Mode</th>
      <th>Agents (Copilot Chat 기반)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>작업 위치</td>
      <td>Word / Excel / PowerPoint 앱(데스크톱·웹) 안에서 사용</td>
      <td>Microsoft 365 Copilot Chat(데스크톱·웹·모바일)에서 사용</td>
    </tr>
    <tr>
      <td>작업 방식</td>
      <td>Copilot이 문서·시트·슬라이드 화면에서 직접 편집하며 함께 완성</td>
      <td>Copilot이 결과물을 먼저 생성 → 채팅으로 수정·보완하거나 앱에서 열어 편집</td>
    </tr>
    <tr>
      <td>강점</td>
      <td>계획–실행–반복을 빠르게 돌리는 실시간 협업 (에이전틱 작업), 구조·브랜딩 유지, 변경 이력 확인</td>
      <td>대화형 프롬프트로 아이디어를 빠르게 완성도 높은 결과물로 변환</td>
    </tr>
  </tbody>
</table>
</div>

<div class="cn-tip blue">
  <strong>💡 핵심 한 줄 요약</strong><br/>
  Agent Mode는 "말로 지시하는 AI"가 아니라 "같이 문서를 고치는 AI"입니다.
</div>

<hr class="cn-divider"/>

<!-- ===== Word ===== -->
<div class="cn-section-h green">📝 Agent Mode in Word — 문서를 다시 쓰지 말고, 함께 다듬으세요</div>

<p>Word의 Agent Mode는 기존 문서를 유지한 채, 요약·수정·보완·형식 변경을 한 번에 처리하는 데 최적화되어 있습니다.</p>

<div class="cn-sub-h">이런 순간에 특히 유용해요</div>
<div class="cn-grid-3">
  <div class="cn-card cyan">매달 반복되는 정기 보고서 업데이트</div>
  <div class="cn-card blue">여러 메일·회의 내용을 반영해야 하는 임원 보고 문서</div>
  <div class="cn-card violet">톤&amp;매너를 맞춰야 하는 공식 문서</div>
</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">📌 실전 활용 예시</div>
  <div class="cn-prompt-text">"이 문서를 이번 달 버전으로 업데이트해줘.<br/>
/9월 데이터 메일을 반영하고,<br/>
지난달 대비 달라진 포인트를 요약해줘."</div>
</div>

<div class="cn-sub-h">Copilot은 이렇게 처리합니다</div>
<ul class="cn-checklist">
  <li>기존 표와 문단을 그대로 유지</li>
  <li>최신 정보만 교체</li>
  <li>변경 포인트를 한눈에 보이게 정리</li>
</ul>

<div class="cn-grid-3" style="margin-top: 0.6rem;">
  <div class="cn-card green"><div class="cn-card-title">✅</div><div class="cn-card-body">문서를 새로 만들 필요 없이</div></div>
  <div class="cn-card green"><div class="cn-card-title">✅</div><div class="cn-card-body">검토 가능한 상태로</div></div>
  <div class="cn-card green"><div class="cn-card-title">✅</div><div class="cn-card-body">사람이 한 것처럼 자연스럽게</div></div>
</div>

<hr class="cn-divider"/>

<!-- ===== Excel ===== -->
<div class="cn-section-h cyan">📊 Agent Mode in Excel — 엑셀 수식 말고, 목적부터 말하세요</div>

<p>Excel의 Agent Mode는 데이터 분석가처럼 생각하고, 컨설턴트처럼 결과를 만듭니다.</p>

<div class="cn-sub-h">이렇게 달라집니다</div>
<div class="cn-grid-2">
  <div class="cn-card red">
    <div class="cn-card-title">이렇게 말하면 아쉬워요 ❌</div>
    <div class="cn-card-body">"피벗 만들어줘"</div>
  </div>
  <div class="cn-card green">
    <div class="cn-card-title">이렇게 말해보세요 ⭕</div>
    <div class="cn-card-body">"이 데이터를 기반으로 의사결정용 리포트 만들어줘"</div>
  </div>
</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">📌 실전 활용 예시</div>
  <div class="cn-prompt-text">"이 매출 데이터를 기반으로<br/>
월별 성장률과 전년 대비 증감을 분석하고,<br/>
경영진용 차트와 요약 탭을 만들어줘."</div>
</div>

<div class="cn-sub-h">Agent Mode는 이렇게 처리합니다</div>
<ul class="cn-checklist">
  <li>데이터 정리</li>
  <li>계산식 생성</li>
  <li>차트, 피벗, 요약 시트까지 한 흐름으로 자동 구성</li>
</ul>

<div class="cn-tip teal">💡 엑셀을 '계산 도구'가 아니라 <strong>'결정 도구'</strong>로 바꿔주는 기능입니다.</div>

<hr class="cn-divider"/>

<!-- ===== PowerPoint ===== -->
<div class="cn-section-h violet">📽 Agent Mode in PowerPoint (Preview) — 슬라이드 작업, 이제 스토리부터 시작하세요</div>

<p>PowerPoint의 Agent Mode는 슬라이드 디자인 이전에 <strong>'논리와 메시지'</strong>를 먼저 잡아줍니다.</p>

<div class="cn-prompt">
  <div class="cn-prompt-label">📌 실전 활용 예시</div>
  <div class="cn-prompt-text">"최근 5년간 반도체 산업 변화를 분석해서<br/>
경영진 보고용 전략 슬라이드를 만들어줘.<br/>
핵심 인사이트 중심으로."</div>
</div>

<div class="cn-sub-h">Copilot은 이렇게 처리합니다</div>
<ul class="cn-checklist">
  <li>슬라이드 구조 설계</li>
  <li>메시지 흐름 구성</li>
  <li>차트·비주얼 제안까지 컨설팅 스타일의 덱을 완성</li>
</ul>

<div class="cn-grid-3" style="margin-top: 0.6rem;">
  <div class="cn-card violet"><div class="cn-card-body">✅ 빈 슬라이드 앞에서 멈추는 시간 ↓</div></div>
  <div class="cn-card violet"><div class="cn-card-body">✅ "무엇을 말할지" 고민하는 시간 ↓</div></div>
  <div class="cn-card violet"><div class="cn-card-body">✅ 전달력 ↑</div></div>
</div>

<hr class="cn-divider"/>

<!-- ===== 핵심 요약 ===== -->
<div class="cn-section-h orange">🔍 Agent Mode, 이렇게 기억하세요</div>

<div class="cn-grid-3">
  <div class="cn-card blue"><div class="cn-card-body">✅ 앱 안에서 바로 일하는 Copilot</div></div>
  <div class="cn-card cyan"><div class="cn-card-body">✅ 여러 단계를 스스로 이어가는 Agentic Collaboration</div></div>
  <div class="cn-card orange"><div class="cn-card-body">✅ 문서·데이터·슬라이드를 사람처럼 다루는 AI</div></div>
</div>

<div class="cn-tip dark">
  🧭 Agent Mode는 "AI가 일을 대신해주는 기능"이 아니라 <strong>"AI와 함께 일하는 방식의 변화"</strong>입니다.
</div>

<hr class="cn-divider"/>

<!-- ===== 실전 프롬프트 ===== -->
<div class="cn-section-h indigo">🙋 여러분도 체험해보세요: Agent Mode 실전 프롬프트 9선</div>

<!-- Word 프롬프트 -->
<div class="cn-sub-h" style="color: #166534; margin-top: 1.2rem;">📝 Word | 문서를 함께 고쳐보세요</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 1. 월간 보고서 업데이트</div>
  <div class="cn-prompt-text">"이 문서를 이번 달 버전으로 업데이트해줘.<br/>
지난달 대비 변경된 핵심 수치와 메시지를 요약해서<br/>
상단에 '이번 달 하이라이트' 섹션을 추가해줘."</div>
  <div class="cn-prompt-tip">👉 정기 보고서, 주간/월간 리포트에 바로 사용</div>
</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 2. 임원용 문서로 톤 조정</div>
  <div class="cn-prompt-text">"이 문서를 임원 보고용으로 다듬어줘.<br/>
문장은 더 간결하게, 핵심 결론은 굵게 표시하고<br/>
마지막에 다음 액션 아이템을 정리해줘."</div>
  <div class="cn-prompt-tip">👉 내용은 유지하고 전달력만 강화</div>
</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 3. 브랜드/용어 정리</div>
  <div class="cn-prompt-text">"문서 전체에서 표현을 통일해줘.<br/>
'AI assistant'는 모두 'Copilot'으로 변경하고,<br/>
제목은 Title Case로 맞춰줘."</div>
  <div class="cn-prompt-tip">👉 전사 표준 문서 정리에 효과적</div>
</div>

<!-- Excel 프롬프트 -->
<div class="cn-sub-h" style="color: #0e7490; margin-top: 1.4rem;">📊 Excel | 엑셀에게 분석을 맡겨보세요</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 4. 경영진용 요약 대시보드</div>
  <div class="cn-prompt-text">"이 데이터를 분석해서<br/>
월별 추이, 전년 대비 증감, 주요 인사이트를 정리해줘.<br/>
차트와 요약 탭을 포함한 경영진용 리포트를 만들어줘."</div>
  <div class="cn-prompt-tip">👉 숫자 → 스토리 → 의사결정까지 한 번에</div>
</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 5. 데이터에서 이상 징후 찾기</div>
  <div class="cn-prompt-text">"이 데이터에서 눈에 띄는 이상치나<br/>
급격한 변화 구간이 있는지 분석해줘.<br/>
원인 가설도 함께 정리해줘."</div>
  <div class="cn-prompt-tip">👉 운영/매출/사용량 데이터 분석에 추천</div>
</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 6. 실무용 자동 리포트</div>
  <div class="cn-prompt-text">"이 데이터를 기준으로<br/>
매달 반복해서 사용할 수 있는 분석 구조를 만들어줘.<br/>
피벗, 차트, 요약 영역을 포함해줘."</div>
  <div class="cn-prompt-tip">👉 '한 번 만들어두고 계속 쓰는' 엑셀</div>
</div>

<!-- PowerPoint 프롬프트 -->
<div class="cn-sub-h" style="color: #6d28d9; margin-top: 1.4rem;">📽 PowerPoint | 슬라이드의 스토리를 맡겨보세요</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 7. 보고용 슬라이드 자동 구성</div>
  <div class="cn-prompt-text">"이 내용을 기반으로<br/>
경영진 보고용 8장 내외의 슬라이드를 만들어줘.<br/>
핵심 메시지가 한눈에 보이게 구성해줘."</div>
  <div class="cn-prompt-tip">👉 빈 슬라이드 공포증 해결</div>
</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 8. 분석 → 인사이트 중심 정리</div>
  <div class="cn-prompt-text">"이 주제를 단순 설명이 아니라<br/>
'왜 중요한지', '무엇을 결정해야 하는지' 중심으로<br/>
스토리라인을 구성해줘."</div>
  <div class="cn-prompt-tip">👉 전략/기획 발표에 특히 효과적</div>
</div>

<div class="cn-prompt">
  <div class="cn-prompt-label">✅ 프롬프트 9. 초안 → 설득형 발표자료</div>
  <div class="cn-prompt-text">"현재 슬라이드를 더 설득력 있게 개선해줘.<br/>
메시지는 줄이고, 인사이트와 시각 자료 중심으로 재구성해줘."</div>
  <div class="cn-prompt-tip">👉 이미 있는 덱을 '잘 만든 덱'으로</div>
</div>

<hr class="cn-divider"/>

<!-- ===== 마무리 CTA ===== -->
<div class="cn-cta">
  <div class="cn-cta-title">✨ 이렇게 활용해보세요</div>
  <div class="cn-cta-items">
    ✅ 길게 설명하지 말고 <strong>'목적'</strong>을 말하기<br/>
    ✅ "만들어줘"보다 <strong>"어떻게 쓰일지"</strong>를 함께 말하기<br/>
    ✅ 한 번에 완벽을 기대하지 말고, <strong>이어서 대화하기</strong>
  </div>
  <div class="cn-cta-note">💬 Agent Mode는 한 번 지시하고 끝나는 AI가 아니라, 계속 같이 일하면서 다듬는 AI입니다.</div>
</div>

</div>
