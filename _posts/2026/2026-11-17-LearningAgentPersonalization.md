---
title: "내 업무에 맞춰 배우는 Copilot: Learning Agent 개인화 학습"
date: 2026-11-17T00:00:00 KST
categories:
  - Copilot
tags:
  - LearningAgent
  - Personalization
  - Microsoft365Copilot
excerpt: "Learning Agent가 역할과 프로젝트, Teams 채팅·메일·회의 기록 등 업무 맥락에 맞는 학습을 제안합니다. 공개 프리뷰와 GA 일정, 조직 및 사용자 측 필수 개인화 설정을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 내 업무에 맞춰 배우는 Copilot: Learning Agent 개인화 학습

Copilot 교육에서 어려운 점은 기능을 아는 것과 자기 업무에 적용하는 것 사이의 간극입니다. MC1556094는 Learning Agent가 사용자의 업무 맥락을 반영해 학습을 개인화하는 변화를 안내합니다.

일괄 교육 과정만 보여 주는 대신 역할·진행 중 프로젝트·업무 활동에 맞춰 학습 기회를 제안하는 방향입니다. 동시에 업무 정보가 개인화에 활용되는 만큼 조직과 사용자 양쪽의 설정을 확인해야 합니다.

---

## 어떤 경험이 추가되나요?

개인화된 홈페이지, 학습 프롬프트, 추천이 제공됩니다. 맥락에는 Teams 채팅, 이메일, 회의 대화 기록이 포함됩니다.

목표는 역할과 직무 초점에 맞는 학습을 제시하고, 일상 업무에 Copilot을 적용하도록 도우며, 필요한 학습을 직접 검색하는 부담을 줄이는 것입니다. 업무 우선순위가 달라지면 학습 경험도 이에 맞춰 변화하도록 설계되었습니다.

![Learning Agent 개인화 학습 관련 화면](/mwkorea/assets/images/2026-11-17-LearningAgentPersonalization/image1.png)

## 제공 일정

| 단계 | 공지의 예상 일정 |
|---|---|
| 공개 프리뷰 | 2026년 11월 중순 시작~말 완료 |
| Worldwide GA | 2026년 12월 중순 시작~말 완료 |

기능 자체는 자동 배포되지만, 개인화 경험이 동작하려면 아래 설정이 활성화되어 있어야 합니다.

## 조직과 사용자가 각각 확인할 설정

관리자는 조직의 **Enhanced personalization**을 활성화해야 합니다. 사용자는 Microsoft Copilot 설정의 **Chat history and Work Insights** 토글을 켜야 합니다.

즉 “자동 배포되니 별도 조건이 없다”는 해석은 맞지 않습니다. 기능 제공 여부와 실제 개인화 사용 조건을 나눠 안내해야 합니다.

관련 API 자료인 [enhancedPersonalizationSetting 리소스](https://learn.microsoft.com/graph/api/resources/enhancedpersonalizationsetting?view=graph-rest-beta)는 Graph **beta** 문서이므로, 안정 버전 API로 단정하지 않도록 주의하세요.

## 도입 담당자가 할 일

조직 교육 담당자는 일반 교육과 업무 맥락형 추천의 역할을 구분하고, 개인정보 담당자와 활용 데이터 및 사용자 설정 안내를 검토하는 것이 좋습니다. 학습 개인화가 곧 직원 평가나 검증된 역량 점수 제공을 뜻하는 것은 아닙니다.

> **출처**: [MC1556094](https://mc.merill.net/message/MC1556094), Microsoft 365 Message Center Archive. [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제시되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
