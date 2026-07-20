---
title: "Cowork가 이제 '지켜보는 일'까지 대신합니다: 이벤트 기반 작업(Event-Triggered Tasks)"
date: 2026-07-16T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCowork
  - Microsoft365Copilot
  - EventTriggeredTasks
  - Automation
  - Teams
  - Outlook
excerpt: "Copilot Cowork에 이벤트 기반 작업이 추가됐습니다. 정해진 시간이 아니라 특정 발신자·@멘션·키워드·이벤트가 발생하는 순간을 Cowork가 Teams·Outlook·회의에서 지켜보다가, 자동으로 요약·분석·초안까지 준비해 둡니다. 모든 작업은 사용자 권한으로 실행되며 기본은 초안-승인 방식입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Cowork가 이제 '지켜보는 일'까지 대신합니다: 이벤트 기반 작업(Event-Triggered Tasks)

예약 작업(scheduled task)은 예측 가능한 일을 처리합니다. 하지만 업무에서 정작 중요한 일들은 시계에 맞춰 돌아가지 않습니다. 그냥 **벌어집니다.** 매니저가 갱신 건으로 메시지를 보내고, 인시던트 채널에 갑자기 소환되고, 마감이 임박해 후속 조치가 필요해집니다.

Copilot Cowork에 **이벤트 기반 작업(event-triggered tasks)**이 추가되면서, Cowork가 Teams 채팅·채널, Outlook 이메일, 회의에 걸쳐 **특정 순간을 지켜보다가 알아서 대응**할 수 있게 됐습니다. 트리거는 발신자, @멘션, 키워드나 주제, 이벤트 이름으로 지정할 수 있습니다.

> **한 줄 요약**
> 트리거를 자연어로 설명해 두면, Cowork가 메일과 Teams에서 중요한 순간을 감시하다가 그 일이 발생하는 즉시 포착해 필요한 대응을 미리 준비합니다. 받은편지함을 새로고침할 필요도, 놓치는 알림도 없습니다.

---

## 무엇이 새로워지나

기존 예약 작업이 "정해진 시간"에 실행됐다면, 이벤트 기반 작업은 "정해진 사건이 발생하는 순간"에 실행됩니다. 트리거는 다음과 같이 지정할 수 있습니다.

- **발신자(sender)**: 특정 사람이 보낸 메일·메시지
- **@멘션**: 나를 언급한 순간
- **키워드·주제(keyword or topic)**: 특정 내용이 등장할 때
- **이벤트 이름(event name)**: 지정한 이벤트 발생 시

트리거를 평범한 문장으로 설명하면 Cowork가 나머지를 처리합니다.

![Cowork 이벤트 기반 작업 예시 화면](/mwkorea/assets/images/2026-07-16-CoworkEventTriggeredTasks/image1.png)

## 활용 시나리오

### "고객이 갱신 건으로 메일을 보내면…"

Cowork가 메일을 포착해 스레드를 요약하고, 거래 조건과 계정 이력을 끌어옵니다. 이어서 갱신 건전성(무엇이 달라졌는지, 사용량 추세, 미해결 티켓, 감정)을 분석해 실제 리스크를 짚고, 여러 시나리오(현행 갱신, 할인, 업셀, 이탈)를 Excel로 모델링해 권장안을 제시합니다. 결과는 **사용자 어투로 된 답장 초안 + 한 페이지 브리프(날짜·리스크·옵션·다음 단계)**, 그리고 계정 팀과 공유할 이메일까지 검토 준비된 형태로 정리됩니다.

### "인시던트 채널에서 내가 @멘션되면…"

Cowork가 스레드를 읽어 한 줄 요약을 보내고, 근본 원인 분석을 수행합니다. 티켓·로그·최근 배포 전반에서 무엇이 바뀌었는지 추적해 증상과 원인을 분리하고, 가능한 원인의 우선순위와 영향 범위(blast radius)를 판단하며, 트레이드오프(빠른 완화 vs 완전한 수정)를 담은 해결책을 제안합니다. 그리고 상태 업데이트 초안, 담당자가 지정된 액션 아이템, 관련 문서, 후속 회의 예약 제안까지 한 번에 패키징합니다.

## 통제된 자율성: 무모하지 않게

이 기능은 능동적이되 무모하지 않습니다.

- 모든 작업은 **사용자 본인 권한으로 실행**되며, 사용자가 볼 수 있는 것만 봅니다.
- 기본값은 **초안 작성 후 승인(draft-and-approve)** 방식입니다.
- 트리거별로 자율성 수준을 사용자가 직접 정합니다.
- 설정은 대화로 하고, 모든 자동화는 한곳에서 관리하며, 언제든 한 번의 클릭으로 끌 수 있습니다.

## 도입 관점 체크포인트

- 트리거가 감시하는 데이터 범위(메일·Teams)와 사용자 권한 경계를 명확히 이해합니다.
- 외부로 나가는 액션(메일 발송, 채널 게시)에는 초안-승인 기본값을 유지하도록 안내합니다.
- 민감한 채널·발신자를 트리거로 지정할 때의 조직 정책을 점검합니다.
- 자동화가 늘어날 경우를 대비해 관리·비활성화 절차를 팀에 공유합니다.

## 마무리

이벤트 기반 작업은 Cowork가 "지시받은 일을 실행"하는 단계에서 "지켜봐야 할 일을 대신 감시"하는 단계로 나아가는 변화입니다. 반복적으로 받은편지함과 채널을 확인하던 시간을 줄이고, 정작 중요한 순간에는 이미 준비된 대응을 검토만 하면 되는 방식으로 업무 흐름이 바뀝니다.

> 참고: 이 글은 Microsoft가 운영하는 리빙(living) 블로그 **(Co)work in Progress**의 최신 업데이트 섹션을 정리한 것입니다. 이 블로그는 하나의 글에 Copilot Cowork의 마일스톤·출시·신기능이 계속 누적되는 형식입니다.

---

> **원문**: [Introducing event-triggered tasks in Cowork — (Co)work in Progress (Microsoft Tech Community, Microsoft 365 Copilot Blog)](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/cowork-in-progress/4511672#community-4511672-toc-hId-2052082034)
>
> 자세한 내용은 원문을 참조하세요.
