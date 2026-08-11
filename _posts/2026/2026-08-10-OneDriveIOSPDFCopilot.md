---
title: "아이폰에서 PDF 읽다가 바로 물어보기 — OneDrive iOS의 Copilot 컨텍스트 메뉴"
date: 2026-08-10T00:00:00 KST
categories:
  - Copilot
tags:
  - M365Copilot
  - OneDrive
  - iOS
  - PDF
  - Mobile
  - Roadmap
excerpt: "OneDrive iOS 앱에서 PDF의 텍스트를 선택하고 'Ask Copilot'을 누르면 설명, 요약, 번역, 사용자 지정 질문이 가능해집니다. 데스크톱에서 이미 제공되던 인컨텍스트 Copilot 경험이 모바일로 확장됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 아이폰에서 PDF 읽다가 바로 물어보기 — OneDrive iOS의 Copilot 컨텍스트 메뉴

이동 중에 휴대폰으로 PDF를 열어 본 적 있으신가요? 계약서, 보고서, 논문, 매뉴얼 — 급하게 확인해야 할 문서는 대개 이동 중에 찾아오는 법입니다. 그런데 모바일에서 PDF를 읽는 일은 여전히 불편합니다. 낯선 용어가 나와도, 긴 단락의 요점이 궁금해도, 외국어 문장을 만나도 **화면을 나가서 따로 찾아봐야** 합니다.

Microsoft 365 Copilot이 이 지점을 파고듭니다. **OneDrive iOS 앱에서 PDF의 텍스트를 선택하고 'Ask Copilot'을 누르면** 그 자리에서 답을 얻을 수 있게 됩니다.

---

## 무엇이 새로워지나요

사용 흐름은 아주 단순합니다.

1. OneDrive iOS에서 **아무 PDF나 열고**
2. **텍스트를 선택**한 뒤
3. **Ask Copilot**을 탭합니다

그다음 선택한 부분에 대해 다음 작업을 요청할 수 있습니다.

| 작업 | 설명 |
|---|---|
| **설명(explain)** | 선택한 내용이 무슨 뜻인지 풀어서 설명 |
| **요약(summarize)** | 긴 단락의 요점 정리 |
| **번역(translate)** | 다른 언어로 옮기기 |
| **사용자 지정 질문** | 선택 영역에 대해 원하는 질문을 직접 입력 |

핵심은 **선택한 부분(the selection)**을 대상으로 한다는 점입니다. 문서 전체가 아니라 지금 눈앞에 있는 그 문단에 집중해 답을 얻는 구조입니다.

---

## 데스크톱 기능의 모바일 확장

이 기능은 완전히 새로운 것이 아닙니다. Microsoft가 명시했듯이, **데스크톱에서 이미 정식 출시(generally available)된 인컨텍스트 Copilot 경험**을 OneDrive iOS로 가져오는 것입니다.

즉 이번 업데이트의 의미는 **기능 자체보다 "어디서 쓸 수 있는가"**에 있습니다. 데스크톱 앞에 앉아 있을 때만 쓰던 편의 기능이, 손안의 기기로 넘어옵니다.

그리고 앞서 소개해 드린 **Word Read Aloud의 음성 Q&A**(RM523205)처럼, 최근 Copilot 업데이트에는 공통된 방향이 보입니다. **사용자가 이미 하고 있는 행동의 흐름을 끊지 않고 그 안으로 들어가는 것**입니다.

---

## 활용 시나리오

### 1. 이동 중 계약서·제안서 확인

출장길이나 이동 중에 받은 PDF에서 이해가 애매한 조항을 선택해 바로 설명을 요청합니다.

### 2. 영문 문서 읽기

국내 실무에서 영문 기술 문서, 해외 계약서, 논문을 모바일로 확인할 일이 적지 않습니다. 문단을 선택해 번역하거나 설명을 요청하면 별도 번역 앱을 오갈 필요가 없습니다.

### 3. 긴 보고서 훑기

전체를 읽을 시간이 없을 때, 핵심으로 보이는 섹션만 선택해 요약을 받아 빠르게 판단합니다.

### 4. 회의 직전 자료 파악

회의실로 이동하면서 첨부 자료의 특정 부분만 확인하고 들어가는 상황에 적합합니다.

### 5. 현장 매뉴얼 조회

제조·건설·의료 등 현장에서 태블릿·휴대폰으로 매뉴얼을 볼 때, 해당 절차 부분만 선택해 설명을 받는 방식이 가능합니다.

---

## 일정

| 항목 | 내용 |
|---|---|
| 대상 제품 | Microsoft Copilot (Microsoft 365), OneDrive, SharePoint |
| 대상 플랫폼 | **OneDrive iOS** |
| 정식 출시(GA) | 2026년 10월(CY2026 October) 예정 |

실제 출시 일정·기능은 변경될 수 있습니다.

---

## 도입 체크포인트

- **iOS 우선입니다.** 로드맵 설명은 **OneDrive iOS**를 명시합니다. Android 지원 여부와 일정은 별도 확인이 필요합니다. 국내 조직은 Android 사용 비중이 높은 경우가 많으므로, 전사 안내 시 이 점을 분명히 하셔야 혼선이 줄어듭니다.
- **모바일 앱 정책 확인.** MDM/MAM 정책으로 OneDrive 모바일 앱의 기능을 제한하고 있는 조직이라면, Copilot 기능이 정책과 충돌하지 않는지 점검이 필요합니다.
- **민감 문서 처리 원칙 재확인.** 모바일에서 PDF를 열고 Copilot에 질의하는 흐름이 쉬워지는 만큼, **민감도 레이블이 붙은 문서에 대한 처리 원칙**을 사용자에게 다시 안내해 두시는 편이 좋습니다.
- **한국어·번역 품질 검증.** 번역 기능은 국내 사용자에게 특히 활용도가 높습니다. 실제 업무 문서로 품질을 확인해 보시길 권합니다.
- **Copilot 라이선스 요건 확인.** Microsoft 365 Copilot 제품군 기능이므로 라이선스 배정 대상을 함께 검토하셔야 합니다.

---

## 마무리

"데스크톱에 있던 걸 모바일에도 넣었다"는 소식은 화려하지 않습니다. 하지만 **PDF를 급하게 확인해야 하는 순간은 대개 책상 앞이 아니라 이동 중**이라는 점을 생각하면, 실제 사용 빈도는 오히려 모바일 쪽이 높을 수도 있습니다.

2026년 10월 GA 예정이니, OneDrive를 문서 저장소로 쓰고 계신 조직이라면 모바일 앱 정책과 라이선스 계획을 함께 점검해 두시길 권합니다.

---

> **출처**: Microsoft 365 Roadmap 메시지 **RM568790** — *Microsoft Copilot (Microsoft 365): Review PDFs using the Copilot context menu on OneDrive iOS*
> - 메시지 원문: [https://mc.merill.net/message/RM568790](https://mc.merill.net/message/RM568790)
> - Microsoft 365 Roadmap: [https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=568790](https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=568790)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
