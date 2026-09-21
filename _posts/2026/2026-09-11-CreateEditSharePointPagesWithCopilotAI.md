---
title: "자연어로 SharePoint 페이지를 만들고 다듬는 Copilot AI 작성 환경"
date: 2026-09-11T00:00:00 KST
categories:
  - Copilot
tags:
  - SharePoint
  - Microsoft365Copilot
  - PageAuthoring
  - GenerativeAI
  - Governance
excerpt: "Microsoft 365 Copilot 라이선스를 보유한 SharePoint 페이지 편집자는 자연어로 페이지 섹션, 텍스트, 레이아웃과 웹 파트를 만들고 수정할 수 있습니다. 전 세계 일반 공급은 2026년 9월 말 완료 예정이며 GCC와 Gallatin은 대상에 포함되지 않습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 자연어로 SharePoint 페이지를 만들고 다듬는 Copilot AI 작성 환경

SharePoint 페이지를 구성하려면 글뿐 아니라 섹션, 레이아웃, 웹 파트까지 함께 손봐야 합니다. Microsoft는 이 편집 과정을 대화형 지시로 처리할 수 있는 Copilot 기반 AI 작성 패널을 도입합니다.

이번 변화의 핵심은 빈 페이지 초안을 만드는 데 그치지 않습니다. 조직의 Microsoft 365 파일을 근거 자료로 연결하고, 기존 페이지의 구성 요소를 수정하면서도 언제든 일반 편집 방식으로 돌아갈 수 있게 한 통합 작성 환경입니다.

---

## 편집 화면 안에서 계획부터 수정까지

대상 사용자가 SharePoint 페이지를 편집하면 AI 작성 패널이 자동으로 열립니다. 작성자는 자연어로 새 섹션을 만들거나 채팅형 지시를 통해 기존 텍스트, 레이아웃, 웹 파트를 수정할 수 있습니다.

![SharePoint 페이지 편집 화면의 Copilot AI 작성 패널](/mwkorea/assets/images/2026-09-11-CreateEditSharePointPagesWithCopilotAI/image1.png)

![페이지 편집 작업을 지원하는 AI 패널](/mwkorea/assets/images/2026-09-11-CreateEditSharePointPagesWithCopilotAI/image2.png)

예를 들어 전달하려는 내용을 프롬프트로 설명해 페이지 섹션 초안을 생성한 뒤, 배치나 문구를 이어서 조정하는 흐름을 사용할 수 있습니다. 생성과 수정이 같은 편집 화면 안에서 이어지므로 초안을 별도 도구에서 옮기는 작업을 줄이는 것이 목표입니다.

![자연어 프롬프트로 새 페이지 섹션 생성](/mwkorea/assets/images/2026-09-11-CreateEditSharePointPagesWithCopilotAI/image3.png)

## Microsoft 365 파일을 근거로 연결

작성자는 Microsoft 365 파일을 첨부해 생성 결과의 근거 맥락으로 제공할 수 있습니다. Copilot은 사용자가 선택한 파일과 기존 SharePoint 페이지 콘텐츠를 생성 시점에 처리해 페이지 안에 제안과 변경 내용을 만듭니다.

![Microsoft 365 파일을 근거 자료로 첨부하는 화면](/mwkorea/assets/images/2026-09-11-CreateEditSharePointPagesWithCopilotAI/image4.png)

AI가 적용한 변경은 페이지에 직접 삽입되며 눈에 띄도록 표시됩니다. 작성자는 결과를 그대로 확정하기보다 원자료, 표현, 레이아웃을 확인한 뒤 게시하는 검토 절차를 유지하는 것이 좋습니다.

![AI가 생성해 페이지에 삽입한 변경 내용](/mwkorea/assets/images/2026-09-11-CreateEditSharePointPagesWithCopilotAI/image5.png)

## AI와 수동 편집을 선택할 수 있습니다

이 기능이 기본 제공되더라도 모든 작업을 AI로 처리해야 하는 것은 아닙니다. 사용자는 필요할 때 AI 지원 편집과 기존 수동 편집 사이를 전환할 수 있습니다.

![AI 지원 편집과 수동 편집 전환](/mwkorea/assets/images/2026-09-11-CreateEditSharePointPagesWithCopilotAI/image6.png)

채팅 기록은 해당 편집 세션 동안 유지되며 사용자가 직접 지울 수도 있습니다. 공지에는 편집 세션을 넘어선 별도 보존 기간이 제시되지 않았으므로 장기 대화 기록 기능으로 확대해석해서는 안 됩니다.

## 대상과 관리 범위

- SharePoint 페이지 편집자 중 **Microsoft 365 Copilot 라이선스가 할당된 사용자**가 대상입니다.
- 프로덕션 테넌트에 제공되며 **GCC와 Gallatin은 제외**됩니다.
- 적격 사용자에게 기본으로 켜집니다.
- 이 기능만을 위한 추가 테넌트 수준 토글은 없으며, 접근 범위는 Copilot 라이선스 할당으로 관리합니다.

기존 페이지와 사용자가 선택한 파일이 AI 생성의 근거로 처리된다는 점도 안내해야 합니다. 페이지 작성자를 정할 때는 편집 권한뿐 아니라 Copilot 라이선스 배정이 조직의 역할 설계와 맞는지 함께 확인해야 합니다.

## 배포 일정과 준비 사항

| 단계 | 일정 |
|---|---|
| 대상 릴리스 | 2026년 4월 초 시작, 4월 중순 완료 예정 |
| 일반 공급, 전 세계 | 배포 시작, 2026년 9월 말 완료 예정 |

원문은 2026년 9월 10일 일정이 갱신됐다고 밝힙니다. 별도 사전 관리 작업은 필요하지 않지만 페이지 작성자 교육, 내부 작성 지침과 Copilot 라이선스 배정을 점검해 두는 것이 권장됩니다.

---

> **출처**
>
> - 원문 ID: **MC1282683** — *Create and edit SharePoint pages with Copilot-powered AI*
> - 원문: [https://mc.merill.net/message/MC1282683](https://mc.merill.net/message/MC1282683)
> - [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
