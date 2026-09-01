---
title: "2026년 8월 Microsoft Copilot 신기능 총정리: Cowork 노력 수준부터 세션 공유, PowerPoint 브랜드 준수까지"
date: 2026-08-31T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Cowork
  - CopilotChat
  - CopilotNotebooks
  - PowerPoint
  - Excel
  - Outlook
  - WhatsNew
excerpt: "2026년 8월 한 달간 Microsoft Copilot에 추가된 기능을 한 번에 정리했습니다. Cowork의 노력 수준과 /cost 스킬, Copilot Chat의 텍스트 선택·세션 공유, Copilot Notebooks의 OneNote 연동, PowerPoint의 엄격한 브랜드 준수와 노트 스티어링, Excel 변경 이력 스킬, 그리고 관리자용 데이터 내보내기까지 담았습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 2026년 8월 Microsoft Copilot 신기능 총정리

매달 나오는 **What's New in Microsoft Copilot** 8월호가 공개됐습니다. 이번 달은 유독 풍성합니다. Cowork에 비용을 조절하는 손잡이가 생겼고, Copilot Chat에서 답변의 일부만 골라 다시 요청할 수 있게 됐으며, PowerPoint에는 브랜드 가이드를 강제하는 옵션까지 들어왔습니다.

여기서는 원문의 항목을 빠짐없이 정리하되, 한국의 도입 담당자와 사용자가 바로 활용할 수 있도록 풀어 씁니다. 각 항목마다 **출시 시점**을 함께 표기했으니 사내 안내 자료를 만들 때 참고하시면 좋겠습니다.

![What's New in Microsoft Copilot August 2026](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image1.png)

---

## 한눈에 보는 8월 업데이트

**사용자 기능**

- Cowork의 노력 수준(effort level)과 비용 제어
- Copilot Chat의 텍스트 선택·세션 공유 등
- Copilot Notebooks의 새로운 작업 방식
- Teams 회의 요약본 언어 변경
- Word의 하이퍼링크·이미지 이해·편집 하이라이트
- Excel의 채팅 기록과 변경 이력 스킬
- SharePoint의 개인 스킬
- Outlook의 에이전트·이메일 작성·관리 기능 강화
- OneDrive의 파일 기능 개선
- Planner의 상태 보고서와 작업 기능 강화
- 신규 커넥터·플러그인

**IT 관리자 기능**

- 데이터 내보내기와 GitHub Copilot AI 크레딧

---

## Cowork: 노력 수준과 비용 제어

### 노력 수준(Effort level)

이제 사용자가 **노력 수준을 선택해 Cowork가 품질·속도·크레딧 사용을 어떻게 조절할지** 직접 정할 수 있습니다.

| 수준 | 용도 |
|---|---|
| **Light** | 더 단순한 작업 |
| **Medium** | **기본값.** 일상 업무 |
| **High / Extra High / Max** | 더 깊은 분석, 복잡한 추론, 더 철저한 응답 |

높은 수준은 **시간이 더 걸리고 한도를 더 빨리 소진**합니다. 모델과 노력 수준 컨트롤이 **작성창(compose box)에 함께** 표시됩니다. *(8월 출시)*

![Cowork 노력 수준](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image2.png)

### /cost 스킬 강화

**/cost** 스킬이 Cowork 크레딧 사용에 대한 가시성을 넓혔습니다. 현재 작업 세션의 예상 크레딧에 더해 다음을 보여 줍니다.

- **월간 크레딧 한도 잔여 비율**
- **월 누적 사용 크레딧**
- **월간 한도 재설정 시점**

*(8월 출시)*

![/cost 스킬](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image3.png)

### Scheduled 탭 → Automations

Cowork의 **Scheduled 탭이 Automations로 이름이 바뀌었습니다.** 예약 작업과 이벤트 트리거 작업을 **한곳에서** 확인·관리할 수 있습니다. *(8월 출시)*

![Automations 탭](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image4.png)

---

## Copilot Chat: 텍스트 선택과 세션 공유

### 답변의 일부만 골라 작업하기

Chat 응답에서 **문장, 문단, 표를 선택해 그 내용에만 작업을 요청**할 수 있습니다. 선택한 텍스트는 전송 전 프롬프트에 미리 표시되어, 더 집중된 설명·요약·번역·다음 단계 제안이 가능합니다. *(8월 출시)*

![텍스트 선택 기능](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image5.png)

### 세션·응답 공유

**전체 채팅 세션이나 개별 응답을 링크로 공유**할 수 있습니다. 수신자는 **읽기 전용 뷰**를 받고, 자기 것처럼 대화를 이어 갈 수 있습니다. 조직 통제 범위 안에서 작업을 재사용하고 협업하는 방식입니다.

- **전체 세션**: 채팅 UX 우측 상단 Share 메뉴 → **Share chat**
- **개별 응답**: 응답 끝의 More options 메뉴 → **Share response**

*(8월 출시)*

![세션 공유](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image6.png)

### Power BI 데이터 추론

Copilot이 **Chat과 Cowork 양쪽에서 Power BI 보고서와 시맨틱 모델의 엔터프라이즈 데이터를 추론**할 수 있습니다. 자연어로 질문하면 접근 권한이 있는 데이터에서 근거 있는 답을 받습니다. *(6월 공개 미리 보기 → 8월 전 세계 출시)*

![Power BI 데이터 추론](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image7.png)

### 모델 기반 답변 카드

날씨, 스포츠, 금융, 이미지, 동영상, 장소, 뉴스 같은 콘텐츠를 **동적으로 표시하는 답변 카드**가 추가됐습니다. Entra 및 Microsoft 계정 사용자를 대상으로 프롬프트에 맞춰 표시됩니다. *(8월 출시)*

![답변 카드](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image8.png)

### 다시 시도(Try again)

대화를 처음부터 다시 시작하지 않고 **마지막 프롬프트에 대한 새 응답을 생성**할 수 있습니다.

- **Try again** — 같은 모델로 새 응답 생성
- **모델 변경 후 재실행** — 다른 모델로 같은 프롬프트 실행

*(8월 출시)*

![Try again](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image9.png)

### 모바일에서 이메일 초안 생성

모바일 사용자가 필요한 메시지를 설명하면 Copilot이 **Copilot Chat 안에 Outlook 초안을 임베드**해 만들어 줍니다. 그 초안을 Outlook 모바일에서 바로 열어 편집·발송할 수 있습니다. *(8월 출시)*

![모바일 이메일 초안](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image10.png)

---

## Copilot Notebooks: 두 갈래 작업 방식

### Copilot 앱 + OneNote

Copilot Notebooks가 **연결된 두 가지 작업 방식**을 제공합니다.

| 환경 | 성격 |
|---|---|
| **Copilot 앱** | 가벼운 경험 — 빠른 대화, 참조 탐색, 아티팩트 생성 |
| **OneNote** | 워크스페이스 경험 — 심층 프로젝트 작업, 확장된 아티팩트 생성, 팀 협업 |

노트북은 **양쪽에서 동기화**되므로 맥락을 잃지 않고 오갈 수 있습니다. Copilot 앱에서 **"Open in OneNote"** 를 선택하면 바로 이동합니다. *(8월 출시)*

![Copilot Notebooks와 OneNote](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image11.jpg)

### 아티팩트 추천

Copilot Notebooks가 **WorkIQ와 노트북 콘텐츠를 바탕으로 아티팩트를 선제적으로 추천**합니다. 추천을 선택하면 노트북 내용과 현재 프로젝트에 맞는 Word·Excel·PowerPoint 아티팩트를 생성합니다. *(8월 출시)*

![아티팩트 추천](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image12.png)

### 멀티모달 캡처

Android에서 대화, 회의, 브레인스토밍 등의 순간을 Copilot Notebooks로 가져올 수 있습니다. **오디오·이미지·메모를 한 경험에서 캡처**하면 Copilot이 자동으로 구조화된 노트를 만듭니다. **iOS·iPad의 OneNote 앱**에서도 사용 가능합니다. *(9월 출시 예정)*

![멀티모달 캡처](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image13.png)

---

## Teams: 회의 요약본 언어 변경

생성된 **회의 요약본의 언어를 사후에 변경**할 수 있습니다. 번역 버튼을 통해 필요한 언어로 바꿀 수 있어, 다국어 환경에서 요약본 활용이 유연해집니다. *(8월 출시)*

한국 기업의 글로벌 협업 상황에서 특히 유용한 기능입니다.

![회의 요약본 언어 변경](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image14.png)

---

## Word: 하이퍼링크·이미지 이해·편집 하이라이트

### 하이퍼링크 추가

Copilot에게 요청하면 **하이퍼링크를 삽입하고 링크 텍스트를 서식까지 적용**해 줍니다. 수동 편집 없이 연결된 문서를 만들 수 있습니다. *(8월 출시)*

![하이퍼링크 추가](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image15.png)

### 참조 문서의 이미지 이해

Copilot이 **참조 문서 안의 이미지를 이해하고 생성 콘텐츠에 반영**합니다. 새 문서를 쓰든 기존 자료를 발전시키든, 참조 파일의 텍스트와 시각 요소를 함께 활용합니다. *(8월 출시)*

### 편집 부분만 하이라이트

Copilot이 텍스트를 다시 쓰거나 다듬을 때, **문단 전체가 아니라 실제로 수정한 단어만 하이라이트**합니다. 변경 사항을 확인하고 수락하기가 훨씬 수월해집니다. *(8월 전 세계 출시)*

![편집 하이라이트](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image16.png)

---

## PowerPoint: 브랜드 준수와 협업 강화

이번 달 PowerPoint 업데이트는 특히 **브랜드 관리** 측면이 강합니다.

### 댓글에서 작업 할당

Copilot으로 **댓글에서 이해관계자를 태그하고 후속 작업을 자동 할당**할 수 있습니다. 피드백에서 실행으로 넘어가는 속도가 빨라지고, 검토 과정이 정리됩니다. *(8월 출시)*

![PowerPoint 댓글 작업 할당](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image17.jpg)

### 엄격한 브랜드 준수(Strict brand adherence)

Copilot을 **승인된 템플릿과 슬라이드 마스터 레이아웃 안으로 제한**합니다. 켜져 있으면 Copilot이 **자리 표시자를 추가·제거하거나 새 레이아웃을 만들지 않습니다.**

> 브랜드 일관성이 창의적 유연성보다 중요한 경우 — **공식 자료, 고객 대면 자료, 규제 대상 프레젠테이션** — 에 사용하세요.

*(8월 출시)*

### 노트 스티어링(Note steering)

슬라이드 **노트에 평문으로 지시를 적어 두면 Copilot이 그것을 따릅니다.** 슬라이드별 거버넌스가 가능해지는 방식입니다. 템플릿으로 프레젠테이션을 만들 때마다 노트를 읽으므로, **같은 선호를 매번 프롬프트에 반복할 필요가 없습니다.** *(8월 출시)*

자세한 내용은 [Manage template settings in your Brand Kit for Copilot in PowerPoint](https://support.microsoft.com/)를 참고하세요.

![노트 스티어링](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image18.jpg)

### 사용자 지정 스킬

PowerPoint에서 **자신만의 사용자 지정 스킬을 업로드·생성·편집·삭제**할 수 있습니다. 반복되는 지시를 재사용 가능한 가이드로 바꿔, 프레젠테이션 작업 흐름 안에서 Copilot이 적용합니다. *(8월 출시)*

### 번역 기능 이동

번역 기능이 **리본에서 Copilot in PowerPoint로 이동**했습니다. 더 빨라졌고, **텍스트 길이에 따라 텍스트 상자 크기를 동적으로 조정**합니다. *(8월 출시)*

한국어↔영어 번역이 잦은 조직에서 체감이 클 변화입니다. 번역 후 글자가 넘치는 문제를 자동으로 다뤄 주기 때문입니다.

![PowerPoint 번역](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image19.gif)

### SmartArt 편집

Copilot이 **브랜드를 유지하면서 SmartArt를 편집**할 수 있습니다. 다이어그램과 도형을 수동으로 추가·정렬하는 대신 캔버스에서 Copilot으로 처리합니다. *(8월 Frontier)*

---

## Excel: 채팅 기록과 변경 이력 스킬

### 변경 이력 스킬(Change history skill)

통합 문서가 시간에 따라 어떻게 변해 왔는지 파악할 수 있습니다. Copilot이 다음을 수행합니다.

- 최근 변경 사항 요약
- **누가 편집했는지 식별**
- **사람과 AI가 각각 어떻게 수정했는지** 설명
- 특정 편집 취소, 수식 복원, 이전 작동 상태로 되돌리기

*(8월 출시)*

AI가 개입한 변경과 사람이 한 변경을 구분해 준다는 점이 눈에 띕니다. 감사 대응이나 오류 추적에 실질적으로 쓰일 만합니다.

![Excel 변경 이력](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image20.png)

### 채팅 기록

이전 대화와 세션이 보존되어 **하던 작업을 이어서** 할 수 있습니다. Copilot in Excel 창 **좌측 상단 메뉴 아이콘**에서 이전 대화를 열 수 있으며, **최신순으로 정렬**됩니다. *(8월 출시)*

![Excel 채팅 기록](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image21.png)

---

## SharePoint: 개인 스킬

Copilot in SharePoint에서 **개인 스킬(personal skills)을 만들어 여러 SharePoint 사이트와 OneDrive에서 사용**할 수 있습니다. 각 사용자 소유 스킬은 **OneDrive에 마크다운 파일로 저장**되므로, 사이트마다 스킬을 다시 만들 필요가 없습니다. *(8월 공개 미리 보기 → 12월 전 세계 출시)*

---

## Outlook: 에이전트·이메일 작성·관리 강화

### 사용자 지정 엔진 에이전트

**Custom engine agents를 Outlook에서 직접** 사용할 수 있습니다. 업무를 관리하는 그 자리에서 에이전트 기능에 접근합니다. *(8월 출시)*

![Outlook 에이전트](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image22.png)

### 자연어로 메일·일정 관리

Copilot in Outlook이 **자연어로 더 많은 메일·일정 작업**을 처리합니다.

- 메시지 정리
- **범주(category) 적용**
- **폴더 생성**
- **받은편지함 규칙 관리**
- 회의·이벤트에 대한 조치

이 모든 작업을 채팅에서 수행할 수 있습니다. *(8월 출시)*

![Outlook 자연어 관리](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image23.png)

---

## OneDrive: 파일 기능 개선

**채팅에서 파일부터 완성된 결과물까지** 처리할 수 있습니다. Copilot이 적절한 콘텐츠를 찾고, 파일과 데이터를 분석하고, **요약·대시보드·프레젠테이션** 같은 결과물을 만들며, OneDrive에서 저장·공유까지 지원합니다. *(8월 공개 미리 보기 → 12월 전 세계 출시)*

---

## Planner: 상태 보고서와 작업 기능

### 상태 보고서 생성

**Planner Agent**가 계획 데이터를 **진행 상황, 위험, 전체 상태, 다음 단계**를 담은 정돈된 상태 보고서로 만들어 줍니다. **대상 독자, 어조, 길이, 섹션**을 지정해 이해관계자용 업데이트를 빠르게 생성할 수 있습니다. *(8월 Frontier)*

![Planner 상태 보고서](/mwkorea/assets/images/2026-08-31-WhatsNewCopilotAugust2026/image24.png)

### Planner 작업 생성·조회

Copilot이 **Planner 작업 생성과 작업 정보 조회**를 지원합니다. Copilot과 Planner를 오가며 작업을 관리할 수 있습니다. *(9월 출시 예정)*

---

## 신규 커넥터·플러그인

Microsoft가 여러 산업에 걸쳐 커넥터·플러그인 생태계를 계속 넓히고 있습니다.

| 산업 | 커넥터·플러그인 |
|---|---|
| **금융 서비스** | Mercury, Xero |
| **법률 서비스** | iManage Work, Boardwise, Harvey, Descrybe Legal Engine, Relativity, Everlaw |
| **전문·비즈니스 서비스** | Statista, Crossbeam, ZoomInfo, IDC |
| **에너지·자원** | S&P Global Energy |
| **헬스케어·생명과학** | Scite, Consensus |
| **소프트웨어·기술** | Adobe Journey Optimizer, GoDaddy, Asana |

---

## IT 관리자 기능

### 데이터 내보내기

**Copilot 및 Agent 365 대시보드**에서 사용자 지정 보고서를 만들 수 있는 데이터 내보내기 기능이 추가됩니다. **비식별화된 행 수준 지표와 속성(de-identified, row-level metrics and attributes)** 을 내보낼 수 있어, **개인 식별자를 제거한 상태로** 조직의 Copilot·에이전트 사용과 사용자 수준 상호작용을 깊이 분석할 수 있습니다. *(9월 출시 예정)*

### GitHub Copilot AI 크레딧

**Insights의 Consumption Dashboard**가 **GitHub Copilot AI 크레딧 사용량**을 지원합니다. 개발자의 GitHub Copilot 사용 방식을 분석해 도입과 크레딧을 관리할 수 있습니다. **관리자, Insights 분석가, 전역 관리자**가 지출과 예산을 비교해 데이터 기반 투자 결정을 내릴 수 있습니다. *(7월 출시)*

---

## 한국 도입 담당자를 위한 정리

이번 달 업데이트에서 특히 눈여겨볼 지점을 추려 봤습니다.

- **비용 가시성이 크게 개선됐습니다**: Cowork의 노력 수준과 `/cost` 스킬(잔여 비율·월 누적·재설정 시점), 관리자용 GitHub Copilot AI 크레딧 대시보드가 함께 나왔습니다. **크레딧 관리 정책을 재점검하기 좋은 시점**입니다.
- **공유 기능은 거버넌스와 함께**: Copilot Chat의 세션·응답 공유는 편리하지만, **어떤 대화가 링크로 나갈 수 있는지**에 대한 사내 기준이 필요합니다. 읽기 전용이라도 내용은 전달됩니다.
- **PowerPoint 브랜드 기능은 즉시 활용 가치**: **엄격한 브랜드 준수**와 **노트 스티어링**은 사내 템플릿 관리 부서에서 바로 쓸 만합니다. 특히 고객 대면·규제 자료가 많은 조직에 적합합니다.
- **번역 개선은 국내 조직 체감이 큼**: PowerPoint 번역이 Copilot으로 이동하면서 **텍스트 상자 크기 자동 조정**이 붙었습니다. 한↔영 자료를 자주 만드는 팀에 안내하세요.
- **Excel 변경 이력의 감사 가치**: **사람과 AI의 수정을 구분**해 설명한다는 점이 중요합니다. AI 개입 이력 추적이 필요한 조직이라면 활용 방안을 검토해 볼 만합니다.
- **12월 출시 항목 기억해 두기**: SharePoint 개인 스킬과 OneDrive 파일 기능 개선은 **8월 공개 미리 보기 → 12월 전 세계 출시**입니다. 미리 보기 기간에 검증해 두면 좋습니다.
- **관리자 데이터 내보내기(9월)**: 비식별화된 행 수준 데이터를 받을 수 있게 되므로, **사내 분석 체계와 개인정보 처리 기준**을 미리 정리해 두세요.

---

## 마무리

8월 업데이트를 관통하는 흐름이 몇 가지 보입니다. **비용을 사용자가 직접 조절하게 하고**(Cowork 노력 수준, /cost), **결과물을 더 세밀하게 다루게 하며**(텍스트 선택, 편집 하이라이트, 변경 이력), **조직의 규칙을 강제할 수단을 주는**(브랜드 준수, 노트 스티어링) 방향입니다.

원문도 안내하듯, 최신 정보는 **AI at Work Roadmap**과 **Microsoft Copilot 릴리스 노트**에서 확인할 수 있습니다. 기사에 언급된 날짜는 잠정적이며 변경될 수 있습니다.

---

> **출처**
>
> - 원문 제목: *What's New in Microsoft Copilot | August 2026*
> - 링크: [https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/what-s-new-in-microsoft-copilot-august-2026/ba-p/4551960](https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/what-s-new-in-microsoft-copilot-august-2026/ba-p/4551960)
>
> 자세한 내용은 원문을 참조하세요.
