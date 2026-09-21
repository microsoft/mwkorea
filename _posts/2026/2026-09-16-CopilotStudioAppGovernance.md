---
title: "Copilot Studio 앱을 만들기 전에 정할 것: 현황·비용·생성 경로 관리"
date: 2026-09-16T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - CopilotCowork
  - AppGovernance
  - CopilotCredits
  - PowerApps
excerpt: "Copilot Studio와 Cowork로 만든 앱은 Microsoft 365 관리 센터에서 현황과 생성 경로를 관리합니다. 제작·실행 비용의 구분, 사용자별 크레딧 한도, 앱 공유와 데이터 권한의 관계를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 앱을 만들기 전에 정할 것: 현황·비용·생성 경로 관리

자연어로 앱을 만드는 과정이 쉬워져도 누가 앱을 소유하고, 얼마를 쓰고, 어떤 데이터에 연결하는지는 정해야 합니다. 화면을 만드는 일과 조직에서 안전하게 운영하는 일은 다르기 때문입니다.

Microsoft의 **Managing apps built in Copilot Studio**는 Copilot Studio와 Copilot Cowork의 앱 제작 기능을 관리하는 방법을 소개합니다. 관리자에게 중요한 항목은 앱 현황 확인, 비용 한도, 앱을 만들 수 있는 경로입니다.

---

## 호스팅은 제공되지만 관리 책임은 남습니다

원문은 앱에 소스 제어, 배포 단계, 버전 격리가 내장되어 있고 Microsoft가 호스팅하는 인프라에서 실행된다고 설명합니다. 별도의 인프라 프로비저닝이나 호스팅 설정, 배포 파이프라인을 준비할 부담을 줄인다는 의미입니다.

![Copilot Studio 앱 제작과 Microsoft 365 관리 센터를 소개하는 원문 대표 이미지](/mwkorea/assets/images/2026-09-16-CopilotStudioAppGovernance/image1.png)

앱은 기존 환경 라우팅 정책에 따라 제작자의 개인 개발 환경에 생성됩니다. 커넥터 권한과 데이터 정책은 제작 중에도, 게시 후에도 적용됩니다.

연결 데이터는 로그인한 사용자를 대신해 접근합니다. **앱을 게시하거나 공유한다고 사용자가 원래 접근할 수 없던 데이터의 권한을 얻는 것은 아닙니다.** 앱 배포 권한과 데이터 접근을 함께 살펴야 하는 이유입니다.

## 게시된 앱 현황을 한곳에서 확인

Microsoft 365 관리 센터의 앱 인벤토리는 제작자, 수명주기 상태, 사용하는 데이터 원본과 커넥터, 적용 정책, 사용 및 운영 지표를 보여 줍니다.

![제작자와 상태, 위치 등을 확인하는 All apps 화면](/mwkorea/assets/images/2026-09-16-CopilotStudioAppGovernance/image2.png)

원문은 같은 경험에서 게시 앱을 차단·비활성화하거나 커넥터를 제거하고, 정책 준수 상태로 조정하고, 공유 가능 여부를 제어하며, 더 이상 쓰지 않는 앱을 폐기할 수 있다고 안내합니다. 앱이 늘어나기 전에 이 업무를 맡을 담당자를 정하는 것이 좋습니다.

## 제작 비용과 실행 비용은 별도 서비스

| 구분 | 소비에 영향을 주는 요소 |
|---|---|
| 제작(Build) | 사용하는 언어 모델, 앱 복잡도, 반복 수정량 |
| 실행(Runtime) | 앱이 처리하는 작업의 양과 복잡도 |

두 활동은 Copilot Credits 사용량 기반 청구에서 **서로 별도의 서비스로 계량**됩니다. 따라서 제작자의 소비와 실제 앱 사용자의 소비를 구분해 관리할 수 있습니다.

실행 사용자가 **Power Apps Premium** 라이선스를 보유한 경우에는 기존 요청 한도 내 사용이 포함됩니다. 그 한도를 넘거나 라이선스가 없으면 Copilot Credits로 청구된다고 원문은 설명합니다. 이 조건을 앱 제작 비용까지 모두 포함된다는 뜻으로 확대하면 안 됩니다.

현재 크레딧 한도는 제작과 실행 모두 **사용자별**로 설정합니다. 모두에게 같은 예산을 주거나 부서 같은 사용자 그룹에 따라 다른 예산을 적용하는 방식입니다. 원문이 언급하는 **환경별 한도는 향후 제공될 항목**이므로 현재 사용할 수 있는 프로젝트 예산 제어로 안내해서는 안 됩니다.

## 앱을 만드는 경로를 선택

Microsoft 365 관리 센터의 **Apps > Overview**에서 **Choose where people can make apps**를 찾습니다.

![Copilot Studio와 Copilot Cowork의 앱 생성 경로 설정](/mwkorea/assets/images/2026-09-16-CopilotStudioAppGovernance/image3.png)

| 경로 | 원문 설명 |
|---|---|
| Copilot Studio | 제작자가 직접 앱을 만드는 경로, 기본 켜짐 및 권장 |
| Copilot Cowork | 채팅으로 앱을 만드는 경로, 조직의 Frontier 참여에 따라 가용성 관리 |

원문은 기본적으로 앱 생성이 제공되지만 조직의 필요에 따라 경로를 제한할 수 있다고 설명합니다. Cowork는 Frontier 참여 조건을 함께 확인해야 합니다.

**생성 경로를 끄면 그 경로에서 새 앱을 만드는 것이 막힙니다. 이미 게시된 앱은 계속 실행됩니다.** 게시 앱을 중단해야 한다면 생성 경로 차단과 별도의 관리 조치를 구분해야 합니다.

## 도입 전에 합의할 운영 항목

게시 앱을 감독할 사람, 제작자와 실행 사용자의 예산, 허용할 커넥터, 사용하지 않는 앱을 정리할 기준을 먼저 정해 두세요. 이 원문은 모든 고객의 GA 일정표를 제시한 공지가 아니라 관리 방법을 설명하는 글이며, 실제 환경의 제공 상태와 라이선스 조건은 최신 안내로 확인해야 합니다.

앱 제작의 진입 장벽이 낮아졌을수록 인벤토리와 비용을 나중에 정리하려 하지 않는 것이 중요합니다. 기존 데이터 권한을 유지하면서 누가 만들고 누가 사용하는지를 계속 볼 수 있는 운영 체계를 준비하는 것이 핵심입니다.

---

> **출처**
>
> - TechCommunity Microsoft Copilot Studio Blog: [Managing apps built in Copilot Studio](https://techcommunity.microsoft.com/t5/copilot-studio-blog/managing-apps-built-in-copilot-studio/ba-p/4556774)
> - 관련 라이선스: [Copilot Credits Licensing Guide](https://aka.ms/CopilotCredits/LicensingGuide)
>
> 자세한 내용은 원문 참조.
