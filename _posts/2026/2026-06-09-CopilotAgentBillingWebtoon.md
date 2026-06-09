---
title: "웹툰으로 보는 코파일럿 에이전트 과금 체계"
date: 2026-06-09T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Agent
  - Billing
  - 과금
  - Webtoon
excerpt: "코파일럿 에이전트의 과금 체계를 14컷 웹툰으로 쉽게 풀어봤습니다. 좌우로 한 장씩 넘겨보는 코믹 뷰어로 감상하세요."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: false
classes: wide
author: 최치원
---

# 웹툰으로 보는 코파일럿 에이전트 과금 체계

코파일럿 에이전트의 과금 체계를 **14컷 웹툰**으로 정리했습니다. 아래 뷰어에서 **한 번에 한 장씩** 넘겨보세요. **화살표 버튼 · 키보드 ←/→ · 이미지 좌우 클릭 · 모바일 스와이프**로 페이지를 넘기고, **전체화면** 버튼으로 크게 볼 수 있습니다.

{% raw %}
<style>
.cv-viewer { margin: 1.6rem auto; max-width: 760px; background: #0f172a; border-radius: 16px; padding: 12px; box-shadow: 0 12px 32px rgba(15, 23, 42, 0.28); outline: none; -webkit-tap-highlight-color: transparent; user-select: none; }
.cv-stage { position: relative; width: 100%; height: min(80vh, 900px); background: #0b1220; border-radius: 10px; overflow: hidden; display: flex; align-items: center; justify-content: center; cursor: pointer; touch-action: pan-y; }
.cv-page { display: none; max-width: 100%; max-height: 100%; width: auto; height: auto; object-fit: contain; margin: 0 !important; padding: 0; border: 0; border-radius: 0; box-shadow: none !important; pointer-events: none; }
.cv-page.is-active { display: block; }
.cv-fs { position: absolute; top: 10px; right: 10px; z-index: 5; display: inline-flex; align-items: center; gap: 6px; height: 34px; padding: 0 12px; font-size: 0.82rem; font-weight: 600; color: #e2e8f0; background: rgba(15, 23, 42, 0.62); border: 1px solid rgba(148, 163, 184, 0.45); border-radius: 999px; cursor: pointer; backdrop-filter: blur(4px); }
.cv-fs:hover { background: rgba(30, 41, 59, 0.85); }
.cv-hint { position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); z-index: 4; padding: 4px 12px; font-size: 0.74rem; color: #cbd5e1; background: rgba(15, 23, 42, 0.55); border-radius: 999px; pointer-events: none; transition: opacity 0.4s ease; }
.cv-viewer.is-touched .cv-hint { opacity: 0; }
.cv-controls { display: flex; align-items: center; justify-content: center; gap: 16px; padding: 12px 4px 4px; }
.cv-btn { display: inline-flex; align-items: center; justify-content: center; width: 46px; height: 46px; font-size: 1.5rem; line-height: 1; color: #0f172a; background: #f8fafc; border: 0; border-radius: 50%; cursor: pointer; transition: transform 0.12s ease, background 0.2s ease; }
.cv-btn:hover:not([disabled]) { background: #e2e8f0; transform: translateY(-1px); }
.cv-btn:active:not([disabled]) { transform: translateY(0); }
.cv-btn[disabled] { opacity: 0.3; cursor: default; }
.cv-counter { min-width: 72px; text-align: center; font-weight: 700; font-size: 1rem; letter-spacing: 0.02em; color: #e2e8f0; font-variant-numeric: tabular-nums; }
.cv-viewer.is-fs { position: fixed; inset: 0; z-index: 9999; max-width: none; margin: 0; border-radius: 0; padding: 16px; display: flex; flex-direction: column; justify-content: center; background: rgba(2, 6, 23, 0.97); }
.cv-viewer.is-fs .cv-stage { flex: 1; height: auto; min-height: 0; background: transparent; }
.cv-viewer.is-fs .cv-controls { padding-top: 16px; }
@media (max-width: 600px) { .cv-stage { height: min(72vh, 720px); } .cv-btn { width: 42px; height: 42px; font-size: 1.35rem; } }
</style>
<div class="cv-viewer" id="cv-credit" tabindex="0" role="group" aria-roledescription="코믹 뷰어" aria-label="코파일럿 에이전트 과금 웹툰 뷰어">
  <div class="cv-stage">
    <img class="cv-page is-active" src="/mwkorea/assets/images/comic_credit/credit_v2_p01.png" alt="코파일럿 에이전트 과금 웹툰 1페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p02.png" alt="코파일럿 에이전트 과금 웹툰 2페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p03.png" alt="코파일럿 에이전트 과금 웹툰 3페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p04.png" alt="코파일럿 에이전트 과금 웹툰 4페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p05.png" alt="코파일럿 에이전트 과금 웹툰 5페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p06.png" alt="코파일럿 에이전트 과금 웹툰 6페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p07.png" alt="코파일럿 에이전트 과금 웹툰 7페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p08.png" alt="코파일럿 에이전트 과금 웹툰 8페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p09.png" alt="코파일럿 에이전트 과금 웹툰 9페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p10.png" alt="코파일럿 에이전트 과금 웹툰 10페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p11.png" alt="코파일럿 에이전트 과금 웹툰 11페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p12.png" alt="코파일럿 에이전트 과금 웹툰 12페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p13.png" alt="코파일럿 에이전트 과금 웹툰 13페이지" />
    <img class="cv-page" data-src="/mwkorea/assets/images/comic_credit/credit_v2_p14.png" alt="코파일럿 에이전트 과금 웹툰 14페이지" />
    <button type="button" class="cv-fs" aria-label="전체화면 전환" aria-pressed="false">전체화면</button>
    <span class="cv-hint" aria-hidden="true">좌우를 누르거나 넘겨서 보세요</span>
  </div>
  <div class="cv-controls">
    <button type="button" class="cv-btn cv-prev" aria-label="이전 페이지" disabled>&#8249;</button>
    <span class="cv-counter" aria-live="polite" aria-atomic="true">1 / 14</span>
    <button type="button" class="cv-btn cv-next" aria-label="다음 페이지">&#8250;</button>
  </div>
</div>
<script>
(function () {
  var viewer = document.getElementById('cv-credit');
  if (!viewer) { return; }
  var stage = viewer.querySelector('.cv-stage');
  var pages = Array.prototype.slice.call(viewer.querySelectorAll('.cv-page'));
  var counter = viewer.querySelector('.cv-counter');
  var prevBtn = viewer.querySelector('.cv-prev');
  var nextBtn = viewer.querySelector('.cv-next');
  var fsBtn = viewer.querySelector('.cv-fs');
  var total = pages.length;
  var lastIdx = total - 1;
  var index = 0;
  var moved = false;
  var startX = null;
  var startY = null;

  function load(i) {
    if (i < 0 || i > lastIdx) { return; }
    var img = pages[i];
    if (img && !img.getAttribute('src') && img.getAttribute('data-src')) {
      img.setAttribute('src', img.getAttribute('data-src'));
    }
  }

  function update() {
    pages.forEach(function (p, n) { p.classList.toggle('is-active', n === index); });
    counter.textContent = (index + 1) + ' / ' + total;
    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === lastIdx;
  }

  function go(i) {
    if (i < 0 || i > lastIdx) { return; }
    index = i;
    load(index);
    load(index - 1);
    load(index + 1);
    update();
  }

  function toggleFs() {
    var on = viewer.classList.toggle('is-fs');
    fsBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
    fsBtn.textContent = on ? '닫기' : '전체화면';
    document.body.style.overflow = on ? 'hidden' : '';
    if (on) { viewer.focus(); }
  }

  prevBtn.addEventListener('click', function (e) { e.stopPropagation(); go(index - 1); });
  nextBtn.addEventListener('click', function (e) { e.stopPropagation(); go(index + 1); });
  fsBtn.addEventListener('click', function (e) { e.stopPropagation(); toggleFs(); });

  stage.addEventListener('click', function (e) {
    if (moved) { moved = false; return; }
    var rect = stage.getBoundingClientRect();
    var x = e.clientX - rect.left;
    if (x < rect.width / 2) { go(index - 1); } else { go(index + 1); }
  });

  stage.addEventListener('touchstart', function (e) {
    viewer.classList.add('is-touched');
    startX = e.touches[0].clientX;
    startY = e.touches[0].clientY;
    moved = false;
  }, { passive: true });
  stage.addEventListener('touchmove', function (e) {
    if (startX === null) { return; }
    var dx = Math.abs(e.touches[0].clientX - startX);
    var dy = Math.abs(e.touches[0].clientY - startY);
    if (dx > 10 || dy > 10) { moved = true; }
  }, { passive: true });
  stage.addEventListener('touchend', function (e) {
    if (startX === null) { return; }
    var dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 40) {
      moved = true;
      if (dx < 0) { go(index + 1); } else { go(index - 1); }
    }
    startX = null;
    startY = null;
  });

  document.addEventListener('keydown', function (e) {
    var isFs = viewer.classList.contains('is-fs');
    var focused = viewer === document.activeElement || viewer.contains(document.activeElement);
    if (e.key === 'Escape' && isFs) { toggleFs(); return; }
    if (!isFs && !focused) { return; }
    if (e.key === 'ArrowLeft') { e.preventDefault(); go(index - 1); }
    else if (e.key === 'ArrowRight') { e.preventDefault(); go(index + 1); }
  });

  go(0);
})();
</script>
{% endraw %}
