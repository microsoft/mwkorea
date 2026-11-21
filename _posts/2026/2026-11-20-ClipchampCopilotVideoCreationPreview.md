---
title: "문서를 설명 영상으로 바꾸는 Copilot: Clipchamp Video Hub 공개 프리뷰"
date: 2026-11-20T00:00:00 KST
categories:
  - Copilot
tags:
  - Clipchamp
  - VideoCreation
  - Frontier
  - CopilotCredits
  - WorkIQ
  - Anthropic
excerpt: "Clipchamp Video Hub에서 프롬프트와 업무 문서를 바탕으로 영상을 만들고 대화로 수정하는 Copilot 기능이 Frontier 공개 프리뷰로 제공됩니다. Copilot Credits 과금, Anthropic 모델 활성화, 파일·민감도 레이블·편집 제한을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 문서를 설명 영상으로 바꾸는 Copilot: Clipchamp Video Hub 공개 프리뷰

긴 안내 문서나 발표 자료를 짧은 설명 영상으로 바꾸고 싶어도, 구성과 편집에 드는 시간이 부담스러울 수 있습니다. Clipchamp Video Hub의 Copilot 영상 생성은 이런 업무 콘텐츠를 대화로 영상화하는 경험을 제공합니다.

Message Center 공지 MC1560920에 따르면 이 기능은 **2026년 11월 17일부터 Frontier 공개 프리뷰로 제공**됩니다. 프롬프트나 OneDrive 문서로 시작해 채팅에서 결과를 보고, 대화로 다듬은 뒤 MP4로 내보낼 수 있습니다.

---

## 무엇을 만들고 어떻게 수정하나요?

사용자는 영상의 주제, 대상, 어조, 길이를 설명하거나 시작 프롬프트를 고를 수 있습니다. 원하는 언어로 요청하고 다른 언어의 대상에 맞춘 현지화도 요청할 수 있습니다. 다만 원문에는 지원 언어 전체 목록이나 한국어 품질 보장이 제시되어 있지 않습니다.

콘텐츠는 OneDrive의 Word, PowerPoint, 이미지, 동영상, PDF를 활용하거나 **Work IQ의 관련 업무 맥락**을 바탕으로 구성할 수 있습니다. 생성 후에는 “더 짧게”, “격식을 갖춘 어조로”, “제목을 바꿔 줘”와 같은 방식으로 수정합니다.

각 버전은 채팅 안에서 미리 보고, 최종 결과를 **MP4**로 저장합니다. 프리뷰에서는 Clipchamp의 개별 장면이나 요소를 직접 편집하는 방식이 지원되지 않습니다.

## 먼저 확인할 것: 라이선스 포함 기능이 아닌 사용량 기반 과금

이 기능은 **사용량 기반 과금(UBB)** 기능입니다. 영상을 만들 때뿐 아니라 **후속 수정에도 Copilot Credits가 사용**됩니다. 생성과 수정 사용량은 Microsoft 365의 Copilot 비용 관리 보고에 반영됩니다.

관리자는 다음 두 조건을 준비해야 합니다.

1. 조직에서 **Anthropic 모델을 활성화**합니다.
2. Microsoft 365 관리 센터의 **Copilot > Cost management**에서 대상 사용자가 포함된 지출 정책에 Copilot video creation을 켭니다.

원문에는 영상당 크레딧 수나 통화별 가격이 제시되어 있지 않습니다. 따라서 수정 횟수를 포함한 실제 사용량을 확인하며 도입 범위를 조정하는 것이 좋습니다.

## 사용 시작하기

관리자 설정이 완료된 사용자는 다음 순서로 진행합니다.

1. 조직의 Clipchamp Video Hub를 엽니다.
2. 왼쪽 메뉴에서 **Create video**를 선택합니다.
3. 만들 영상을 설명하고 필요한 파일을 추가합니다.
4. 미리 보기를 확인하고 대화로 수정합니다.
5. **Export**를 선택해 MP4로 저장합니다.

원문이 안내하는 주소 형식은 다음과 같습니다. `CompanyName`은 실제 조직의 SharePoint 호스트명으로 바꿔야 합니다.

```text
https://CompanyName.sharepoint.com/_layouts/15/videohub.aspx?vhnav=video-agent-home
```

## 프리뷰 제한사항을 놓치지 마세요

| 항목 | 공지 기준 제한·동작 |
|---|---|
| 민감도 레이블 | General보다 높은 레이블이 있는 문서로 생성한 영상은 볼 수 있지만 아직 다운로드할 수 없음 |
| 모델 가용성 | Anthropic 모델이 비활성화되어 있으면 영상 생성 불가 |
| 입력 자료 | Work IQ, 웹 검색, Word, PowerPoint, 이미지, 동영상, PDF 지원 |
| 이미지 수 | 프롬프트당 최대 3개 |
| 동영상 크기 | 50MB 미만 |
| 직접 편집 | 개별 장면·요소 편집 미지원, 대화로 수정 후 MP4 출력 |
| 세션 | 생성 중 브라우저 탭을 열어 두어야 하며 한 번에 한 세션만 지원 |
| 안정성 | 생성·수정에 시간이 걸릴 수 있고 요청 실패, 시간 초과, 미리 보기·재생 문제가 발생할 수 있음 |

더 많은 파일 형식과 다중 소스 지원은 향후 계획으로 안내됩니다. 현재 지원이 완료된 것으로 전제하지 마세요.

## 업무 자료와 AI 표시 관리

영상은 **사용자가 이미 접근할 수 있는 업무 콘텐츠만 활용**합니다. 내보낸 영상에는 **Made with AI 워터마크**가 붙으며, 관리자가 이를 끌 수 있습니다.

한국 조직에서 사내 교육이나 안내 영상에 활용한다면, 원본 문서의 공개 범위와 민감도 레이블을 먼저 확인하고 결과물의 사실관계와 배포 범위를 검토하는 것이 좋습니다. 워터마크를 끌 수 있다는 사실과 조직의 AI 생성물 표시 정책은 별도로 판단해야 합니다.

## 제공 일정과 마무리

공개 프리뷰 제공일은 2026년 11월 17일입니다. 원문은 전 세계 **GA를 “2월 예정”으로 표현하면서 최종 확인 전이라고 명시**하므로, 이를 확정 일정으로 안내해서는 안 됩니다.

문서를 영상으로 바꾸는 진입 장벽은 낮아지지만, 비용·보안·편집 제약은 여전히 운영 설계의 일부입니다. 먼저 제한된 사용자와 비민감 자료로 생성부터 내보내기까지 경험을 확인하는 접근이 적절합니다.

> **출처:** Message Center **MC1560920**, [Copilot video creation in Clipchamp Video Hub is now live in Frontier Public](https://mc.merill.net/message/MC1560920). [Microsoft 365 Roadmap 570963](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&searchterms=570963). 실제 출시 일정·기능은 변경될 수 있습니다.
