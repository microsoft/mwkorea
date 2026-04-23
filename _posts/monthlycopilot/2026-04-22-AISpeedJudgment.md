---
title: "AI는 속도를, 사람은 판단을 통해 완성도를 만든다"
date: 2026-04-22T00:00:00 KST
excerpt: "AI 보안 어시스턴트의 권고대로 AD CS 서버를 강화했지만, 다음 날 아침 SSO 장애가 발생했습니다. AI의 권고는 틀리지 않았지만 조직의 맥락까지는 이해하지 못한 일반적인 정답이었을 뿐. AI는 속도를, 사람은 판단을 — IT 운영 현장에서 벌어진 실제 사건이 보여주는 AI와 인간 협업의 본질을 다룹니다."
tags:
  - AI
  - IT 운영
  - 보안
  - Human-in-the-loop
categories:
  - monthlycopilot
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
classes: wide
toc: false
toc_sticky: true
author: 김은숙
---

<div class="monthlycopilot-page monthlycopilot-page--tour">
<div class="mc-issue-strip">Monthly Copilot · May 2026 · 월간 코파일럿 5월호 · Case Study</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Case Study</div>
  <div class="mc-cover-title">AI는 속도를, 사람은 판단을 통해 완성도를 만든다</div>
  <div class="mc-cover-subtitle">IT 운영 현장에서 벌어진 한 사건이 보여준 AI보다 '사람'의 가치</div>
</div>

<div style="margin: 0 0 1.3rem; padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #ecfeff 0%, #f8fafc 100%); border: 1px solid #99f6e4; color: #1f2937;">
  <div style="font-weight: 800; color: #0f766e; margin-bottom: 0.35rem;">Article Summary</div>
  <div style="line-height: 1.85;">어느 기업의 IT 운영팀은 AI가 요약한 보안 강화 권고안을 바탕으로 AD CS 서버에 보안 패치를 적용했습니다. AI의 권고는 틀리지 않았지만, 조직의 맥락까지 이해하지 못한 '일반적인 정답'이었을 뿐이었습니다. 그날 벌어진 일이 보여주는, AI와 인간 협업의 본질.</div>
</div>

<img src="/mwkorea/assets/images/20260416-ai-speed-judgment/image1.jpeg" alt="AI와 인간의 협업" style="border-radius: 12px; margin-bottom: 1.4rem;" />

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #0f766e; background: #f8fafc;">들어가며</h2>

<p>어느 기업의 IT 운영팀은 평소와 다름없는 하루를 시작하고 있었습니다. 그러나 그날 아침, 재택근무용 VDI 환경(Citrix 기반) 로그인 화면에서 갑작스러운 인증 오류가 발생했다는 VoC가 연이어 접수되기 시작했습니다.</p>

<p>해당 시스템은 사용자 편의성을 위해 인증서 기반 SSO(Single Sign-On) 방식으로 설계되어 있었지만, 어느 순간부터 인증이 완료되지 않고 로그온 창이 반복적으로 나타나는 현상이 발생한 것입니다.</p>

<p>다행히도 ID와 암호를 다시 입력하면 로그온은 가능했습니다. 그래서 초기에는 "일시적인 오류일 수 있다"는 판단이 우세했고, 즉각적인 대형 장애로 인식되지는 않았습니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fef2f2; border: 1px solid #fecaca; color: #991b1b; font-weight: 700; line-height: 1.85;">
  하지만 오후가 되자 상황은 달라졌습니다. VDI 운영 부서로부터 <strong>"SSO 처리가 되지 않는다"</strong>는 정식 장애 보고가 접수되었고, 운영팀은 AD 및 AD CS 서버 변경 이력 확인을 요청받게 됩니다.
</div>

<p>전날 밤 진행되었던 AD CS 서버 보안 강화 작업이 떠올랐지만, 운영팀의 첫 반응은 부정이었습니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a; font-weight: 700; line-height: 1.85;">
  "아니야, 그 작업 때문은 아닐 거야." — 인증서는 여전히 정상적으로 발급되고 있었고, 해외 법인 사용자들 또한 HTTPS 기반 웹 접근에서 문제를 겪고 있지 않았기 때문입니다.
</div>

<p>그러나 이 판단은 곧 뒤집히게 됩니다.</p>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">🔍 1. 사건의 발단 – AI가 요약해준 '보안 강화' 가이드</h2>

<p>며칠 전, 정보보호팀은 AD CS 서버를 대상으로 모의 침투 테스트를 수행했습니다. 그 결과, ESC1 계열 취약점을 통해 일반 사용자 계정이 도메인 관리자 수준 권한을 획득할 수 있는 가능성이 확인되었습니다.</p>

<p>즉, <strong>인증서 인프라 전체가 조직의 핵심 보안 약점이 될 수 있는 상황</strong>이었습니다.</p>

<p>경영진은 즉각적인 조치를 지시했고, 시간 압박 속에서 운영팀은 벤더의 공식 문서와 AI 기반 보안 어시스턴트가 요약한 권고안을 바탕으로 보안 강화를 결정합니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #1d4ed8;">🤖 AI가 제시한 보안 강화 권고 (요약)</div>
  <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
    <tr style="background: #eff6ff;">
      <th style="padding: 0.6rem; border: 1px solid #bfdbfe; text-align: left;">구분</th>
      <th style="padding: 0.6rem; border: 1px solid #bfdbfe; text-align: left;">권고 내용</th>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">인증서 웹 서비스</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">HTTP 비활성화, HTTPS만 허용</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">인증서 템플릿</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">SAN 필드 제한, 관리자 권한 요청 차단</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">인증 방식</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">NTLM 인증 차단 또는 감사 모드</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">인증 보호</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">EPA(Extended Protection for Authentication) 활성화</td>
    </tr>
  </table>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59; font-weight: 700; line-height: 1.85;">
  운영팀은 이 권고를 신뢰했고, 작업은 빠르게 완료되었습니다. "이제 ESC1 공격은 차단됐을 거야."
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #ea580c; background: #f8fafc;">⚠️ 2. 위기의 전개 – 장애는 조용히 시작됐다</h2>

<p>겉보기에는 모든 것이 정상처럼 보였습니다. 인증서 발급도 문제없었고, 초기 점검에서도 이상 징후는 발견되지 않았습니다.</p>

<p>그러나 다음 날 아침부터 Citrix VDI의 SSO 기능이 작동하지 않기 시작했습니다. 직원들은 매번 ID와 암호를 수동으로 입력해야 했고, 작은 불편은 점차 업무 지연으로 이어졌습니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #ea580c;">🧩 장애 원인 정리</div>
  <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
    <tr style="background: #fff7ed;">
      <th style="padding: 0.6rem; border: 1px solid #fdba74; text-align: left;">변경 사항</th>
      <th style="padding: 0.6rem; border: 1px solid #fdba74; text-align: left;">영향</th>
      <th style="padding: 0.6rem; border: 1px solid #fdba74; text-align: left;">결과</th>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">HTTP 차단</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">CRL 접근 불가</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">인증서 유효성 검증 실패</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">NTLM 차단</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">Citrix 인증 흐름 일부 중단</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">SSO 실패</td>
    </tr>
  </table>
</div>

<p>핵심 원인은 두 가지였습니다.</p>

<div style="display: grid; grid-template-columns: 1fr; gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fef2f2; border: 1px solid #fecaca; color: #991b1b;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">원인 1: HTTP 차단 → CRL 접근 불가</div>
    <div>인증서는 발급되었지만, 이미 발급된 인증서가 참조하는 CRL 배포 지점은 여전히 HTTP 기반이었고, 클라이언트는 유효성 검증 단계에서 실패하게 되었습니다.</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fef2f2; border: 1px solid #fecaca; color: #991b1b;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">원인 2: NTLM 차단 → Citrix SSO 충돌</div>
    <div>일부 인증 구간에서 NTLM에 의존하고 있던 구조를 충분히 고려하지 못한 결과였습니다.</div>
  </div>
</div>

<p>운영팀은 일부 설정을 롤백했고, SSO는 정상화되었습니다.</p>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #7c3aed; background: #f8fafc;">🧠 3. AI는 빠르지만, 판단은 사람의 몫이다</h2>

<p>정확한 기술적 Fact로 접근하여 작업을 진행한 운영팀은 스스로에게 질문했습니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6; font-weight: 700; line-height: 1.85;">
  "우리는 무엇을 놓쳤을까? 벤더의 권장 사항이 맞는 것으로 AI가 활용한 출처 정보까지 확인을 했는데 무엇이 문제였을까?"
</div>

<p>AI의 권고와 벤더의 권장사항은 <strong>틀리지 않았습니다</strong>. 그러나 그것은 일반적인 정답이었을 뿐, <strong>지금과 같은 상황에 맞는 해답은 아니었습니다</strong>.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #7c3aed;">👤 AI와 인간 전문가의 역할 차이</div>
  <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
    <tr style="background: #f5f3ff;">
      <th style="padding: 0.6rem; border: 1px solid #c4b5fd; text-align: left;">구분</th>
      <th style="padding: 0.6rem; border: 1px solid #c4b5fd; text-align: left;">AI</th>
      <th style="padding: 0.6rem; border: 1px solid #c4b5fd; text-align: left;">인간</th>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">강점</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">속도, 방대한 문서 요약</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">맥락 이해, 영향 예측</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">한계</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">환경 특수성 반영 어려움</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">속도</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">책임</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">없음</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">최종 판단과 책임</td>
    </tr>
  </table>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fefce8; border: 1px solid #fde68a; color: #854d0e; font-weight: 700; line-height: 1.85;">
  🔑 AI는 "무엇을 해야 하는지"는 알려주었지만, "그로 인해 무엇이 깨질 수 있는지"까지는 알려주지 못했습니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #dc2626; background: #f8fafc;">🚨 4. 만약 AI가 틀렸거나, 직접 실행했다면?</h2>

<p>이번 사례는 AI가 맞는 말을 했고, 사람이 적용했기 때문에 비교적 가벼운 장애로 끝났습니다. 그러나 만약 AI가 환각으로 잘못된 정보를 확신에 차서 제시했거나, 더 나아가 시스템에 쓰기 권한을 가진 상태였다면 결과는 달라졌을 것입니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #dc2626;">⚖️ 위험 시나리오 비교</div>
  <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
    <tr style="background: #fef2f2;">
      <th style="padding: 0.6rem; border: 1px solid #fecaca; text-align: left;">구분</th>
      <th style="padding: 0.6rem; border: 1px solid #fecaca; text-align: left;">이번 사례</th>
      <th style="padding: 0.6rem; border: 1px solid #fecaca; text-align: left;">환각 발생</th>
      <th style="padding: 0.6rem; border: 1px solid #fecaca; text-align: left;">쓰기 권한 보유</th>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">정보 정확성</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">정확</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">부정확</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">부정확</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">사람 개입</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">있음</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">약함</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">없음</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">장애 범위</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">제한적</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">예측 불가</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">전면적</td>
    </tr>
    <tr>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">복구 난이도</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">낮음</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">중~높음</td>
      <td style="padding: 0.6rem; border: 1px solid #e5e7eb;">매우 높음</td>
    </tr>
  </table>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #059669; background: #f8fafc;">🌱 5. 에필로그 – 공존의 기술</h2>

<p>이 사건 이후, 해당 기업은 다음 원칙을 수립했습니다.</p>

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">원칙 1</div>
    <div>AI 권고는 참고 자료로 활용</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">원칙 2</div>
    <div>공식 문서와 반드시 교차 검증</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">원칙 3</div>
    <div>운영계 적용 시 테스트 환경에서 사전 검증</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">원칙 4</div>
    <div>모든 변경에 승인 단계 포함</div>
  </div>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #1d4ed8; background: #f8fafc;">🎯 핵심 메시지 요약</h2>

<div style="display: grid; grid-template-columns: 1fr; gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">
    <div style="font-weight: 800;">AI는 빠르지만, 조직의 맥락까지는 이해하지 못한다</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fefce8; border: 1px solid #fde68a; color: #854d0e;">
    <div style="font-weight: 800;">"맞는 말"도 환경에 따라 장애가 될 수 있다</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fef2f2; border: 1px solid #fecaca; color: #991b1b;">
    <div style="font-weight: 800;">AI에 쓰기 권한이 부여될수록, 사람의 판단은 더 중요해진다</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800;">미래의 IT 운영은 AI + 인간 판단의 균형에 달려 있다</div>
  </div>
</div>

<hr/>

<div style="margin: 1rem 0 0; padding: 1.15rem 1.2rem; border-radius: 18px; background: linear-gradient(135deg, #111827 0%, #1f2937 100%); color: #f9fafb; line-height: 1.85;">
  <div style="font-weight: 800; margin-bottom: 0.5rem; font-size: 1.05rem;">AI와 인간의 협업은 선택이 아니라, 운영의 완성도를 결정하는 핵심 역량이 되고 있습니다</div>
  AI는 이제 IT 운영의 필수 도구입니다. 그러나 속도를 통제하고, 위험을 상상하며, 멈출 줄 아는 판단력은 여전히 사람의 몫입니다.
</div>

</div>

