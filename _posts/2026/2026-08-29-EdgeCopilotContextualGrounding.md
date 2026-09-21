---
title: "여러 탭·문서·YouTube를 맥락으로 묻기: Edge용 Copilot Chat"
date: 2026-08-29T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftEdge
  - CopilotChat
  - ContextualGrounding
  - DLP
  - YouTube
excerpt: "Microsoft Edge for Business의 Copilot Chat이 여러 열린 탭, Microsoft 365 문서, YouTube 영상을 바탕으로 요약하고 질문에 답합니다. 기본 비활성화, Entra ID와 라이선스 요건, DLP 및 Edge 정책의 적용 방식과 최신 일정을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 여러 탭·문서·YouTube를 맥락으로 묻기: Edge용 Copilot Chat

조사 중인 웹페이지 여러 개와 Office 문서, 설명 영상을 번갈아 보면서 질문하면 맥락을 옮기는 데 시간이 듭니다. Microsoft Edge for Business의 Microsoft 365 Copilot Chat은 Edge 사이드 창에서 열린 탭과 문서, YouTube 영상을 바탕으로 요약과 맥락 기반 질의를 지원합니다.

메시지 센터 **MC1187682**는 페이지 하나를 요약하는 기능보다 넓은 범위를 다룹니다. 다만 사용자의 환경과 정책에 상관없이 모든 페이지를 읽는 기능은 아니며, 기본 상태와 데이터 보호 제어를 함께 확인해야 합니다.

---

## 지원하는 세 가지 맥락

사용자는 Edge 사이드 창의 Copilot에 다음 자료를 바탕으로 질문할 수 있습니다.

- 여러 개의 열린 브라우저 탭
- Word, Excel, PowerPoint 같은 Microsoft 365 문서
- YouTube 영상

이를 통해 탭 사이의 공통점 비교, 문서 요약, 영상 내용에 관한 후속 질문 같은 흐름을 한곳에서 이어갈 수 있습니다. 공지는 YouTube 영상 지원을 밝히지만 모든 영상의 언어, 자막 상태, 접근 제한에서 같은 결과를 보장한다고 설명하지는 않습니다.

## 대상과 필수 조건

대상은 **Entra ID로 Microsoft Edge for Business에 로그인**하고 **Microsoft 365 Copilot에 접근할 수 있는 사용자**입니다. 조직의 테넌트가 Microsoft 365 Copilot을 지원하도록 구성돼 있어야 하며 적용 가능한 Microsoft 365 서비스 플랜을 포함한 라이선스 전제 조건을 충족해야 합니다.

기능은 **기본으로 꺼져 있습니다**. 배포가 시작된다고 해서 모든 사용자에게 즉시 페이지 맥락 접근이 켜지는 것은 아닙니다. 관리자는 실제 활성화 상태와 대상 범위를 조직 정책에 맞춰 확인해야 합니다.

## DLP와 Edge 정책을 우회하지 않습니다

Copilot의 페이지 콘텐츠 접근이 데이터 손실 방지(DLP) 정책 또는 **EdgeEntraCopilotPageContext** 정책으로 제한돼 있으면 맥락 기능이 억제됩니다. 기존 DLP 및 정책 구성은 그대로 존중됩니다.

이는 생산성 기능을 켰다는 이유로 보호된 페이지 내용이 Copilot에 자동 노출되지 않도록 하는 중요한 경계입니다. 정책은 Entra ID 그룹 멤버십을 이용해 범위를 지정할 수 있으므로, 부서나 정보 등급에 따라 단계적으로 적용할 수 있습니다.

## 현재와 변경된 출시 일정

| 맥락 유형 | 정식 출시 상태 |
|---|---|
| 여러 브라우저 탭 | 현재 사용 가능 |
| YouTube 영상 | 현재 사용 가능 |
| Microsoft 365 문서 | 2026년 9월 중순 배포 시작 예정 |

Microsoft 365 문서 지원은 이전에 8월 말 시작으로 안내됐으나 2026년 8월 28일 업데이트에서 **9월 중순**으로 변경됐습니다. 여러 탭과 YouTube의 현재 제공 상태와 문서 지원의 향후 배포를 구분해야 합니다.

## 관리자가 점검할 사항

사전 필수 작업 없이 일정에 따라 배포되지만, 실제 사용 전에는 다음을 검토하는 것이 좋습니다.

1. 대상 사용자의 Entra ID 로그인과 Copilot 접근 권한 확인
2. 현재 DLP와 EdgeEntraCopilotPageContext 정책 검토
3. 허용할 사용자 그룹과 페이지 콘텐츠 범위 정의
4. 지원팀과 사용자에게 기본 비활성화 상태 안내
5. 요약 결과의 출처 확인과 민감 정보 취급 교육

여러 소스를 한 번에 활용하는 만큼 잘못된 탭이나 오래된 문서가 포함되면 답변의 맥락도 달라질 수 있습니다. 사용자는 질문 전에 포함할 자료를 확인하고, 중요한 결론은 원본 탭·문서·영상으로 검증해야 합니다.

---

> **출처**
>
> - 원문 ID: **MC1187682** — *Microsoft Edge: Microsoft 365 Copilot will support summarization and contextual grounding*
> - 원문: [MC1187682](https://mc.merill.net/message/MC1187682)
> - Microsoft 365 Roadmap: [496364](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=496364), [499423](https://www.microsoft.com/en-us/microsoft-365/roadmap?rtc=1%26filters%3D&searchterms=499423), [499424](https://www.microsoft.com/microsoft-365/roadmap?rtc=1%26filters%3D&searchterms=499424)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
