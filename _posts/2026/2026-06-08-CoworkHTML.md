---
title: "'쉽게 이해되는 HTML 결과물' 만들기 by M365 Copilot"
date: 2026-06-08T00:00:00 KST
last_modified_at: 2026-06-09T00:00:00 KST
excerpt: "Karpathy의 통찰처럼, Markdown은 '지식을 표현'하는 데 강하고 HTML은 '소비 경험'에서 압도적입니다. M365 Copilot의 Researcher로 자료를 모으고, Cowork로 카드·하이라이트·표가 살아 있는 HTML 결과물을 만든 뒤, Word·PowerPoint로 확장하는 4단계 워크플로를 정리했습니다."
description: "M365 Copilot Researcher와 Cowork로 자료 수집부터 HTML 결과물 생성, 결과물 확인, Word·PowerPoint 전환까지 이어지는 4단계 워크플로를 단계별 프롬프트 예시와 함께 정리했습니다."
keywords: "M365 Copilot, Microsoft 365 Copilot, Cowork, Researcher Agent, HTML 문서 생성, HTML 슬라이드, Word 변환, PowerPoint 변환, Markdown vs HTML, AI 문서 자동화, Karpathy"
tags:
  - M365 Copilot
  - HTML
  - Researcher
  - Cowork
categories:
  - Copilot
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
  og_image: https://ms.studydev.com/m365/cowork_html_guide/images/copilot_cowork_html.png
classes: wide
toc: false
toc_sticky: true
author: 김현수
---


<div class="monthlycopilot-page monthlycopilot-page--tour">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "headline": "'쉽게 이해되는 HTML 결과물' 만들기 by M365 Copilot",
      "description": "M365 Copilot Researcher와 Cowork로 자료 수집부터 HTML 결과물 생성, 결과물 확인, Word·PowerPoint 전환까지 이어지는 4단계 워크플로를 단계별 프롬프트 예시와 함께 정리했습니다.",
      "inLanguage": "ko-KR",
      "datePublished": "2026-06-08",
      "dateModified": "2026-06-09",
      "author": { "@type": "Person", "name": "김현수" },
      "publisher": { "@type": "Organization", "name": "Monthly Copilot Korea" },
      "mainEntityOfPage": { "@type": "WebPage", "@id": "{{ page.url | absolute_url }}" },
      "image": "https://ms.studydev.com/m365/cowork_html_guide/images/copilot_cowork_html.png",
      "keywords": "M365 Copilot, Microsoft 365 Copilot, Cowork, Researcher Agent, HTML 문서 생성, HTML 슬라이드, Word 변환, PowerPoint 변환, Markdown vs HTML, AI 문서 자동화",
      "articleSection": "Monthly Copilot"
    },
    {
      "@type": "HowTo",
      "name": "M365 Copilot으로 HTML 결과물 만들기 — 4단계 워크플로",
      "description": "M365 Copilot Researcher와 Cowork를 활용해 Markdown 자료 수집부터 HTML 결과물 생성, 확인, Word·PowerPoint 전환까지 진행하는 4단계 절차입니다.",
      "inLanguage": "ko-KR",
      "totalTime": "PT20M",
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "name": "Researcher로 Markdown 자료 수집",
          "text": "M365 Copilot Researcher Agent로 사내 문서(Microsoft Graph)와 웹 검색을 심층 조사해 주제에 맞는 Markdown 기반 자료를 확보합니다.",
          "url": "{{ page.url | absolute_url }}#3-1"
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "name": "Cowork로 HTML 결과물 생성",
          "text": "수집한 Markdown 자료를 첨부하고 Cowork Agent에 요청해 카드·하이라이트·표가 포함된 HTML 문서와 슬라이드를 생성합니다.",
          "url": "{{ page.url | absolute_url }}#3-2"
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "name": "HTML 결과물 확인",
          "text": "OneDrive 동기화 폴더의 세션 ID 폴더(output)에 저장된 HTML 파일을 브라우저에서 열어 확인하고 점검합니다.",
          "url": "{{ page.url | absolute_url }}#3-3"
        },
        {
          "@type": "HowToStep",
          "position": 4,
          "name": "Word·PowerPoint로 전환",
          "text": "같은 대화에서 Word 또는 PowerPoint로 전환을 요청해 세부 문구·순서·이미지를 익숙한 도구로 편집·배포합니다.",
          "url": "{{ page.url | absolute_url }}#3-4"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "inLanguage": "ko-KR",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "M365 Copilot으로 HTML 문서를 어떻게 만드나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Researcher Agent로 자료를 모은 뒤, 그 자료(Markdown 또는 Page)를 Cowork Agent에 첨부하고 원하는 형태의 HTML을 요청하면 됩니다. 카드·하이라이트·표·코드 블록까지 갖춘 HTML이 몇 분 안에 생성되며, CSS나 JavaScript를 직접 작성할 필요가 없습니다."
          }
        },
        {
          "@type": "Question",
          "name": "Markdown과 HTML은 각각 언제 쓰는 게 좋나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Markdown은 자료 수집·초안 작성·구조화 같은 '지식 표현'에 강하고, HTML은 카드·강조·표·인터랙션으로 '소비 경험(전달·발표·공유)'에 강합니다. 둘은 경쟁이 아니라 Markdown으로 모으고 HTML로 전달하는 릴레이로 함께 쓰는 것이 좋습니다."
          }
        },
        {
          "@type": "Question",
          "name": "Cowork가 만든 HTML 파일은 어디에 저장되나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "로컬 파일 시스템의 OneDrive 동기화 폴더에 자동 저장됩니다. Windows 기준 경로는 C:\\Users\\(사용자명)\\Documents\\Coworker\\sessions\\(세션-ID)\\output\\ 이며, 각 세션마다 고유 세션 ID 폴더가 생성되고 가장 최근 수정된 폴더가 마지막 작업 세션입니다."
          }
        },
        {
          "@type": "Question",
          "name": "만든 HTML을 Word나 PowerPoint로 바꿀 수 있나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "네. 같은 대화 안에서 Word 또는 PowerPoint로 전환해 달라고 요청하면 됩니다. 제목 계층 구조와 표·이미지 캡션을 유지한 Word 문서, 디자인 일관성을 유지한 PowerPoint 슬라이드로 변환되어 세밀한 편집과 배포가 쉬워집니다."
          }
        },
        {
          "@type": "Question",
          "name": "만든 HTML 결과물을 어떻게 공유하나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "GitHub Pages를 이용하면 별도 서버 없이 브라우저에서 클릭 몇 번만으로 공개 URL을 만들 수 있습니다. 비개발자도 따라 할 수 있으며, 만든 링크 한 줄로 동료나 고객에게 바로 공유할 수 있습니다."
          }
        },
        {
          "@type": "Question",
          "name": "어떤 형태의 HTML을 만들 수 있나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Executive Brief(보고·요약), Comparison Matrix(비교·판단), Annotated Technical Review(코드·기술 설명), One-page Proposal(고객 제안), Interactive Learning(학습·교육), Mini Web App(계산기·체크리스트 등 업무 도구) 6가지 형태가 대표적입니다. 프롬프트 첫머리에 형태를 지정하면 결과 품질이 올라갑니다."
          }
        }
      ]
    }
  ]
}
</script>

<div class="mc-issue-strip">Monthly Copilot · July 2026 · 월간 코파일럿 7월호 · Workflow</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Workflow</div>
  <div class="mc-cover-title">'쉽게 이해되는 HTML 결과물' 만들기 by M365 Copilot</div>
  <div class="mc-cover-subtitle">"읽기 좋은 문서"를 넘어, "보는 순간 이해되는 문서"를 만든다면?</div>
</div>

<div class="mc-card">
  <div class="mc-card-title"><strong>Article Summary</strong></div>
  <div>Andrej Karpathy는 "같은 내용이라도 Markdown보다 HTML이 사람이 '보는 결과물'로 훨씬 풍부하다"고 말했습니다. Markdown은 초안을 쓰고 지식을 구조화하는 데 최적이지만, HTML은 카드·하이라이트·표·인터랙션으로 <strong>소비 경험</strong>을 끌어올립니다. 이 글은 M365 Copilot이 제공하는 Researcher로 자료 수집 → Cowork로 HTML 결과물 생성 → 결과물 확인 → Word·PowerPoint 전환의 4단계로, 쉽고 빠르게 완성도 높은 문서를 만드는 방법을 안내합니다.</div>
</div>

<img src="https://ms.studydev.com/m365/cowork_html_guide/images/copilot_cowork_html.png" alt="흔어진 자료를 스스로 정리해서 HTML 문서로 만든다" style="border:1px solid #d1d5db; border-radius:12px;" />

<hr/>

<h2 class="mc-section-title">1. 왜 지금 HTML인가 — Karpathy의 화두</h2>

<p>AI 시대 프롬프트의 중요성과 함께 Markdown 형식의 문서를 많이 사용했습니다. 가볍고, 버전 관리가 쉽고, 어디서나 열립니다. 하지만 Markdown은 본질적으로 <strong>"읽는" 포맷</strong>입니다. 제목·목록·코드 블록은 있지만, 시선을 잡는 강조도, 한눈에 비교되는 카드도, 클릭으로 펼쳐지는 인터랙션도 없습니다.</p>

<p>Andrej Karpathy가 짚은 핵심은 단순합니다. <strong>"같은 내용이라도 HTML이 '보는 결과물'로 훨씬 풍부하다"</strong>는 것입니다. 사람은 줄글보다 <strong>시각적 위계</strong>에서 더 빠르게 의미를 길어 올립니다. 색으로 구분된 박스, 좌우로 비교되는 표, 강조된 한 문장은 같은 정보를 더 짧은 시간에, 더 정확하게 전달합니다.</p>

<div class="mc-card mc-card--blue">
  <div class="mc-card-title"><strong>한 줄 요약</strong></div>
  <div style="color:#1f2937;">Markdown = <strong>지식 표현</strong>(초안·구조화·편집)에 최적 · HTML = <strong>소비 경험</strong>(전달·설득·발표)에 최적. 둘은 경쟁이 아니라 <strong>릴레이</strong>입니다.</div>
  <div class="mc-card-note">참고: <a href="https://x.com/karpathy/status/2053872850101285137?s=20" target="_blank" rel="noopener noreferrer">Andrej Karpathy — Markdown vs HTML</a></div>
</div>

<p style="margin:1.75rem 0 0.5rem;"><strong>Markdown vs HTML — 무엇에 강한가</strong></p>

<div class="mc-table-wrap" style="margin-top:0.4rem;">
  <table>
  <tr>
    <th>관점</th>
    <th>Markdown</th>
    <th>HTML</th>
  </tr>
  <tr>
    <td>목적</td>
    <td>지식 표현 · 초안</td>
    <td>소비 경험 · 전달</td>
  </tr>
  <tr>
    <td>강점</td>
    <td>가볍고 구조적, 편집·버전관리 용이</td>
    <td>시각 위계, 강조, 카드·표·인터랙션</td>
  </tr>
  <tr>
    <td>한계</td>
    <td>시각적 강조·레이아웃에 제약</td>
    <td>직접 작성 시 CSS·JS 부담</td>
  </tr>
  <tr>
    <td>최적 단계</td>
    <td>자료 수집·구조 설계</td>
    <td>고객 전달·발표·공유</td>
  </tr>
  </table>
</div>

<p>문제는 <strong>"HTML이 좋은 건 알겠는데, 직접 만들기는 번거롭다"</strong>는 점이었습니다. 예전에는 카드 레이아웃 하나, 하이라이트 박스 하나를 위해 CSS와 JavaScript를 직접 써야 했죠. <strong>이 지점을 M365 Copilot Cowork가 바꿉니다.</strong> 원하는 형태를 말로 설명하면, 반응형 레이아웃·하이라이트·코드 블록까지 갖춘 HTML을 몇 분 안에 받을 수 있습니다.</p>

<hr/>

<h2 class="mc-section-title">2. 어떤 HTML을 만들 것인가 — 실용적인 6가지 형태</h2>

<p>"HTML로 만들자"는 막연합니다. 용도에 따라 형태를 먼저 정하면 프롬프트가 명확해지고 결과물 품질이 올라갑니다. 실무에서 가장 자주 쓰이는 6가지를 정리했습니다.</p>

<div class="mc-table-wrap">
  <table>
    <tr>
      <th>형태</th>
      <th>용도</th>
      <th>활용 예시</th>
    </tr>
    <tr>
      <td><strong>Executive Brief HTML</strong></td>
      <td>보고 / 요약</td>
      <td>리서치, 회의록, 고객 분석, 의사결정 자료</td>
    </tr>
    <tr>
      <td><strong>Comparison Matrix HTML</strong></td>
      <td>비교 / 판단</td>
      <td>솔루션 비교, 경쟁사 분석, 제품 선택</td>
    </tr>
    <tr>
      <td><strong>Annotated Technical Review HTML</strong></td>
      <td>코드 / 기술 설명</td>
      <td>코드 리뷰, 아키텍처 설명, 변경사항 리뷰</td>
    </tr>
    <tr>
      <td><strong>One-page Proposal HTML</strong></td>
      <td>고객 제안</td>
      <td>고객 미팅 후 follow-up, 제안서 초안</td>
    </tr>
    <tr>
      <td><strong>Interactive Learning HTML</strong></td>
      <td>학습 / 교육</td>
      <td>워크샵, 교육자료, 내부 enablement</td>
    </tr>
    <tr>
      <td><strong>Mini Web App HTML</strong></td>
      <td>업무 도구</td>
      <td>계산기, 체크리스트, ROI·비용 계산기</td>
    </tr>
  </table>
</div>

<div class="mc-card mc-card--blue">
  <div class="mc-card-title"><strong>형태 선택 팁</strong></div>
  <div style="color:#1f2937;">프롬프트 첫 문장에서 <strong>"어떤 형태의 HTML"</strong>인지를 먼저 못 박으세요. 예: "이 자료를 <em>Comparison Matrix 형태</em>의 HTML로 만들어줘." 형태가 정해지면 Cowork가 레이아웃·강조·구성요소를 그에 맞게 자동 선택합니다.</div>
</div>
<hr/>

<h2 class="mc-section-title">3. 전체 워크플로 — 4단계 한눈에 보기</h2>

<p>Markdown의 강점(구조화·편집)과 HTML의 강점(소비 경험)을 모두 살리는 길은 <strong>"릴레이"</strong>입니다. Researcher가 Markdown으로 지식을 모으고, Cowork가 그것을 HTML로 '보는 결과물'로 바꾸고, 필요하면 Word·PPT로 확장합니다. 아래 표로 전체 흐름을 먼저 살펴본 뒤, <strong>3-1부터 3-4까지</strong> 각 단계를 차례로 따라가 보겠습니다.</p>

<div class="mc-card mc-arch" style="text-align:center;">
  <div class="mc-card-title" style="text-align:left;"><strong>전체 파이프라인</strong></div>
  <div style="display:flex; flex-wrap:wrap; align-items:stretch; justify-content:center; gap:0.5rem; padding-top:0.4rem;">
    <div style="flex:1 1 150px; min-width:140px; max-width:210px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.55rem; background:#ffffff; border:1px solid #dbe4f0; border-radius:16px; padding:1.1rem 0.8rem;">
      <img src="https://ms.studydev.com/icons/copilot_researcher_tools.png" alt="Researcher" style="width:34px; height:34px;" />
      <div style="font-weight:700; color:#1d4ed8; line-height:1.4;">Researcher로<br/>자료 수집</div>
    </div>
    <div style="display:flex; align-items:center; color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/></svg></div>
    <div style="flex:1 1 150px; min-width:140px; max-width:210px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.55rem; background:linear-gradient(135deg,#1e3a8a 0%,#2563eb 100%); border:1px solid #1d4ed8; border-radius:16px; padding:1.1rem 0.8rem;">
      <img src="https://ms.studydev.com/icons/copilot_cowork.png" alt="Cowork" style="width:34px; height:34px;" />
      <div style="font-weight:700; color:#ffffff; line-height:1.4;">Cowork에서<br/>HTML 생성</div>
    </div>
    <div style="display:flex; align-items:center; color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/></svg></div>
    <div style="flex:1 1 150px; min-width:140px; max-width:210px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.55rem; background:#ffffff; border:1px solid #dbe4f0; border-radius:16px; padding:1.1rem 0.8rem;">
      <span style="color:#1d4ed8;"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M.54 3.87.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.826a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31zM2.19 4a1 1 0 0 0-.996 1.09l.637 7a1 1 0 0 0 .995.91h10.348a1 1 0 0 0 .995-.91l.637-7A1 1 0 0 0 13.81 4zm4.69-1.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981l.006.139q.323-.119.684-.12h5.396z"/></svg></span>
      <div style="font-weight:700; color:#1d4ed8; line-height:1.4;">출력 파일<br/>확인</div>
    </div>
    <div style="display:flex; align-items:center; color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/></svg></div>
    <div style="flex:1 1 150px; min-width:140px; max-width:210px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.55rem; background:#ffffff; border:1px solid #dbe4f0; border-radius:16px; padding:1.1rem 0.8rem;">
      <div style="display:flex; align-items:center; gap:0.3rem;"><img src="https://ms.studydev.com/icons/word.svg" alt="Word" style="width:30px; height:30px;" /><img src="https://ms.studydev.com/icons/powerpoint.svg" alt="PowerPoint" style="width:30px; height:30px;" /></div>
      <div style="font-weight:700; color:#1d4ed8; line-height:1.4;">Word · PPT<br/>전환 편집</div>
    </div>
  </div>
</div>

<div class="mc-table-wrap">
  <table>
    <tr>
      <th>단계</th>
      <th>작업</th>
      <th>내용</th>
    </tr>
    <tr>
      <td><strong>1단계</strong></td>
      <td>자료 수집</td>
      <td>M365 Copilot <strong>Researcher Agent</strong>로 사내 문서·웹을 심층 조사해 <strong>Markdown</strong> 기반 자료 확보</td>
    </tr>
    <tr>
      <td><strong>2단계</strong></td>
      <td>HTML 생성</td>
      <td>M365 Copilot <strong>Cowork Agent</strong>로 카드·하이라이트·표가 살아 있는 <strong>HTML 결과물</strong> 생성</td>
    </tr>
    <tr>
      <td><strong>3단계</strong></td>
      <td>결과물 확인</td>
      <td>세션 폴더에 저장된 <strong>HTML 파일</strong>을 브라우저에서 열어 확인·점검</td>
    </tr>
    <tr>
      <td><strong>4단계</strong></td>
      <td>Word·PPT 전환</td>
      <td>같은 대화에서 <strong>Word·PowerPoint</strong>로 전환해 세밀하게 편집·배포</td>
    </tr>
  </table>
</div>

<div class="mc-card">
  <div class="mc-card-title"><strong>핵심 원리</strong></div>
  <div>콘텐츠는 <strong>HTML에서 먼저 확정</strong>하고, 세부 문구·순서·이미지 교체 같은 마감 작업은 <strong>Word·PPT</strong>에서 합니다. 콘텐츠 작업과 디자인 마감을 분리하면 수정 비용이 크게 줄어듭니다.</div>
</div>

<h3>3-1. 1단계 — Researcher로 Markdown 자료 수집</h3>

<p>좋은 HTML은 좋은 콘텐츠에서 나옵니다. M365 Copilot의 <strong>Researcher Agent</strong>를 이용하면 사내 문서와 웹 검색 결과를 심층 조사해 주제에 맞는 자료를 한 번에 모을 수 있습니다. 사내 콘텐츠는 <strong>Microsoft Graph</strong>를 통해 Entra ID 인증·ACL 권한 범위 안에서만 조회되고, 웹 검색은 별도 외부 채널로 확장됩니다.</p>

<style>
.page__content .monthlycopilot-page .mc-card.mc-arch img { display:inline-block; width:auto; margin:0; border:0; border-radius:0; box-shadow:none; vertical-align:middle; }
.page__content .monthlycopilot-page .mc-card.mc-arch svg { vertical-align:middle; }
</style>
<div class="mc-card mc-arch" style="position:relative; left:50%; transform:translateX(-50%); width:min(96vw, 1180px); box-sizing:border-box;">
  <div class="mc-card-title"><strong>연결되는 데이터 소스 — 아키텍처</strong></div>
  <div style="position:relative; padding-top:0.3rem;">
    <div style="position:absolute; top:0; right:0; display:flex; align-items:center; gap:0.5rem; background:#fffbeb; border:1px dashed #f59e0b; border-radius:12px; padding:0.5rem 0.75rem;">
      <img src="https://ms.studydev.com/icons/enter_id.svg" alt="Entra ID" style="width:22px;height:22px;" />
      <div>
        <div style="font-weight:800; color:#92400e;">Entra ID</div>
        <div style="font-size:0.78rem; color:#b45309;">인증 · ACL 권한 검증</div>
      </div>
    </div>
    <div style="display:flex; justify-content:center;">
      <div style="display:flex; align-items:center; gap:0.6rem; background:#eff6ff; border:1px solid #bfdbfe; border-radius:12px; padding:0.6rem 1rem;">
        <span style="flex-shrink:0; width:32px; height:32px; display:inline-flex; align-items:center; justify-content:center; background:#dbeafe; border-radius:50%; color:#2563eb;"><svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" fill="currentColor" viewBox="0 0 16 16"><path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/></svg></span>
        <div style="line-height:1.35;">
          <div style="font-weight:800;">사용자</div>
          <div style="font-size:0.82rem; color:#475569;">"이 주제로 자료를 모아줘"</div>
        </div>
      </div>
    </div>
    <div style="text-align:center; font-size:1.4rem; line-height:1.5; color:#94a3b8;">↓</div>
    <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:0.8rem;">
      <div style="flex:1 1 360px; max-width:620px; background:linear-gradient(135deg,#1e3a8a 0%,#2563eb 100%); color:#eff6ff; border-radius:16px; padding:1.15rem 1.35rem;">
        <div style="display:flex; align-items:center; gap:1rem;">
          <span style="flex-shrink:0; width:54px; height:54px; display:inline-flex; align-items:center; justify-content:center; background:#ffffff; border-radius:50%; box-shadow:0 2px 8px rgba(0,0,0,0.15);"><img src="https://ms.studydev.com/icons/copilot.svg" alt="M365 Copilot" style="width:30px; height:30px;" /></span>
          <div>
            <div style="font-weight:800; font-size:1.15rem;">M365 Copilot</div>
            <div style="font-size:0.88rem; margin:0.3rem 0 0.7rem; color:#dbeafe;">사용자 요청을 해석하고, 적절한 채널로 데이터를 수집·정제·요약</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.45rem;">
              <span style="display:inline-flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.16); color:#fff; border-radius:999px; padding:0.32rem 0.85rem; font-size:0.84rem; font-weight:700;"><img src="https://ms.studydev.com/icons/copilot_researcher_tools.png" alt="" style="flex-shrink:0; width:18px;height:18px;" />Researcher Agent</span>
              <span style="display:inline-flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.16); color:#fff; border-radius:999px; padding:0.32rem 0.85rem; font-size:0.84rem; font-weight:700;"><img src="https://ms.studydev.com/icons/copilot_cowork.png" alt="" style="flex-shrink:0; width:18px;height:18px;" />Cowork Agent</span>
            </div>
          </div>
        </div>
      </div>
      <div style="display:flex; align-items:center; gap:0.5rem;">
        <span style="font-weight:700; font-size:0.82rem; white-space:nowrap; color:#64748b;">호출 →</span>
        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:0.7rem 0.9rem;">
          <div style="font-size:0.75rem; font-weight:700; margin-bottom:0.4rem; color:#64748b;">LLM 모델</div>
          <div style="display:flex; align-items:center; gap:0.4rem; font-size:0.88rem; font-weight:600;"><img src="https://ms.studydev.com/icons/chatgpt.svg" alt="" style="flex-shrink:0; width:18px;height:18px;" />GPT</div>
          <div style="display:flex; align-items:center; gap:0.4rem; font-size:0.88rem; font-weight:600; margin-top:0.3rem;"><img src="https://ms.studydev.com/icons/claude.svg" alt="" style="flex-shrink:0; width:18px;height:18px;" />Claude</div>
        </div>
      </div>
    </div>
    <div style="text-align:center; font-size:1.4rem; line-height:1.5; color:#94a3b8;">↓</div>
    <div style="display:flex; flex-wrap:wrap; gap:1rem;">
      <div style="flex:2 1 440px;">
        <div style="text-align:center; font-size:0.8rem; font-weight:800; letter-spacing:0.02em; color:#64748b; margin-bottom:0.5rem;">사내 콘텐츠 채널</div>
        <div style="display:flex; align-items:center; justify-content:center; gap:0.55rem; background:#ffffff; border:1.5px solid #93c5fd; border-radius:12px; padding:0.7rem 0.9rem;">
          <img src="https://ms.studydev.com/icons/msgraph.svg" alt="" style="flex-shrink:0; width:26px;height:26px;" />
          <div style="text-align:center; line-height:1.35;">
            <div style="font-weight:800;">Microsoft Graph</div>
            <div style="font-size:0.8rem; color:#475569;">권한 기반 통합 액세스 레이어</div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-around; font-size:1.15rem; color:#93c5fd; padding:0.1rem 0;"><span>↑</span><span>↑</span><span>↑</span></div>
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem;">
          <div style="flex:2 1 220px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:0.7rem 0.8rem;">
            <div style="font-weight:700; font-size:0.85rem; margin-bottom:0.5rem; display:flex; align-items:center; gap:0.35rem; flex-wrap:wrap;"><img src="https://ms.studydev.com/icons/onedrive.svg" alt="" style="width:18px;height:18px;" />OneDrive · <img src="https://ms.studydev.com/icons/sharepoint.svg" alt="" style="width:18px;height:18px;" />SharePoint</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.3rem;">
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.5rem; font-size:0.76rem; font-weight:600; color:#334155;"><img src="https://ms.studydev.com/icons/word.svg" alt="" style="width:14px;height:14px;" />Word</span>
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.5rem; font-size:0.76rem; font-weight:600; color:#334155;"><img src="https://ms.studydev.com/icons/excel.svg" alt="" style="width:14px;height:14px;" />Excel</span>
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.5rem; font-size:0.76rem; font-weight:600; color:#334155;"><img src="https://ms.studydev.com/icons/powerpoint.svg" alt="" style="width:14px;height:14px;" />PPT</span>
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.5rem; font-size:0.76rem; font-weight:600; color:#334155;"><img src="https://ms.studydev.com/icons/pages.svg" alt="" style="width:14px;height:14px;" />Pages</span>
            </div>
          </div>
          <div style="flex:1 1 130px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:0.7rem 0.8rem;">
            <div style="font-weight:700; font-size:0.85rem; margin-bottom:0.5rem; display:flex; align-items:center; gap:0.35rem;"><img src="https://ms.studydev.com/icons/outlook.svg" alt="" style="width:18px;height:18px;" />Outlook</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.3rem;">
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.5rem; font-size:0.76rem; font-weight:600; color:#334155;"><img src="https://ms.studydev.com/icons/Mail.svg" alt="" style="width:14px;height:14px;" />메일</span>
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.5rem; font-size:0.76rem; font-weight:600; color:#334155;"><img src="https://ms.studydev.com/icons/Mail%20Attach.svg" alt="" style="width:14px;height:14px;" />첨부</span>
            </div>
          </div>
          <div style="flex:1 1 130px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:0.7rem 0.8rem;">
            <div style="font-weight:700; font-size:0.85rem; margin-bottom:0.5rem; display:flex; align-items:center; gap:0.35rem;"><img src="https://ms.studydev.com/icons/teams.svg" alt="" style="width:18px;height:18px;" />Teams</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.3rem;">
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.5rem; font-size:0.76rem; font-weight:600; color:#334155;"><img src="https://ms.studydev.com/icons/Chat.svg" alt="" style="width:14px;height:14px;" />채팅</span>
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.5rem; font-size:0.76rem; font-weight:600; color:#334155;"><img src="https://ms.studydev.com/icons/Video.svg" alt="" style="width:14px;height:14px;" />회의</span>
            </div>
          </div>
        </div>
      </div>
      <div style="flex:1 1 280px;">
        <div style="text-align:center; font-size:0.8rem; font-weight:800; letter-spacing:0.02em; color:#64748b; margin-bottom:0.5rem;">외부 지식 채널</div>
        <div style="display:flex; align-items:center; justify-content:center; gap:0.55rem; background:#ffffff; border:1.5px solid #c4b5fd; border-radius:12px; padding:0.7rem 0.9rem;">
          <span style="flex-shrink:0; width:30px; height:30px; display:inline-flex; align-items:center; justify-content:center; background:#ede9fe; border-radius:50%; color:#7c3aed;"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a7 7 0 1 1 2.898 5.673c-.167-.121-.216-.406-.002-.62l1.8-1.8a3.5 3.5 0 0 0 4.572-.328l1.414-1.415a.5.5 0 0 0 0-.707l-.707-.707 1.559-1.563a.5.5 0 1 0-.708-.706l-1.559 1.562-1.414-1.414 1.56-1.562a.5.5 0 1 0-.707-.706l-1.56 1.56-.707-.706a.5.5 0 0 0-.707 0L5.318 5.975a3.5 3.5 0 0 0-.328 4.571l-1.8 1.8c-.58.58-.62 1.6.121 2.137A8 8 0 1 0 0 8a.5.5 0 0 0 1 0"/></svg></span>
          <div style="text-align:center; line-height:1.35;">
            <div style="font-weight:800;">외부 도구 · 커넥터</div>
            <div style="font-size:0.8rem; color:#475569;">웹 검색 · 플러그인으로 확장</div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-around; font-size:1.15rem; color:#c4b5fd; padding:0.1rem 0;"><span>↑</span><span>↑</span></div>
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem;">
          <div style="flex:1 1 130px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:0.7rem 0.8rem;">
            <div style="font-weight:700; font-size:0.85rem; margin-bottom:0.5rem; display:flex; align-items:center; gap:0.35rem;"><img src="https://ms.studydev.com/icons/Globe.svg" alt="" style="width:18px;height:18px;" />Bing 웹 검색</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.3rem;">
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.55rem; font-size:0.76rem; font-weight:600; color:#334155;"><svg xmlns="http://www.w3.org/2000/svg" width="11" height="11" fill="currentColor" viewBox="0 0 16 16"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/></svg>뉴스</span>
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.55rem; font-size:0.76rem; font-weight:600; color:#334155;"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" viewBox="0 0 16 16"><path d="M0 2.5A1.5 1.5 0 0 1 1.5 1h11A1.5 1.5 0 0 1 14 2.5v10.528c0 .3-.05.654-.238.972h.738a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 1 1 0v9a1.5 1.5 0 0 1-1.5 1.5H1.497A1.497 1.497 0 0 1 0 13.5zM12 14c.37 0 .654-.211.853-.441.092-.106.147-.279.147-.531V2.5a.5.5 0 0 0-.5-.5h-11a.5.5 0 0 0-.5.5v11c0 .278.223.5.497.5z"/><path d="M2 3h10v2H2zm0 3h4v3H2zm0 4h4v1H2zm0 2h4v1H2zm5-6h2v1H7zm3 0h2v1h-2zM7 8h2v1H7zm3 0h2v1h-2zm-3 2h2v1H7zm3 0h2v1h-2zm-3 2h2v1H7zm3 0h2v1h-2z"/></svg>컴텐츠</span>
            </div>
          </div>
          <div style="flex:1 1 130px; background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:0.7rem 0.8rem;">
            <div style="font-weight:700; font-size:0.85rem; margin-bottom:0.5rem; display:flex; align-items:center; gap:0.35rem;"><span style="flex-shrink:0; width:18px; height:18px; display:inline-flex; align-items:center; justify-content:center; color:#7c3aed;"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16"><path d="M3.112 3.645A1.5 1.5 0 0 1 4.605 2H7a.5.5 0 0 1 .5.5v.382c0 .696-.497 1.182-.872 1.469a.5.5 0 0 0-.115.118l-.012.025L6.5 4.5v.003l.003.01q.005.015.036.053a.9.9 0 0 0 .27.194C7.09 4.9 7.51 5 8 5c.492 0 .912-.1 1.19-.24a.9.9 0 0 0 .271-.194.2.2 0 0 0 .036-.054l.003-.01v-.008l-.012-.025a.5.5 0 0 0-.115-.118c-.375-.287-.872-.773-.872-1.469V2.5A.5.5 0 0 1 9 2h2.395a1.5 1.5 0 0 1 1.493 1.645L12.645 6.5h.237c.195 0 .42-.147.675-.48.21-.274.528-.52.943-.52.568 0 .947.447 1.154.862C15.877 6.807 16 7.387 16 8s-.123 1.193-.346 1.638c-.207.415-.586.862-1.154.862-.415 0-.733-.246-.943-.52-.255-.333-.48-.48-.675-.48h-.237l.243 2.855A1.5 1.5 0 0 1 11.395 14H9a.5.5 0 0 1-.5-.5v-.382c0-.696.497-1.182.872-1.469a.5.5 0 0 0 .115-.118l.012-.025.001-.006v-.003l-.003-.01a.2.2 0 0 0-.036-.053.9.9 0 0 0-.27-.194C8.91 11.1 8.49 11 8 11s-.912.1-1.19.24a.9.9 0 0 0-.271.194.2.2 0 0 0-.036.054l-.003.01v.002l.001.006.012.025c.016.027.05.068.115.118.375.287.872.773.872 1.469v.382a.5.5 0 0 1-.5.5H4.605a1.5 1.5 0 0 1-1.493-1.645L3.356 9.5h-.238c-.195 0-.42.147-.675.48-.21.274-.528.52-.943.52-.568 0-.947-.447-1.154-.862C.123 9.193 0 8.613 0 8s.123-1.193.346-1.638C.553 5.947.932 5.5 1.5 5.5c.415 0 .733.246.943.52.255.333.48.48.675.48h.238z"/></svg></span>플러그인</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.3rem;">
              <span style="display:inline-flex; align-items:center; gap:0.25rem; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:999px; padding:0.2rem 0.55rem; font-size:0.76rem; font-weight:600; color:#334155;"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M6 3.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 0-1 0v2A1.5 1.5 0 0 0 6.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-8A1.5 1.5 0 0 0 5 3.5v2a.5.5 0 0 0 1 0z"/><path fill-rule="evenodd" d="M11.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H1.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708z"/></svg>사용자 정의 도구</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="mc-card-note">사용자 요청 → <strong>M365 Copilot</strong>(Researcher · Cowork Agent)이 해석 → 사내 콘텐츠는 <strong>Microsoft Graph</strong> 권한 범위 안에서, 외부 지식은 <strong>외부 도구·커넥터</strong>로 수집. 모든 접근은 <strong>Entra ID</strong> 인증·ACL로 검증됩니다.</div>
</div>

<div class="mc-card mc-card--blue" style="position:relative; margin-top:1.75rem;">
  <div class="mc-card-title"><strong>프롬프트 예시 — Researcher Agent</strong></div>
  <button type="button" aria-label="프롬프트 복사" onclick="const c=this.parentElement.querySelector('pre');navigator.clipboard.writeText(c.innerText);const t=this.textContent;this.textContent='복사됨';setTimeout(()=>{this.textContent=t;},1500);" style="position:absolute; top:0.85rem; right:0.85rem; padding:0.3rem 0.7rem; font-size:0.8rem; font-weight:700; color:#374151; background:#ffffff; border:1px solid #d1d5db; border-radius:8px; cursor:pointer;">복사</button>
  <pre style="white-space:pre-wrap; word-break:break-word; background:#f3f4f6; border:1px solid #e5e7eb; border-radius:10px; padding:0.9rem 1rem; margin:0.4rem 0 0; font-size:0.9rem; line-height:1.7; color:#111827;">"AI 시대에 내가 일하는 방식은 어떻게 바뀌고 있는가?"라는 주제에 대해, 현업과 개발자 관점에서 일하는 방식이 어떻게 변화하고 있는지를 조사해줘. 핵심 트렌드와 근거 자료를 정리해줘.</pre>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>출력 형식 선택 팁</strong></div>
  <ul>
    <li><strong>Markdown</strong> — 이후 Cowork 프롬프트에 통째로 붙여 넣기 쉬움 <em>(이 워크플로의 권장 형식)</em></li>
    <li><strong>Pages</strong> — 팀과 공동 편집하며 자료를 보강할 때 유리</li>
    <li><strong>Word</strong> — 사내 결재·공식 배포용 원본으로 재사용</li>
  </ul>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>실제 작업 화면 — 전체 6단계</strong></div>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/01_researcher_01.png" alt="리서치 도구 시작 — 주제 입력 및 소스 선택" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 1</strong> · 리서치 도구를 열고 프롬프트 입력 · 소스(웹 / Microsoft 365) 선택</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/01_researcher_02.png" alt="분석 관점 명확화 질문" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 2</strong> · 활용 목적 · 범위 · 관점 비중을 좁히는 후속 질문에 응답</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/01_researcher_03.png" alt="Researcher가 단계별 추론 진행" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 3</strong> · Researcher가 분석 계획을 세우고 단계별 추론을 진행</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/01_researcher_04.png" alt="핵심 요약과 본문 보고서 생성" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 4</strong> · 핵심 요약 + 관점별 본문 보고서가 자동 생성</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/01_researcher_05.png" alt="페이지로 내보내기" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 5</strong> · "다음으로 내보내기 → Pages"로 내보낼 형식 선택</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/01_researcher_06.png" alt="Pages에 보고서 저장 완료" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 6</strong> · Pages 문서로 저장 완료 — Cowork 단계에서 그대로 재사용</figcaption>
  </figure>
</div>

<h3>3-2. 2단계 — Cowork로 HTML 결과물 생성</h3>

<p>1단계에서 모은 Markdown 자료(또는 Page)를 첨부하고, Cowork에 원하는 결과물을 요청합니다. Markdown으로 표현하기 어려운 <strong>카드 레이아웃 · 하이라이트 박스 · 아이콘 · 코드 블록</strong>까지 자동으로 구성됩니다.</p>

<div class="mc-card mc-card--blue" style="position:relative; margin-top:1.75rem;">
  <div class="mc-card-title"><strong>프롬프트 예시 — Cowork Agent (웹 문서 + 슬라이드 동시 생성)</strong></div>
  <button type="button" aria-label="프롬프트 복사" onclick="const c=this.parentElement.querySelector('pre');navigator.clipboard.writeText(c.innerText);const t=this.textContent;this.textContent='복사됨';setTimeout(()=>{this.textContent=t;},1500);" style="position:absolute; top:0.85rem; right:0.85rem; padding:0.3rem 0.7rem; font-size:0.8rem; font-weight:700; color:#374151; background:#ffffff; border:1px solid #d1d5db; border-radius:8px; cursor:pointer;">복사</button>
  <pre style="white-space:pre-wrap; word-break:break-word; background:#f3f4f6; border:1px solid #e5e7eb; border-radius:10px; padding:0.9rem 1rem; margin:0.4rem 0 0; font-size:0.9rem; line-height:1.7; color:#111827;">AI 시대 일하는 방식 변화 조사.page

첨부된 Page 내용을 바탕으로, 고객에게 전달하기 위한 두 가지 형태의 HTML 문서를 작성해줘.
1. 웹 문서 형태의 HTML (한 페이지 세로로 읽는 형태)
2. 슬라이드 형태의 HTML (페이지 넘기기 기능 포함)

요구사항:
- 전체 배경은 흰색
- 제목·소제목·본문이 구조적으로 잘 보이도록 구성
- 핵심 메시지나 고객에게 꼭 강조할 부분은 Highlight 처리
- (슬라이드의 경우) 불필요한 설명은 줄이고, 짧고 명확한 문장 위주로 요약, 슬라이드 화면 비율 고려
- 고객이 빠르게 이해할 수 있도록 읽기 쉬운 레이아웃 유지
결과물은 바로 사용 가능한 HTML 코드 형태로 제공해줘.</pre>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>실제 작업 화면 — 전체 4단계</strong></div>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/02_cowork_01.png" alt="Cowork에 프롬프트 입력" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 1</strong> · Cowork에 Page 첨부 후 HTML 생성 프롬프트 입력</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/02_cowork_02.png" alt="Cowork가 파일 읽기 및 작업 시작" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 2</strong> · 첨부 Page 내용을 읽고 HTML 문서 작성 시작</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/02_cowork_03.png" alt="웹문서 + 슬라이드 HTML 생성 완료" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 3</strong> · 웹 문서형 + 슬라이드형 HTML 두 파일 생성 완료</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/02_cowork_04.png" alt="산출물 확인 및 다운로드" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 4</strong> · 산출물 확인 — 출력 폴더에서 HTML 파일 다운로드</figcaption>
  </figure>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>단계적 고도화 전략</strong></div>
  <div>한 번에 완벽을 기대하기보다, 대화를 이어가며 점진적으로 품질을 높이세요.</div>
  <ul>
    <li><strong>1차 · 콘텐츠 생성</strong> — "수집한 자료를 HTML 문서로 정리해줘" → 기본 구조·콘텐츠 확보</li>
    <li><strong>2차 · 시각적 개선</strong> — "흰색 배경에 스타일을 더 세련되게. 카드 레이아웃과 아이콘을 적용해줘"</li>
    <li><strong>3차 · 강조·디테일</strong> — "핵심 메시지는 하이라이트 박스로, 비교 항목은 표로 바꿔줘"</li>
  </ul>
</div>

<h3>3-3. 3단계 — HTML 결과물 확인</h3>

<p>Cowork가 생성한 HTML 파일은 로컬 파일 시스템(OneDrive 동기화 폴더)에 자동 저장됩니다. 각 세션마다 고유 세션 ID 폴더가 만들어지며, <strong>가장 최근 수정된 폴더</strong>가 마지막 작업 세션입니다.</p>

<div class="mc-card mc-arch" style="position:relative; background:#0f172a; border-color:#1e293b; padding:0; overflow:hidden;">
  <div style="display:flex; align-items:center; padding:0.55rem 0.9rem; background:#1e293b; border-bottom:1px solid #334155;">
    <span style="display:inline-flex; align-items:center; gap:0.4rem; font-size:0.72rem; font-weight:800; letter-spacing:0.08em; color:#34d399;"><svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="currentColor" viewBox="0 0 16 16"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3m-8.322.12q.322-.119.684-.12h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981z"/></svg>WINDOWS 경로</span>
  </div>
  <pre style="margin:0; background:#0f172a; color:#e2e8f0; padding:1rem 1.1rem; overflow-x:auto; font-size:0.88rem; line-height:1.8;">C:\Users\<span style="color:#fbbf24;">&lt;사용자명&gt;</span>\Documents\Coworker\sessions\<span style="color:#fbbf24;">&lt;세션-ID&gt;</span>\output\
<span style="color:#64748b;"># 예시:</span>
C:\Users\hyounsoo\Documents\Coworker\sessions\<span style="color:#f59e0b;">a1b2c3d4-e5f6-da4d</span>\output\<span style="color:#fffff0;">AI_시대_일하는_방식_변화_웹문서.html</span></pre>
</div>

<div class="mc-card-title" style="margin-top:1.75rem;"><strong>폴더 구조 예시</strong></div>
<div class="mc-card mc-arch" style="margin-top:0.5rem; background:#0f172a; border-color:#1e293b;">
  <pre style="background:transparent; color:#cbd5e1; padding:0.6rem 0.2rem 0.2rem; overflow-x:auto; font-size:0.86rem; line-height:1.35; margin:0;"><span style="color:#fbbf24;"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3m-8.322.12q.322-.119.684-.12h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981z"/></svg></span> <span style="color:#e2e8f0;">Documents</span>
└─ <span style="color:#fbbf24;"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3m-8.322.12q.322-.119.684-.12h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981z"/></svg></span> <span style="color:#e2e8f0;">Coworker</span>
   └─ <span style="color:#fbbf24;"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3m-8.322.12q.322-.119.684-.12h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981z"/></svg></span> <span style="color:#e2e8f0;">sessions</span>
      ├─ <span style="color:#fbbf24;"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3m-8.322.12q.322-.119.684-.12h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981z"/></svg></span> <span style="color:#f59e0b;">a1b2c3d4-e5f6-da4d</span>
      │  └─ <span style="color:#fbbf24;"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3m-8.322.12q.322-.119.684-.12h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981z"/></svg></span> <span style="color:#e2e8f0;">output</span>
      │     ├─ <span style="color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/><path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/></svg></span> <span style="color:#22d3ee;">AI_시대_일하는_방식_변화_웹문서.html</span>
      │     └─ <span style="color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/><path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/></svg></span> <span style="color:#22d3ee;">AI_시대_일하는_방식_변화_슬라이드.html</span>
      └─ <span style="color:#fbbf24;"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3m-8.322.12q.322-.119.684-.12h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981z"/></svg></span> <span style="color:#f59e0b;">f9e8d7c6-b5a4-3210</span>
         └─ <span style="color:#fbbf24;"><svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.825a2 2 0 0 1-1.991-1.819l-.637-7a2 2 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3m-8.322.12q.322-.119.684-.12h5.396l-.707-.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981z"/></svg></span> <span style="color:#e2e8f0;">output</span>
            └─ <span style="color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 16 16" style="vertical-align:-2px;"><path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/><path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/></svg></span> <span style="color:#22d3ee;">guide.html</span></pre>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>실제 작업 화면 — 전체 4단계</strong></div>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/03_cowork_01.png" alt="출력 폴더 확인" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 1</strong> · OneDrive 세션 폴더에서 생성된 HTML 파일 확인</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/03_cowork_02.png" alt="웹 문서형 HTML 결과" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 2</strong> · 웹 문서형 HTML — 한 페이지 세로 스크롤 형태</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/03_cowork_03.png" alt="슬라이드형 HTML 표지" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 3</strong> · 슬라이드형 HTML — 표지 슬라이드</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/03_cowork_04.png" alt="슬라이드형 HTML 목차" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 4</strong> · 슬라이드형 HTML — 목차 및 내비게이션</figcaption>
  </figure>
</div>

<h3>3-4. 4단계 — Word·PowerPoint 파일 생성</h3>

<p>HTML은 시각적으로 강력하지만, 세부 문구 수정·순서 변경·이미지 교체 같은 작업은 익숙한 도구가 더 편합니다. <strong>같은 대화 안에서</strong> Word 또는 PowerPoint로 전환해 달라고 요청하면, 편집과 소유권 관리가 한층 쉬워집니다.</p>

<div class="mc-card mc-card--blue" style="position:relative;">
  <div class="mc-card-title"><strong>전환 요청 예시</strong></div>
  <button type="button" aria-label="프롬프트 복사" onclick="const c=this.parentElement.querySelector('pre');navigator.clipboard.writeText(c.innerText);const t=this.textContent;this.textContent='복사됨';setTimeout(()=>{this.textContent=t;},1500);" style="position:absolute; top:0.85rem; right:0.85rem; padding:0.3rem 0.7rem; font-size:0.8rem; font-weight:700; color:#374151; background:#ffffff; border:1px solid #d1d5db; border-radius:8px; cursor:pointer;">복사</button>
  <pre style="white-space:pre-wrap; word-break:break-word; background:#f3f4f6; border:1px solid #e5e7eb; border-radius:10px; padding:0.9rem 1rem; margin:0.4rem 0 0; font-size:0.9rem; line-height:1.7; color:#111827;">방금 만든 HTML 웹문서는 본문 스타일을 제목 1~3 계층 구조로 맞추고, 표와 이미지 캡션은 그대로 유지하면서 Word 파일로 전환해줘. 그리고 HTML 슬라이드는 디자인 일관성을 유지하면서 PowerPoint 파일로 전환해줘.</pre>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>실제 작업 화면 — 전체 4단계</strong></div>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/04_cowork_01.png" alt="Cowork에서 Word·PPT 전환 요청" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 1</strong> · Cowork에 Word · PowerPoint 전환 프롬프트 입력</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/04_cowork_02.png" alt="전환된 Word 문서 — 계층 구조와 스타일 유지" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 2</strong> · 전환된 Word 문서 — 계층 구조와 스타일 유지</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/04_cowork_03.png" alt="Word·PPT 작업 완료 및 산출물 확인" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 3</strong> · Word · PPT 변환 완료 — 출력 폴더에 4개 파일 생성</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/m365/cowork_html_guide/images/04_cowork_04.png" alt="PowerPoint 슬라이드 전환 결과 확인" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 4</strong> · 전환된 PowerPoint — 디자인 일관성 유지</figcaption>
  </figure>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>권장 작업 순서</strong></div>
  <div>HTML에서 <strong>구조와 콘텐츠를 먼저 확정</strong>하고, 수정이 필요할 때 Word/PPT로 변환하세요. 콘텐츠 작업과 디자인 마감이 분리되어 수정 비용이 크게 줄어듭니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">4. 고급 활용 팁</h2>

<p>원하는 결과를 더 빠르고 일관되게 얻기 위한 다섯 가지 실전 팁입니다. 각 항목을 펼쳐 자세한 방법을 확인하세요.</p>

<style>
.page__content .monthlycopilot-page .mc-acc-list { margin:1rem 0 0; }
.page__content .monthlycopilot-page .mc-acc { background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; margin-bottom:0.7rem; box-shadow:0 1px 2px rgba(15,23,42,0.04); overflow:hidden; }
.page__content .monthlycopilot-page .mc-acc summary { list-style:none; cursor:pointer; display:flex; align-items:center; gap:0.75rem; padding:0.95rem 1.1rem; font-weight:700; color:#1e293b; }
.page__content .monthlycopilot-page .mc-acc summary::-webkit-details-marker { display:none; }
.page__content .monthlycopilot-page .mc-acc summary::marker { content:""; }
.page__content .monthlycopilot-page .mc-acc .mc-acc-ico { flex-shrink:0; width:26px; height:26px; display:inline-flex; align-items:center; justify-content:center; color:#2563eb; }
.page__content .monthlycopilot-page .mc-acc .mc-acc-chevron { margin-left:auto; flex-shrink:0; color:#94a3b8; display:inline-flex; transition:transform 0.2s ease; }
.page__content .monthlycopilot-page .mc-acc[open] .mc-acc-chevron { transform:rotate(180deg); }
.page__content .monthlycopilot-page .mc-acc .mc-acc-body { padding:0 1.1rem 1.05rem 3.2rem; color:#475569; line-height:1.75; }
.page__content .monthlycopilot-page .mc-acc svg { vertical-align:middle; }
</style>
<div class="mc-acc-list">
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M8 0a.5.5 0 0 1 .5.5V1h4A1.5 1.5 0 0 1 14 2.5V11a1.5 1.5 0 0 1-1.5 1.5h-2.879l1.682 2.523a.5.5 0 1 1-.832.554L8.7 12.5H7.3l-1.77 3.077a.5.5 0 0 1-.833-.554L6.38 12.5H3.5A1.5 1.5 0 0 1 2 11V2.5A1.5 1.5 0 0 1 3.5 1h4V.5A.5.5 0 0 1 8 0M3.5 2a.5.5 0 0 0-.5.5V11a.5.5 0 0 0 .5.5h9a.5.5 0 0 0 .5-.5V2.5a.5.5 0 0 0-.5-.5z"/></svg></span>HTML 슬라이드 → PowerPoint 변환으로 일관된 디자인<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">슬라이드형 HTML을 PowerPoint로 전환할 때 <strong>"디자인 일관성을 유지하면서 변환해줘"</strong>라고 명시하면 표지·본문·색상 테마가 흐트러지지 않습니다. <strong>화면 비율(16:9)</strong>과 폰트 계층을 함께 지정하면 슬라이드 레이아웃이 안정적으로 유지되고, 발표 자료로 바로 쓸 수 있는 완성도가 나옵니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M6 3.5A1.5 1.5 0 0 1 7.5 2h1A1.5 1.5 0 0 1 10 3.5v1A1.5 1.5 0 0 1 8.5 6v1H14a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0v-1A.5.5 0 0 1 2 7h5.5V6A1.5 1.5 0 0 1 6 4.5zm-6 8A1.5 1.5 0 0 1 1.5 10h1A1.5 1.5 0 0 1 4 11.5v1A1.5 1.5 0 0 1 2.5 14h-1A1.5 1.5 0 0 1 0 12.5zm6 0A1.5 1.5 0 0 1 7.5 10h1a1.5 1.5 0 0 1 1.5 1.5v1A1.5 1.5 0 0 1 8.5 14h-1A1.5 1.5 0 0 1 6 12.5zm6 0a1.5 1.5 0 0 1 1.5-1.5h1a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1-1.5 1.5h-1a1.5 1.5 0 0 1-1.5-1.5z"/></svg></span>Researcher → Cowork 체이닝으로 품질 높이기<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">Researcher 결과(Markdown 또는 Page)를 그대로 Cowork에 넘기면, <strong>출처가 풍부한 콘텐츠</strong> 위에 디자인이 입혀져 품질이 한 단계 올라갑니다. 자료 수집과 디자인을 분리하면 각 단계에 집중할 수 있어, 근거가 탄탄하면서도 보기 좋은 결과물이 나옵니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M11.534 7h3.932a.25.25 0 0 1 .192.41l-1.966 2.36a.25.25 0 0 1-.384 0l-1.966-2.36a.25.25 0 0 1 .192-.41m-11 2h3.932a.25.25 0 0 0 .192-.41L2.692 6.23a.25.25 0 0 0-.384 0L.342 8.59A.25.25 0 0 0 .534 9"/><path fill-rule="evenodd" d="M8 3c-1.552 0-2.94.707-3.857 1.818a.5.5 0 1 1-.771-.636A6.002 6.002 0 0 1 13.917 7H12.9A5 5 0 0 0 8 3M3.1 9a5 5 0 0 0 8.757 2.182.5.5 0 1 1 .771.636A6 6 0 0 1 2.083 9z"/></svg></span>기존 HTML을 부분만 갱신하기<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body"><strong>"3번 섹션 표만 최신 수치로 바꿔줘"</strong>처럼 부분 갱신을 요청하면, 전체를 다시 만들지 않고 필요한 곳만 수정됩니다. 토큰과 시간을 아끼면서도 나머지 영역의 디자인 일관성이 그대로 유지되어, 반복 수정에 특히 유용합니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0"/><path d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1z"/></svg></span>이미지가 포함된 문서 처리<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">이미지 <strong>캡션·정렬·크기</strong>를 명시하면 레이아웃이 안정적으로 유지됩니다. 슬라이드 전환 시에는 <strong>화면 비율</strong>도 함께 지정하세요. 이미지가 본문 흐름을 깨지 않도록 "이미지는 본문 너비에 맞춰 가운데 정렬"처럼 배치 규칙을 함께 요청하면 더 깔끔합니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M9.5 2.672a.5.5 0 1 0 1 0V.843a.5.5 0 0 0-1 0zm4.5.035A.5.5 0 0 0 13.293 2L12 3.293a.5.5 0 1 0 .707.707L14 2.707a.5.5 0 0 0 0-.707M7.293 4A.5.5 0 1 0 8 3.293L6.707 2A.5.5 0 0 0 6 2.707zm-.621 2.5a.5.5 0 1 0 0-1H4.843a.5.5 0 1 0 0 1zm8.485 0a.5.5 0 1 0 0-1h-1.829a.5.5 0 0 0 0 1zM13.293 10A.5.5 0 1 0 14 9.293L12.707 8a.5.5 0 1 0-.707.707zM9.5 11.157a.5.5 0 0 0 1 0V9.328a.5.5 0 0 0-1 0zm1.854-5.097a.5.5 0 0 0 0-.706l-.708-.708a.5.5 0 0 0-.707 0L8.646 5.94a.5.5 0 0 0 0 .707l.708.708a.5.5 0 0 0 .707 0zm-3 3a.5.5 0 0 0 0-.706l-.708-.708a.5.5 0 0 0-.707 0L.646 13.94a.5.5 0 0 0 0 .707l.708.708a.5.5 0 0 0 .707 0z"/></svg></span>Cowork 프롬프트 고급 기법<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">2번에서 소개한 6가지 형태(Executive Brief, Comparison Matrix 등) 중 하나를 <strong>프롬프트 첫머리에 지정</strong>하면 결과가 일관됩니다. 여기에 <strong>"Bootstrap 5 흰 배경에 ECharts로 수치를 차트화해줘"</strong>처럼 라이브러리·차트까지 함께 요청하면, 데이터가 살아 있는 시각적 결과물을 한 번에 받을 수 있습니다.</div>
  </details>
</div>

<hr/>

<h2 class="mc-section-title">다음 단계 — 이 결과물을 팀과 공유하려면</h2>

<p>여기까지 오셨다면 보기 좋은 HTML 결과물이 손에 있을 겁니다. 이제 이 결과물을 <strong>링크 한 줄</strong>로 동료나 고객에게 공유해 보세요. 별도 서버 없이, 브라우저만 있으면 됩니다.</p>

<div class="mc-card" style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; display:flex; flex-wrap:wrap; align-items:center; gap:1.1rem;">
  <span style="flex-shrink:0; color:#1e293b; display:inline-flex;"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8"/></svg></span>
  <div style="flex:1 1 280px; min-width:240px;">
    <div style="font-weight:800; font-size:1.05rem; color:#1e293b; margin-bottom:0.35rem;">내가 만든 HTML 결과물을 함께 공유하고 싶다면!</div>
    <div style="color:#475569; line-height:1.65;">GitHub 웹사이트에서 클릭 몇 번만 하면 공개 URL이 생깁니다. 비개발자도 따라 할 수 있는 가장 쉬운 방법을 정리해 두었습니다.</div>
  </div>
  <a href="https://ms.studydev.com/github/pages_publishing/" target="_blank" rel="noopener noreferrer" style="flex-shrink:0; display:inline-flex; align-items:center; gap:0.45rem; background:#1e293b; color:#ffffff; font-weight:700; padding:0.7rem 1.25rem; border-radius:10px; text-decoration:none; white-space:nowrap;">공유 가이드 보러 가기 →</a>
</div>

<hr/>

<h2 class="mc-section-title">자주 묻는 질문 (FAQ)</h2>

<p>M365 Copilot으로 HTML 결과물을 만들 때 가장 자주 나오는 질문을 정리했습니다.</p>

<div class="mc-acc-list">
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>M365 Copilot으로 HTML 문서를 어떻게 만드나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">Researcher Agent로 자료를 모은 뒤, 그 자료(Markdown 또는 Page)를 Cowork Agent에 첨부하고 원하는 형태의 HTML을 요청하면 됩니다. 카드·하이라이트·표·코드 블록까지 갖춘 HTML이 몇 분 안에 생성되며, <strong>CSS나 JavaScript를 직접 작성할 필요가 없습니다.</strong></div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>Markdown과 HTML은 각각 언제 쓰는 게 좋나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body"><strong>Markdown</strong>은 자료 수집·초안 작성·구조화 같은 '지식 표현'에 강하고, <strong>HTML</strong>은 카드·강조·표·인터랙션으로 '소비 경험(전달·발표·공유)'에 강합니다. 둘은 경쟁이 아니라 <strong>Markdown으로 모으고 HTML로 전달하는 릴레이</strong>로 함께 쓰는 것이 좋습니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>Cowork가 만든 HTML 파일은 어디에 저장되나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">로컬 파일 시스템의 <strong>OneDrive 동기화 폴더</strong>에 자동 저장됩니다. Windows 기준 경로는 <code>C:\Users\&lt;사용자명&gt;\Documents\Coworker\sessions\&lt;세션-ID&gt;\output\</code> 이며, 각 세션마다 고유 세션 ID 폴더가 생성되고 <strong>가장 최근 수정된 폴더</strong>가 마지막 작업 세션입니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>만든 HTML을 Word나 PowerPoint로 바꿀 수 있나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">네. <strong>같은 대화 안에서</strong> Word 또는 PowerPoint로 전환해 달라고 요청하면 됩니다. 제목 계층 구조와 표·이미지 캡션을 유지한 Word 문서, 디자인 일관성을 유지한 PowerPoint 슬라이드로 변환되어 세밀한 편집과 배포가 쉬워집니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>만든 HTML 결과물을 어떻게 공유하나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body"><strong>GitHub Pages</strong>를 이용하면 별도 서버 없이 브라우저에서 클릭 몇 번만으로 공개 URL을 만들 수 있습니다. 비개발자도 따라 할 수 있으며, 만든 링크 한 줄로 동료나 고객에게 바로 공유할 수 있습니다. 위 <strong>"공유 가이드 보러 가기"</strong>에서 자세한 방법을 확인하세요.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>어떤 형태의 HTML을 만들 수 있나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body"><strong>Executive Brief</strong>(보고·요약), <strong>Comparison Matrix</strong>(비교·판단), <strong>Annotated Technical Review</strong>(코드·기술 설명), <strong>One-page Proposal</strong>(고객 제안), <strong>Interactive Learning</strong>(학습·교육), <strong>Mini Web App</strong>(계산기·체크리스트 등 업무 도구) 6가지 형태가 대표적입니다. 프롬프트 첫머리에 형태를 지정하면 결과 품질이 올라갑니다.</div>
  </details>
</div>

<hr/>

<h2 class="mc-section-title">마무리</h2>

<div class="mc-callout mc-callout--dark">
  Markdown은 여전히 강력합니다 — 지식을 구조화하고 초안을 다듬는 데 이만한 도구가 없죠. 하지만 그 지식을 <strong>사람에게 전달</strong>하는 마지막 단계에서는 HTML이 압도적입니다. Karpathy의 통찰처럼, '보는 결과물'은 같은 내용을 더 빠르고 정확하게 전합니다. 이제 그 HTML을 직접 코딩할 필요가 없습니다. <strong>Researcher로 모으고, Cowork로 디자인하고, Word·PPT로 확장하세요.</strong> 당신의 지식이 가장 보기 좋은 형태로 세상에 나가는 길입니다.
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>참고 자료</strong></div>
  <ul>
    <li><a href="https://x.com/karpathy/status/2053872850101285137?s=20" target="_blank" rel="noopener noreferrer">Andrej Karpathy — Markdown vs HTML (X 인용)</a></li>
    <li><a href="https://learn.microsoft.com/ko-kr/copilot/researcher" target="_blank" rel="noopener noreferrer">Microsoft Learn — M365 Copilot Researcher 개요</a></li>
    <li><a href="https://cowork.microsoft.com/" target="_blank" rel="noopener noreferrer">Microsoft 365 Copilot Cowork</a></li>
    <li><a href="https://microsoft.github.io/mwkorea/monthlycopilot/CopilotUsefulNewFeatures/" target="_blank" rel="noopener noreferrer">Copilot의 유용한 새로운 기능 — ModernWork Korea</a></li>
    <li><a href="https://microsoft.github.io/mwkorea/monthlycopilot/CopilotCowork/" target="_blank" rel="noopener noreferrer">일의 흐름을 바꾸는 새로운 경험, Copilot Cowork — ModernWork Korea</a></li>
    <li><a href="https://microsoft.github.io/mwkorea/monthlycopilot/CopilotResearcherCouncilCritique/" target="_blank" rel="noopener noreferrer">이제 AI도 팀플하는 시대 — ModernWork Korea</a></li>
    <li><a href="https://microsoft.github.io/mwkorea/copilot/CopilotWave3/" target="_blank" rel="noopener noreferrer">Copilot Wave 3 상세 안내: Copilot Cowork, 멀티모델 인텔리전스, Agent 365 — ModernWork Korea</a></li>
  </ul>
</div>

</div>
