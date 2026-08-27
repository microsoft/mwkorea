---
title: "PowerPoint 에이전트 모드가 SharePoint·OneDrive 파일을 참조합니다"
date: 2026-08-22T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - PowerPoint
  - AgentMode
  - SharePoint
  - OneDrive
  - Presentation
  - Roadmap
excerpt: "PowerPoint 에이전트 모드로 프레젠테이션을 만들 때 SharePoint 라이브러리와 OneDrive 폴더에 저장된 파일을 참조할 수 있게 됩니다. 자료를 일일이 열어 붙여 넣지 않고도 사내 문서를 근거로 슬라이드를 생성할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# PowerPoint 에이전트 모드가 SharePoint·OneDrive 파일을 참조합니다

발표 자료를 만드는 일은 대개 "자료 모으기"에서 시작합니다. 지난 분기 보고서, 팀 공유 폴더의 데이터 파일, 기획 문서. 이것들을 열어 필요한 내용을 확인하고, 요약해서 슬라이드로 옮깁니다.

PowerPoint의 **에이전트 모드(Agent Mode)** 는 이 과정을 대신해 주는 기능입니다. 그런데 지금까지는 참조할 수 있는 자료의 범위에 제약이 있었습니다. 정작 필요한 자료는 SharePoint 라이브러리나 OneDrive 폴더에 있는데, 그것을 근거로 삼기 어려웠던 거죠.

메시지 센터 공지 **RM555894·RM555895·RM555897**로 안내된 이번 변경은 이 제약을 풉니다. **에이전트 모드로 프레젠테이션을 만들 때 SharePoint 라이브러리와 OneDrive 폴더에 저장된 파일을 참조할 수 있습니다.**

---

## 무엇이 달라지나요

Microsoft가 공지에서 밝힌 내용은 간결합니다.

> 이제 PowerPoint에서 **에이전트 모드**를 사용해 Copilot으로 프레젠테이션을 만들 때, **SharePoint 라이브러리와 OneDrive 폴더에 저장된 파일을 참조**할 수 있습니다.

### 참조 가능해지는 위치

- **SharePoint 라이브러리(SharePoint libraries)**
- **OneDrive 폴더(OneDrive folders)**

두 곳은 조직에서 업무 문서가 실제로 쌓이는 자리입니다. 팀 사이트의 공유 문서함, 개인 작업 폴더, 프로젝트별 라이브러리 등이 모두 여기에 해당합니다.

### 세 건의 공지에 대하여

이번 항목은 **RM555894, RM555895, RM555897** 세 건의 메시지 센터 공지로 나뉘어 안내되었습니다. 세 공지의 내용과 GA 일정은 동일하며, 일반적으로 이런 분할은 **플랫폼이나 채널별 롤아웃 트랙**을 구분하기 위한 것입니다. 실제 적용 대상과 시점은 각 조직의 메시지 센터에서 개별 항목을 확인하시는 편이 정확합니다.

---

## 왜 의미가 있나요

에이전트 모드의 가치는 "슬라이드를 예쁘게 만들어 주는 것"이 아니라 **"근거가 있는 슬라이드를 만들어 주는 것"** 에 있습니다. 참조할 수 있는 자료의 범위가 곧 결과물의 품질을 좌우하죠.

SharePoint·OneDrive 참조가 열리면 이런 작업이 가능해집니다.

- **사내 자료 기반 발표 자료 작성** — "이 폴더의 분기 보고서를 바탕으로 임원 보고용 자료 만들어 줘"
- **여러 문서 종합** — 흩어져 있는 문서를 각각 열지 않고 한 번에 참조
- **최신 자료 반영** — 로컬에 복사해 둔 오래된 버전이 아니라 공유 위치의 현재 파일을 참조
- **팀 협업 자료 활용** — 팀 사이트에 축적된 자료를 발표 자료로 재구성

특히 **자료를 열어 복사·붙여넣기 하는 단계가 줄어드는 것**이 실무에서 체감되는 부분입니다.

---

## 활용 시나리오 예시

**시나리오 1 — 프로젝트 현황 보고**
프로젝트 팀 사이트의 문서 라이브러리를 참조하도록 지정하고, 진행 상황을 정리한 발표 자료를 요청합니다.

**시나리오 2 — 데이터 기반 슬라이드**
OneDrive에 저장된 실적 데이터 파일을 참조해 수치가 반영된 슬라이드를 생성합니다.

**시나리오 3 — 기존 문서 재구성**
Word로 작성된 기획서를 참조해 같은 내용을 발표용 슬라이드 구조로 바꿉니다.

---

## 일정

| 구분 | 시점 |
|---|---|
| 정식 출시(GA) | 2026년 6월 |

세 공지 모두 GA 시점이 **2026년 6월(June CY2026)** 로 동일합니다. 이미 롤아웃이 진행된 항목이 메시지 센터에 정리되어 올라온 것으로 보이며, 조직에 따라 이미 사용 가능한 상태일 수 있습니다.

---

## 도입 담당자를 위한 체크포인트

- **권한 체계 점검이 우선**: Copilot이 참조하는 범위는 **사용자가 이미 접근 권한을 가진 자료**입니다. 다만 SharePoint 라이브러리 권한이 필요 이상으로 넓게 설정되어 있다면, 그만큼 발표 자료에 반영될 수 있는 범위도 넓어집니다. **라이브러리 권한 정리**를 함께 검토하세요.
- **민감도 레이블 확인**: 참조 대상 문서에 민감도 레이블(sensitivity label)이 적용되어 있다면, 생성된 프레젠테이션의 취급 기준도 그에 맞춰야 합니다. 조직의 레이블 상속 정책을 확인해 두세요.
- **사용자 안내 필요**: 에이전트 모드 자체를 모르는 사용자가 많습니다. **"어디에 있는 자료까지 참조할 수 있는지"** 를 구체적인 예시와 함께 안내하면 활용도가 올라갑니다.
- **자료 정리 상태가 결과를 좌우**: 참조 대상 폴더에 오래된 버전이나 초안이 섞여 있으면 결과물의 정확도가 떨어집니다. **자주 참조되는 라이브러리의 파일 정리**를 병행하는 것이 좋습니다.
- **라이선스 전제**: 공지의 제품 분류에 **Microsoft Copilot (Microsoft 365)** 가 포함되어 있습니다.
- **세 공지 개별 확인**: RM555894·RM555895·RM555897이 각각 다른 롤아웃 트랙일 수 있으므로, 조직 메시지 센터에서 세 항목의 적용 대상을 각각 확인하세요.

---

## 마무리

에이전트 모드가 "빈 슬라이드를 채워 주는 도구"에서 **"우리 조직 자료를 근거로 슬라이드를 만들어 주는 도구"** 로 한 걸음 나아갔습니다. 참조 범위가 넓어지는 것은 결국 결과물이 실무에 얼마나 가까워지느냐의 문제이기도 합니다.

조직에서 SharePoint를 문서 저장소로 활용하고 있다면, 이번 기능을 계기로 발표 자료 제작 흐름을 한 번 점검해 보셔도 좋겠습니다.

---

> **출처**
>
> - 원문 ID: **RM555894 / RM555895 / RM555897** — *Microsoft Copilot (Microsoft 365): Reference files saved in SharePoint libraries and OneDrive folders when creating a presentation with Agent Mode in PowerPoint*
> - 메시지 센터: [https://mc.merill.net/message/RM555894](https://mc.merill.net/message/RM555894) · [https://mc.merill.net/message/RM555895](https://mc.merill.net/message/RM555895) · [https://mc.merill.net/message/RM555897](https://mc.merill.net/message/RM555897)
> - Microsoft 365 로드맵: [https://www.microsoft.com/microsoft-365/roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
