---
title: "말 많이 하는 에이전트가 좋은 에이전트일까? Teams 협업의 소음을 줄이는 3가지 패턴"
date: 2026-08-13T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftTeams
  - TeamsSDK
  - Agent
  - Collaboration
  - EmojiReactions
  - ThreadedReplies
excerpt: "Teams 그룹 대화에서는 답을 잘하는 것만큼 언제 조용히 있을지 아는 것이 중요합니다. 에이전트가 이모지 반응, 스레드 답글, 인용 답글을 활용해 협업을 방해하지 않고 참여하는 설계 패턴을 코드와 함께 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 말 많이 하는 에이전트가 좋은 에이전트일까? Teams 협업의 소음을 줄이는 3가지 패턴

일대일 에이전트 채팅은 규칙이 단순합니다. 나와 에이전트만 있으므로 모든 대화의 의도가 분명하고, 추가 질문을 하거나 멈추거나 다시 시작해도 다른 사람에게 영향을 주지 않습니다.

그룹 협업은 다릅니다. 모든 메시지가 구성원의 주의를 두고 경쟁합니다. 한 사람에게 유용한 답변이 다른 다섯 명에게는 방해가 될 수 있습니다. 그래서 좋은 협업은 **언제 답하고 언제 조용히 있을지, 얼마나 말할지, 어떤 대화 관습을 쓸지** 판단하는 수많은 작은 사회적 결정 위에 세워집니다.

Microsoft 365 Developer Blog가 Teams에 참여하는 에이전트가 익혀야 할 세 가지 패턴을 소개했습니다. **이모지 반응, 스레드 답글, 인용 답글**입니다.

---

## 핵심 원칙: 모든 행동이 새 메시지일 필요는 없습니다

그룹 대화에서 에이전트가 내용을 이해하고 답할 수 있다는 것만으로는 부족합니다. **대화를 더 따라가기 어렵게 만들지 않으면서 참여**해야 합니다.

에이전트의 기본 상호작용이 늘 새 메시지라면 채팅은 금세 시끄러워집니다. 협업 공간에는 더 가벼운 방식이 필요합니다.

- 확인했다는 **표시**
- 논의를 한곳에 담는 **후속 답변**
- 원래 질문에 연결된 **맥락 있는 응답**

## 1. 이모지 반응: 답장 없이 상태 알리기

때로는 이모지 하나면 충분합니다. 사용자가 “@agent, 최신 영업 보고서를 가져와 줘”라고 요청했을 때, 에이전트는 바로 👀 반응을 달아 요청을 봤고 작업 중임을 알릴 수 있습니다. 완료되면 이를 ✅로 바꿉니다.

사용자는 상태를 알 수 있고, 채팅에는 불필요한 메시지가 추가되지 않습니다.

![Teams 에이전트의 이모지 반응](/mwkorea/assets/images/2026-08-13-TeamsAgentCollaborationNoise/image1.gif)

```javascript
app.on('message', async ({ api, activity }) => {
  // 들어온 사용자 메시지에 👍 반응 추가
  await api.conversations.addReaction(
    activity.conversation.id,
    activity.id,
    'like'
  );

  // 작업이 끝난 뒤 반응 제거
  await api.conversations.deleteReaction(
    activity.conversation.id,
    activity.id,
    'like'
  );

  return;
});
```

### 적합한 상황

- 요청 접수 확인
- 작업 진행 중 상태 표시
- 완료 여부 표시
- 단순 동의나 승인

## 2. 스레드 답글: 논의를 주 채널에서 분리하기

채널에서는 스레드가 대화를 이어 가기에 알맞은 장소인 경우가 많습니다. 코드 리뷰가 채널에서 시작됐다면 에이전트는 분석 결과를 해당 스레드에 남깁니다. 관련자는 펼쳐 볼 수 있고, 나머지 구성원은 방해받지 않고 지나갈 수 있습니다.

![Teams 에이전트의 스레드 답글](/mwkorea/assets/images/2026-08-13-TeamsAgentCollaborationNoise/image2.gif)

```javascript
app.on('message', async ({ reply }) => {
  // reply()는 올바른 스레드에 인용 답글을 자동 전송
  await reply('This is a threaded reply to your message.');
  return;
});
```

### 적합한 상황

- 코드 리뷰 결과
- 장애 분석 과정
- 특정 안건에 대한 긴 후속 논의
- 일부 구성원에게만 관련된 세부 정보

## 3. 인용 답글: 시간이 지난 뒤에도 원래 맥락으로 돌아가기

대화가 이미 열 메시지쯤 진행된 뒤 이전 질문에 답해야 한다면, 그냥 새 답변을 쓰는 것보다 원래 메시지를 인용하는 편이 낫습니다. 모든 사람이 “무슨 말에 답하는 거지?”라고 되묻지 않아도 됩니다.

특히 비동기 작업에 유용합니다. 에이전트에게 장애 후속 조사를 맡긴 뒤 팀은 다른 대화를 계속할 수 있습니다. 몇 시간 후 작업이 끝나도 인용 답글이 응답을 원래 요청에 다시 연결합니다.

![Teams 에이전트의 인용 답글](/mwkorea/assets/images/2026-08-13-TeamsAgentCollaborationNoise/image3.gif)

```javascript
app.on('message', async ({ quote, send }) => {
  const sent = await send('The meeting has been moved to 3 PM tomorrow.');
  await quote(
    sent.id,
    'Just to confirm — does the new time work for everyone?'
  );
  return;
});
```

### 적합한 상황

- 장시간 실행된 작업의 결과 보고
- 여러 대화가 섞인 그룹 채팅
- 과거 질문에 대한 뒤늦은 답변
- 중요한 결정이나 변경 사항의 재확인

---

## 세 패턴을 어떻게 선택할까

| 상황 | 권장 패턴 |
|---|---|
| “요청을 확인했고 작업 중”만 알리기 | **이모지 반응** |
| 특정 안건의 세부 논의를 이어 가기 | **스레드 답글** |
| 과거 메시지와 결과를 명확히 연결하기 | **인용 답글** |
| 전체 채널이 꼭 알아야 할 새 정보 | 새 메시지 |

핵심은 **에이전트가 할 수 있는 가장 큰 행동이 아니라, 목적을 달성하는 가장 작은 행동을 선택하는 것**입니다.

## 개발·도입 체크포인트

- **응답 기준을 명시하세요.** 멘션될 때만 답할지, 특정 키워드에도 반응할지, 어느 상황에서 조용히 있을지 정책을 정해야 합니다.
- **진행 상태는 반응으로 표현하세요.** “작업을 시작합니다”, “완료했습니다”라는 메시지를 매번 보내기보다 👀 → ✅ 패턴을 사용하면 소음이 줄어듭니다.
- **비동기 작업은 원문을 보존하세요.** 장시간 작업의 요청 메시지 ID를 저장해 두었다가 결과를 인용 답글로 연결해야 합니다.
- **채널과 채팅의 차이를 반영하세요.** 채널은 스레드 중심, 그룹 채팅은 인용 답글 중심으로 설계하는 편이 자연스럽습니다.
- **과도한 반응도 소음입니다.** 모든 메시지에 이모지를 달면 반응 자체가 무의미해집니다. 상태 전달이 필요한 경우에만 사용하세요.
- **사람의 협업 관습을 관찰하세요.** 조직마다 이모지와 스레드 사용 문화가 다릅니다. 기술 기능보다 팀의 실제 관습에 맞추는 것이 중요합니다.

## 시작하기

이 패턴들은 지금 **Teams SDK**와 **coding agent skill**을 사용해 에이전트에 구현할 수 있습니다.

- [Teams SDK 시작하기](https://learn.microsoft.com/microsoftteams/platform/teams-sdk/welcome)
- [Teams SDK coding agent skill](https://learn.microsoft.com/microsoftteams/platform/teams-sdk/developer-tools/agent-skills)
- [Build 데모: Build agents where work happens](https://build.microsoft.com/sessions/DEM334)

## 마무리

공유 공간의 에이전트를 설계하는 일은 능력을 더 많이 주는 데서 끝나지 않습니다. **사회적 단서를 고려해 참여하게 만드는 일**입니다.

가장 좋은 협업 에이전트는 가장 많이 답하는 에이전트가 아닙니다. **언제, 어떤 방식으로 답해야 하는지 아는 에이전트**입니다.

---

> **출처**: [*Building Agents for Teams: Managing the noise of collaboration*](https://devblogs.microsoft.com/microsoft365dev/building-agents-for-teams-managing-the-noise-of-collaboration/) (Microsoft 365 Developer Blog)
>
> 자세한 내용은 원문 참조.
