---
title: "말로 설명한 업무 도구를 앱으로: Copilot Code, Frontier 배포 시작"
date: 2026-10-22T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotCode
  - Frontier
  - WorkIQ
  - Governance
excerpt: "Copilot Code가 2026년 10월 말 Frontier 프로그램에서 배포를 시작합니다. 자연어로 업무 앱을 만들고 게시하는 경험이지만, Copilot 라이선스 외에 사용량 기반 과금과 지출 정책을 함께 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 말로 설명한 업무 도구를 앱으로: Copilot Code, Frontier 배포 시작

팀의 요청 현황을 추적하는 도구나 프로젝트 대시보드를 만들 때, 업무를 가장 잘 아는 사람이 필요한 기능을 직접 설명하고 구현까지 이어 갈 수 있다면 어떨까요? Microsoft는 Copilot 안에서 자연어로 솔루션을 만드는 **Copilot Code**를 안내했습니다.

이번 공지는 **2026년 10월 말 Frontier 배포 시작**에 관한 것입니다. 모든 Microsoft 365 Copilot 사용자에게 일반 제공이 완료됐다는 의미는 아니며, 사용 자격과 비용 정책을 관리자가 먼저 점검해야 합니다.

---

## 업무 맥락을 이해하며 만들고 수정하는 경험

사용자는 Copilot 앱 탐색 메뉴의 Code에서 만들고 싶은 것을 설명합니다. Copilot은 필요한 사항을 되묻고, 대화나 직접 편집을 통해 결과물을 다듬을 수 있게 합니다.

Work IQ는 이메일, 회의, 문서, 채팅, 연결된 데이터를 바탕으로 업무 맥락을 제공합니다. 예를 들어 프로젝트 현황을 보여 주는 앱을 구상할 때 업무 자료를 맥락으로 활용하는 방식입니다. 다만 **기초 데이터에 대한 접근은 계속 사용자의 권한을 따릅니다.**

![Copilot Code 안내 이미지](/mwkorea/assets/images/2026-10-22-CopilotCodeFrontier/image1.png)

## 게시와 실행 환경

만든 프로젝트는 Microsoft가 관리하는 클라우드 환경인 **Copilot Managed Runtime**에 게시하고 조직 내 다른 사용자와 공유할 수 있습니다. 공지는 게시된 앱이 조직의 거버넌스·보안·관리 제어를 적용받는다고 설명합니다.

관리자가 허용하면 GitHub를 연결할 수 있습니다. PC에서는 로컬 코딩을 켠 경우 로컬 파일과 도구, 터미널도 활용할 수 있지만, 이는 기본 클라우드 실행과 구분되는 선택 사항입니다.

## 라이선스만으로 끝나지 않는 사용 조건

Copilot Code를 실제로 사용하려면 **Microsoft 365 Copilot 라이선스와 지출 정책(spending policy)**이 필요하며 사용량 기반 과금이 적용됩니다.

| 관리 상태 | 사용자가 경험하는 동작 |
|---|---|
| 지출 정책 할당, 실행 위치 Cloud | 웹과 PC에서 클라우드 코딩 사용 |
| 지출 정책 할당, 실행 위치 Cloud and local | 클라우드 코딩과 PC 로컬 코딩 사용 |
| 정책 미할당, 사용량 기반 AI 경험 탐색 허용 | Code 진입점과 환영 화면은 보이지만 사용 불가 |
| 정책 미할당, 탐색도 허용하지 않음 | Code 진입점 숨김 |

**로컬 코딩은 기본적으로 꺼져 있습니다.** 관리자는 Microsoft 365 관리 센터의 Code execution location을 Cloud and local로 바꿔 PC 로컬 실행을 허용할 수 있습니다.

기존 지출 정책에서 **Allow new Agents and services as they become available**이 켜져 있으면 해당 정책을 적용받는 사용자가 Code 접근 권한을 자동으로 받을 수 있습니다. 자동 포함 범위를 비용 관리 관점에서 확인할 필요가 있습니다.

## 도입 담당자가 준비할 사항

- 통합 Microsoft Copilot 앱을 배포하고, Frontier에 참여하는 Windows 장치의 대상 채널을 **Beta**로 설정합니다.
- 관리 센터 **Copilot > Cost management**에서 Copilot Credit 소비와 대상 사용자의 지출 정책을 확인합니다.
- 클라우드 전용 실행과 클라우드·로컬 병행 실행 중 조직에 맞는 범위를 정합니다.
- GitHub 연결, 게시 앱 공유, 데이터 접근 권한, 사용자의 접근 요청 절차를 지원팀과 정리합니다.

원문은 프로젝트·앱 생성에 따른 새로운 고객 데이터 저장, Work IQ를 통한 데이터 처리, 선택적 외부 통합 및 로컬 파일 상호작용을 검토 대상으로 제시합니다. 앱을 쉽게 만드는 것과 조직에서 안전하게 운영하는 것은 함께 설계해야 합니다.

## 마무리

Copilot Code의 의미는 업무 담당자가 자연어로 앱을 만들 수 있다는 데만 있지 않습니다. 업무 맥락을 활용해 만들고, 관리되는 실행 환경에 게시하는 흐름을 Copilot 안으로 가져온다는 점이 중요합니다. 초기 도입은 Frontier 대상과 지출 정책을 좁혀 시작하는 방식이 적절합니다.

> 출처: **MC1519871 — Copilot Code is rolling out in Frontier**, [Microsoft 365 Message Center Archive](https://mc.merill.net/message/MC1519871). 관련 일정은 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서도 확인하세요. 이 공지에는 개별 Roadmap ID가 제시되지 않았습니다. **실제 출시 일정·기능은 변경될 수 있습니다.**
