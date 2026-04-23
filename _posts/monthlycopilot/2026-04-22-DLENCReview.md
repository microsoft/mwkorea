---
title: "도면이 바뀌면 누가 확인하나요? — DLENC의 AI 에이전트 이야기"
date: 2026-04-22T00:00:00 KST
excerpt: "비정형 문서 자동 추출, GA 도면 설계 변경 검증, 발주서 자동 생성까지 — DLENC가 AI Tour 에이전톤 로우코드 부문 1위를 차지하며 Copilot Studio로 현장의 반복 업무를 바꾼 세 가지 방법을 소개합니다. 별도 개발 조직 없이 현업이 직접 만든 Human-in-the-loop AI 에이전트의 실전 사례입니다."
tags:
  - Copilot Studio
  - AI Builder
  - 에이전톤
  - 건설·플랜트
  - AI Tour
categories:
  - Copilot
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
classes: wide
toc: false
toc_sticky: true
author: 김현지
---

<div class="monthlycopilot-page monthlycopilot-page--tour">
<div class="mc-issue-strip">Monthly Copilot · AI Tour Agenthon Recap · 에이전톤 1위 · 제조·플랜트 · Copilot Studio</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">AI Tour Agenthon Recap</div>
  <div class="mc-cover-title">도면이 바뀌면 누가 확인하나요?</div>
  <div class="mc-cover-subtitle">— 이 질문에서 AI 에이전트가 탄생했습니다</div>
</div>

<div style="margin: 0 0 1.3rem; padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #ecfeff 0%, #f8fafc 100%); border: 1px solid #99f6e4; color: #1f2937;">
  <div style="font-weight: 800; color: #0f766e; margin-bottom: 0.35rem;">Article Summary</div>
  <div style="line-height: 1.85;">비정형 문서 자동 추출, GA 도면 설계 변경 검증, 발주서 자동 생성까지 — DLENC가 Copilot Studio로 현장의 반복 업무를 바꾼 세 가지 방법. 2026 AI Tour 에이전톤 로우코드 부문 1위 사례 소개입니다.</div>
</div>

<div style="margin: 0 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="line-height: 1.85; color: #374151;">이 내용은 2026 AI Tour 라이트닝 토크 세션에서 직접 발표된 내용을 바탕으로 정리했습니다. 현장에서 미처 못 보신 분들을 위해, 핵심 내용을 다시 Recap으로 전달드립니다.</div>
</div>

<img src="/mwkorea/assets/images/20260416-dlenc-review/image1.jpeg" alt="DLENC 에이전톤 발표 현장" style="border-radius: 12px; margin-bottom: 1.4rem;" />

<p>건설·플랜트 프로젝트를 한 번이라도 들여다보신 분이라면 아실 거예요. 현장에서 만들어지는 문서의 양은 어마어마합니다. 지반 조사 보고서, 도면, 스펙 시트, 그리고 수십 개 벤더와 나눈 미팅 기록까지 — 그 모든 데이터들이 제대로 옮겨지고, 반영되고, 검증되어야 프로젝트가 진행됩니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a; font-weight: 700; line-height: 1.85;">
  문제는 그 "옮기고 검증하는" 일을 지금껏 사람이 직접 해왔다는 점입니다. DLENC는 AI Tour 에이전톤에서 바로 이 지점을 Copilot Studio 기반 AI 에이전트로 대체하며 1위에 올랐습니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #0f766e; background: #f8fafc;">01 사례 1 · 비정형 문서 자동화 — 시추주상도, 이제 AI가 읽고 엑셀에 채웁니다</h2>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827; font-size: 0.92rem;">
  <strong>⚙ Microsoft Copilot Studio + AI Builder 기반 로우코드 구현</strong>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59; font-size: 0.92rem;">
  <strong>용어 설명 | 시추주상도 (Boring Log)</strong> — 지반 조사 시 땅을 뚫어 얻은 흙·암석의 특성을 층별로 기록한 문서입니다. 토층의 종류, 깊이(심도), 지반의 강도(N값) 등이 기재되며 구조 설계의 기초 자료로 활용됩니다.
</div>

<p>지반 조사를 마치면 시추주상도(Boring Log)가 만들어집니다. 흙의 층위, 강도(N값), 깊이(심도) 같은 정밀 수치가 담긴 이 문서는 프로젝트 하나에 수십~수백 장씩 쌓입니다. 지금까지는 PDF나 스캔 이미지로 전달받아 담당자가 하나씩 열어보며 엑셀에 직접 입력하는 방식이었습니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6; font-weight: 700; line-height: 1.85;">
  "건당 평균 2~4시간이 걸립니다. 대형 프로젝트라면 수십 명이 똑같은 작업을 동시에 진행하게 됩니다. 숫자 하나가 잘못 입력되면 구조 계산 전체가 흔들릴 수 있습니다."
</div>

<p>DLENC 팀이 선택한 방향은 명쾌했습니다. <strong>데이터를 옮기는 일은 AI에게, 사람은 결과를 확인하는 일에만 집중하자.</strong> 이것을 Microsoft Copilot Studio와 AI Builder — 즉, 로우코드 플랫폼만으로 구현했습니다. 별도의 개발 조직도, 프로그래밍 언어도 필요하지 않았습니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #0f766e;">처리 흐름</div>
  <div style="line-height: 1.85;">PDF/이미지 업로드 → 자동 감지 & 실행 → 핵심 데이터 추출 → Excel 자동 입력 → <strong>담당자 최종 검토</strong></div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fefce8; border: 1px solid #fde68a; color: #854d0e; font-weight: 700; line-height: 1.85;">
  🔑 마지막 단계가 핵심입니다. 완전 자동화가 아니라 AI가 추출하고, 사람이 검토하는 구조로 설계했습니다. 기술의 완성도보다 현업에서의 신뢰를 먼저 고려한 선택입니다.
</div>

<img src="/mwkorea/assets/images/20260416-dlenc-review/image2.png" alt="시추주상도 자동 추출 프로세스" style="border-radius: 12px; margin-bottom: 1.4rem;" />

<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">입력 소요 시간</div>
    <div>건당 2~4시간 → <strong>수 초</strong></div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">대폭 단축</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">입력 오류</div>
    <div>오타·누락 빈번 → <strong>목표 0건</strong></div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">AI 추출로 원천 방지</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">담당자 역할</div>
    <div>직접 입력 → <strong>검토·판단</strong></div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">더 중요한 일에 집중</div>
  </div>
</div>

<p>시추주상도에서 멈추지 않습니다. 토질조사보고서, 지반조사 결과표 등 동일한 반복 입력 구조를 가진 문서라면 같은 에이전트 패턴을 그대로 적용할 수 있습니다.</p>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">02 사례 2 · 발주서(PO) 자동 생성 — "미팅 기록이 발주서가 됩니다"</h2>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827; font-size: 0.92rem;">
  <strong>⚙ Microsoft Copilot Studio + AI Builder 기반 로우코드 구현</strong>
</div>

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59; font-size: 0.92rem;">
    <strong>용어 | MoM (Minutes of Meeting)</strong> — 벤더·협력사와의 협의 내용을 정리한 공식 회의록. 계약 조건, 납기, 보증 등 핵심 합의 내용이 담기며, 발주서(PO) 작성의 기초 자료로 활용됩니다.
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59; font-size: 0.92rem;">
    <strong>용어 | PO (Purchase Order, 발주서)</strong> — 구매자가 공급자에게 물품·서비스를 공식 요청하는 계약 문서. Bond 조건, Payment 조건, 납기, Warranty, Liquidated Damages 등 핵심 계약 항목이 포함됩니다.
  </div>
</div>

<p>해외 건설 프로젝트에서는 수십~수백 개 벤더와 계약 협의를 동시에 진행합니다. 각 미팅 후에는 MoM 문서가 생성되고, 담당자는 이 문서를 읽어 Bond 조건, Payment 조건, 납기, Warranty 등 핵심 계약 항목을 직접 추출해 PO 양식에 입력해야 합니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6; font-weight: 700; line-height: 1.85;">
  "저는 이 발주 리드타임을 대폭 단축시키기 위해서 MoM 내용을 기반으로 PO를 자동 생성해 주는 에이전트를 개발했습니다." — 발표자 현장 발언 중
</div>

<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #fef2f2; border: 1px solid #fecaca; color: #991b1b;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">문제 1 · 비정형 데이터</div>
    <div>업체·프로젝트별로 MoM 양식이 달라 표준화된 추출이 불가능했습니다.</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #fef2f2; border: 1px solid #fecaca; color: #991b1b;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">문제 2 · 수작업 입력</div>
    <div>추출한 내용을 PO 양식에 수동으로 옮기는 과정에서 오탈자·누락이 빈번했습니다.</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #fef2f2; border: 1px solid #fecaca; color: #991b1b;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">문제 3 · 긴 소요 시간</div>
    <div>PO 초안 작성에 건당 평균 1~2시간이 소요됐습니다. 벤더가 많을수록 병목이 커졌습니다.</div>
  </div>
</div>

<h3>2-Stage AI 에이전트로 해결했습니다</h3>

<p>담당자가 해야 할 일은 단 두 가지로 줄었습니다. <strong>파일 업로드, 그리고 최종 검토·승인.</strong> 그 사이의 모든 과정은 에이전트가 처리합니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #2563eb;">처리 흐름</div>
  <div style="line-height: 1.85;">MoM PDF 업로드 (SharePoint) → Copilot Studio 에이전트 자동 실행 → AI 문서 분석 및 JSON 추출 → Word PO 문서 자동 생성 → <strong>담당자 검토·승인</strong></div>
</div>

<img src="/mwkorea/assets/images/20260416-dlenc-review/image3.png" alt="MoM에서 PO 자동 생성 프로세스" style="border-radius: 12px; margin-bottom: 1.4rem;" />

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">Stage 1 — MoM 문서 구조 파악</div>
    <div style="line-height: 1.85;">AI는 MoM 문서를 단순히 읽는 것이 아니라, 세 가지 관점에서 먼저 문맥을 파악합니다. <strong>"구조"</strong> — 문서가 어떤 형식인지, <strong>"형식"</strong> — 섹션·테이블·자유 텍스트 등 레이아웃, <strong>"내용"</strong> — 어떤 미팅이었는지. 이 선행 분석 덕분에 업체마다 완전히 다른 MoM 양식도 정확하게 처리할 수 있습니다.</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">Stage 2 — PO 양식 추출 및 Word 변환</div>
    <div style="line-height: 1.85;">Stage 1에서 파악한 문맥을 기반으로 Bond, Payment, Warranty, Liquidated Damages 등 핵심 조건을 JSON 포맷으로 구조화하여 추출합니다. 이후 PO 표준 양식(Word Placeholder 기반)에 자동 매핑하여 완성된 Word 문서(.docx)를 출력합니다.</div>
  </div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fefce8; border: 1px solid #fde68a; color: #854d0e; font-weight: 700; line-height: 1.85;">
  🔑 특히 주목할 만한 변화는 다수 벤더를 동시에 병렬 처리할 수 있게 된 것입니다. 기존에는 벤더 수가 늘어날수록 선형적으로 시간이 늘어났지만, 이제는 10개 벤더이든 50개 벤더이든 처리 시간이 크게 다르지 않습니다. 발주 병목이 구조적으로 해소된 셈입니다.
</div>

<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">PO 작성 시간</div>
    <div>건당 1~2시간 → <strong>수 분</strong></div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">80% 이상 단축</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">조건 누락·오탈자</div>
    <div>빈번 발생 → <strong>0건</strong></div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">AI 구조화 추출로 원천 방지</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">처리 방식</div>
    <div>순차 수작업 → <strong>병렬 동시</strong></div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">발주 리드타임 대폭 단축</div>
  </div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #2563eb;">사용 기술 스택</div>
  <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
    <tr style="background: #eff6ff;"><th style="padding: 0.6rem; border: 1px solid #bfdbfe; text-align: left;">구성 요소</th><th style="padding: 0.6rem; border: 1px solid #bfdbfe; text-align: left;">역할</th></tr>
    <tr><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">Microsoft Copilot Studio</td><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">에이전트 및 Agent Flow 구현</td></tr>
    <tr><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">AI Builder (프롬프트)</td><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">비정형 MoM 문서 분석 및 구조화 추출</td></tr>
    <tr><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">SharePoint</td><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">MoM 문서 업로드 및 관리</td></tr>
    <tr><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">Microsoft Word (Placeholder)</td><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">PO 양식 템플릿 및 필드 정의</td></tr>
    <tr><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">JSON → Word 변환 프로그램</td><td style="padding: 0.6rem; border: 1px solid #e5e7eb;">추출 JSON을 표준 Word 문서로 변환</td></tr>
  </table>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #7c3aed; background: #f8fafc;">03 사례 3 · 도면 설계 변경 자동화 — "도면이 바뀌면 누가 확인하나요?"</h2>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827; font-size: 0.92rem;">
  <strong>⚙ Microsoft Copilot Studio + AI Builder 기반 로우코드 구현</strong>
</div>

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59; font-size: 0.92rem;">
    <strong>용어 | GA 도면 (General Arrangement Drawing)</strong> — 설비나 장치의 전체 배치·치수·재질·연결 관계를 나타낸 종합 배치도. 벤더(제조사)가 납품 전 제공하며, 이 도면을 기반으로 3D 모델링과 시공이 진행됩니다.
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59; font-size: 0.92rem;">
    <strong>용어 | EPC 프로젝트</strong> — 설계(Engineering), 조달(Procurement), 시공(Construction)을 한 업체가 일괄 수행하는 방식의 대형 건설·플랜트 사업. 정유·화학·발전소 건설에 주로 활용됩니다.
  </div>
</div>

<p>플랜트·EPC 프로젝트에서 벤더가 제공하는 GA 도면에는 치수, 재질, 스펙 등 3D 모델링과 시공 전반을 좌우하는 핵심 데이터가 담겨 있습니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6; font-weight: 700; line-height: 1.85;">
  "도면이 바뀌었는데, 그 변경이 제대로 반영됐는지 확신이 안 설 때가 가장 위험합니다. 플랜트 현장에서 이런 순간이 반복되면 비용과 일정 모두 타격을 입습니다."
</div>

<p>기존 방식: PDF 도면을 사람이 눈으로 확인하고 치수와 스펙을 수작업으로 입력한 뒤, 도면 버전(Revision)이 바뀔 때마다 동일한 과정을 반복했습니다. 누락된 내용은 대부분 3D 모델링 이후, 심지어 시공 단계에서야 발견됐습니다. <strong>앞에서 놓친 것이 뒤에서 훨씬 큰 재작업으로 돌아오는 구조</strong>였습니다.</p>

<p>DLENC 팀은 이 구조 자체에 손을 댔습니다. Copilot Studio의 로우코드 환경 안에서 도면 분석부터 조건 검증, 데이터 매핑까지 이어지는 2-Stage 에이전트를 설계했습니다. <strong>전담 개발팀 없이, 현업이 직접 만들었습니다.</strong></p>

<img src="/mwkorea/assets/images/20260416-dlenc-review/image4.png" alt="도면 설계 변경 자동화 프로세스" style="border-radius: 12px; margin-bottom: 1.4rem;" />

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">Stage 1 · 도면 분석 & 데이터 추출</div>
    <ul style="margin: 0.5rem 0 0; padding-left: 1.2rem; line-height: 1.85;">
      <li>GA Drawing PDF 업로드</li>
      <li>치수 테이블·BOM·스펙 자동 인식</li>
      <li>추출 결과를 JSON으로 표준화</li>
    </ul>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">Stage 2 · 조건 검증 & 자동 매핑</div>
    <ul style="margin: 0.5rem 0 0; padding-left: 1.2rem; line-height: 1.85;">
      <li>밸브 타입·스펙 조건 기반 분기</li>
      <li>검증된 데이터만 Excel 양식 입력</li>
      <li>3D 셋업 파일로 자동 반영</li>
    </ul>
  </div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fefce8; border: 1px solid #fde68a; color: #854d0e; font-weight: 700; line-height: 1.85;">
  🔑 이 에이전트가 단순 문자 인식(OCR)과 다른 점이 바로 여기에 있습니다. 도면 이미지를 텍스트로 읽는 것이 아니라, 설계 데이터로 이해하고 조건에 따라 검증까지 수행합니다.
</div>

<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">설계 수정 정확도</div>
    <div>누락·오입력 방지</div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">최신 도면 기준 자동 반영</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">변경 대응 속도</div>
    <div>즉시 데이터화</div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">수작업 입력·검증 제거</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">후행 공정 리스크</div>
    <div>재작업 감소</div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem; color: #6b7280;">시공 단계 오류 예방</div>
  </div>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a; font-weight: 700; line-height: 1.85;">
  설계 수정 자동화의 본질은 "속도"가 아니라 "신뢰"입니다.
</div>

<p>ISO Drawing, 타 공종 GA 도면, 3D 모델 QA/QC까지 같은 구조로 확장할 수 있습니다.</p>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #ea580c; background: #f8fafc;">세 에이전트가 공통으로 보여준 것</h2>

<div style="display: grid; grid-template-columns: 1fr; gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fff7ed; border: 1px solid #fdba74; color: #9a3412;">
    <div style="font-weight: 800;">현장에서 실제로 반복되는 문제를 골랐습니다</div>
    <div style="margin-top: 0.3rem;">시연용 데모가 아니라, 매일 일어나는 업무를 정확히 타겟</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fff7ed; border: 1px solid #fdba74; color: #9a3412;">
    <div style="font-weight: 800;">로우코드 플랫폼으로 현업이 직접 만들었습니다</div>
    <div style="margin-top: 0.3rem;">Copilot Studio + AI Builder, 별도 개발 조직 없이 현업 주도 구현</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fff7ed; border: 1px solid #fdba74; color: #9a3412;">
    <div style="font-weight: 800;">완전 자동이 아닌 Human-in-the-loop</div>
    <div style="margin-top: 0.3rem;">AI가 추출·생성하고 사람이 최종 검토. 신뢰를 설계에 먼저 반영</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #fff7ed; border: 1px solid #fdba74; color: #9a3412;">
    <div style="font-weight: 800;">하나의 에이전트가 아닌 확산 가능한 구조</div>
    <div style="margin-top: 0.3rem;">같은 패턴으로 전사 확장·멀티 에이전트 연결 가능</div>
  </div>
</div>

<hr/>

<div style="margin: 1rem 0 1.4rem; padding: 1.15rem 1.2rem; border-radius: 18px; background: linear-gradient(135deg, #111827 0%, #1f2937 100%); color: #f9fafb; line-height: 1.85;">
  <div style="font-weight: 800; margin-bottom: 0.5rem; font-size: 1.05rem;">건설·플랜트 현장의 디지털 전환은 거창한 기술 발표에서 시작되지 않습니다.</div>
  현장 업무를 가장 잘 아시는 분이, 그 문제를 직접 풀 수 있을 때 비로소 시작됩니다. 비슷한 반복 업무가 있으시다면, 이 질문 하나로 시작해 보세요.
  <div style="margin-top: 0.8rem; font-weight: 800; font-size: 1.05rem; color: #67e8f9;">"이 일, 정말 사람이 계속 해야 할까요?"</div>
  <div style="margin-top: 1rem; font-size: 0.92rem; color: #9ca3af;">NEXT ISSUE · 월간 코파일럿, 다음 호에도 또 다른 에이전톤 우승 팀의 이야기로 찾아옵니다. 현장에서 탄생한 AI 에이전트 — 다음 우승 사례 Recap도 놓치지 마세요.</div>
</div>

</div>

