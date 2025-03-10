---
title: "Custom Engine Agent 만들기 3"
date: 2025-03-03T00:00:00 KST
categories:
  - AgentSchool
tags:
  - AI
  - Agent
  - Copilot
excerpt: "커스텀 엔진 에이전트를 만들어 봅시다 3"
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  #actions:
  #  - label: "원문보기"
  #    url: "https://www.microsoft.com/en-us/microsoft-365/blog/2025/02/10/discover-the-total-economic-impact-of-microsoft-365-e3/?msockid=20f4fd7af5a86c603f7ae8f6f4df6ddb"
toc: false
toc_sticky: true
classes: wide
author: 조항우
---

# 📚 A. 이전 학습 내용  

이전 학습에서는, **AI Agent**가 **엑셀에서 받아온 정보를 바탕으로 이메일을 보내는 기능**을 구현했어요.  
그리고 실제로 **Custom Engine Agent를 테스트**하고, **배포**까지 완료했죠!  

---

# 🚀 B. 이번 학습 내용  

이번 학습에서는 **Trigger 기능을 사용**해,  
엑셀에서 정보를 받아오고 이메일을 보내는 **Flow를 매일 오전 9시에 자동으로 실행**되도록 설정할 거예요.  

사실 이런 **Trigger 기능**을 사용하는 게 **Custom Engine Agent의 진짜 이유**이기도 해요.  
Declarative Agent로는 할 수 없는 자동화 기능을 활용할 수 있거든요.  

그럼, **시작해볼까요?** 😊  

---

# ⏰ C. Recurrence 트리거를 만들어보자!  

### 🛠️ 일정 시간마다 액션을 실행하는 트리거 설정  

트리거를 만드는 건 정말 **간단**해요!  

1. **Auto_Report_Agent**로 들어가 주세요.  
2. **Overview 탭**에서 **Add Trigger**를 클릭해 줍니다.  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image.png)

3. **Recurrence**를 선택해 주세요.  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-1.png)

4. 설정 화면이 나오면 **Next**를 눌러요.  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-2.png)

5. 기본 설정 그대로 두고, **Create Trigger** 버튼을 눌러 줍니다.  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-3.png)

💡 만약 트리거가 **시작되는 시간은 중요하지 않고**,  
**주기만 설정**하고 싶다면 여기서 간단히 설정해도 돼요.  

---

# ⚙️ D. Power Automate에서 구체적으로 설정하기  

위까지 진행했다면, 아래 화면처럼 **Trigger가 생성**된 걸 볼 수 있어요.  

1. **Trigger의 3dot 버튼**을 클릭  
2. **Edit in Power Automate Flow**를 선택해 주세요.  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-4.png)

이제 **Trigger의 Power Automate Flow**로 이동했어요.  
여기서 우리는 **간단하게 두 가지만 설정**해 줄 거예요.  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-5.png)

---

## ⏲️ Recurrence 설정  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-6.png)

| 설정 항목      | 값                 |
|----------------|---------------------|
| **Interval**   | 1                   |
| **Frequency**  | Day                 |
| **Time Zone**  | Seoul               |
| **At the hours** | 9                 |
| **At the minutes** | 15             |

이렇게 설정하면, **Seoul 타임존 기준으로 매일 오전 9시 15분**에  
**Sends a prompt to the specified copilot for processing** 액션이 시작돼요!  

---

## 💬 Sends a prompt to the specified copilot for processing  

이 액션은 **Copilot Agent에게 특정 프롬프트를 보내는 역할**을 해요.  
**Recurrence 트리거**와 합쳐지면, **정해진 시간에 자동으로 액션을 시작**할 수 있게 돼요!  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-8.png)

### ✍️ 프롬프트 설정  

**Body/Message** 부분에 **보낼 프롬프트**를 설정해 줘야 해요.  
```plaintext
엑셀에서 PR row 받아와서 정우님께 메일로 보내줄래?
```

이렇게 되면 아침 9시 15분 마다 코파일럿에서 액션을 실행할 수 있어요!
설정한 후 **save draft하고 Publish** 해주면 트리거 설정 끝!

# 📅 E. 테스트해보자  

### 💡 Trigger는 어떻게 테스트할까?  

"그럼 매일 아침 9시 15분까지 기다려야 하나요?" 라는 의문이 생길 수 있죠.  

하지만 걱정하지 마세요!  

**Copilot Studio**에서는 **Trigger 테스트 기능**을 제공해 줍니다.  

1. **실험실 버튼**을 클릭해 보세요.  
![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-9.png) 

2. 다음과 같은 **팝업 창**이 뜨게 돼요.  

- **과거의 트리거가 성공적으로 실행되었던 시점**을 선택해 테스트할 수 있어요.  
- 저는 보통 **트리거를 테스트할 때**는 **1분 간격**으로 설정해 놓고,  
- **정상 작동을 확인한 후** 다시 **원하는 간격**으로 되돌려 놓아요.  

3. 테스트할 시점을 선택하고 **Start testing**을 눌러주세요.  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-10.png)

4. 그러면 아래처럼 **성공적으로 엑셀에서 정보를 불러오고, 이메일을 보내는 것**을 확인할 수 있어요.  

![alt text](/mwkorea/assets/images/agentschool/3_automateAgent/image-11.png)

---

# 🎯 F. 결론  

오늘 배운 내용은 다음과 같아요!  

| 주요 내용                                   | 설명                                                                                 |
|--------------------------------------------|-------------------------------------------------------------------------------------|
| **Recurrence 트리거 설정 방법**               | 매일 아침 **9시 15분에 자동으로 액션을 실행**하도록 설정했어요.                       |
| **Copilot Agent에 프롬프트 보내기**            | **특정 프롬프트를 설정**해 정해진 시간에 **자동으로 액션을 실행**하도록 했어요.        |
| **Trigger 테스트 방법**                      | **실험실 버튼**을 통해 과거의 트리거를 활용해 **빠르게 테스트**하는 방법을 배웠어요.     |
| **자동화 Workflow 완성**                      | 엑셀 데이터를 가져와 **자동으로 이메일을 보내주는 Workflow 에이전트**를 만들어 봤어요. |

---

## 🚀 자동화 에이전트의 무한 가능성  

이걸로 매일 **정해진 시간에 엑셀 데이터를 이메일로 보내주는 자동화**를 완성했어요!  

하지만 사실 이것은 **단지 하나의 예시**일 뿐이에요.  

Copilot Studio를 활용하면 **무궁무진한 자동화 가능성**을 실현할 수 있어요.  
특히 **일상의 반복적인 작업**을 에이전트에게 넘겨줄 수 있다는 게 큰 장점이죠.  

---

## 💡 생산성을 혁신해보자!  

여기서 멈추지 말고, **다양한 에이전트**를 만들어서  
**업무 생산성을 혁신**해 보길 바라요.  
이떄까지 수고 많으셔습니다!