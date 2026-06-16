---
title: "'내가 만든 HTML 결과물' 공유하기 by GitHub Pages"
date: 2026-06-09T00:00:00 KST
last_modified_at: 2026-06-09T00:00:00 KST
excerpt: "잘 만든 HTML 결과물도 내 PC 안에만 있으면 전달이 번거롭습니다. GitHub Pages를 쓰면 서버·비용·터미널 없이 브라우저 클릭 몇 번으로 공개 URL이 생깁니다. 저장소 만들기 → HTML 배포 → 결과 공유의 3단계 워크플로를 비개발자도 따라 할 수 있도록 정리했습니다."
description: "M365 Copilot Cowork로 만든 HTML 결과물을 GitHub Pages로 공유하는 방법. 저장소 생성·Pages 설정부터 HTML 작성·업로드, 공개 URL 공유까지 비개발자용 3단계 가이드를 단계별로 정리했습니다."
keywords: "GitHub Pages, HTML 공유, HTML 호스팅, 정적 사이트, 무료 호스팅, github.io, 공개 URL, 저장소 만들기, docs 폴더, M365 Copilot, Cowork, HTML 배포"
tags:
  - GitHub Pages
  - HTML
  - 공유
  - M365 Copilot
categories:
  - Copilot
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
  og_image: https://ms.studydev.com/github/pages_publishing/images/00_hero_infographic.png
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
      "headline": "'내가 만든 HTML 결과물' 공유하기 by GitHub Pages",
      "description": "M365 Copilot Cowork로 만든 HTML 결과물을 GitHub Pages로 공유하는 방법. 저장소 생성·Pages 설정부터 HTML 작성·업로드, 공개 URL 공유까지 비개발자용 3단계 가이드를 단계별로 정리했습니다.",
      "inLanguage": "ko-KR",
      "datePublished": "2026-06-09",
      "dateModified": "2026-06-09",
      "author": { "@type": "Person", "name": "김현수" },
      "publisher": { "@type": "Organization", "name": "Monthly Copilot Korea" },
      "mainEntityOfPage": { "@type": "WebPage", "@id": "{{ page.url | absolute_url }}" },
      "image": "https://ms.studydev.com/github/pages_publishing/images/00_hero_infographic.png",
      "keywords": "GitHub Pages, HTML 공유, HTML 호스팅, 정적 사이트, 무료 호스팅, github.io, 공개 URL, 저장소 만들기, docs 폴더",
      "articleSection": "Monthly Copilot"
    },
    {
      "@type": "HowTo",
      "name": "GitHub Pages로 HTML 결과물 공유하기 — 3단계 워크플로",
      "description": "GitHub 저장소를 만들고 Pages를 켠 뒤, HTML 파일을 작성·업로드해 공개 URL로 공유하는 3단계 절차입니다.",
      "inLanguage": "ko-KR",
      "totalTime": "PT10M",
      "step": [
        {
          "@type": "HowToStep",
          "position": 1,
          "name": "저장소 만들고 Pages 켜기",
          "text": "GitHub에 로그인해 New repository로 공개 저장소를 만들고, Settings → Pages에서 Source를 Deploy from a branch(main, /docs)로 지정해 저장합니다.",
          "url": "{{ page.url | absolute_url }}#3-1"
        },
        {
          "@type": "HowToStep",
          "position": 2,
          "name": "HTML 파일 직접 작성하고 배포 확인",
          "text": "저장소 Code 탭에서 docs/index.html을 만들어 간단한 HTML을 작성하고 커밋한 뒤, Pages의 'Your site is live' 메시지와 실제 페이지 출력을 확인합니다.",
          "url": "{{ page.url | absolute_url }}#3-2"
        },
        {
          "@type": "HowToStep",
          "position": 3,
          "name": "기존 HTML 파일 업로드하고 결과 공유",
          "text": "docs 폴더에 완성된 HTML 파일을 드래그 앤 드롭으로 업로드하고 커밋하면, 1~2분 후 공개 URL이 갱신되어 링크 한 줄로 공유할 수 있습니다.",
          "url": "{{ page.url | absolute_url }}#3-3"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "inLanguage": "ko-KR",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "GitHub Pages는 무료인가요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "공개(Public) 저장소에서는 무료로 사용할 수 있습니다. 별도 서버나 비용 없이 HTTPS까지 자동 적용됩니다. 단, 비공개(Private) 저장소에서 Pages를 쓰려면 Pro·Team·Enterprise 등 유료 플랜이 필요합니다."
          }
        },
        {
          "@type": "Question",
          "name": "HTML 파일은 어디에 두어야 하나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "docs 폴더 사용을 권장합니다. Settings → Pages에서 Source 폴더를 /docs로 설정하고, 파일 경로를 docs/index.html로 만들면 됩니다. 폴더에 접근하면 index.html이 자동으로 열립니다."
          }
        },
        {
          "@type": "Question",
          "name": "배포까지 얼마나 걸리나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "커밋한 뒤 실제 사이트에 반영되기까지 보통 수 초에서 수십 초, 길어도 1~2분 정도 걸립니다. 커밋 직후 페이지가 안 보이면 잠시 기다린 뒤 새로고침하세요."
          }
        },
        {
          "@type": "Question",
          "name": "페이지가 안 보이면 어떻게 하나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "세 가지를 확인하세요. (1) Pages Source 폴더 설정이 실제 업로드한 폴더와 같은지, (2) 파일 이름이 index.html인지(대소문자 주의), (3) 배포 완료 전일 수 있으니 1~2분 기다린 뒤 새로고침했는지 확인합니다."
          }
        },
        {
          "@type": "Question",
          "name": "만든 링크는 어떻게 공유하나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "배포된 URL은 https://(계정).github.io/(저장소)/ 형식입니다. 이 링크를 Teams·Outlook·카카오톡 등에 그대로 붙여 넣으면 동료나 고객이 바로 열어볼 수 있습니다."
          }
        },
        {
          "@type": "Question",
          "name": "동적 기능(DB·API)도 사용할 수 있나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "GitHub Pages는 정적(static) 호스팅 전용이라 데이터베이스나 API 서버 같은 동적 백엔드는 지원하지 않습니다. HTML·CSS·JavaScript로 동작하는 정적 결과물 공유에 적합합니다."
          }
        },
        {
          "@type": "Question",
          "name": "HTML을 특정 사용자에게만 보이도록 비밀번호로 보호하려면 어떻게 하나요?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "GitHub Pages는 공개 웹사이트라 자체적인 비밀번호 보호 기능이 없습니다. 접근을 제한하려면 같은 HTML을 Azure Static Web Apps로 배포하세요. GitHub·Microsoft Entra ID 로그인 기반의 인증은 모든 요금제에서 기본 제공되며, Standard 요금제를 쓰면 초대 기반 사용자 지정 역할(allowedRoles)·사용자 지정 인증 공급자·IP 제한까지 구성해 허용된 사용자만 본인 계정 자격 증명(비밀번호)으로 로그인해 HTML에 접근하도록 만들 수 있습니다. staticwebapp.config.json의 routes에서 보호할 경로에 allowedRoles를 지정하고, Azure Portal의 Role management에서 사용자를 초대해 역할을 부여합니다."
          }
        }
      ]
    }
  ]
}
</script>

<div class="mc-issue-strip">Monthly Copilot · July 2026 · 월간 코파일럿 7월호 · Share</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Share</div>
  <div class="mc-cover-title">'내가 만든 HTML 결과물' 공유하기 by GitHub Pages</div>
  <div class="mc-cover-subtitle">잘 다듬어진 HTML 파일이 있다고요? 저장소 만들고 → 올리고 → URL로 공유하면 끝!</div>
</div>

<div class="mc-card">
  <div class="mc-card-title"><strong>Article Summary</strong></div>
  <div>Cowork로 멋진 HTML 결과물을 만들었어도, 그 파일이 내 PC 안에만 있으면 전달이 번거롭습니다. <strong>GitHub Pages</strong>를 쓰면 서버·비용·터미널 없이 브라우저 클릭 몇 번으로 <strong>공개 URL</strong>이 생기고, HTTPS까지 자동 적용됩니다. 이 글은 ① 저장소 만들고 Pages 켜기 → ② HTML 파일 작성·배포 확인 → ③ 기존 HTML 업로드·공유의 <strong>3단계</strong>로, 비개발자도 따라 할 수 있도록 정리했습니다.</div>
</div>

<img src="https://ms.studydev.com/github/pages_publishing/images/00_hero_infographic.png" alt="Markdown의 한계 → HTML의 시각적 힘 → 공유의 번거로움 → GitHub Pages로 간단히 해결 — 4컷 인포그래픽" style="border:1px solid #d1d5db; border-radius:12px;" />

<hr/>

<h2 class="mc-section-title">1. 왜 GitHub Pages인가 — 공유의 마지막 한 걸음</h2>

<p>Markdown으로 지식을 모으고, Cowork로 <strong>'보는 결과물'</strong>인 HTML을 완성했습니다. 그런데 그 결과물이 로컬 폴더 안에만 있으면, 동료에게 보내려고 파일을 압축하고 메일에 첨부하고 "브라우저로 열어주세요"라고 설명해야 합니다. 공유의 마지막 단계가 의외로 가장 번거롭습니다.</p>

<p>이 지점을 <strong>GitHub Pages</strong>가 해결합니다. 정적 HTML 파일을 저장소에 올리면, GitHub가 이를 <strong>공개 웹사이트</strong>로 자동 게시합니다. 별도 서버를 빌릴 필요도, 결제 정보를 넣을 필요도, 터미널 명령을 외울 필요도 없습니다. 브라우저만 있으면 됩니다.</p>

<div class="mc-card mc-card--blue">
  <div class="mc-card-title"><strong>한 줄 요약</strong></div>
  <div style="color:#1f2937;">Markdown은 <strong>모으고</strong>, HTML은 <strong>보여주고</strong>, GitHub Pages는 <strong>전달</strong>합니다. 잘 만든 결과물도 공유되지 않으면 가치를 다 발휘하지 못합니다. <strong>URL 한 줄</strong>이 그 마지막 거리를 좁힙니다.</div>
</div>

<p style="margin:1.75rem 0 0.5rem;"><strong>GitHub Pages가 좋은 세 가지 이유</strong></p>

<div class="mc-table-wrap" style="margin-top:0.4rem;">
  <table>
  <tr>
    <th>특징</th>
    <th>의미</th>
    <th>장점</th>
  </tr>
  <tr>
    <td><strong>공개 저장소 무료</strong></td>
    <td>별도 서버·비용 없음</td>
    <td>결제 정보 없이 바로 시작</td>
  </tr>
  <tr>
    <td><strong>HTTPS 기본</strong></td>
    <td>인증서 자동 발급·갱신</td>
    <td>보안 경고 없이 안전하게 공유</td>
  </tr>
  <tr>
    <td><strong>1~2분이면 배포</strong></td>
    <td>저장 즉시 전 세계 공개</td>
    <td>커밋하면 곧바로 링크 갱신</td>
  </tr>
  </table>
</div>

<hr/>

<h2 class="mc-section-title">2. 한눈에 보는 흐름 — 내 파일이 URL이 되기까지</h2>

<p>내 PC의 HTML 파일이 어떻게 공개 URL로 바뀌는지, 전체 경로를 먼저 그림으로 살펴보겠습니다. 핵심은 <strong>"저장소에 올리면 GitHub가 알아서 웹사이트로 게시한다"</strong>는 것입니다.</p>

<style>
.page__content .monthlycopilot-page .mc-card.mc-arch img { display:inline-block; width:auto; margin:0; border:0; border-radius:0; box-shadow:none; vertical-align:middle; }
.page__content .monthlycopilot-page .mc-card.mc-arch svg { vertical-align:middle; }
</style>
<div class="mc-card mc-arch" style="text-align:center;">
  <div class="mc-card-title" style="text-align:left;"><strong>전체 파이프라인</strong></div>
  <div style="display:flex; flex-wrap:wrap; align-items:stretch; justify-content:center; gap:0.5rem; padding-top:0.4rem;">
    <div style="flex:1 1 150px; min-width:140px; max-width:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.55rem; background:#ffffff; border:1px solid #dbe4f0; border-radius:16px; padding:1.1rem 0.8rem;">
      <span style="color:#1d4ed8;"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/><path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/></svg></span>
      <div style="font-weight:700; color:#1d4ed8; line-height:1.4;">내 HTML 파일<br/><span style="font-size:0.82rem; color:#64748b;">index.html</span></div>
    </div>
    <div style="display:flex; align-items:center; color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/></svg></div>
    <div style="flex:1 1 150px; min-width:140px; max-width:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.55rem; background:#ffffff; border:1px solid #dbe4f0; border-radius:16px; padding:1.1rem 0.8rem;">
      <span style="color:#1e293b;"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8"/></svg></span>
      <div style="font-weight:700; color:#1d4ed8; line-height:1.4;">GitHub 저장소<br/><span style="font-size:0.82rem; color:#64748b;">main / docs/</span></div>
    </div>
    <div style="display:flex; align-items:center; color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/></svg></div>
    <div style="flex:1 1 150px; min-width:140px; max-width:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.55rem; background:linear-gradient(135deg,#1e3a8a 0%,#2563eb 100%); border:1px solid #1d4ed8; border-radius:16px; padding:1.1rem 0.8rem;">
      <span style="color:#ffffff;"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m7.5-6.923c-.67.204-1.335.82-1.887 1.855-.143.268-.276.56-.395.872.705.157 1.472.257 2.282.287zM4.249 3.539q.214-.577.481-1.078a7 7 0 0 1 .597-.933A7 7 0 0 0 3.051 3.05q.544.277 1.198.49zM3.509 7.5c.036-1.07.188-2.087.436-3.008a9 9 0 0 1-1.565-.667A6.96 6.96 0 0 0 1.018 7.5zm1.4-2.741a12.3 12.3 0 0 0-.4 2.741H7.5V5.091c-.91-.03-1.783-.145-2.591-.332zM8.5 5.09V7.5h2.99a12.3 12.3 0 0 0-.399-2.741c-.808.187-1.681.301-2.591.332zM4.51 8.5c.035.987.176 1.914.399 2.741A13.6 13.6 0 0 1 7.5 10.91V8.5zm3.99 0v2.409c.91.03 1.783.145 2.591.332.223-.827.364-1.754.399-2.741zm-3.282 3.696q.118.312.395.872c.552 1.035 1.218 1.65 1.887 1.855V11.91c-.81.03-1.577.13-2.282.287zm.11 2.276a7 7 0 0 1-.598-.933 9 9 0 0 1-.481-1.079 8.4 8.4 0 0 0-1.198.49 7 7 0 0 0 2.276 1.522zm-1.383-2.964A13.4 13.4 0 0 1 3.508 8.5h-2.49a6.96 6.96 0 0 0 1.362 3.675c.47-.258.995-.482 1.565-.667zm6.728 2.964a7 7 0 0 0 2.275-1.521 8.4 8.4 0 0 0-1.197-.49 9 9 0 0 1-.481 1.078 7 7 0 0 1-.597.933M8.5 11.909v3.014c.67-.204 1.335-.82 1.887-1.855q.276-.519.395-.872A12.6 12.6 0 0 0 8.5 11.91zm3.555-.401c.57.185 1.095.409 1.565.667A6.96 6.96 0 0 0 14.982 8.5h-2.49a13.4 13.4 0 0 1-.437 3.008M14.982 7.5a6.96 6.96 0 0 0-1.362-3.675c-.47.258-.995.482-1.565.667.248.92.4 1.938.437 3.008zM11.27 2.461q.266.502.482 1.078a8.4 8.4 0 0 0 1.196-.49 7 7 0 0 0-2.275-1.52c.218.283.418.597.597.932m-.488 1.343a8 8 0 0 0-.395-.872C9.835 1.897 9.17 1.282 8.5 1.077V4.09c.81-.03 1.577-.13 2.282-.287z"/></svg></span>
      <div style="font-weight:700; color:#ffffff; line-height:1.4;">GitHub Pages<br/><span style="font-size:0.82rem; color:#dbeafe;">*.github.io</span></div>
    </div>
    <div style="display:flex; align-items:center; color:#94a3b8;"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/></svg></div>
    <div style="flex:1 1 150px; min-width:140px; max-width:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.55rem; background:#ffffff; border:1px solid #dbe4f0; border-radius:16px; padding:1.1rem 0.8rem;">
      <span style="color:#1d4ed8;"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16"><path d="M7 14s-1 0-1-1 1-4 5-4 5 3 5 4-1 1-1 1zm4-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6m-5.784 6A2.24 2.24 0 0 1 5 13c0-1.355.68-2.75 1.936-3.72A6.3 6.3 0 0 0 5 9c-4 0-5 3-5 4s1 1 1 1z"/><path d="M4.5 8a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5"/></svg></span>
      <div style="font-weight:700; color:#1d4ed8; line-height:1.4;">동료 · 고객<br/><span style="font-size:0.82rem; color:#64748b;">링크 한 줄로 공유</span></div>
    </div>
  </div>
  <div class="mc-card-note">내 <strong>HTML 파일</strong>을 <strong>GitHub 저장소</strong>(main/docs)에 올리면, <strong>GitHub Pages</strong>가 자동으로 <code>*.github.io</code> 주소에 게시합니다. 생성된 URL을 <strong>동료·고객</strong>에게 링크 한 줄로 공유하면 끝입니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">3. 핵심 3단계 — 비개발자도 OK</h2>

<p>이제 실제로 따라 해보겠습니다. <strong>3-1부터 3-3까지</strong> 세 단계만 거치면, 내 HTML 결과물이 공개 URL로 바뀝니다. 아래 표로 전체 흐름을 먼저 본 뒤 차례로 진행하세요.</p>

<div class="mc-table-wrap">
  <table>
    <tr>
      <th>단계</th>
      <th>작업</th>
      <th>내용</th>
    </tr>
    <tr>
      <td><strong>1단계</strong></td>
      <td>저장소 · Pages 설정</td>
      <td>GitHub에서 <strong>공개 저장소</strong>를 만들고 Settings → Pages에서 게시 소스를 지정</td>
    </tr>
    <tr>
      <td><strong>2단계</strong></td>
      <td>HTML 작성 · 배포 확인</td>
      <td><strong>docs/index.html</strong>을 만들어 커밋하고, 배포된 페이지가 열리는지 확인</td>
    </tr>
    <tr>
      <td><strong>3단계</strong></td>
      <td>HTML 업로드 · 공유</td>
      <td>완성된 HTML 파일을 <strong>드래그 앤 드롭</strong>으로 올리고, 공개 URL을 공유</td>
    </tr>
  </table>
</div>

<div class="mc-card">
  <div class="mc-card-title"><strong>핵심 원리</strong></div>
  <div>GitHub Pages는 저장소의 특정 폴더(<strong>/docs</strong> 권장)를 <strong>웹 루트</strong>로 삼아 게시합니다. 그래서 <strong>폴더 이름</strong>과 <strong>파일 이름(index.html)</strong>만 규칙에 맞추면, 나머지는 GitHub가 자동으로 처리합니다.</div>
</div>

<h3 id="3-1">3-1. 1단계 — 저장소 만들고 Pages 켜기</h3>

<p>GitHub에 로그인한 뒤, 브라우저에서 아래 순서대로 클릭만 하면 됩니다. <a href="https://github.com/signup" target="_blank" rel="noopener noreferrer">GitHub 계정</a>이 없다면 먼저 무료로 가입하세요.</p>

<div class="mc-card">
  <div class="mc-card-title"><strong>작업 순서</strong></div>
  <ol>
    <li>우측 상단 <strong>＋ → New repository</strong> 클릭</li>
    <li>저장소 이름 입력(예: <code>home</code>), <strong>Public</strong> 선택, <strong>Add a README</strong> 체크 후 <strong>Create repository</strong></li>
    <li>저장소 화면에서 <strong>Settings → Pages</strong> 이동</li>
    <li>Source: <strong>Deploy from a branch</strong> → Branch는 <code>main</code>, 폴더는 <code>/(root)</code> 또는 <code>/docs</code> 선택 후 <strong>Save</strong> <em>(이 가이드는 /docs 기준)</em></li>
  </ol>
</div>

<div class="mc-card mc-card--blue" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>완료 확인 · /docs 폴더 추천</strong></div>
  <div style="color:#1f2937;">Settings → Pages 상단에 <strong>"Your site is live at …"</strong> 메시지가 뜨면 성공입니다. URL은 <code>https://(계정).github.io/(저장소)/</code> 형식입니다. 폴더를 <strong>/docs</strong>로 두면 웹사이트 파일과 다른 자료를 분리할 수 있어 관리가 편합니다. <a href="https://namu.wiki/w/Jekyll" target="_blank" rel="noopener noreferrer">Jekyll</a> 같은 정적 사이트 빌드 도구를 쓰지 않을 거라면, 해당 폴더에 <code>.nojekyll</code> 빈 파일을 추가하면 불필요한 빌드를 건너뜁니다.</div>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>실제 작업 화면 — 전체 6단계</strong></div>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/01_repo_create.png" alt="우측 상단 + 버튼에서 New repository 클릭" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 1</strong> · 우측 상단 ＋ → New repository 클릭</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/02_repo_init.png" alt="저장소 이름 입력, Public 선택, Add README 체크" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 2</strong> · 저장소 이름 입력 · Public 선택 · Add a README 체크 후 생성</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/03_repo_setting.png" alt="Settings → Pages 이동" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 3</strong> · 저장소 화면에서 Settings → Pages로 이동</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/04_repo_setting_branch.png" alt="Branch를 main으로 선택" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 4</strong> · Source: Deploy from a branch → Branch를 main으로 선택</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/05_repo_setting_folder.png" alt="폴더를 /docs로 선택" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 5</strong> · 게시 폴더를 /docs로 선택</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/06_repo_setting_save.png" alt="Save 버튼 클릭 후 Pages 활성화 확인" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 6</strong> · Save 클릭 후 Pages 활성화 확인</figcaption>
  </figure>
</div>

<h3 id="3-2">3-2. 2단계 — HTML 파일 직접 작성하고 배포 확인</h3>

<p>저장소에서 바로 HTML 파일을 만들어, Pages가 정상 동작하는지 먼저 확인합니다. 간단한 한 줄짜리 HTML이면 충분합니다.</p>

<div class="mc-card">
  <div class="mc-card-title"><strong>작업 순서</strong></div>
  <ol>
    <li>저장소 <strong>Code 탭</strong>에서 <strong>Add file → Create new file</strong> 클릭</li>
    <li>파일 경로에 <code>docs/index.html</code> 입력 후 간단한 HTML 코드 작성</li>
    <li>하단 <strong>Commit changes</strong> 버튼 클릭</li>
    <li><strong>Settings → Pages</strong>에서 "Your site is live" 메시지 확인 → <strong>Visit site</strong></li>
    <li>브라우저에서 배포된 페이지가 정상 출력되는지 확인</li>
  </ol>
</div>

<div class="mc-card mc-arch" style="margin-top:1.75rem; background:#0f172a; border-color:#1e293b; padding:0; overflow:hidden;">
  <div style="display:flex; align-items:center; padding:0.55rem 0.9rem; background:#1e293b; border-bottom:1px solid #334155;">
    <span style="display:inline-flex; align-items:center; gap:0.4rem; font-size:0.72rem; font-weight:800; letter-spacing:0.08em; color:#34d399;"><svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="currentColor" viewBox="0 0 16 16"><path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/></svg>docs/index.html</span>
  </div>
  <pre style="margin:0; background:#0f172a; color:#e2e8f0; padding:1rem 1.1rem; overflow-x:auto; font-size:0.88rem; line-height:1.7;">&lt;!doctype html&gt;
&lt;html lang="ko"&gt;
  &lt;head&gt;&lt;meta charset="utf-8" /&gt;&lt;title&gt;<span style="color:#fbbf24;">My First Page</span>&lt;/title&gt;&lt;/head&gt;
  &lt;body&gt;&lt;h1&gt;<span style="color:#22d3ee;">배포 성공! 🎉</span>&lt;/h1&gt;&lt;/body&gt;
&lt;/html&gt;</pre>
</div>

<div class="mc-card mc-card--blue" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>파일 이름은 index.html · 배포는 잠시 기다리기</strong></div>
  <div style="color:#1f2937;">폴더에 접근하면 자동으로 <code>index.html</code>이 열립니다. 1단계에서 Pages Source를 <strong>/docs</strong>로 설정했다면, 파일 경로도 반드시 <code>docs/index.html</code>로 만들어야 합니다. 파일을 만들거나 업로드한 뒤 실제 사이트에 반영되기까지 <strong>수 초~수십 초</strong>가 걸리니, 커밋 직후 안 보이면 잠시 기다린 뒤 새로고침하세요.</div>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>실제 작업 화면 — 전체 5단계</strong></div>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/07_repo_code_create.png" alt="Add file 메뉴에서 Create new file 또는 Upload files 선택" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 1</strong> · 저장소 Code 탭에서 Add file → Create new file 클릭</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/08_repo_code_index.png" alt="docs/index.html 파일 경로 입력 및 HTML 코드 작성" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 2</strong> · 파일 경로에 docs/index.html 입력 후 HTML 코드 작성</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/09_repo_code_commit.png" alt="Commit changes 다이얼로그에서 커밋 메시지 입력 후 커밋" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 3</strong> · Commit changes에서 커밋 메시지 입력 후 커밋</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/10_repo_pages_visit.png" alt="Settings → Pages에서 Your site is live 확인 및 Visit site 클릭" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 4</strong> · Settings → Pages에서 "Your site is live" 확인 후 Visit site</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/11_repo_pages_verify.png" alt="브라우저에서 배포된 페이지 확인" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 5</strong> · 브라우저에서 배포된 페이지가 정상 출력되는지 확인</figcaption>
  </figure>
</div>

<h3 id="3-3">3-3. 3단계 — 기존 HTML 파일 업로드하고 결과 공유</h3>

<p>이미 완성된 HTML 파일(예: Cowork로 만든 웹 문서·슬라이드)이 있다면, <strong>드래그 앤 드롭</strong>으로 저장소에 올리고 바로 공유할 수 있습니다.</p>

<div class="mc-card">
  <div class="mc-card-title"><strong>작업 순서</strong></div>
  <ol>
    <li><code>docs/</code> 폴더로 이동 → <strong>Add file → Upload files</strong> 클릭</li>
    <li>HTML 파일과 필요한 리소스를 화면으로 <strong>드래그 앤 드롭</strong></li>
    <li>커밋 메시지 입력 후 <strong>Commit changes</strong> 클릭</li>
    <li>1~2분 후 배포된 URL로 접속해 결과 확인</li>
  </ol>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>공유 · 수정 요령</strong></div>
  <ul>
    <li>잘 보이면 그 링크를 <strong>Teams · Outlook · 카카오톡</strong> 등에 그대로 붙여 공유하면 끝.</li>
    <li>수정이 필요할 땐 저장소에서 파일을 열어 <strong>연필 아이콘</strong>으로 편집 후 Commit — 즉시 반영됩니다.</li>
  </ul>
</div>

<div class="mc-card mc-card--blue" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>안 보일 때 체크 3가지</strong></div>
  <ul style="color:#1f2937;">
    <li>Pages Source 폴더 설정이 실제 업로드한 폴더와 같은가</li>
    <li>파일 이름이 <code>index.html</code>인가 (대소문자 주의)</li>
    <li>배포 완료 전일 수 있음 — 1~2분 기다린 뒤 새로고침</li>
  </ul>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>직접 확인해 보세요 — 데모</strong></div>
  <div>아래는 위 가이드대로 실제 배포한 테스트 사이트입니다.</div>
  <ul>
    <li>직접 만든 HTML 결과물: <a href="https://studydev.github.io/home" target="_blank" rel="noopener noreferrer">https://studydev.github.io/home</a></li>
    <li>업로드한 웹 문서형 HTML: <a href="https://studydev.github.io/home/ai_doc.html" target="_blank" rel="noopener noreferrer">https://studydev.github.io/home/ai_doc.html</a></li>
    <li>업로드한 슬라이드형 HTML: <a href="https://studydev.github.io/home/ai_slide.html" target="_blank" rel="noopener noreferrer">https://studydev.github.io/home/ai_slide.html</a></li>
  </ul>
  <div class="mc-card-note">소스 코드: <a href="https://github.com/studydev/home" target="_blank" rel="noopener noreferrer">github.com/studydev/home</a></div>
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>실제 작업 화면 — 전체 4단계</strong></div>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/12_repo_upload_html.png" alt="docs 폴더에서 Add file → Upload files로 HTML 파일 업로드" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 1</strong> · docs 폴더에서 Add file → Upload files 클릭</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/13_repo_upload_commit.png" alt="드래그 앤 드롭으로 파일 추가 후 Commit changes 클릭" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 2</strong> · 드래그 앤 드롭으로 파일 추가 후 Commit changes 클릭</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/14_page_check_ai_doc.png" alt="배포된 웹 문서형 HTML 페이지 확인" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 3</strong> · 배포된 웹 문서형 HTML 페이지 확인</figcaption>
  </figure>
  <figure>
    <img src="https://ms.studydev.com/github/pages_publishing/images/15_page_check_ai_slide.png" alt="배포된 슬라이드형 HTML 페이지 확인" style="border:1px solid #d1d5db; border-radius:12px;" />
    <figcaption class="mc-card-note"><strong>STEP 4</strong> · 배포된 슬라이드형 HTML 페이지 확인</figcaption>
  </figure>
</div>

<hr/>

<h2 class="mc-section-title">4. 실습으로 더 깊이 익히기</h2>

<p>GitHub Pages의 기본 개념을 먼저 이해하고, 실습으로 직접 따라 해 보세요. <strong>이론 → 실습</strong> 순서로 진행하면 더 효과적입니다.</p>

<div class="mc-card" style="display:flex; flex-wrap:wrap; gap:1rem;">
  <a href="https://github-skills.studydev.com/learn/github-pages.html#/t-intro" target="_blank" rel="noopener noreferrer" style="flex:1 1 240px; min-width:220px; text-decoration:none; background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:1rem 1.1rem; color:#1e293b;">
    <div style="font-size:0.75rem; font-weight:800; color:#2563eb; letter-spacing:0.04em;">이론</div>
    <div style="font-weight:800; margin:0.3rem 0;">GitHub Pages 기본 이론</div>
    <div style="font-size:0.88rem; color:#475569;">Pages의 동작 원리·구조·핵심 개념을 빠르게 파악하는 이론 문서</div>
  </a>
  <a href="https://github.com/skills-kr/github-pages" target="_blank" rel="noopener noreferrer" style="flex:1 1 240px; min-width:220px; text-decoration:none; background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:1rem 1.1rem; color:#1e293b;">
    <div style="font-size:0.75rem; font-weight:800; color:#16a34a; letter-spacing:0.04em;">실습</div>
    <div style="font-weight:800; margin:0.3rem 0;">GitHub Pages 핸즈온 (한국어)</div>
    <div style="font-size:0.88rem; color:#475569;">내 저장소에서 단계별 이슈를 따라가며 직접 배포해 보는 공식 실습</div>
  </a>
</div>

<div class="mc-card mc-card--blue" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>추천 학습 순서</strong></div>
  <ol style="color:#1f2937;">
    <li>먼저 <strong>이론 문서</strong>로 Pages의 동작 방식과 개념을 파악</li>
    <li>이어서 <strong>핸즈온 실습</strong>으로 내 저장소에 직접 배포하며 체험</li>
  </ol>
</div>

<hr/>

<h2 class="mc-section-title">5. 고급 · 개발자용 (선택)</h2>

<p>아래 항목은 <strong>필요한 경우에만</strong> 펼쳐 보세요. 기본 공유에는 필요 없습니다.</p>

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
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1zm13 2.383-4.708 2.825L15 11.105zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741M1 11.105l4.708-2.897L1 5.383z"/></svg></span>커스텀 도메인(docs.example.com) 연결<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body"><code>github.io</code> 기본 주소 대신 회사·개인 도메인을 쓰고 싶다면, 저장소 Settings → Pages의 <strong>Custom domain</strong>에 도메인을 입력하고, DNS 공급자에서 <strong>CNAME</strong>(서브도메인) 또는 <strong>A 레코드</strong>(루트 도메인)를 GitHub Pages로 가리키게 설정합니다. 설정 후 <strong>Enforce HTTPS</strong>를 켜면 인증서가 자동 적용됩니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M4.177 7.823A4.5 4.5 0 1 1 8 14.5a4.47 4.47 0 0 1-1.653-.316.5.5 0 1 1 .371-.928A3.5 3.5 0 1 0 4.5 9.5a.5.5 0 0 1-1 0V8.207l-.146.147a.5.5 0 1 1-.708-.708l1-1a.5.5 0 0 1 .708 0l1 1a.5.5 0 1 1-.708.708z"/><path d="M4.5 1.5a.5.5 0 0 0-.5.5v4.5a.5.5 0 0 1-1 0V2a1.5 1.5 0 0 1 1.5-1.5h7A1.5 1.5 0 0 1 13 2v12a1.5 1.5 0 0 1-1.5 1.5h-7A1.5 1.5 0 0 1 3 14v-1a.5.5 0 0 1 1 0v1a.5.5 0 0 0 .5.5h7a.5.5 0 0 0 .5-.5V2a.5.5 0 0 0-.5-.5z"/></svg></span>Git CLI로 로컬에서 작업하고 push로 배포<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">파일이 많거나 자주 수정한다면 로컬에서 작업하는 편이 빠릅니다. <code>git clone</code>으로 저장소를 받고, 파일을 수정한 뒤 <code>git add .</code> → <code>git commit -m "메시지"</code> → <code>git push</code>로 올리면 됩니다. push할 때마다 Pages가 자동 재배포되어, 브라우저 업로드보다 반복 작업이 수월합니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M2.5 12a.5.5 0 1 0 0 1 .5.5 0 0 0 0-1m2-.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5M2.5 7a.5.5 0 1 0 0 1 .5.5 0 0 0 0-1M5 7.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 0 1h-8a.5.5 0 0 1-.5-.5M2.5 2a.5.5 0 1 0 0 1 .5.5 0 0 0 0-1M5 2.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 0 1h-8a.5.5 0 0 1-.5-.5"/></svg></span>HTML이 많아졌을 때 — 네비게이션 자동 생성<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">공유할 HTML이 여러 개로 늘어나면 <code>index.html</code>을 <strong>목록(허브) 페이지</strong>로 만들어 각 결과물로 가는 링크를 모아두면 편합니다. 파일이 더 많아지면 <strong>Jekyll</strong> 같은 정적 사이트 생성기를 붙여 사이드바·목차를 자동 생성할 수도 있습니다. 다만 단순 공유 단계에서는 굳이 필요하지 않습니다.</div>
  </details>
</div>

<hr/>

<h2 class="mc-section-title">6. 꼭 알아둘 제한 사항</h2>

<p>GitHub Pages는 <strong>비상업적 · 정적 용도</strong>의 무료 서비스입니다. 아래 한도를 넘기지 않는 선에서 자유롭게 쓸 수 있습니다.</p>

<div class="mc-table-wrap">
  <table>
    <tr>
      <th>항목</th>
      <th>한도 · 정책</th>
    </tr>
    <tr>
      <td>저장소 / 게시 사이트 크기</td>
      <td>각 <strong>1 GB</strong> 권장</td>
    </tr>
    <tr>
      <td>월 대역폭</td>
      <td><strong>100 GB</strong> (soft limit)</td>
    </tr>
    <tr>
      <td>빌드 횟수</td>
      <td>시간당 <strong>10회</strong> (custom Actions 사용 시 미적용)</td>
    </tr>
    <tr>
      <td>배포 타임아웃</td>
      <td><strong>10분</strong> 초과 시 자동 중단</td>
    </tr>
    <tr>
      <td>상업 · 전자상거래 · SaaS 용도</td>
      <td><strong>사용 금지</strong></td>
    </tr>
  </table>
</div>

<div class="mc-card mc-card--blue" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>참고</strong></div>
  <div style="color:#1f2937;">GitHub Free 플랜은 <strong>공개 저장소</strong>에서만 Pages를 무료로 제공합니다. 비공개(Private) 저장소에 쓰려면 Pro·Team·Enterprise 플랜이 필요합니다. 또한 <strong>동적 백엔드(DB·API 서버)</strong>는 지원하지 않습니다. 자세한 내용은 <a href="https://docs.github.com/ko/pages/getting-started-with-github-pages/github-pages-limits" target="_blank" rel="noopener noreferrer">GitHub Pages 제한 문서</a>를 확인하세요.</div>
</div>

<hr/>

<h2 class="mc-section-title">자주 묻는 질문 (FAQ)</h2>

<p>GitHub Pages로 HTML을 공유할 때 가장 자주 나오는 질문을 정리했습니다.</p>

<div class="mc-acc-list">
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>GitHub Pages는 무료인가요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body"><strong>공개(Public) 저장소</strong>에서는 무료로 사용할 수 있고, 별도 서버나 비용 없이 HTTPS까지 자동 적용됩니다. 단, <strong>비공개(Private)</strong> 저장소에서 Pages를 쓰려면 Pro·Team·Enterprise 등 유료 플랜이 필요합니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>HTML 파일은 어디에 두어야 하나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body"><strong>docs 폴더</strong> 사용을 권장합니다. Settings → Pages에서 Source 폴더를 <code>/docs</code>로 설정하고, 파일 경로를 <code>docs/index.html</code>로 만들면 됩니다. 폴더에 접근하면 <code>index.html</code>이 자동으로 열립니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>배포까지 얼마나 걸리나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">커밋한 뒤 실제 사이트에 반영되기까지 보통 <strong>수 초~수십 초</strong>, 길어도 1~2분 정도 걸립니다. 커밋 직후 페이지가 안 보이면 잠시 기다린 뒤 새로고침하세요.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>페이지가 안 보이면 어떻게 하나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">세 가지를 확인하세요. (1) <strong>Pages Source 폴더</strong> 설정이 실제 업로드한 폴더와 같은지, (2) 파일 이름이 <code>index.html</code>인지(대소문자 주의), (3) 배포 완료 전일 수 있으니 1~2분 기다린 뒤 새로고침했는지 확인합니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>만든 링크는 어떻게 공유하나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">배포된 URL은 <code>https://(계정).github.io/(저장소)/</code> 형식입니다. 이 링크를 <strong>Teams·Outlook·카카오톡</strong> 등에 그대로 붙여 넣으면 동료나 고객이 바로 열어볼 수 있습니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/></svg></span>동적 기능(DB·API)도 사용할 수 있나요?<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">GitHub Pages는 <strong>정적(static) 호스팅 전용</strong>이라 데이터베이스나 API 서버 같은 동적 백엔드는 지원하지 않습니다. HTML·CSS·JavaScript로 동작하는 정적 결과물 공유에 적합합니다.</div>
  </details>
  <details class="mc-acc">
    <summary><span class="mc-acc-ico"><svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" viewBox="0 0 16 16"><path d="M5.338 1.59a61 61 0 0 0-2.837.856.48.48 0 0 0-.328.39c-.554 4.157.726 7.19 2.253 9.188a10.7 10.7 0 0 0 2.287 2.233c.346.244.652.42.893.533q.18.085.293.118a1 1 0 0 0 .101.025 1 1 0 0 0 .1-.025q.114-.034.294-.118c.24-.113.547-.29.893-.533a10.7 10.7 0 0 0 2.287-2.233c1.527-1.997 2.807-5.031 2.253-9.188a.48.48 0 0 0-.328-.39c-.651-.213-1.75-.56-2.837-.855C9.552 1.29 8.531 1.067 8 1.067c-.53 0-1.552.223-2.662.524zM5.072.56C6.157.265 7.31 0 8 0s1.843.265 2.928.56c1.11.3 2.229.655 2.887.87a1.54 1.54 0 0 1 1.044 1.262c.596 4.477-.787 7.795-2.465 9.99a11.8 11.8 0 0 1-2.517 2.453 7 7 0 0 1-1.048.625c-.28.132-.581.24-.829.24s-.548-.108-.829-.24a7 7 0 0 1-1.048-.625 11.8 11.8 0 0 1-2.517-2.453C1.42 10.235.038 6.917.634 2.44A1.54 1.54 0 0 1 1.678 1.18C2.336.965 3.455.61 4.565.31z"/><path d="M9.5 6.5a1.5 1.5 0 0 1-1 1.415l.385 1.99a.5.5 0 0 1-.491.595h-.788a.5.5 0 0 1-.49-.595l.384-1.99a1.5 1.5 0 1 1 2-1.415z"/></svg></span>HTML을 특정 사용자에게만 허용하고 싶다면? (비밀번호 보호)<span class="mc-acc-chevron"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/></svg></span></summary>
    <div class="mc-acc-body">GitHub Pages는 <strong>공개 웹사이트</strong>라 자체적인 비밀번호 보호 기능이 없습니다. 특정 사용자에게만 공개하려면 같은 HTML을 <strong><a href="https://learn.microsoft.com/ko-kr/azure/static-web-apps/overview" target="_blank" rel="noopener noreferrer">Azure Static Web Apps</a></strong>로 배포하세요. GitHub·Microsoft Entra ID 로그인 기반 인증은 <strong>모든 요금제</strong>에서 기본 제공되고, <strong>Standard 요금제(SKU)</strong>에서는 다음이 추가됩니다.
      <ul style="margin:0.6rem 0 0.3rem;">
        <li><strong>초대 기반 사용자 지정 역할</strong> — Azure Portal의 Role management에서 허용할 사용자만 초대해 역할을 부여</li>
        <li><strong>경로별 접근 제어</strong> — <code>staticwebapp.config.json</code>의 <code>routes</code>에서 보호할 경로에 <code>allowedRoles</code>를 지정</li>
        <li><strong>사용자 지정 인증 공급자·IP 제한</strong> — 특정 Entra ID 테넌트로 제한하거나 허용 IP 대역만 접속 허용</li>
      </ul>
      이렇게 하면 허용된 사용자만 <strong>본인 계정 자격 증명(비밀번호)</strong>으로 로그인해야 HTML을 볼 수 있습니다. 단, GitHub Pages처럼 하나의 공통 암호를 공유하는 방식이 아니라, <strong>사용자별 신원 기반</strong> 접근 제어입니다. 자세한 설정은 <a href="https://learn.microsoft.com/ko-kr/azure/static-web-apps/authentication-authorization" target="_blank" rel="noopener noreferrer">인증·권한 부여 문서</a>를 참고하세요.</div>
  </details>
</div>

<hr/>

<h2 class="mc-section-title">마무리</h2>

<div class="mc-callout mc-callout--dark">
  좋은 결과물을 만드는 일과 그것을 <strong>전달하는 일</strong>은 다른 문제입니다. 아무리 멋진 HTML도 내 PC 폴더에 머물러 있으면, 그 가치를 다 보여주지 못합니다. GitHub Pages는 그 마지막 거리를 <strong>URL 한 줄</strong>로 좁혀줍니다. <strong>저장소 만들고, 올리고, 링크로 공유하세요.</strong> 서버도, 비용도, 터미널도 필요 없습니다. 당신의 결과물이 가장 쉬운 방법으로 세상과 만나는 길입니다.
</div>

<div class="mc-card" style="margin-top:1.75rem;">
  <div class="mc-card-title"><strong>참고 자료</strong></div>
  <ul>
    <li><a href="https://github-skills.studydev.com/learn/github-pages.html#/t-intro" target="_blank" rel="noopener noreferrer">GitHub Pages 기본 이론 — 동작 원리·구조·핵심 개념</a></li>
    <li><a href="https://github.com/skills-kr/github-pages" target="_blank" rel="noopener noreferrer">skills-kr/github-pages — 공식 한국어 핸즈온 실습</a></li>
    <li><a href="https://docs.github.com/ko/pages/getting-started-with-github-pages/creating-a-github-pages-site" target="_blank" rel="noopener noreferrer">GitHub Pages 사이트 만들기 (공식 문서)</a></li>
    <li><a href="https://docs.github.com/ko/pages/getting-started-with-github-pages/github-pages-limits" target="_blank" rel="noopener noreferrer">GitHub Pages 제한 사항 (공식 문서)</a></li>
  </ul>
</div>

</div>
