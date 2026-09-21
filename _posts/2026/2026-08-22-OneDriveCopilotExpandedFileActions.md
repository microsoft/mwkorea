---
title: "OneDrive Web의 Copilot 파일 작업 확대: 찾기부터 생성·공유까지"
date: 2026-08-22T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - OneDrive
  - SharePoint
  - FileActions
  - Governance
  - PublicPreview
excerpt: "OneDrive Web의 Copilot이 자연어로 파일을 찾고 이해·분석하며 새 콘텐츠를 만들고 파일 작업을 수행하는 경험으로 확대됩니다. 2026년 8월 24일부터 opt-out 미리 보기로 배포되며, OneDrive와 SharePoint가 동일한 테넌트 수준 미리 보기 제어를 공유합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# OneDrive Web의 Copilot 파일 작업 확대: 찾기부터 생성·공유까지

SharePoint의 expanded preview에서 제공되던 Copilot 경험이 OneDrive Web으로 확장됩니다. 사용자는 파일을 하나씩 열거나 폴더를 직접 뒤지지 않고 자연어로 필요한 내용을 찾고, 이해하고, 분석하고, 새 콘텐츠를 만들며 후속 작업까지 이어갈 수 있습니다.

관리자가 가장 주의할 부분은 배포 방식입니다. 이번 기능은 2026년 8월 24일부터 적격 테넌트에 **opt-out 미리 보기**로 배포되며, OneDrive와 SharePoint의 Copilot 미리 보기 제어가 하나로 묶여 있어 제품별로 따로 끌 수 없습니다.

---

## OneDrive 안에서 가능한 작업

Microsoft 365 Copilot 라이선스 사용자는 OneDrive Home, My Files, Shared, People, Meetings 보기와 PDF를 포함한 지원 파일 미리 보기에서 갱신된 Copilot 진입점을 보게 됩니다.

자연어로 수행할 수 있는 대표 작업은 다음과 같습니다.

- 프로젝트, 주제, 회의, 사람, 최근 활동과 관련된 파일 찾기
- 문서, 프레젠테이션, PDF, 이미지, 회의 녹화 등 지원 콘텐츠 요약
- 파일 내용 질문과 버전 간 변경점 비교
- 스프레드시트와 여러 문서의 추세·차이 분석
- 선택한 파일·폴더 또는 관련 업무 맥락을 바탕으로 FAQ, 보고서, 프레젠테이션, Office 문서, 동적 HTML 대시보드 초안 생성
- 파일·폴더 공유 지원, 권한 확인, 공유 설정 갱신

질문은 지원되는 Microsoft 365 위치의 맥락을 활용할 수 있으며 공지는 OneDrive, SharePoint, Teams, Outlook을 예로 듭니다. 실제 지원 형식과 문맥에 따라 가능한 작업은 달라질 수 있습니다.

## 권한을 새로 부여하지 않습니다

Copilot in OneDrive는 사용자의 기존 파일·폴더 권한 안에서 동작합니다. 사용자가 이미 보거나 편집할 권한이 있는 콘텐츠만 접근하고 요약·분석·작업할 수 있으며, Copilot이 파일, 폴더, 라이브러리, 사이트 또는 다른 Microsoft 365 콘텐츠의 새 접근 권한을 부여하지 않습니다.

기존 민감도 레이블, 보존 정책, 공유 제어, 접근 제한도 계속 적용됩니다. 생성된 응답은 사용자가 접근할 수 있는 콘텐츠에 근거합니다. 파일 생성·이동·이름 변경·공유·삭제처럼 콘텐츠를 바꾸는 작업은 완료 전에 사용자의 검토 또는 확인을 요구합니다.

이 기능은 Purview Communication Compliance, eDiscovery, Data Retention, Sensitivity Labels, Customer Lockbox, DLP를 지원하며 저장 데이터용 Customer Key, 역할 기반 접근 제어, 상위 서비스의 데이터 상주·처리 약정도 따릅니다. 새로 생성된 개체는 Agent 365 Registry 인벤토리에 나타납니다.

## 미리 보기 제어는 SharePoint와 공동입니다

관리자는 PowerShell cmdlet으로 테넌트 전체를 미리 보기에서 제외할 수 있습니다. 하지만 **Copilot in OneDrive와 Copilot in SharePoint가 동일한 테넌트 수준 미리 보기 제어를 사용**합니다.

따라서 opt-out하면 OneDrive만 꺼지는 것이 아니라 두 제품의 Copilot 미리 보기가 모두 비활성화됩니다. OneDrive와 SharePoint를 각각 제어하는 별도 설정은 없습니다. 변경 전에 SharePoint 담당자와 OneDrive 담당자가 함께 영향 범위를 확인해야 합니다.

정식 출시를 기다리려는 조직이나 미리 보기 사용을 제한하는 정책이 있는 조직은 [SharePoint AI 시작 문서](https://learn.microsoft.com/sharepoint/ai-in-sharepoint-get-started)의 opt-out 절차를 검토하세요.

## 출시 일정과 라이선스

| 단계 | 일정 |
|---|---|
| Opt-out 미리 보기 시작 | 2026년 8월 24일 |
| Public Preview, Worldwide | 2026년 8월 말 시작, 9월 말 완료 예상 |
| General Availability, Worldwide | 2026년 12월 말 시작 및 완료 예상 |

대상은 **Microsoft 365 Copilot 라이선스가 있는 OneDrive Web 사용자**입니다. 라이선스가 없는 사용자는 Copilot in OneDrive 기능에 접근할 수 없습니다. 미리 보기를 받기 위한 별도 작업은 필요하지 않으며 적격 사용자에게 자동 갱신됩니다.

## 준비 체크리스트

1. 미리 보기 사용 여부를 OneDrive·SharePoint 공동 의사결정으로 정합니다.
2. 대상 사용자에게 Microsoft 365 Copilot 라이선스가 있는지 확인합니다.
3. 민감한 파일·폴더의 기존 권한과 공유 링크를 점검합니다.
4. 민감도 레이블, 보존, DLP, 접근 제한 정책을 검토합니다.
5. 변경 작업은 사용자 확인 후 실행된다는 점을 교육합니다.
6. 미리 보기 opt-out이 두 제품에 동시에 적용된다는 점을 변경 기록에 남깁니다.
7. Helpdesk에 Home, My Files, Shared, People, Meetings 등 새 진입 위치를 안내합니다.

## 정리

이번 업데이트는 OneDrive의 Copilot을 단순 파일 요약에서 **찾기·분석·생성·작업**을 잇는 경험으로 넓힙니다. 사용자가 파일을 열지 않고도 업무의 다음 단계로 이동할 수 있다는 점이 가장 큰 변화입니다.

동시에 opt-out 미리 보기이고 SharePoint와 제어를 공유한다는 운영 조건이 중요합니다. 기존 권한과 거버넌스가 계속 적용되더라도, 확대된 검색과 작업 범위를 고려해 권한·공유 상태를 배포 전에 점검해야 합니다.

---

> **출처**
>
> - 원문 ID: **MC1459130** — *Improved capabilities for files with Copilot in OneDrive Web*
> - 메시지 센터: [https://mc.merill.net/message/MC1459130](https://mc.merill.net/message/MC1459130)
> - Microsoft 365 로드맵: [https://www.microsoft.com/microsoft-365/roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
