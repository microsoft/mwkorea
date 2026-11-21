---
title: "SharePoint 페이지 안에서 에이전트와 대화하기: Agent Chat 웹 파트"
date: 2026-11-19T00:00:00 KST
categories:
  - Copilot
tags:
  - SharePoint
  - Microsoft365Copilot
  - CopilotStudio
  - Agents
excerpt: "SharePoint의 Agent Chat 웹 파트로 기존 Copilot 에이전트를 인트라넷 페이지에 배치할 수 있게 됩니다. 프리뷰와 GA 일정, 라이선스 조건, 페이지와 에이전트의 독립적인 권한 모델을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# SharePoint 페이지 안에서 에이전트와 대화하기: Agent Chat 웹 파트

사내 에이전트를 만들어도 직원들이 어디서 찾아야 할지 모르면 활용은 늘어나기 어렵습니다. 업무 안내와 규정이 있는 SharePoint 페이지에 대화 창이 함께 있다면 에이전트를 발견하는 경로가 짧아집니다.

MC1559633은 바로 이 경험을 위한 **Agent Chat 웹 파트**를 안내합니다. 기존 Microsoft 365 Copilot 에이전트를 SharePoint 페이지에 배치하고, 사용자가 페이지 안에서 대화를 시작하도록 하는 기능입니다.

---

## 페이지 작성자와 사용자의 경험

페이지 작성자는 일반적인 SharePoint 페이지 편집 화면에서 Agent Chat 웹 파트를 추가합니다. 이후 Microsoft 365 Copilot에서 본인에게 이미 제공된 게시 완료 에이전트를 선택할 수 있습니다.

사용자는 페이지에서 에이전트와 대화하고 전체 화면 채팅 경험으로 대화를 이어갈 수 있습니다. 공지상 이용 대상은 **Microsoft 365 Copilot 라이선스와 해당 에이전트 접근 권한을 갖춘 사용자**입니다.

## 가장 중요한 제한: 페이지 접근과 에이전트 접근은 다릅니다

두 권한은 독립적으로 유지됩니다. 페이지에 에이전트를 추가했다고 해서 그 페이지의 모든 방문자에게 에이전트 사용 권한이 자동 부여되지는 않습니다.

또한 **SharePoint 페이지 내용이 에이전트에 자동 전달되지 않습니다.** 안내 페이지 옆에 채팅을 배치하는 것과, 그 페이지를 에이전트 지식으로 연결하는 것은 별도의 문제입니다.

공지에 따르면 SharePoint는 이 변경으로 Copilot 에이전트의 채팅 데이터를 저장하거나 에이전트 데이터 처리 방식을 바꾸지 않습니다.

## 배포 일정

| 구분 | 시작 예정 | 완료 예상 |
|---|---|---|
| 전 세계 공개 프리뷰 | 2026년 11월 중순 | 2027년 1월 말 |
| 전 세계 GA | 2027년 1월 중순 | 2027년 3월 말 |
| GCC GA | 2027년 1월 중순 | 2027년 3월 말 |
| GCC High GA | 2027년 1월 중순 | 2027년 3월 말 |
| DoD GA | 2027년 1월 중순 | 2027년 3월 말 |

프리뷰와 GA의 배포 기간은 일부 겹칩니다. 일정만으로 개별 조직의 활성화 여부를 단정하지 않아야 합니다.

## 도입 체크포인트

배포 전 필수 관리자 작업은 없습니다. 페이지 작성자와 지원 담당자에게 기능을 알리고, [Agent Chat 웹 파트 사용 안내](https://support.microsoft.com/en-us/sharepoint/pages-in-sharepoint/use-agent-chat-web-part)를 참고하도록 준비하면 됩니다.

실무적으로는 페이지 접근은 가능하지만 에이전트 접근은 불가능한 사용자로도 확인하는 것이 좋습니다. 인사 안내나 IT 지원 페이지를 시범 대상으로 삼되, 페이지 배치만으로 지식 연결과 권한 설정까지 끝났다고 생각하지 않는 것이 핵심입니다.

## 마무리

Agent Chat은 직원이 이미 방문하는 업무 공간으로 에이전트를 가져오는 기능입니다. 성공적인 도입의 기준은 채팅 창을 띄우는 것뿐 아니라 **정확한 이용 권한과 기대 동작을 함께 안내하는 것**입니다.

> 출처: [MC1559633 — Microsoft SharePoint: Agent Chat web part to bring Copilot agents into SharePoint pages](https://mc.merill.net/message/MC1559633) · [Microsoft 365 Roadmap 575298](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&searchterms=575298)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
