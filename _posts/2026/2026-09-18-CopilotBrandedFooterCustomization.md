---
title: "업무용 Copilot임을 로고로 표시하기: 조직 브랜드 바닥글 설정"
date: 2026-09-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Branding
  - AdminCenter
  - OrganizationTheme
excerpt: "Microsoft 365 Copilot 앱의 Chat 화면 아래에 조직 로고와 라벨을 표시하는 기능이 안내됐습니다. 기본값은 꺼짐이며, 관리 센터의 기본 테마에서 로고와 바닥글 표시를 구성해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 업무용 Copilot임을 로고로 표시하기: 조직 브랜드 바닥글 설정

사용자가 Copilot을 열었을 때 조직에서 관리하는 업무용 환경인지 쉽게 알아볼 수 있으면 안내와 지원에 도움이 됩니다. 이번 기능은 Chat 화면 아래에 회사 로고와 선택한 라벨을 표시하는 방식입니다.

메시지 센터 **MC1238432**는 Microsoft 365 Copilot 앱의 **브랜드 바닥글** 설정을 소개합니다. 2026년 9월 17일 본문이 수정됐으며, 로드맵 **555852**와 연결된 공지입니다.

---

## 어떤 정보가 표시되나요

바닥글은 다른 Microsoft 365 앱에서도 사용하는 **조직 테마의 로고**를 이용합니다. 이번 릴리스에서 적용되는 것은 로고뿐이며 다른 테마 설정까지 반영되는 것은 아닙니다.

![Copilot Chat 화면 아래에 Approved by 라벨과 조직 로고를 표시한 원문 예시](/mwkorea/assets/images/2026-09-18-CopilotBrandedFooterCustomization/image1.png)

| 설정 | 표시 내용 |
|---|---|
| No label | 라벨 없이 로고만 표시 |
| Approved by | 승인 주체를 나타내는 라벨과 로고 |
| Provided by | 제공 주체를 나타내는 라벨과 로고 |
| Managed by | 관리 주체를 나타내는 라벨과 로고 |

이는 업무용 환경을 알아보기 위한 시각적 표시입니다. 로고나 Approved by 라벨이 모든 AI 답변의 정확성 또는 개별 콘텐츠의 승인 여부를 보증하는 것으로 안내해서는 안 됩니다.

## 기본값은 꺼짐

이 기능은 **기본적으로 꺼져 있으며 관리자 설정이 필요**합니다. 관리자가 바닥글을 켜지 않으면 사용자에게 영향이 없습니다. 로고가 이미 다른 Microsoft 365 앱에 표시된다는 이유만으로 Copilot에도 자동 적용된다고 가정하지 마세요.

현재 바닥글은 조직의 **기본 테마**를 사용하고 **모든 사용자에게 적용**됩니다. 사용자 그룹마다 다른 로고를 지정하는 기능은 이후 업데이트에서 지원할 예정이라고 원문은 설명합니다.

## 관리 센터에서 구성하는 순서

1. Microsoft 365 관리 센터에서 **Org settings > Custom theme**으로 이동해 **default theme**을 엽니다.
2. **Logos** 탭에서 조직 로고가 구성되어 있는지 확인합니다.
3. **Copilot Chat** 탭을 열고 **Add your brand to Copilot Chat footer area**를 선택합니다.
4. **Footer style**에서 No label, Approved by, Provided by, Managed by 중 하나를 선택합니다.
5. 변경 내용을 저장합니다.

라벨을 정할 때는 사용자 안내에서 실제로 전달하려는 의미와 일치하도록 검토하는 것이 좋습니다. 그룹별 로고 구분이 필요한 조직은 이번 버전의 전체 사용자 적용 범위를 먼저 확인하세요.

## 배포 일정

| 구분 | 현재 공지의 일정 |
|---|---|
| 전 세계 GA 시작 | 2026년 8월, 기존 7월 중순에서 변경 |
| 완료 예상 | 2026년 9월 중순, 기존 7월 말에서 변경 |
| 본문 수정일 | 2026년 9월 17일 |

이미 지난 일정이 포함된 수정 공지이므로 수집일을 새 출시일로 볼 수는 없습니다. 실제 테넌트의 설정 화면에서 제공 상태를 확인한 뒤 적용하세요. 원문에는 별도로 확인된 준수 고려사항은 없다고 적혀 있으나, 조직의 브랜드·지원 정책에 맞는 검토는 필요합니다.

---

> **출처**
>
> - 원문 ID: **MC1238432** — *Microsoft 365 Copilot app: Branded footer customization*
> - 원문: [MC1238432](https://mc.merill.net/message/MC1238432)
> - [Microsoft 365 Roadmap 555852](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=555852)
> - 관련 안내: [Customize the theme for your organization](https://learn.microsoft.com/microsoft-365/admin/setup/customize-your-organization-theme)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
