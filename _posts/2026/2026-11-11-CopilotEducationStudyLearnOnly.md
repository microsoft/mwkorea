---
title: "정답 대신 학습 과정을 돕는 Copilot: 학교가 선택하는 Study and Learn 전용 모드"
date: 2026-11-11T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Education
  - StudyAndLearn
  - Administration
excerpt: "교육기관 관리자가 학생의 Copilot Chat을 Study and Learn 에이전트로 제한할 수 있게 됩니다. 대상 라이선스, 기존 채팅에 미치는 영향, 2026년 11~12월 예정된 배포 일정을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 정답 대신 학습 과정을 돕는 Copilot: 학교가 선택하는 Study and Learn 전용 모드

학생에게 AI를 제공할 때 중요한 것은 답을 얼마나 빨리 얻느냐만이 아닙니다. 스스로 생각하고 시행착오를 거치는 학습 과정을 어떻게 지킬지도 함께 고려해야 합니다.

Microsoft의 MC1548047 공지는 교육기관 IT 관리자가 Copilot Chat을 **Study and Learn 에이전트만 사용하는 환경**으로 제한할 수 있는 선택지를 소개합니다. Study and Learn은 학생 대신 과제를 수행하기보다, 학습에 필요한 생산적인 고민을 유지하도록 설계된 AI 튜터이자 코치입니다.

---

## 무엇이 달라지나요?

관리자가 전용 모드를 활성화하면 학생은 항상 Study and Learn으로 진입합니다. 에이전트를 닫고 일반 Copilot Chat으로 돌아가거나, 다른 에이전트·스킬·기능을 선택할 수 없습니다.

| 항목 | 전용 모드에서의 동작 |
|---|---|
| 일반 Copilot Chat 전환 | 불가 |
| 다른 에이전트·스킬·기능 선택 | 불가 |
| 학생 본인의 파일을 참고자료로 추가 | 계속 가능 |
| 기존 Copilot 채팅 | Study and Learn과 함께 이용 가능 |
| 다른 에이전트와 나눈 기존 채팅 | 읽기 전용 |

![Microsoft 365 관리 센터의 Study and Learn 전용 모드 설정](/mwkorea/assets/images/2026-11-11-CopilotEducationStudyLearnOnly/image1.png)

단순히 기본 시작 화면만 바꾸는 설정이 아니라 **학생이 이용할 수 있는 대화 경험의 범위를 제한하는 관리 기능**이라는 점이 핵심입니다.

## 대상과 배포 일정

공지의 대상은 **Starter Education 라이선스(A1, A3, A5)를 사용하는 학생**입니다. 별도의 Microsoft 365 Copilot 라이선스는 필요하지 않습니다.

전 세계 일반 공급(GA) 배포는 **2026년 11월 중순 시작, 12월 중순 완료 예정**입니다. 이는 공지 시점의 예정 일정이며 모든 테넌트에 이미 제공되었다는 의미는 아닙니다.

적용 범위에는 웹과 앱의 Copilot Chat, 에이전트 스토어, 직접 링크, 이전 채팅이 포함됩니다. Teams와 Outlook에서도 일부 범위에서 제공된다고 설명하지만, 원문은 두 앱에서의 완전한 기능 동일성을 약속하지 않습니다.

## 학교 IT 관리자가 준비할 일

설정은 **Microsoft 365 관리 센터의 Microsoft Education 패널**에서 제공합니다. 필수 조치는 없으며 학교가 교육 목적에 맞춰 활성화 여부를 판단하면 됩니다.

도입 전에는 일반 채팅과 다른 에이전트의 사용이 제한되고 기존 대화 일부가 읽기 전용으로 바뀐다는 점을 교사와 학생에게 안내하는 것이 좋습니다. 파일 첨부는 계속 가능하므로 학습자료 활용 지침도 함께 정리할 수 있습니다.

교육 테넌트와 학생 연령 설정은 다음 공식 문서를 참고할 수 있습니다.

- [Education Tenant Identifier 설정](https://learn.microsoft.com/microsoft-365/education/guide/2-baseline/setup/baseline-setup-tenant-identifier)
- [학생 연령 그룹 설정](https://learn.microsoft.com/microsoft-365/education/guide/2-baseline/setup/baseline-setup-set-student-age-group)

## 관리자용 설정 안내 영상

원문은 13세 이상 학생을 위한 Copilot Chat 관리자 설정 안내 영상을 연결합니다. 전용 모드만을 설명하는 데모로 단정하지 않고, 교육기관의 기본 설정을 이해하는 참고자료로 활용하세요.

{% include video id="PBMUtNZizM8" provider="youtube" %}

## 마무리

이번 변화는 학생용 AI를 일괄 차단하는 것과 모든 기능을 개방하는 것 사이에 새로운 운영 선택지를 제공합니다. 학교의 목표가 답안 생성보다 학습 과정 지원에 있다면, 대상 라이선스와 실제 배포 여부를 확인한 뒤 전용 모드를 검토해 볼 수 있습니다.

> 출처: [MC1548047 — Microsoft Copilot Chat: New Study and Learn-only mode for Education](https://mc.merill.net/message/MC1548047)  
> [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 기재되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
