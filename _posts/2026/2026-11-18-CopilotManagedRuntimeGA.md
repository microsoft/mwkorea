---
title: "Copilot으로 만든 앱, 이제 정식 운영으로: Managed Runtime GA와 관리자 준비사항"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotManagedRuntime
  - CopilotStudio
  - Governance
excerpt: "Copilot Managed Runtime이 공개 프리뷰에서 일반 공급으로 전환됩니다. Cowork 앱 제작 확대와 함께 환경 라우팅, 데이터 접근 권한, Copilot Credits 지출 정책을 점검해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot으로 만든 앱, 이제 정식 운영으로: Managed Runtime GA와 관리자 준비사항

Copilot이 앱을 만들어 주더라도, 기업에서는 실행 환경과 데이터 접근, 비용을 누가 통제하는지가 중요합니다. Microsoft는 MC1558033에서 **Microsoft 365 테넌트 경계 안에서 코드를 실행하는 IT 관리형 플랫폼**, Copilot Managed Runtime의 일반 공급 전환을 안내했습니다.

이번 변화의 핵심은 Copilot Cowork에서 앱을 만드는 경험이 Frontier 프로그램 밖으로 확대된다는 점입니다. 다만 발표 직후 모든 테넌트에 적용이 끝났다는 의미는 아닙니다. 아래 일정은 원문 공지 시점의 배포 계획입니다.

---

## 무엇이 정식 공급으로 바뀌나요?

Copilot Managed Runtime은 Copilot Cowork, Copilot Studio, Copilot Code와 전용 CLI에서 만드는 앱을 지원합니다. 조직 정책이 허용하는 커넥터로 조직 데이터를 이용하고, 관리자는 Microsoft 365 관리 센터에서 앱을 관리합니다.

| 구분 | 원문에 안내된 일정 |
|---|---|
| 공개 프리뷰 | 2026년 9월 시작, 11월 중순 완료 예상 |
| 전 세계 일반 공급 | 2026년 11월 중순 시작, 12월 중순 완료 예상 |

Runtime의 GA와 개별 제작 도구의 제공 상태는 구분해야 합니다. 원문의 플랫폼 목록에서는 **Copilot Code가 여전히 Frontier로 표시**됩니다. Cowork의 앱 제작 제한 완화를 모든 도구·기능의 일괄 GA로 해석하지 않는 것이 안전합니다.

## 개인 환경에도 조직 정책이 적용됩니다

메이커는 처음 필요할 때 생성되고 이후 재사용되는 개인 환경에서 앱을 만듭니다. 환경 라우팅이 적용되며, 별도 라우팅 규칙이 없는 테넌트에서는 기본 환경 그룹의 개인 환경으로 사용자를 보냅니다. 기존 라우팅 규칙은 변경하지 않습니다.

개인 환경은 기본 환경 그룹의 **커넥터, 콘텐츠 보안, 공유 정책**을 상속합니다. 메이커가 이 정책을 임의로 덮어쓸 수는 없습니다. 관리자는 Microsoft 365 관리 센터의 **Apps > Settings**에서 관련 정책을 관리할 수 있습니다.

또한 **앱을 공유했다고 앱이 사용하는 원본 데이터 권한까지 부여되는 것은 아닙니다.** 예를 들어 부서 앱을 배포할 때는 앱 이용 가능 여부와 데이터 접근 권한을 별도로 확인해야 합니다.

## 비용 정책은 어떻게 준비하나요?

원문은 일반 공급 전 다음 설정을 권고합니다.

1. **Copilot > Cost management**에서 사용자를 포괄하는 지출 정책을 만들고 **Copilot Managed Runtime**을 포함합니다.
2. Cowork와 Copilot Code 메이커를 해당 지출 정책에 포함합니다.
3. Copilot Studio에서는 메이커가 앱을 만드는 환경에 크레딧을 할당합니다.

Microsoft는 일반적인 이용을 위한 작은 월 한도의 예로 **사용자당 100 Copilot Credits, 미화 1달러**를 제시합니다. 이는 원문의 예시이지 모든 업무의 비용 상한이나 충분한 용량을 보장하는 수치는 아닙니다. 사용량이 많은 그룹에는 더 높은 한도의 정책을 별도로 마련할 수 있습니다.

원문에 따르면 **Power Apps Premium 라이선스 사용자에게는 앱 실행을 위한 지출 정책이 필요하지 않습니다.** 조직의 실제 라이선스와 청구 조건은 [라이선스 및 청구 안내](https://learn.microsoft.com/microsoft-365/admin/manage/apps/?view=o365-worldwide#licensing-and-billing)에서 확인해야 합니다.

## 도입 담당자가 확인할 사항

초안과 게시된 앱 모두 **Apps > All apps**에 표시됩니다. 관리자는 앱 정보를 검토하고 차단·삭제 등 수명 주기 작업을 수행할 수 있습니다. 프리뷰 때 만든 앱도 이번 점검 대상에 포함하는 편이 좋습니다.

국내 조직에서는 메이커 교육을 늘리기 전에 개인 환경 정책, 공유 범위, 데이터 권한, 비용 담당자를 먼저 정리하는 접근을 권합니다. 앱을 쉽게 만드는 것과 안전하게 운영하는 것은 별개의 과제이기 때문입니다.

## 마무리

Managed Runtime의 GA는 Copilot 앱 제작을 실험에서 관리 가능한 운영 단계로 확장하는 변화입니다. 기능 배포 확인과 함께 환경 라우팅 및 지출 정책을 준비하면, 제작의 편의성과 IT 통제를 함께 확보할 수 있습니다.

> **출처**: [MC1558033 — Microsoft 365 Copilot: Copilot Managed Runtime expands app building at general availability](https://mc.merill.net/message/MC1558033)
>
> **Microsoft 365 Roadmap**: [공식 로드맵](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 명시되지 않았습니다.
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
