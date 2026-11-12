---
title: "제출했는데 또 입력하라고요? Copilot Studio Adaptive Card의 중복 제출 UX 해결하기"
date: 2026-11-11T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - AdaptiveCards
  - MicrosoftTeams
  - WebChat
  - UniversalActions
  - Microsoft365Copilot
excerpt: "Adaptive Card를 제출한 뒤 입력값이 사라지고 버튼은 남아 있으면 사용자는 실패한 것으로 오해하기 쉽습니다. WebChat의 클라이언트 비활성화, Teams의 카드 교체 방식, Microsoft 365 Copilot 채널의 지원 제한을 구분해 구현 포인트를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 제출했는데 또 입력하라고요? Copilot Studio Adaptive Card의 중복 제출 UX 해결하기

에이전트가 보여준 양식을 작성하고 **Submit**을 눌렀는데 입력값이 사라집니다. 그런데 카드의 입력란과 버튼은 여전히 살아 있습니다. 사용자가 “전송이 안 됐나?” 하고 다시 제출하면, 이번에는 대화가 이미 다음 단계로 넘어가 오류가 발생할 수 있습니다.

MCSCAT의 *Disabling Adaptive Cards After Submission in Copilot Studio Agents*는 이처럼 **처리는 성공했지만 화면이 성공을 알려주지 않는 문제**를 다룹니다. 핵심은 에이전트 로직을 무조건 고치는 것이 아니라, 에이전트가 실행되는 채널에 맞는 제출 후 피드백을 만드는 것입니다.

한국 조직에서도 사내 포털, Teams, Microsoft 365 Copilot에 같은 에이전트를 배포할 수 있습니다. 하지만 카드가 비슷하게 보인다고 세 채널의 해결책까지 같지는 않습니다.

![Copilot Studio Adaptive Card의 제출 후 사용자 경험을 다루는 원문 이미지](/mwkorea/assets/images/2026-11-11-CopilotStudioAdaptiveCardSubmitFeedback/image1.png)

---

## 문제의 원인과 채널별 해법

원문이 다루는 기본 동작에서는 제출 후 입력값이 화면에서 지워져도 카드가 계속 조작 가능한 상태로 남을 수 있습니다. **Adaptive Card에 제출 후 자동 비활성화가 기본으로 내장된 것은 아니기 때문**입니다.

| 실행 채널 | 적용할 패턴 | 실제 바뀌는 부분 |
|---|---|---|
| 직접 호스팅하는 WebChat 포털 | Attachment middleware | 클라이언트에서 이전 카드를 비활성화 |
| Microsoft Teams | Universal Actions | 서버 응답으로 원래 카드를 확인 카드로 교체 |
| Microsoft 365 Copilot | 위 두 패턴을 그대로 적용할 수 없음 | 질문 노드·대화형 입력 등으로 흐름 재설계 |

이 표는 모든 제출 오류의 원인을 설명하는 진단표는 아닙니다. 실제 저장이나 연결 작업이 실패했다면 먼저 그 오류를 해결해야 합니다. 여기서는 **처리 성공 후의 화면 피드백 부재**를 해결합니다.

## 1. 자체 WebChat 포털: 이전 카드를 읽기 전용으로 만듭니다

### 전제조건

이 방식은 **BotFramework-WebChat SDK로 직접 호스팅하는 웹 클라이언트**에 적용합니다. ReactWebChat의 렌더링과 store, attachment middleware를 수정할 수 있어야 합니다.

Microsoft의 **Employee Self-Service(ESS)** 에이전트에는 이름만 보고 이 방식을 적용하면 안 됩니다. 원문에서 설명하는 ESS는 Microsoft 365 Copilot 채널에서 실행되므로, 조직이 해당 클라이언트에 WebChat middleware를 끼워 넣을 수 없습니다.

### 구현의 핵심

원문 샘플의 middleware는 store에서 `type === 'message'`인 activity를 추리고 마지막 항목과 현재 카드를 가진 activity를 비교합니다. 마지막 메시지에 속하지 않는 Adaptive Card는 `AdaptiveCardContent`의 `disabled` 속성을 켜서 렌더링합니다.

즉, 단순히 모든 카드를 비활성화하는 것이 아니라 **대화가 다음 단계로 진행됐을 때 과거 카드를 다시 조작하지 못하도록 하는 패턴**입니다. 비활성 카드의 입력란은 읽기 전용이 되고 버튼은 작동하지 않습니다.

연결 지점은 다음과 같습니다.

```jsx
<ReactWebChat
  store={store}
  directLine={directLine}
  attachmentMiddleware={attachmentMiddleware}
/>
```

`attachmentMiddleware`와 카드 렌더러의 전체 연결 코드는 [BotFramework-WebChat 공식 샘플](https://github.com/microsoft/BotFramework-WebChat/tree/main/samples/05.custom-components/l.disable-adaptive-cards)에서 확인할 수 있습니다. 위 코드는 통합 지점만 보여주며 독립 실행 예제는 아닙니다.

### 버튼의 시각적 피드백도 함께 처리합니다

원문은 `actionPerformedClassName`에 `card__action--performed`를 지정하고 해당 CSS 클래스에 배경색 `#0063b1`, 같은 테두리색, 흰색 글자를 적용합니다. 이미 실행한 버튼이 눈에 띄도록 만드는 보완책입니다.

**이 방법은 클라이언트 UI 제어이지 서버의 중복 처리 방지 장치가 아닙니다.** 업무상 동일 요청이 두 번 실행되면 안 되는 경우에는 UI 비활성화만으로 충분하다고 판단하지 말고, 서버 측 중복 요청 검증도 별도로 설계해야 합니다. 이는 이 패턴을 적용할 때의 추가 운영 권고입니다.

## 2. Teams: Action.Execute로 원래 카드를 교체합니다

Teams에서는 클라이언트를 직접 수정할 수 없으므로 WebChat middleware 대신 **Universal Actions**를 사용합니다.

사용자가 버튼을 누르면 Teams가 `invoke` activity를 보내고, Copilot Studio 토픽이 입력을 처리한 뒤 새 카드를 반환합니다. Teams는 기존 양식 카드를 확인 카드로 교체합니다.

### 1단계: 제출과 건너뛰기에 서로 다른 verb를 지정합니다

원문은 `Action.Submit` 대신 `Action.Execute`를 사용하고, 제출에는 `feedbackSubmitForm`, 건너뛰기에는 `feedbackSkipForm`이라는 `verb`를 지정합니다.

아래는 같은 구조를 설명하는 액션 예시입니다. 전체 Adaptive Card의 `ActionSet` 등에 넣는 일부 구성입니다.

```json
{
  "type": "Action.Execute",
  "title": "제출",
  "verb": "feedbackSubmitForm",
  "data": { "actionType": "submitted" },
  "fallback": "Action.Submit"
}
```

건너뛰기 액션에는 `associatedInputs: "none"`을 지정해 입력 수집·검증에 묶이지 않도록 구성합니다. 원문은 Universal Actions 미지원 클라이언트를 고려해 `fallback: "Action.Submit"`도 포함하도록 안내합니다.

다만 **fallback이 있다는 이유로 카드 교체 기능까지 모든 채널에서 보장되는 것은 아닙니다.** Microsoft 365 Copilot의 `Action.Execute` 지원 제한을 우회하는 수단으로 해석해서는 안 됩니다.

### 2단계: Ask with Adaptive Card가 아니라 Send a message로 보냅니다

Copilot Studio에서는 **Send a message** 노드에 Adaptive Card JSON을 넣어 보냅니다.

이 패턴에서 **Ask with Adaptive Card** 노드를 쓰면 안 됩니다. 원문에 따르면 해당 노드는 내부적으로 `Action.Submit`을 사용하므로, 여기서 필요한 `invoke`와 카드 교체 흐름을 만들지 못합니다.

### 3단계: invoke를 받는 리스너 토픽을 구성합니다

리스너 토픽은 들어오는 `invoke` activity의 payload를 파싱합니다. 원문 스키마는 최상위 `action`과 `trigger`를 가지며, `action` 안에 `data.userResponse`, `id`, `title`, `type`, `verb`를 문자열로 정의합니다.

파싱 결과의 `resultData.action.verb`를 기준으로 분기합니다.

- `feedbackSubmitForm`: 입력을 처리하고 감사·접수 확인 카드를 반환합니다.
- `feedbackSkipForm`: 건너뛰기 확인 카드를 반환합니다.

카드의 실제 입력 ID가 다르면 `data` 스키마도 그 구조에 맞춰야 합니다. 샘플의 `userResponse` 필드가 모든 양식에 자동으로 생기는 것은 아닙니다.

### 4단계: Universal Action 응답 형식으로 확인 카드를 돌려줍니다

응답에는 다음 외피가 필요합니다.

| 필드 | 값 또는 구성 |
|---|---|
| `statusCode` | `200` |
| `type` | `application/vnd.microsoft.card.adaptive` |
| `value` | 교체할 Adaptive Card 객체 |

원문은 `value` 안에 `$schema`, `type: "AdaptiveCard"`, `version: "1.5"`와 접수 완료를 알리는 `TextBlock`을 구성합니다. **교체 카드에 입력란과 제출 버튼을 두지 않는 것**이 다시 입력·제출할 여지를 없애는 핵심입니다.

설정 후에는 **Copilot Studio 테스트 패널만이 아니라 Teams에서 직접 검증**해야 합니다. 원문은 테스트 패널에서 `invoke`와 카드 갱신 흐름이 동작하지 않을 수 있다고 경고합니다.

전체 구현은 [CopilotStudioSamples의 adaptive-card-refresh 솔루션](https://github.com/microsoft/CopilotStudioSamples/tree/main/authoring/solutions/adaptive-card-refresh)을 참고할 수 있습니다. 원문은 Nghiem Doan이 만든 가져오기 가능한 샘플로 소개합니다.

## 3. Microsoft 365 Copilot과 ESS: 채널 제한을 전제로 설계합니다

원문은 이 부분을 **2026년 7월 기준 상황**이라고 명시합니다. 따라서 11월에 수집된 글이라고 해서 본문의 모든 지원 상태가 11월 기준으로 새로 확인된 것이라고 읽으면 안 됩니다.

추가로 확인한 [Microsoft Learn의 채널 연결 문서](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams#known-limitations)는 **2026년 10월 29일 갱신본**에서도 Microsoft Copilot 채널의 미지원 노드 유형으로 **Adaptive Cards with `Action.Execute`**를 명시합니다. 이 문서는 standard harness 기반 에이전트·흐름을 설명한다는 범위 안내도 함께 제공합니다.

이 채널에서는 조직이 WebChat 클라이언트를 호스팅하지 않으므로 attachment middleware를 추가할 수 없고, Teams에서 쓰는 `Action.Execute` 기반 카드 교체도 그대로 적용할 수 없습니다.

원문이 제안하는 대안은 다음과 같습니다.

- 가능하면 카드를 **정보 표시용**으로 사용합니다.
- 입력은 **Question 노드 또는 대화 턴**으로 수집합니다.
- 카드·후속 메시지에서 접수 여부가 분명하게 전달되도록 문구를 설계합니다.

ESS도 이 채널 차이를 먼저 확인해야 합니다. 자체 포털의 셀프서비스 양식과 비슷해 보여도 WebChat 방식이나 Teams 방식이 자동으로 적용되는 것은 아닙니다.

## 배포 전 점검: 화면 잠금과 업무 완료는 별개입니다

다음 항목은 원문의 구현 방식을 실제 배포에 적용하기 위한 점검 목록입니다.

1. 에이전트가 실행되는 채널과 클라이언트 수정 가능 여부를 먼저 확인합니다.
2. WebChat에서는 과거 카드의 입력·버튼 상태와 실행 버튼 표시를 확인합니다.
3. Teams에서는 제출·건너뛰기 verb 분기와 확인 카드 교체를 실제 Teams 클라이언트에서 확인합니다.
4. 데이터 저장 실패를 성공 확인 카드로 덮지 않도록 오류 경로도 설계합니다.
5. 중복 실행이 치명적인 업무는 UI 상태 외에 서버 측 중복 처리 방지 요건도 검토합니다.

이 글은 특정 기능의 새 GA나 프리뷰 출시 발표가 아니라 **채널별 구현 패턴과 지원 제한**을 설명합니다. 배포 시점의 공식 지원 범위와 실제 대상 채널에서의 동작을 함께 확인하는 것이 안전합니다.

## 마무리

사용자가 궁금한 것은 카드 내부의 이벤트 이름이 아니라 **“내 요청이 접수됐는가?”**입니다. 같은 제출 버튼이라도 자체 WebChat에서는 비활성화, Teams에서는 카드 교체, Microsoft 365 Copilot에서는 대화 흐름 재설계가 필요할 수 있습니다.

다음 에이전트를 배포하기 전에 직접 Submit을 눌러 보세요. 처리 결과뿐 아니라 그 직후 사용자가 보는 화면까지 확인해야 제출 경험이 완성됩니다.

---

> 출처: MCSCAT Blog — The Custom Engine, [Disabling Adaptive Cards After Submission in Copilot Studio Agents](https://microsoft.github.io/mcscatblog/posts/disable-adaptive-cards-after-submission/). 자세한 내용은 원문 참조.
>
> 지원 범위 추가 확인: [Microsoft Learn — Connect and configure an agent for Teams and Microsoft Copilot](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams#known-limitations), 문서 갱신일 2026년 10월 29일.
