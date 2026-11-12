---
title: "Copilot이 외부 메일을 읽지 않게 하려면? Purview DLP의 새 제어와 바뀐 출시 일정"
date: 2026-11-07T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotChat
  - MicrosoftPurview
  - DLP
  - Security
  - Governance
excerpt: "Microsoft Purview DLP에 외부·신뢰하지 않는 도메인의 메일을 Copilot의 참조·요약·응답 근거에서 제외하는 제어가 추가됩니다. 11월 6일 갱신된 공지는 전 세계 일반 공급을 2027년 6월로 안내하며, 정책을 켜더라도 메일 수신과 사용자 열람에는 영향을 주지 않습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot이 외부 메일을 읽지 않게 하려면? Purview DLP의 새 제어와 바뀐 출시 일정

Copilot이 답변을 만들 때는 어떤 자료를 근거로 사용하는지도 중요합니다. 회사 내부 문서와 외부 발신자의 메일을 같은 방식으로 활용해도 되는지, 보안·데이터 거버넌스 담당자는 별도로 판단해야 합니다.

Microsoft는 **Microsoft Purview Data Loss Prevention(DLP)**에 Microsoft 365 Copilot과 Copilot Chat의 외부 메일 처리를 제한하는 제어를 추가한다고 안내했습니다. 메일 자체를 차단하는 것이 아니라, 해당 메일이 Copilot의 참조·요약·grounding에 사용되지 않도록 하는 기능입니다.

이번 글은 **MC1301714의 2026년 11월 6일 갱신 내용**을 기준으로 정리합니다. RSS에 표시된 갱신 시각은 한국시간 11월 7일이며, 원래 공지는 2026년 5월 5일 게시되었습니다. 새로 발표된 기능으로 오해하기보다는, 변경된 출시 일정과 적용 범위를 확인하는 업데이트로 읽어 주세요.

---

## 무엇을 제한하나요?

관리자가 정책을 활성화하면 **외부 또는 신뢰하지 않는 도메인에서 보낸 메일**을 Microsoft 365 Copilot과 Copilot Chat이 다음 목적으로 처리하지 않도록 제외합니다.

- 답변에 메일 내용을 참조하기
- 메일 내용을 요약하기
- 답변 생성의 근거 데이터, 즉 grounding으로 사용하기

Grounding은 AI가 답변을 만들 때 업무 자료를 근거로 연결하는 과정입니다. 이 제어의 핵심은 **메일의 보관 위치나 수신 여부가 아니라, AI가 사용할 수 있는 근거의 범위**를 조정한다는 데 있습니다.

정책 적용 이후에도 Copilot은 기존 라이선스와 정책이 허용하는 범위에서 SharePoint, OneDrive, 내부 Exchange 콘텐츠 등 신뢰하는 내부 Microsoft 365 데이터를 이용해 응답할 수 있습니다.

## 메일을 막는 기능과는 다릅니다

| 항목 | 공지에서 설명하는 영향 |
|---|---|
| 외부 메일의 Copilot 참조·요약·grounding | 정책을 켜면 제외 |
| 메일 수신·전달 | 변경 없음 |
| 메일 보존·eDiscovery | 변경 없음 |
| 사용자의 메일 접근·열람 | 변경 없음 |
| 정책을 설정하지 않은 기존 Copilot 사용 | 변경 없음 |
| 기본 설정 | 꺼짐 |

**기본값은 Off**입니다. 관리자가 Microsoft Purview에서 명시적으로 설정하지 않으면 이 공지만으로 기존 동작이 바뀌지는 않습니다.

예를 들어 외부 고객의 메일은 사람이 읽고 처리하되 Copilot의 요약 근거에는 포함하지 않도록 운영할 수 있습니다. 다만 이는 기능을 설명하기 위한 활용 예시이며, 특정 고객·도메인별 상세 예외 설정 방법은 이 공지에 제시되어 있지 않습니다.

## 일반 공급은 2027년 6월로 안내됩니다

11월 6일 갱신된 원문 일정은 다음과 같습니다.

| 단계 | 공지의 배포 일정 |
|---|---|
| Public preview | 2026년 6월 초 시작, 6월 말 완료 예정으로 기재 |
| General availability, Worldwide | 2027년 6월 초 시작, 6월 말 완료 예정 |

일반 공급 일정은 기존의 **1월 말 시작·2월 말 완료** 안내에서 변경되었습니다. 갱신 공지는 새 일정을 **2027년 6월**로 명시합니다.

공개 프리뷰 일정은 이미 지난 날짜지만, 이것만으로 모든 테넌트에서 기능이 활성화되었다고 단정할 수는 없습니다. 실제 사용 가능 여부는 테넌트의 Microsoft Purview 정책 설정 화면과 최신 Message Center 안내에서 확인해야 합니다. **프리뷰 일정과 GA 일정은 구분**해 도입 계획에 반영하세요.

## 관리자가 준비할 사항

이 기능을 사용하지 않을 조직은 별도 조치가 필요하지 않습니다. 도입하려는 조직은 다음을 확인할 수 있습니다.

1. 관리 계정에 DLP 정책 생성·배포에 필요한 Microsoft Purview 역할이 있는지 확인합니다.
2. Microsoft Purview 포털에서 Microsoft 365 Copilot용 DLP 정책을 새로 만들거나 기존 정책을 검토합니다.
3. 정책 위치로 **Microsoft 365 Copilot and Copilot Chat**을 선택하고, 외부 메일 처리 제한 설정을 확인합니다.
4. 외부 메일이 응답 근거에서 빠질 때 기존 업무에 미치는 영향을 검토합니다.
5. IT·보안·헬프데스크에 정책의 범위를 공유하고 AI 사용 안내 문서를 갱신합니다.

![Microsoft Purview DLP 정책 위치에서 Microsoft 365 Copilot과 Copilot Chat을 선택하는 화면](/mwkorea/assets/images/2026-11-07-CopilotExternalEmailDlp/image1.png)

![Copilot의 외부 메일 콘텐츠 처리를 제한하는 새 DLP 설정 화면](/mwkorea/assets/images/2026-11-07-CopilotExternalEmailDlp/image2.png)

도입 검토 시에는 “외부 메일을 요약하지 못한다”는 사용자 문의가 발생할 수 있음을 고려하는 것이 좋습니다. 메일이 사라지거나 권한이 회수된 것이 아니라 **Copilot이 이용하는 근거만 제한된 것**이라는 설명이 필요합니다.

## 마무리

이번 제어는 Copilot이 활용할 수 있는 메일의 범위를 조직의 데이터 정책에 맞추는 장치입니다. 기본적으로 꺼져 있고 메일 전달·보관·열람을 바꾸지 않는다는 점, GA가 2027년 6월로 안내되었다는 점을 함께 확인해야 합니다.

관련 문서는 [Copilot과 Copilot Chat 상호작용 보호를 위한 Purview DLP](https://learn.microsoft.com/purview/dlp-microsoft365-copilot-location-learn-about), [DLP 개요](https://learn.microsoft.com/purview/dlp-learn-about-dlp?view=o365-worldwide), [DLP 정책 생성·배포 권한](https://learn.microsoft.com/purview/dlp-create-deploy-policy#permissions)을 참고하세요. 이 글의 기능·일정 설명은 갱신된 MC 원문 기준이며, 이후 문서나 테넌트 안내가 달라질 수 있습니다.

> 출처: **MC1301714** — [Microsoft Purview | Data Loss Prevention- DLP to restrict processing external emails in M365 Copilot and Copilot Chat](https://mc.merill.net/message/MC1301714), 2026년 11월 6일 갱신. [Microsoft 365 Roadmap ID 561552](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=561552). 실제 출시 일정·기능은 변경될 수 있습니다.
