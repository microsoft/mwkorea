---
title: "선언적 에이전트에서 오토메이트 흐름을 작업으로 사용하는 워크어라운드"
date: 2025-01-26T00:00:00 KST
categories:
  - Copilot Studio
tags:
  - Copilot Studio
  - Agent
  - Action
  - Flow
excerpt: "선언적 에이전트에서 오토메이트 흐름을 작업으로 사용하는 워크어라운드 를 소개합니다."
header:
  overlay_image: /assets/images/unsplash-image-1.jpg
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  #actions:
  #  - label: "원문보기"
  #    url: "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-new-agents-in-microsoft-365/4296918"
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

# 선언적 에이전트에서 오토메이트 흐름을 작업으로 사용하는 워크어라운드

이 글에서 다루는 내용은 코파일럿 스튜디오의 기능이 정식으로 제공되기 전까지 사용할 수 있는 일종의 워크어라운드 입니다. 현재 테스트 환경에서 동작한다고 하여 앞으로도 계속적인 기능의 정상동작이 보장되지 않습니다. 테스트의 목적으로 사용하시기를 권장합니다.
{: .notice--info}

M365 코파일럿 챗이 공개되고 에이전트의 사용범위가 확대됨에 따라, 코파일럿 스튜디오로 만드는 선언적 에이전트 (Declarative Agent)의 중요성이 더욱 강조되고 있습니다. 지침과 지식정보를 활용할 기본적인 에이전트도 생산성 향상에 도움이 되겠지만, 많은 고객과 파트너 개발자 분들이 파워 오토메이트를 연동하여 사용하지 못하는 점을 답답해 하고 있습니다.

최근 코파일럿 스튜디오의 기능이 업데이트 되면서 이 부분이 개선되는 것처럼 보이지만, 아직 완벽하게 기능이 오픈되지 않은 상태입니다. 이에 당장 활용해서 테스트 해볼 수 있는 방법을 아래에 소개합니다.

---

이 워크어라운드의 개요는 아래와 같습니다.

1. 코파일럿 스튜디오의 커스텀 에이전트에 오토메이트 흐름을 작업으로 추가합니다.
2. 오토메이트 흐름의 코드편집기에서 코드를 복사합니다.
3. 코파일럿 스튜디오의 선언적 에이전트에 아무 작업이나 추가합니다.
4. 추가한 액션의 코드편집기를 열어 가져온 오토메이트 흐름의 코드로 교체합니다.
5. 동작을 테스트 합니다.

---

## 현재 상황 확인

코파일럿 스튜디오의 M365 코파일럿 에이전트의 작성화면입니다. 작업추가 버튼을 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action01.png) 

---

작업 선택 창에서 흐름으로 카테고리를 선택하면, 이미 존재하는 코파일럿 용 흐름의 갯수가 표시되는데, 선택을 못합니다. 이게 문제 입니다.

![에이전트](/mwkorea/assets/images/20250126/action02.png) 

---

## 커스텀 에이전트에서 흐름작업 추가

저틑 테스트를 위해 이미 존재하는 커스텀 에이전트를 사용할 것입니다.

![에이전트](/mwkorea/assets/images/20250126/action03.png) 

---

작업을 추가하기 위해 동작추가 버튼을 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action04.png) 

---

새 파워오토메이트 흐름을 추가하도록 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action05.png) 

---

브라우저에 새로운 탭이 추가되면서 파워오토메이스 하나가 바로 만들어지고 편집화면이 열립니다.

![에이전트](/mwkorea/assets/images/20250126/action06.png) 

---

일단 이름을 바꾸고 저장하고 게시하겠습니다.

![에이전트](/mwkorea/assets/images/20250126/action07.png) 

---

입력값을 추가하기 위해 Copilot에서서 흐름 실행 블럭을 클릭합니다. 왼쪽에 패널 화면이 열리면 입력 추가를 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action08.png) 

---

텍스트 타입으로 입력값을 받겠습니다.

![에이전트](/mwkorea/assets/images/20250126/action09.png) 

---

입력값의 변수명과 설명을 적습니다. 여기에 입력하는 설명이 코파일럿이 사용자의 말로부터 파라미터 값을 추출하는 기준이 됩니다.

![에이전트](/mwkorea/assets/images/20250126/action10.png) 

---

이번에는 출력을 추가하기 위해 Respond to Copilot 블럭을 클릭합니다. 왼쪽에 패널 화면이 열리면 출력 추가를 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action11.png) 

---

텍스트 타입으로 출력값을 보내겠습니다.

![에이전트](/mwkorea/assets/images/20250126/action12.png) 

---

출력의 파라미터 이름과 값을 입력합니다. 나중에 흐름의 로직을 개발하면 이 부분이 변경되겠죠.

![에이전트](/mwkorea/assets/images/20250126/action13.png) 

---

이제 흐름을 게시하겠습니다.

![에이전트](/mwkorea/assets/images/20250126/action14.png) 

---

이제 다시 브라우저의 코파일럿 스튜디오가 열려있던 탭으로 돌아갑니다. 새로고침 하라고 팝업창이 떠 있으므로 버튼을 클릭하여 새로 고침 합니다.

![에이전트](/mwkorea/assets/images/20250126/action15.png) 

---

흐름 카테고리로 이동해보면 방금 만들어 게시한 흐름이 보입니다. 클릭해 줍니다.

![에이전트](/mwkorea/assets/images/20250126/action16.png) 

---

작업을 추가하는 화면에서 에이전트의 설명을 적절하게 변경합니다. 이 작업이 무엇을 하는지 알려주어 코파일럿이 상황에 따라 선택할 수 있는 근거가 됩니다. 바로 작업을 추가합니다.

![에이전트](/mwkorea/assets/images/20250126/action18.png) 

---

작업이 추가되었습니다. 이름을 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action19.png) 

---

만들어진 작업이 열리면, 세부정보를 확인해 봅니다.

![에이전트](/mwkorea/assets/images/20250126/action20.png) 

---

만들어진 작업이 열리면, 입력을 확인해 봅니다.

![에이전트](/mwkorea/assets/images/20250126/action21.png) 

---

만들어진 작업이 열리면, 출력을 확인해 봅니다.

![에이전트](/mwkorea/assets/images/20250126/action22.png) 

---

이제 이 작업으 동작하는 것을 테스트 해보겠습니다. 작업의 설명과 유관한 질문을 합니다. 작업인 흐름을 호출하여 답변하는 것을 볼 수 있습니다.

![에이전트](/mwkorea/assets/images/20250126/action23.png) 

---

파워오토메이트에서도 실제 흐름이 호출되어 수행된 것을 볼 수 있습니다.

![에이전트](/mwkorea/assets/images/20250126/action24.png) 

---

입력값도 잘 넘어 옵니다.

![에이전트](/mwkorea/assets/images/20250126/action25.png) 

---

출력값도 잘 전달 됩니다.

![에이전트](/mwkorea/assets/images/20250126/action26.png) 

---

이제 다시 코파일럿 스튜디오로 돌아가서 작업의 코드 편집기를 엽니다.

![에이전트](/mwkorea/assets/images/20250126/action27.png) 

---

코드 편집기의 내용을 복사해둡니다. (메모장에 복사해 두십시오)

![에이전트](/mwkorea/assets/images/20250126/action28.png) 

---

## 선언적 에이전트에 흐름 작업 추가하기

이제 코파일럿 스튜디오의 M365 코파일럿 에이전트 즉, 선언적 에이전트에 작업을 진행할 차례입니다.

![에이전트](/mwkorea/assets/images/20250126/action29.png) 

---

저는 이미 만들어져 있는 선언적 에이전트를 사용하려고 합니다.

![에이전트](/mwkorea/assets/images/20250126/action30.png) 

---

선언적 에이전트에 작업을 추가하기 위해 작업 추가 버튼을 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action31.png) 

---

아무 작업이 추가합니다. 저는 눈에 보이는 아무작업이나 클릭하여 추가하였습니다.

![에이전트](/mwkorea/assets/images/20250126/action32.png) 

---

바로 다음 을 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action33.png) 

---

바로 작업 추가 합니다.

![에이전트](/mwkorea/assets/images/20250126/action34.png) 

---

작업이 추가되었습니다. 추가된 작업을 클릭하여 엽니다.

![에이전트](/mwkorea/assets/images/20250126/action35.png) 

---

작업이 열리면 코드편집기로 이동합니다.

![에이전트](/mwkorea/assets/images/20250126/action36.png) 

---

커스텀 에이전트에서 (메모장에) 복사해두었던 코드를 덮어 씁니다.

![에이전트](/mwkorea/assets/images/20250126/action37.png) 

---

코드가 변경되면 저장 버튼을 클릭합니다.

![에이전트](/mwkorea/assets/images/20250126/action38.png) 

---

작업이 흐름을 사용하는 타입으로 변경된 것을 확인할 수 있습니다.

![에이전트](/mwkorea/assets/images/20250126/action39.png) 

---

작업 이름을 표시이름과 동일하게 변경해 주고 저장합니다.

![에이전트](/mwkorea/assets/images/20250126/action40.png) 

---

아무 작업이나 추가했던 것이 흐름과 연결된 작업으로 탈바꿈하였습니다.

![에이전트](/mwkorea/assets/images/20250126/action41.png) 

---

테스트 해보면 잘 동작합니다.

![에이전트](/mwkorea/assets/images/20250126/action42.png) 

---

파워오토메이트에서 실행기록을 확인해 보면 실제로 호출되어 동작한 내역을 확인할 수 있습니다.

![에이전트](/mwkorea/assets/images/20250126/action43.png) 

---

입력값이 잘 넘어 옵니다.

![에이전트](/mwkorea/assets/images/20250126/action44.png) 

---

선언적 에이전트를 실제 코파일럿에서 테스트 하기 위해 게시합니다.

![에이전트](/mwkorea/assets/images/20250126/action45.png) 

---

게시가 완료되면 에이전트 사용 URL을 복사합니다.

![에이전트](/mwkorea/assets/images/20250126/action46.png) 

---

이미 존재하던 선언적 에이전트를 수정한 것이므로 업데이트 합니다.

![에이전트](/mwkorea/assets/images/20250126/action47.png) 

---

에이전트가 잘 업데이트 되었습니다.

![에이전트](/mwkorea/assets/images/20250126/action48.png) 

---

테스트 해보면, 에이전트가 작업을 통해 쿼리하기 위해 사용자의 승인을 요청합니다.

![에이전트](/mwkorea/assets/images/20250126/action49.png) 

---

흐름을 호출하여 받아온 값으로 답변하는 것을 확인할 수 있습니다.

![에이전트](/mwkorea/assets/images/20250126/action50.png) 

---

파워오토메이트에서도 실행 기록을 확인할 수 있습니다.

![에이전트](/mwkorea/assets/images/20250126/action51.png) 

---

과일창고를 위한 작업과 자재창고를 위한 작업 두개를 모두 활용하여 답변하는 것도 잘 동작합니다.

![에이전트](/mwkorea/assets/images/20250126/action53.png) 

---

