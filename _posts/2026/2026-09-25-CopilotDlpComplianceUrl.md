---
title: "Copilot이 접근을 차단했을 때, 이제 우리 회사 안내 페이지로 연결하세요"
date: 2026-09-25T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - MicrosoftPurview
  - DLP
  - Compliance
  - Governance
excerpt: "Purview DLP로 Copilot의 데이터 접근이 제한될 때 조직 전용 안내 URL을 보여줄 수 있습니다. 설정 절차와 여러 정책이 일치할 때의 우선순위, 바뀌지 않는 제한 사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot이 접근을 차단했을 때, 이제 우리 회사 안내 페이지로 연결하세요

Copilot에서 데이터를 사용할 수 없다는 메시지를 받았을 때, 사용자가 필요한 것은 대개 일반적인 제품 설명보다 “우리 회사에서는 누구에게 문의해야 하는가”입니다. MC1478467은 이 연결을 조직에 맞게 바꿀 수 있는 Purview DLP 기능을 소개합니다.

Microsoft 365 Copilot의 데이터 접근 제한 메시지에 있는 **Learn about access restrictions** 링크를 사내 컴플라이언스 안내, 데이터 관리 포털, 헬프데스크 요청 페이지 등으로 연결할 수 있습니다. 차단 정책 자체를 완화하는 기능은 아닙니다.

---

## 바뀌는 것은 링크 목적지입니다

기존에는 Purview DLP가 Copilot의 콘텐츠 참조·처리·응답을 제한하면 Microsoft의 공개 DLP 문서로 연결했습니다. 이제 지원되는 DLP 규칙에 **compliance URL**을 지정할 수 있습니다.

![Copilot 데이터 접근 제한 메시지와 안내 링크](/mwkorea/assets/images/2026-09-25-CopilotDlpComplianceUrl/image1.png)

메시지 본문과 링크 이름은 계속 Microsoft가 관리하고 현지화합니다. **관리자가 안내 메시지 문구를 직접 작성하는 기능은 이번 릴리스에 포함되지 않습니다.** URL을 설정하지 않으면 기존 공개 문서 연결이 유지됩니다.

## 설정 절차

1. Microsoft 365 Copilot 위치에 적용되는 Purview DLP 정책을 확인합니다.
2. Microsoft Purview 포털에서 해당 DLP 규칙을 편집합니다.
3. **User notifications**를 펼치고 **Policy tips**를 켭니다.
4. **Provide a compliance URL for the end user to learn more about your organization's policies**를 선택합니다.
5. 사용자가 열어야 할 조직의 안내 URL을 입력합니다.

![Purview DLP 규칙의 User notifications와 compliance URL 설정](/mwkorea/assets/images/2026-09-25-CopilotDlpComplianceUrl/image2.png)

자동으로 조직 전용 URL이 활성화되는 것은 아닙니다. 기본 Microsoft 문서 연결을 유지할 조직은 작업하지 않아도 됩니다.

## 여러 규칙이 일치해도 링크는 하나입니다

여러 정책이나 규칙이 동일한 Copilot 상호작용에 일치하면 Purview는 **정책 우선순위와 가장 제한적인 동작**을 사용해 하나의 우선 정책 팁을 결정합니다. 사용자는 이때 선택된 규칙의 URL 하나만 보며, 나머지 규칙의 URL은 표시되지 않습니다.

따라서 안내 URL만 입력할 것이 아니라 기존 정책 우선순위도 검토해야 합니다. 또한 이 설정은 **Purview DLP 제한에만 적용**되며 다른 접근 제어 기술의 조직별 링크 처리까지 포함하지 않습니다. 기존 DLP 집행 동작도 바뀌지 않습니다.

## 어떤 사용 경험이 대상인가요?

원문은 Copilot 웹 경험(copilot.microsoft.com, Microsoft365.com), Teams의 Copilot 앱, Copilot 모바일 앱·Search·Pages를 열거합니다. Teams의 1:1·그룹 채팅, 실시간 회의, 회의 후 Recap, 채널, 통화의 Copilot도 포함됩니다.

Outlook on the web, Edge의 웹페이지 Copilot 사이드바 및 웹 모드 채팅 역시 안내된 대상입니다. 이는 원문이 열거한 범위이며 모든 앱·버전에 대한 포괄적인 지원 보장은 아닙니다.

## 배포 일정과 꼭 확인할 제한

Worldwide GA는 **2026년 9월 말 시작·완료 예정**, GCC·GCC High·DoD는 **9월 말 시작하여 10월 중순 완료 예정**입니다.

특히 **Purview는 URL 형식은 검증하지만 실제 접속 가능 여부는 검사하지 않습니다.** 정책 대상 사용자가 안내 페이지에 접근할 수 있는지, 로그인 후 올바른 내용이 보이는지 직접 점검하세요. 헬프데스크 문서와 FAQ도 함께 갱신하면 접근 제한 이후의 지원 흐름을 연결할 수 있습니다.

> 출처: [MC1478467 — Microsoft Purview | Data Loss Prevention: Admin-configurable compliance URL in M365 Copilot data access messages](https://mc.merill.net/message/MC1478467)  
> [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 명시되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
