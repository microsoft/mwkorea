---
title: "SharePoint Copilot, 이제 고칠 부분을 직접 선택하고 요청하세요"
date: 2026-09-25T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - SharePoint
  - PageAuthoring
excerpt: "SharePoint 페이지에서 섹션이나 웹 파트를 먼저 선택한 뒤 Copilot에 수정을 요청할 수 있습니다. 선택 범위를 명확히 전달하는 새로운 편집 방식과 라이선스 조건을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# SharePoint Copilot, 이제 고칠 부분을 직접 선택하고 요청하세요

SharePoint 페이지를 편집하면서 “이 부분만 바꿔 줘”라고 요청했는데, Copilot이 어느 부분을 뜻하는지 정확히 알지 못한다면 불편하겠죠. MC1478958은 이 맥락 전달을 더 직접적으로 만드는 페이지 작성 기능을 소개합니다.

이제 작성자는 **페이지 캔버스의 특정 섹션이나 개별 웹 파트를 선택한 뒤 Copilot에 프롬프트를 보낼 수 있습니다.** 페이지 전체를 설명하는 대신 수정 대상부터 지정하는 방식입니다.

---

## 달라진 편집 흐름

1. SharePoint 페이지를 Copilot으로 편집하는 상황에서 변경할 캔버스 요소를 선택합니다.
2. Copilot 채팅 입력 상자 위에 표시되는 선택 표시를 확인합니다.
3. 선택한 부분에 원하는 변경을 자연어로 요청합니다.

![SharePoint 페이지에서 선택한 요소를 Copilot 편집 맥락으로 전달하는 화면](/mwkorea/assets/images/2026-09-25-SharePointCopilotCanvasSelection/image1.png)

**섹션 전체와 개별 웹 파트 모두 선택 대상**입니다. Copilot은 선택된 요소를 요청한 변경의 맥락으로 사용합니다. 원문은 이 기능이 모든 결과의 정확성을 보장하거나 다른 요소의 변경 가능성을 완전히 차단한다고 설명하지는 않습니다.

## 아무것도 선택하지 않으면 어떻게 되나요?

기존 방식도 유지됩니다. 캔버스 요소를 선택하지 않은 경우, Copilot은 프롬프트를 기반으로 페이지에서 변경하기에 가장 적절한 영역을 판단합니다.

따라서 페이지 전반에 대한 요청과 특정 부분에 대한 요청을 구분해 사용할 수 있습니다. 예를 들어 특정 안내 문구를 다듬고 싶다면 해당 웹 파트를 먼저 선택하는 것이 대상 전달에 도움이 됩니다. 이 예시는 기능을 업무에 적용하는 방법이며 원문의 공식 데모 프롬프트는 아닙니다.

## 누가 사용할 수 있나요?

대상은 **Microsoft 365 Copilot 라이선스가 있는 SharePoint 페이지 작성자**입니다. 서비스는 SharePoint Online과 Microsoft 365 Copilot이며, 원문은 Worldwide·GCC·GCC High·DoD에서 **일반 공급(GA), 현재 사용 가능** 상태로 안내합니다.

관리자가 별도로 수행해야 할 작업은 없다고 명시되어 있습니다. 다만 페이지 작성 업무에 적용할 때는 해당 사용자의 라이선스와 실제 편집 화면을 확인하는 것이 좋습니다.

## 팀에 공유할 작은 작성 원칙

요청 전에 대상을 선택하고, 요청 후에는 변경 결과를 검토하세요. 부서 포털·공지·업무 안내처럼 여러 종류의 콘텐츠가 한 페이지에 모인 경우, “무엇을 바꿀지”와 “어떻게 바꿀지”를 분리해 전달하는 습관이 유용합니다.

> 출처: [MC1478958 — Microsoft SharePoint Online: Select page canvas elements for Copilot-assisted editing](https://mc.merill.net/message/MC1478958)  
> [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 명시되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
