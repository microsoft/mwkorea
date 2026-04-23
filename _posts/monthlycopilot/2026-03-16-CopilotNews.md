---
title: "코파일럿 뉴우쓰: Copilot으로 편집, 이제 AI가 문서 안에서 같이 일합니다"
date: 2026-03-16T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - AI
  - 코파일럿으로 편집
  - Microsoft 365 Copilot
excerpt: "Word, Excel, PowerPoint에서 Copilot이 직접 편집하고 이어서 일하는 '코파일럿으로 편집'을 정리했습니다. Chat 기반 Agents와의 차이, 대표 활용 장면, 바로 써볼 수 있는 실전 프롬프트 9개까지 담았습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 고현
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · Copilot News · '코파일럿으로 편집' · New Feature</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Copilot New Feature</div>
  <div class="mc-cover-title">이제 Copilot은 ‘도구’가 아니라 ‘동료’입니다. <br/>From AI Assistant to AI Doer</div>
  <div class="mc-cover-subtitle">'코파일럿으로 편집'으로 바뀌는 일하는 방식을 소개합니다.</div>
</div>


<div style="margin: 0 0 1.3rem; padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%); border: 1px solid #bfdbfe; color: #1f2937;">
  <div style="font-weight: 800; color: #1d4ed8; margin-bottom: 0.35rem;">🤖 Copilot New Feature</div>
  <div style="line-height: 1.8;">이번 달 월간 코파일럿에서는 Microsoft 365 Copilot의 새로운 진화, "Copilot으로 편집" 기능을 소개합니다. 이제 Copilot은 단순히 “물어보면 답해주는 AI”를 넘어, 문서·데이터·슬라이드 안에서 함께 일하는 협업 파트너로 진화하고 있습니다.<br/>
  ⚠️ "Copilot으로 편집" 기능은 Microsoft 365 Copilot 라이선스가 있는 사용자에게 제공됩니다.</div>
</div>



<div style="margin: 0 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #1d4ed8;">이 글에서 바로 보는 포인트</div>
  <div style="line-height: 1.8; color: #374151;">Word, Excel, PowerPoint 안에서 Copilot이 실제 결과물을 함께 편집하는 방식이 무엇인지 설명하고, Copilot Chat 기반 Agents와의 차이를 표로 정리했습니다. 뒤쪽에는 바로 써볼 수 있는 실전 프롬프트 9개를 이어서 담았습니다.</div>
</div>


<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">✨ '코파일럿으로 편집'이란 무엇인가요?</h2>

<div style="margin: 0.85rem 0 1rem; padding: 0.95rem 1.05rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  👉 실제 문서(Canvas) 위에서<br/>
  👉 여러 단계를 스스로 계획하고 실행하며<br/>
  👉 사람과 협업하듯 작업을 이어가는<br/>
  새로운 작업 방식입니다.
</div>

<div style="overflow-x: auto; margin: 1rem 0 1.5rem;">
  <table style="width: 100%; min-width: 760px; border-collapse: collapse; border-radius: 16px; overflow: hidden;">
    <thead>
      <tr style="background: #111827; color: #f9fafb;">
        <th style="padding: 0.85rem; text-align: left; border: 1px solid #1f2937;">구분</th>
        <th style="padding: 0.85rem; text-align: left; border: 1px solid #1f2937;">코파일럿으로 편집</th>
        <th style="padding: 0.85rem; text-align: left; border: 1px solid #1f2937;">Agents(Copilot Chat기반)</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background: #f8fafc;">
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;"><strong>작업 위치</strong></td>
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;">Word/Excel/PowerPoint 앱(데스크톱/웹) 안에서 사용</td>
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;">Microsoft 365 Copilot Chat(데스크톱/웹/모바일)에서 사용</td>
      </tr>
      <tr style="background: #ffffff;">
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;"><strong>작업 방식</strong></td>
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;">Copilot이 문서/시트/슬라이드 화면에서 직접 편집하며 함께 완성</td>
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;">Copilot이 결과물을 먼저 생성 → 채팅으로 수정·보완하거나 앱에서 열어 편집</td>
      </tr>
      <tr style="background: #f8fafc;">
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;"><strong>강점</strong></td>
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;">계획–실행–반복을 빠르게 돌리는 실시간 협업(에이전틱 작업), 구조·브랜딩 유지, 변경 이력 확인</td>
        <td style="padding: 0.85rem; border: 1px solid #d1d5db;">대화형 프롬프트로 아이디어를 빠르게 완성도 높은 결과물로 변환</td>
      </tr>
    </tbody>
  </table>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
  <strong>💡 핵심 한 줄 요약</strong><br/>
  '코파일럿으로 편집'은 “말로 지시하는 AI”가 아니라 “같이 문서를 고치는 AI”입니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #0f766e; background: #f8fafc;">📝 '코파일럿으로 편집' in Word — 문서를 다시 쓰지 말고, 함께 다듬으세요</h2>

<p>Word의 '코파일럿으로 편집'은 기존 문서를 유지한 채, 요약·수정·보완·형식 변경을 한 번에 처리하는 데 최적화되어 있습니다.</p>

<div style="margin: 0 0 0.85rem; font-weight: 800; color: #1f2937;">이런 순간에 특히 유용해요</div>

<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59;">매달 반복되는 정기 보고서 업데이트</div>
  <div style="padding: 1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">여러 메일·회의 내용을 반영해야 하는 임원 보고 문서</div>
  <div style="padding: 1rem; border-radius: 14px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6;">톤&매너를 맞춰야 하는 공식 문서</div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem;">📌 실전 활용 예시</div>
  <div style="line-height: 1.85;">“이 문서를 이번 달 버전으로 업데이트해줘.<br/>'9월 데이터 메일'을 반영하고,<br/>지난달 대비 달라진 포인트를 요약해줘.”</div>
  <div style="margin-top: 0.7rem; font-weight: 800; color: #334155;">Copilot은:</div>
  <ul style="margin: 0.8rem 0 0; padding-left: 1.2rem;">
    <li>기존 표와 문단을 그대로 유지</li>
    <li>최신 정보만 교체</li>
    <li>변경 포인트를 한눈에 보이게 정리합니다.</li>
  </ul>
  <div style="margin-top: 0.7rem; color: #334155;">✅ 문서를 새로 만들 필요 없이 · ✅ 검토 가능한 상태로 · ✅ 사람이 한 것처럼 자연스럽게</div>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #0891b2; background: #f8fafc;">📊 '코파일럿으로 편집' in Excel — 엑셀 수식 말고, 목적부터 말하세요</h2>

<p>Excel의 '코파일럿으로 편집'은 데이터 분석가처럼 생각하고, 컨설턴트처럼 결과를 만듭니다.</p>

<div style="margin: 0 0 0.85rem; font-weight: 800; color: #1f2937;">이렇게 달라집니다</div>

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #fef2f2; border: 1px solid #fecaca; color: #991b1b;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">이렇게 말하면 아쉬워요</div>
    <div>“피벗 만들어줘” ❌</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">이렇게 말해보세요</div>
    <div>“이 데이터를 기반으로 의사결정용 리포트 만들어줘” ⭕</div>
  </div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem;">📌 실전 활용 예시</div>
  <div style="line-height: 1.85;">“이 매출 데이터를 기반으로<br/>월별 성장률과 전년 대비 증감을 분석하고,<br/>경영진용 차트와 요약 탭을 만들어줘.”</div>
  <div style="margin-top: 0.7rem; font-weight: 800; color: #334155;">'코파일럿으로 편집'은:</div>
  <ul style="margin: 0.8rem 0 0; padding-left: 1.2rem;">
    <li>데이터 정리</li>
    <li>계산식 생성</li>
    <li>차트, 피벗, 요약 시트까지 한 흐름으로 자동 구성합니다.</li>
  </ul>
  <div style="margin-top: 0.7rem; color: #0f766e; font-weight: 700;">💡 엑셀을 ‘계산 도구’가 아니라 ‘결정 도구’로 바꿔주는 기능입니다.</div>
  <div style="margin-top: 0.5rem; color: #475569;">원문 포함 자료: AgentMode_Excel.mp4</div>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #7c3aed; background: #f8fafc;">📽 '코파일럿으로 편집' in PowerPoint (Preview) — 슬라이드 작업, 이제 스토리부터 시작하세요</h2>

<p>PowerPoint의 '코파일럿으로 편집'은 슬라이드 디자인 이전에 ‘논리와 메시지’를 먼저 잡아줍니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem;">📌 실전 활용 예시</div>
  <div style="line-height: 1.85;">“최근 5년간 반도체 산업 변화를 분석해서<br/>경영진 보고용 전략 슬라이드를 만들어줘.<br/>핵심 인사이트 중심으로.”</div>
  <div style="margin-top: 0.7rem; font-weight: 800; color: #334155;">'코파일럿으로 편집'은:</div>
  <ul style="margin: 0.8rem 0 0; padding-left: 1.2rem;">
    <li>슬라이드 구조 설계</li>
    <li>메시지 흐름 구성</li>
    <li>차트·비주얼 제안까지 컨설팅 스타일의 덱을 완성합니다.</li>
  </ul>
  <div style="margin-top: 0.7rem; color: #334155;">✅ 빈 슬라이드 앞에서 멈추는 시간 ↓ · ✅ “무엇을 말할지” 고민하는 시간 ↓ · ✅ 전달력 ↑</div>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #ea580c; background: #f8fafc;">🔍 '코파일럿으로 편집', 이렇게 기억하세요</h2>

<div style="display: grid; grid-template-columns: 1fr; gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">✅ 앱 안에서 바로 일하는 '코파일럿으로 편집'</div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59;">✅ 여러 단계를 스스로 이어가는 Agentic Collaboration</div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fff7ed; border: 1px solid #fdba74; color: #c2410c;">✅ 문서·데이터·슬라이드를 사람처럼 다루는 AI</div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #111827; color: #f9fafb;">
  🧭 '코파일럿으로 편집'은 “AI가 일을 대신해주는 기능”이 아니라 “AI와 함께 일하는 방식의 변화”입니다.
</div>

<div style="margin: 0 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eef2ff; border: 1px solid #c7d2fe; color: #3730a3;">
  <strong>한 줄 해석</strong><br/>
  '코파일럿으로 편집'의 핵심은 더 똑똑한 답변이 아니라, 앱 안에서 사람과 같은 흐름으로 같이 수정하고 완성해 간다는 점입니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">🙋‍♀️ 여러분도 체험해보세요: '코파일럿으로 편집' 실전 프롬프트 모음</h2>

<h3 style="margin-top: 1rem; color: #1d4ed8;">📝 Word | 문서를 함께 고쳐보세요</h3>


<div style="margin: 1rem 0 1.1rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 1. 월간 보고서 업데이트</div>
  <div style="line-height: 1.85;">“이 문서를 이번 달 버전으로 업데이트해줘.<br/>지난달 대비 변경된 핵심 수치와 메시지를 요약해서<br/>상단에 ‘이번 달 하이라이트’ 섹션을 추가해줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 정기 보고서, 주간/월간 리포트에 바로 사용</div>
</div>

<div style="margin: 1rem 0 1.1rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 2. 임원용 문서로 톤 조정</div>
  <div style="line-height: 1.85;">“이 문서를 임원 보고용으로 다듬어줘.<br/>문장은 더 간결하게, 핵심 결론은 굵게 표시하고<br/>마지막에 다음 액션 아이템을 정리해줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 내용은 유지하고 전달력만 강화</div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 3. 브랜드/용어 정리</div>
  <div style="line-height: 1.85;">“문서 전체에서 표현을 통일해줘.<br/>‘AI assistant’는 모두 ‘Copilot’으로 변경하고,<br/>제목은 Title Case로 맞춰줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 전사 표준 문서 정리에 효과적</div>
</div>

<h3 style="margin-top: 1rem; color: #0891b2;">📊 Excel | 엑셀에게 분석을 맡겨보세요</h3>


<div style="margin: 1rem 0 1.1rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 4. 경영진용 요약 대시보드</div>
  <div style="line-height: 1.85;">“이 데이터를 분석해서<br/>월별 추이, 전년 대비 증감, 주요 인사이트를 정리해줘.<br/>차트와 요약 탭을 포함한 경영진용 리포트를 만들어줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 숫자 → 스토리 → 의사결정까지 한 번에</div>
</div>

<div style="margin: 1rem 0 1.1rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 5. 데이터에서 이상 징후 찾기</div>
  <div style="line-height: 1.85;">“이 데이터에서 눈에 띄는 이상치나<br/>급격한 변화 구간이 있는지 분석해줘.<br/>원인 가설도 함께 정리해줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 운영/매출/사용량 데이터 분석에 추천</div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 6. 실무용 자동 리포트</div>
  <div style="line-height: 1.85;">“이 데이터를 기준으로<br/>매달 반복해서 사용할 수 있는 분석 구조를 만들어줘.<br/>피벗, 차트, 요약 영역을 포함해줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 ‘한 번 만들어두고 계속 쓰는’ 엑셀</div>
</div>

<h3 style="margin-top: 1rem; color: #7c3aed;">📽 PowerPoint | 슬라이드의 스토리를 맡겨보세요</h3>


<div style="margin: 1rem 0 1.1rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 7. 보고용 슬라이드 자동 구성</div>
  <div style="line-height: 1.85;">“이 내용을 기반으로<br/>경영진 보고용 8장 내외의 슬라이드를 만들어줘.<br/>핵심 메시지가 한눈에 보이게 구성해줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 빈 슬라이드 공포증 해결</div>
</div>

<div style="margin: 1rem 0 1.1rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 8. 분석 → 인사이트 중심 정리</div>
  <div style="line-height: 1.85;">“이 주제를 단순 설명이 아니라<br/>‘왜 중요한지’, ‘무엇을 결정해야 하는지’ 중심으로<br/>스토리라인을 구성해줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 전략/기획 발표에 특히 효과적</div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 14px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.4rem;">✅ 프롬프트 9. 초안 → 설득형 발표자료</div>
  <div style="line-height: 1.85;">“현재 슬라이드를 더 설득력 있게 개선해줘.<br/>메시지는 줄이고, 인사이트와 시각 자료 중심으로 재구성해줘.”</div>
  <div style="margin-top: 0.65rem; color: #475569;">👉 이미 있는 덱을 ‘잘 만든 덱’으로</div>
</div>

<hr/>

<div style="margin: 1rem 0 0; padding: 1.15rem 1.2rem; border-radius: 18px; background: linear-gradient(135deg, #111827 0%, #1f2937 100%); color: #f9fafb;">
  <div style="font-size: 0.85rem; font-weight: 900; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.45rem;">✨ 이렇게 활용해보세요</div>
  <div style="line-height: 1.85;">✅ 길게 설명하지 말고 ‘목적’을 말하기<br/>✅ “만들어줘”보다 “어떻게 쓰일지”를 함께 말하기<br/>✅ 한 번에 완벽을 기대하지 말고, 이어서 대화하기</div>
  <div style="margin-top: 0.75rem; color: #cbd5e1;">💬 코파일럿은 한 번 지시하고 끝나는 AI가 아니라, 계속 같이 일하면서 다듬는 AI입니다.</div>
</div>

</div>