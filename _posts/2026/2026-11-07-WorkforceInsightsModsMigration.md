---
title: "Workforce Insights 조직 데이터, 11월 18일 전에 Microsoft 365 profile로 전환하세요"
date: 2026-11-07T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - WorkforceInsights
  - MODS
  - Microsoft365Profile
  - Agent
  - Frontier
  - DataGovernance
excerpt: "MODS의 Workforce Insights 전용 엔드포인트가 2026년 11월 18일부터 폐지됩니다. 조직 데이터 수집 경로를 Microsoft 365 profile로 직접 전환해야 하며, 직무 레벨 같은 비공개 사용자 정의 속성은 private preview 참여와 접근 정책 검토가 필요합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Workforce Insights 조직 데이터, 11월 18일 전에 Microsoft 365 profile로 전환하세요

에이전트가 조직에 대해 답하려면 최신 조직 데이터가 필요합니다. 데이터를 한 번 올려 두는 것만으로는 충분하지 않습니다. 업로드 경로가 폐지되면 기존 데이터가 남아 있더라도 이후 변경 사항을 반영하지 못할 수 있습니다.

Microsoft는 **Microsoft 365 Organizational Data Service(MODS)**에서 Workforce Insights 전용 엔드포인트를 폐지하고, 앞으로 **Microsoft 365 profile 엔드포인트**를 통해 조직 데이터를 전달하도록 변경한다고 안내했습니다.

MC1542066의 원문은 미국 기준 2026년 11월 6일에 게시되었으며, RSS 발행 시각은 한국시간 11월 7일입니다. 전용 엔드포인트 폐지 시작일은 **2026년 11월 18일**이므로, 현재 이 경로에 사용자 정의 속성을 업로드하는 조직은 전환을 서둘러야 합니다.

---

## 어떤 서비스가 바뀌나요?

MODS는 조직 데이터를 Microsoft 365에 가져오는 서비스입니다. 이번 변경은 그 안에서 **Workforce Insights agent에 사용자 정의 조직 속성을 전달하는 수집 대상**을 바꿉니다.

| 구분 | 변경 내용 |
|---|---|
| 기존 경로 | MODS의 Workforce Insights 전용 엔드포인트 |
| 새 경로 | MODS의 Microsoft 365 profile 엔드포인트 |
| 기존 엔드포인트 폐지 | 2026년 11월 18일부터 |
| 전환 방식 | 관리자가 새 엔드포인트를 명시적으로 선택 |
| 주요 담당자 | Organizational Data Source Administrator |

**기존 선택은 자동으로 이전되지 않습니다.** Workforce Insights 엔드포인트를 선택해 둔 상태가 Microsoft 365 profile 선택으로 이어지는 것이 아니므로, 관리자가 직접 수집 대상을 바꿔야 합니다.

현재 Workforce Insights 엔드포인트에 사용자 정의 속성을 보내지 않는 조직은 즉시 수행해야 할 조치는 없습니다. 다만 앞으로 Copilot과 Workforce Insights에서 조직 속성을 활용하려는 조직은 새 경로와 제공 단계를 확인해야 합니다.

## 공개 속성과 비공개 속성은 제공 단계가 다릅니다

원문은 세 가지 상태를 구분합니다.

| 대상 | 원문 시점의 제공 단계 |
|---|---|
| Workforce Insights agent 자체 | Microsoft Frontier 프로그램의 프리뷰 |
| Microsoft 365 profile을 통한 사용자 정의 공개 속성 수집 | 일반 공급, GA |
| 사용자 정의 비공개 속성 수집 | Private preview 참여 필요 |

따라서 “새 엔드포인트가 있으니 모든 속성을 바로 옮길 수 있다”고 해석하면 안 됩니다. **공개 속성 수집의 GA와 에이전트 프리뷰, 비공개 속성 private preview는 서로 다른 범위**입니다.

직무 레벨(job level)처럼 원문이 비공개 속성의 예로 든 정보를 가져오려면, 기존에 사용 중인 조직과 처음 도입하는 조직 모두 private preview에 참여해야 합니다. 신청 연락처는 원문의 Message Center 안내에서 확인하세요.

여기서 공개·비공개는 원문이 구분하는 조직 속성 유형입니다. 이를 인터넷 공개 여부나 특정 데이터의 자동 공개로 확대 해석해서는 안 됩니다. 실제 적용 시에는 데이터 거버넌스 담당자와 속성의 접근 정책을 검토해야 합니다.

## 전환하지 않으면 데이터는 어떻게 되나요?

원문에 따르면 이전에 Workforce Insights 엔드포인트로 업로드한 데이터는 남아 있어 Workforce Insights agent와 Copilot의 조직 관련 질의에 계속 사용됩니다. 하지만 **폐지된 엔드포인트로 후속 데이터를 업로드할 수 없으므로 기존 데이터는 갱신되지 않은 상태로 남습니다.**

이는 “데이터가 모두 즉시 삭제된다”는 변화가 아닙니다. 반대로 “기존 데이터가 남으니 아무 조치도 필요 없다”는 의미도 아닙니다. 예를 들어 조직 이동이나 속성 변경이 발생해도 이전 업로드 데이터가 계속 쓰이는 상황을 피하려면 새 수집 경로로 전환해야 합니다.

데이터 업데이트·변경·관리 방법은 [CSV 파일로 조직 데이터를 가져오고 관리하기](https://learn.microsoft.com/microsoft-365-apps/org-data-service/import/import-orgdata#update-or-make-other-changes-to-your-data)를 확인할 수 있습니다.

## 11월 18일 전에 확인할 체크포인트

1. 현재 Workforce Insights 엔드포인트에 넣는 사용자 정의 속성을 목록화합니다.
2. 공개 속성은 MODS의 **Microsoft 365 profile 엔드포인트**를 선택해 최신 데이터로 수집합니다.
3. 비공개 속성을 사용한다면 원문 안내에 따라 private preview 참여를 요청합니다.
4. 개인정보·데이터 거버넌스 담당자와 비공개 속성의 접근 정책을 정한 뒤 새 경로로 수집합니다.
5. 프리뷰 시작 시 기존 Workforce Insights 엔드포인트가 화면에 남아 있더라도 새 업로드 대상으로 선택하지 않습니다.
6. **2026년 11월 18일 전에 전환을 완료**합니다.

전환 후에는 업로드 경로뿐 아니라 데이터의 최신성도 확인하는 것이 좋습니다. 조직 질의가 계속 응답한다고 해서 새 데이터가 반영되고 있다고 볼 수는 없기 때문입니다.

## 에이전트 전용 데이터라는 가정도 점검하세요

원문은 비공개 속성이 향후 기능 배포에 따라 **Workforce Insights agent뿐 아니라 Copilot 경험에도 제공될 수 있음**을 명시합니다. 기존 고객의 수집 속성이 Microsoft 365 profile, Copilot 경험, Workforce Insights agent에서 이용 가능해지는 변화도 컴플라이언스 고려 사항으로 설명합니다.

따라서 전환을 단순한 기술 설정 변경으로만 처리하기보다, 어떤 속성을 누구에게 어떤 용도로 제공할지 재검토해야 합니다. 특정 에이전트만 이용한다는 기존 가정이 조직의 데이터 정책과 일치하는지도 확인하세요.

## 마무리

이번 공지에서 중요한 것은 **자동 이전이 없다는 점, 기존 데이터는 남지만 갱신이 중단된다는 점, 비공개 속성에는 private preview가 필요하다는 점**입니다. 현재 사용자 정의 속성을 수집하는 조직이라면 데이터 담당자와 거버넌스 담당자가 함께 11월 18일 이전 전환을 준비해야 합니다.

시작할 때는 [Workforce Insights agent 개요](https://learn.microsoft.com/microsoft-365/copilot/workforce-insights-agent)와 [MODS 소개](https://learn.microsoft.com/microsoft-365-apps/org-data-service/organizational-data)를 참고하세요. 제공 단계와 마감 설명은 MC 원문 시점 기준입니다.

> 출처: **MC1542066** — [Microsoft 365 Copilot: Changes to custom organizational data in MODS for Workforce Insights](https://mc.merill.net/message/MC1542066). 원문에는 개별 Roadmap ID가 기재되어 있지 않습니다. [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 후속 공개 정보를 확인할 수 있습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
