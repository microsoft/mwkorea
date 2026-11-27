---
title: "SPFx 자동 배포가 멈추기 전에: SharePoint App Catalog의 새 앱 전용 권한을 확인하세요"
date: 2026-11-25T00:00:00 KST
categories:
  - Copilot
tags:
  - SharePoint
  - SPFx
  - Microsoft365Copilot
  - MicrosoftEntra
  - AppCatalog
  - CICD
excerpt: "SharePoint 테넌트 App Catalog에 패키지를 업로드하거나 수정하는 앱 전용 자동화에 추가 권한이 요구됩니다. 2027년 1월 31일 예정된 변경을 앞두고 SPFx 배포 파이프라인과 무인 스크립트의 인증 리소스, 관리자 동의, 토큰을 점검하는 방법을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# SPFx 자동 배포가 멈추기 전에: SharePoint App Catalog의 새 앱 전용 권한을 확인하세요

Copilot 확장과 사내 업무 솔루션을 운영하다 보면, SharePoint Framework(SPFx) 패키지를 배포하는 과정도 자동화하게 됩니다. 개발자가 직접 파일을 올리는 대신 CI/CD 파이프라인이나 인증서 기반 PnP PowerShell 작업이 테넌트 App Catalog를 갱신하는 방식입니다.

Microsoft는 2026년 11월 25일, 이처럼 **앱 전용(app-only) 인증으로 테넌트 App Catalog의 특정 영역에 직접 쓰는 작업에 추가 권한 검사**를 도입한다고 발표했습니다. 예정된 기준일은 **2027년 1월 31일**입니다. 현재 배포가 정상이어도 다음 패키지 업데이트에서 문제가 생길 수 있으므로 운영 인증을 미리 확인해야 합니다.

이 글은 원문 발표 시점의 적용 범위를 정리합니다. 모든 Copilot 실행이나 모든 SharePoint API가 바뀐다는 뜻은 아니며, 실제 영향은 **인증 방식과 수행 작업**의 조합으로 판단해야 합니다.

---

## 무엇이 달라지나요?

영향받는 직접 app-only 쓰기 작업에는 **Office 365 SharePoint Online 리소스의 `SharePointTenantSettings.ReadWrite.All` 애플리케이션 권한**이 필요합니다.

| 작업 | 새 검사 적용 범위 |
|---|---|
| Apps for SharePoint에 패키지 추가 | app-only로 직접 수행하면 대상 |
| 기존 패키지 교체·업데이트 및 카탈로그 항목 수정 | app-only로 직접 수행하면 대상 |
| Tenant-Wide Extensions 항목 추가·업데이트 | app-only로 직접 수행하면 대상 |

패키지 검사는 App Catalog의 추가·업데이트 진입점에서 수행됩니다. 따라서 **테넌트 전체 확장을 등록하지 않는 패키지라도** app-only 업로드·업데이트라면 새 권한이 필요할 수 있습니다.

기존 `Sites.ReadWrite.All`이나 `Sites.FullControl.All`만으로는 이 추가 검사를 충족하지 못합니다. 그렇다고 새 권한이 기존 사이트 권한을 대체하는 것은 아닙니다. 다른 사이트 작업에 필요한 권한은 그대로 유지해야 하고, 패키지·컴포넌트 검증 등 다른 검사도 계속 적용됩니다.

## 같은 권한 이름이라도 리소스가 다르면 다릅니다

이번 변경에서 가장 혼동하기 쉬운 부분은 **Microsoft Graph와 Office 365 SharePoint Online에 같은 이름의 권한이 존재한다**는 점입니다. 두 권한은 서로 다른 리소스에 속한 별도의 애플리케이션 역할입니다.

PnP PowerShell, SharePoint REST, CSOM으로 SharePoint에 직접 요청하는 자동화라면 다음을 확인해야 합니다.

- 권한을 부여한 리소스가 **Office 365 SharePoint Online**인지 확인합니다.
- 해당 리소스의 **애플리케이션 권한**으로 `SharePointTenantSettings.ReadWrite.All`을 추가합니다.
- 새로 발급받은 **SharePoint 액세스 토큰**에 그 권한이 포함되어야 합니다.

Microsoft Graph의 동명 권한만 추가해서는 SharePoint의 권한 검사를 만족하지 않습니다. 반대로 이번 발표만으로 모든 Graph 작업이 영향을 받는다고 판단해서도 안 됩니다. Graph 통합은 사용하는 API와 인증 흐름을 별도로 검토해야 합니다.

## 어떤 배포 방식이 영향을 받나요?

| 사용 방식 | 영향 |
|---|---|
| 권한 있는 관리자가 App Catalog UI에서 직접 업로드 | 새 애플리케이션 권한 요구사항은 적용되지 않음 |
| 사용자·위임 인증으로 실행하는 PnP PowerShell | 기존 사용자·위임 권한 적용 |
| 인증서 기반 무인 PnP PowerShell | 대상 쓰기 작업이면 새 권한 필요 |
| app-only 인증의 SharePoint REST·CSOM 앱 | 대상 쓰기 작업이면 새 권한 필요 |
| 고객 테넌트에 패키지를 배포하는 파트너 서비스 | 같은 인증·작업 조건으로 점검 필요 |

즉, PnP PowerShell이나 SPFx를 사용한다는 사실만으로 영향 대상이 되는 것은 아닙니다. **사용자 대신 앱이 인증하고, 해당 테넌트 카탈로그 쓰기를 수행하는지**를 확인하는 것이 먼저입니다.

## 배포 담당자의 점검 순서

1. 패키지 업로드·업데이트 또는 Tenant-Wide Extensions 갱신에 사용하는 Microsoft Entra 앱 등록을 식별합니다.
2. **Office 365 SharePoint Online**의 `SharePointTenantSettings.ReadWrite.All` **애플리케이션 권한**을 추가합니다.
3. 테넌트 관리자의 동의를 받습니다.
4. 연결을 다시 하거나 인증을 갱신해 **새 SharePoint 액세스 토큰**을 발급받습니다.
5. 패키지 추가, 기존 패키지 수정, Tenant-Wide Extensions 변경 중 실제 사용하는 작업을 다시 시험합니다.
6. 다른 작업에 필요한 기존 권한은 유지합니다.

권한 추가와 관리자 동의만 끝내고 오래된 토큰을 계속 사용하는 상황을 피해야 합니다. 내부 운영에서는 어떤 앱이 어떤 테넌트에 배포하는지 목록으로 관리하고, 권한 변경과 재시험 결과를 함께 기록하는 것을 권장합니다. 이는 원문의 권한 요구사항을 운영에 적용하기 위한 실무 제안입니다.

## 이번 변경에 포함되지 않는 범위

원문은 다음을 새 app-only 권한 요구사항의 대상에서 제외합니다.

- 권한 있는 관리자의 대화형 App Catalog 작업과 사용자·위임 인증 요청
- 읽기 전용 App Catalog 작업 및 삭제 작업
- 사이트 컬렉션 App Catalog 작업의 기존 권한 체계
- 이미 배포한 SPFx 솔루션의 런타임 사용
- 별도 권한 경로를 사용하는 신뢰된 내부 배포 작업

위임 인증에서는 필요한 경우 `ManageWeb` 등 기존 권한 요구사항이 계속 적용됩니다. 또한 이미 배포된 솔루션이 실행된다는 사실과 **이후 자동 패키지·설정 업데이트가 성공한다는 사실은 별개**입니다. 런타임에 영향이 없더라도 다음 배포는 새 조건의 대상일 수 있습니다.

## 일정과 참고 문서

**2027년 1월 31일은 원문이 제시한 예정 기준일**입니다. 이후에는 대상 app-only 쓰기에서 새 SharePoint 리소스 권한이 요구되며, `Sites.ReadWrite.All`만 사용하는 흐름은 거부될 수 있습니다. 고객과 파트너는 이 날짜 전에 자동 배포를 점검하고 다시 시험해야 합니다.

- [테넌트 App Catalog 작업의 앱 전용 권한 구성](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/tenant-app-catalog-app-only-permissions)
- [Microsoft Entra ID 앱 전용 접근 구성](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azuread)
- [Microsoft Graph SharePoint 설정 권한 참고](https://learn.microsoft.com/en-us/graph/api/sharepointsettings-get?view=graph-rest-1.0)

마지막 링크는 **Graph 리소스**에 관한 문서입니다. SharePoint 직접 호출에 필요한 Office 365 SharePoint Online 역할의 대체 근거로 사용하지 않아야 합니다. 위 문서는 후속 확인을 위한 링크이며, 이 글이 최신 문서와 발표 이후의 변경 사항까지 별도로 검증했다는 뜻은 아닙니다.

## 마무리

이번 공지는 Copilot의 새 대화 기능보다 **확장 솔루션을 안정적으로 배포하는 기반**에 관한 변화입니다. 사내 Copilot·에이전트 관련 SPFx 솔루션을 자동 배포한다면, 도구 이름이 아니라 인증 방식, 대상 작업, 권한 리소스, 실제 토큰을 기준으로 점검하세요.

> **출처**: [Action required: Update app-only permissions for SharePoint tenant App Catalog writes](https://devblogs.microsoft.com/microsoft365dev/action-required-update-app-only-permissions-for-sharepoint-tenant-app-catalog-writes/) — Microsoft 365 Developer Blog, 2026년 11월 25일. 자세한 내용은 원문 참조.
