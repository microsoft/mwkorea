---
title: "Cowork에서 업무 앱을 만들고 조직에 공유하기: App 스킬 Frontier 프리뷰"
date: 2026-09-11T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCowork
  - AppSkill
  - WorkIQ
  - CopilotStudio
  - Frontier
  - Governance
excerpt: "Copilot Cowork에서 자연어로 업무 앱을 만들고, 미리보기와 대화로 다듬은 뒤 게시·공유하는 기능이 Frontier 프리뷰로 배포됩니다. 지원 커넥터의 실제 업무 데이터 연결과 Microsoft 365 관리 센터의 앱 관리까지 포함한 변화입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Cowork에서 업무 앱을 만들고 조직에 공유하기: App 스킬 Frontier 프리뷰

팀의 진행 상황은 문서, 스프레드시트, 회의, 채팅에 흩어져 있기 쉽습니다. 내용을 요약하는 것만으로 부족하고, 담당자가 데이터를 입력하거나 진행 상태를 바꿀 수 있는 업무 화면이 필요할 때도 있습니다.

Copilot Cowork 리빙 블로그의 **Create, publish, and share apps** 섹션은 이런 업무 앱을 Cowork 안에서 만드는 기능을 소개합니다. 필요한 앱을 말로 설명하면 초안을 만들고, 미리보기로 확인하며 대화로 수정한 뒤 조직에 게시·공유할 수 있습니다. Copilot Studio의 앱 제작과 같은 플랫폼을 사용합니다.

---

## HTML 결과물에서 데이터와 연결된 업무 앱으로

Cowork는 이전에도 작업 중 대화형 HTML 파일을 만들 수 있었습니다. 이번 App 기능은 Work IQ로 파악한 문서·스프레드시트·회의·메시지 맥락을 팀이 사용하는 앱으로 연결한다는 점에서 범위가 넓습니다.

**지원되는 커넥터에서는 앱 제작 과정에서 데이터 구조를 정의하고 원본을 연결**할 수 있습니다. 화면만 있는 정적 시안이 아니라 실제 업무 데이터와 연결된 앱을 만들 수 있다는 설명입니다. 다만 모든 연결 대상에서 데이터 구조를 자동 생성한다는 뜻은 아니며, 커넥터별 지원 범위를 확인해야 합니다.

![Cowork에서 자연어 요청을 받아 App 스킬로 앱을 만드는 화면](/mwkorea/assets/images/2026-09-11-CoworkCreatePublishShareApps/image1.png)

## 만들기부터 공유까지

1. **앱의 목적을 설명합니다.** `/app`으로 App 스킬을 사용하거나, Cowork에 만들고 싶은 앱과 원하는 결과를 말합니다.
2. **미리보기에서 동작을 살펴봅니다.** Cowork가 만든 초안을 열어 사용자가 실제로 보게 될 화면을 확인합니다.
3. **대화로 수정합니다.** 기능 추가, 레이아웃 변경, 정보 표시 방식 조정 등을 요청합니다.
4. **게시하고 공유합니다.** Cowork에서 게시한 앱을 조직 내 사용자가 공유 링크로 열어 사용하도록 할 수 있습니다.

Microsoft Learn은 작업 중 앱이 자동 저장되지만, 공유 사용자에게 앱과 최신 변경을 제공하는 단계는 **게시(Publish)**라고 구분합니다. 수정한 내용이 저장됐다는 것과 사용자에게 새 버전이 게시됐다는 것을 혼동하지 않는 것이 좋습니다.

![온보딩 대시보드 앱의 미리보기와 Publish 버튼](/mwkorea/assets/images/2026-09-11-CoworkCreatePublishShareApps/image2.png)

## 원문이 제시한 업무 예시

첫 번째는 **제품 출시 현황 앱**입니다. 가상 제품 Zava NanoFiber의 출시 준비에 필요한 메일, 회의, 채팅, 파일, 실행 항목, 로드맵 문서를 모아 준비 상태 KPI, 마일스톤, 담당자, 위험, 기한, 미해결 의존 관계와 최근 결정을 보여 달라는 요청입니다. 마케팅·제품·영업·지원·운영의 업무별 진행 상황을 추적하고 단계 카드를 수정하도록 요구합니다.

두 번째는 **신규 입사자 온보딩 대시보드**입니다. 입사 계획, 회의, 메일, Teams 대화를 바탕으로 진행률, 처리되지 않은 지원 요청, 주요 장애 요인을 보여 주고 회사 브랜드에 맞춰 달라는 예시입니다.

이 예시에서 참고할 점은 “대시보드를 만들어 줘”에서 끝내지 않는다는 것입니다. 어떤 자료를 모으고, 무엇을 표시하며, 사용자가 무엇을 바꿀 수 있어야 하는지까지 설명합니다. 실제 도입 시에도 처음부터 범위를 크게 잡기보다 업무 하나와 필요한 데이터 원본을 정해 시작하는 편이 좋습니다.

## 공유 링크와 데이터 권한을 함께 검토하세요

앱은 Microsoft Entra 인증을 사용하며, 관리자는 **Microsoft 365 관리 센터의 Apps 영역**에서 Cowork로 만든 앱을 관리할 수 있습니다. 원문은 배포·공유 정책과 **1,500개 이상 데이터 원본**에 대한 연결 및 접근 관리도 안내합니다.

이 수치를 모든 데이터 원본이 기본 허용되거나 App 스킬에서 동일하게 동작한다는 의미로 읽으면 안 됩니다. 관리자가 승인한 연결 대상과 사용자가 실제 접근할 데이터 범위를 함께 확인해야 합니다.

![연결 데이터에 대한 접근 필요 안내가 포함된 앱 공유 화면](/mwkorea/assets/images/2026-09-11-CoworkCreatePublishShareApps/image3.png)

원문 화면은 앱을 사용하려면 연결된 데이터 원본에 대한 접근이 필요하다고 안내합니다. Microsoft Learn 역시 앱과 그 안의 데이터가 공유 대상에게 노출된다는 점을 고려해 신중하게 공유하도록 설명합니다. 링크를 전달하기 전에는 앱에 표시되는 정보, 연결 권한, 실제 공유 범위를 함께 살펴보세요.

## 누가 사용할 수 있나요

| 항목 | 원문 안내 |
|---|---|
| 제공 단계 | Frontier 프리뷰, 순차 배포 |
| 대상 | Cowork 접근 권한이 있는 Microsoft 365 Copilot 사용자 |
| 클라이언트 | 웹, Windows, Mac |
| 제작 플랫폼 | Copilot Studio의 앱 제작과 동일한 플랫폼 |

정식 출시된 모든 고객용 기능으로 안내하지 않도록 주의해야 합니다. Microsoft Learn은 Frontier 참여가 필요하며, 프리뷰 기능의 제공 범위와 기능이 변경될 수 있다고 설명합니다. 원문 섹션만으로 앱 제작·실행의 별도 과금 조건을 확정할 수는 없습니다.

Cowork에서 시작한 작업을 팀이 반복해서 사용하는 앱으로 발전시킬 수 있다는 것이 이번 변화입니다. 제작의 편의성뿐 아니라 앱 게시 담당자와 데이터·공유 정책 담당자를 함께 정해 두면 프리뷰를 업무에 맞게 평가하기가 수월합니다.

---

> **출처**
>
> - 섹션: [Create, publish, and share apps — (Co)work in Progress](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/cowork-in-progress/4511672#community-4511672-toc-hId-2052082034)
> - 관련 안내: [Use Copilot Cowork — Build apps with the App skill (Frontier)](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork#build-apps-with-the-app-skill-frontier)
>
> 자세한 내용은 원문 참조.
>
> 이 글은 하나의 글에 Cowork 업데이트가 누적되는 리빙 블로그의 최신 섹션입니다. 파일 날짜는 수집 데이터의 `pubDate`를 한국 시간으로 변환한 값이며, 이 데이터는 리빙 블로그의 수정 시각을 사용합니다.
