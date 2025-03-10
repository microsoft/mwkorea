---
title: "Custom Engine Agent 만들기 2"
date: 2025-03-03T00:00:00 KST
categories:
  - AgentSchool
tags:
  - AI
  - Agent
  - Copilot
excerpt: "커스텀 엔진 에이전트를 만들어 봅시다 2"
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
이전 학습에서는 Power Automate을 활용해 **커스텀 엔진 에이전트**가 **엑셀의 테이블 행들을 불러오는 액션**을 만들어 보았어요!

---
<br/>
<br/>

# 🚀 B. 이번 학습 내용  
이번에는 에이전트가 엑셀에서 받아온 정보를 활용해 **이메일을 보낼 수 있도록 이메일 액션**을 생성하고 테스트까지 진행해볼 거예요!

---
<br/>
<br/>

# ✉️ C. 이메일 액션을 만들어보자!  

이메일 액션을 만드는 방법은 **이전 학습과 동일한 방식**으로 **Power Automate Flow**를 생성하면 돼요.  

1. **설정한 에이전트의 4번째 Action 탭**으로 들어가기  
2. **Add an Action** 선택하기  
3. **New Action**을 선택하기  
4. **New Power Automate Flow** 버튼을 클릭해 Flow 만들어주기  

이전 학습에서 이미 자세히 설명했으니, 이번에는 간단하게만 설명할게요.  
혹시 기억이 나지 않는다면 **이전 강의**를 다시 확인해보세요!  

위의 4단계를 모두 마치면 아래와 같은 **Power Automate 화면**으로 이동하게 될 거예요.  
아래 화면을 기준으로 설명을 이어갈게요.  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image.png)

---

## 🔄 Run a flow from Copilot 설정  

이전 강의에서는 엑셀의 row를 불러올 때 **Run a flow from Copilot**을 따로 설정하지 않았어요.  
왜냐하면, **Power Automate에 넘겨줄 파라미터가 없었기 때문**이죠.  

하지만 이번에는 **이메일에 담길 내용**을 Power Automate에 넘겨줘야 해요.  

### 💡 파라미터 추가하기  

아래 화면처럼 파라미터를 추가해 주세요!  

| Type | Name       | Description                                  |
|------|-------------|----------------------------------------------|
| Text | Mail Input | Please put the organized text for the email. |

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-1.png)

위 파라미터는 결국 **Copilot이 이전 액션의 output인 엑셀의 row들을 넘겨주는 부분**이에요.  

### 🤔 파라미터 Description의 중요성  

Description에 **어떤 표현을 쓰느냐에 따라** Copilot이 Power Automate에 넘기는 값이 달라져요.  

- **정중한 표현을 원할 때:** "Please provide a polite email text."  
- **Raw text를 그대로 넘길 때:** "Send the raw text as is."  

이처럼 실제로 결과가 많이 달라지니, **다양한 프롬프트를 테스트**해 보기를 추천해요!  

---

## 📧 Send an email 설정  

이제 Copilot으로부터 **이메일 내용을 받아왔다면**, 실제로 **이메일을 보내야겠죠?**  

1. **Run a flow from Copilot**과 **Respond to Copilot** 사이의 **+ 버튼**을 눌러요.  
2. **Send an email**을 검색하고 선택해 주세요.  
![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-2.png)

### 📋 파라미터 설정  

모듈을 추가했다면 **Parameter를 설정**해야 해요.  
아래 화면처럼 파라미터를 설정해 주세요.  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-3.png)

| 항목       | 설명                                              |
|------------|--------------------------------------------------|
| **To**     | 이메일을 보낼 사람을 선택해 주세요.                 |
| **Subject** | 이메일 제목을 적어 주세요.                          |
| **Body**   | 이메일 본문을 적어 주세요.                          |

### 🚨 주의할 점!  

- Body 부분은 마음대로 커스텀해도 괜찮지만, **Run a flow from Copilot에서 받아온 Mail Input을 사용**해야 해요.  
- `/`를 눌러 **다이나믹 컨텐츠**를 사용해 **Mail Input을 Body에 넣어줘야 해요.**  
- 그래야 **이전 액션에서 받아온 엑셀의 row 정보**들이 이메일 본문에 **자동으로 적힐 수 있어요!**  

---

## 💡 참고) 이메일 발신인과 제목을 파라미터로 받을 수도 있답니다. 

조금 더 **심화**해 볼까요?  

만약 **이메일 발신인**이나 **제목**도 **파라미터로 받아서 동적으로 설정**하고 싶다면,  
**Run a flow from Copilot 부분에 파라미터를 추가**해 주면 돼요. 
따라하지 마시고 참고로만 알아주세요! 

| Type | Name       | Description                          |
|------|-------------|--------------------------------------|
| Text | Sender Email | Please provide the sender's email.  |
| Text | Email Subject | What is the subject of the email? |

그 후, 엑셀 액션에서  **이메일과 제목을 넘겨주면**  
Copilot을 활용해서 **대화형으로 이메일 발신인과 제목을 설정**할 수 있어요!  
---

## 💌 이번 학습의 이메일 설정 예시  

하지만 이번 학습에서는 **구체적으로 보낼 사람이 정해져 있기 때문에**  
굳이 파라미터로 받지 않아도 괜찮아요.  

저는 **내 멘토인 정우님**께 이메일을 보내는 것으로 설정했어요! 😊  

---
<br/>
<br/>


# 📩 D. Respond to Copilot 설정  

이메일 보내는 설정까지 완료했다면, 이제 **Copilot에게 이메일을 보낸 결과를 리턴**해줘야 해요.  
여기까지 **프로세스가 성공적으로 진행되면**, "성공"이라고 넘겨주는 것이 좋겠죠?  

---

## ✅ Respond to Copilot 파라미터 설정  

| Type | Content       | Description               |
|------|---------------|---------------------------|
| Text | Email Success | Result for the email      |

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-4.png)

💡 **Tip:** 사실 Description은 **자세하게 적어줄수록 좋음**.  
어떤 이메일이었는지, 성공의 기준이 무엇인지 적어주면 더 좋겠죠. 
이 Description을 보고 전달되는 이 변수가 어떤 변수인지 판단합니다!

---
<br/>
<br/>

# 🛠️ E. 이름 설정하고, 저장하고, Flow 배포하기  

이제 Flow를 완성했으니, **저장(Save)**하고 **이름을 설정**한 후 **Flow를 배포(Publish)**해 주세요.  

1. 이름을 **Send An Email**로 설정  
2. **Save draft** 버튼 클릭  
3. **Publish** 버튼 클릭  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-5.png)

---

## 🔄 에이전트에 액션 등록하기  

Flow 배포까지 완료했다면, 이전 강의에서 했던 것처럼  

- **에이전트로 돌아가서 Refresh**  
- **액션을 등록**해 줘요.  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-6.png)

아래 화면처럼 **Action이 두 개** 등록되어 있다면 성공! 🎉  

---
<br/>
<br/>

# 🤖 F. Generative AI 설정하기  

이제 가장 중요한 부분이 나왔어요!  
바로 **Generative 설정**을 켜줄 거예요.  

### 💡 Generative 설정이란?  

- 기존의 **Custom Engine Agent**는 **Topics과 Trigger** 기반으로 정해진 로직에 따라 액션이 실행되었어요.  
- 그러나 **Preview 업데이트 이후**, **Copilot 오케스트레이터**가 액션을 **자동으로 선택**하고,  
  사용자의 **인풋에 따라** 실행할 액션을 **자동으로 결정**할 수 있게 되었어요.  

### 🔥 Generative 설정 켜는 법  

1. **Settings**에 들어갑니다.  
![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-7.png)

2. **Generative AI** 탭(두 번째)을 클릭한 후, 아래처럼 설정해 주세요.  

- **Generative (preview)** 기능을 켜고  
- **Save** 버튼을 눌러줍니다.  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-8.png)  

---
<br/>
<br/>

# 🚦G. 테스트와 배포  

## 🎯 테스트 해보기  

이제 모든 기능이 준비되었으니 **테스트를 진행**해 봐야겠죠?  
사실 **가장 좋은 습관**은 **기능 단위로 테스트**를 진행하는 거예요.  
그래서 **매 액션을 만들 때마다 테스트해 보길 추천**해요!  

### 이번 테스트에서는 두 가지 기능을 한꺼번에 테스트해 볼게요!  

- 에이전트에게 **엑셀에서 PR Data를 읽어**서  
  **담당자인 정우님께 메일을 보내라고** 요청해 봅시다.  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-9.png) 

---

## 🧠 테스트 결과 분석  

- 테스트를 진행하면 **Activity Map**이 활성화돼요.  
- **중간 과정들을 트래킹**할 수 있고,  
- 에이전트가 **스스로 get comment 액션을 실행**하고  
  **send a email을 실행**해야겠다고 판단해 작업하는 모습을 볼 수 있어요.  

### ✉️ 실제 이메일 발송 확인  

- Copilot에게 **이메일 성공 답장**을 받고,  
- **연결된 Outlook**에서도 **이메일이 성공적으로 발송된 것**을 확인할 수 있어요!  

---

## 🚀 배포해보기  

### 배포 채널 선택  

사실 처음에 **Custom Engine Agent**의 강점으로 **Trigger과 Topic 설정**을 언급했었죠?  
그런데 사실 **다양한 배포 채널**도 **Custom Engine Agent의 장점** 중 하나예요!  

1. **7번째 Channels 탭**을 클릭해 주세요.  
2. **14개의 배포 채널**을 확인할 수 있어요.  

이번에는 **Teams와 Microsoft 365**에 배포할 거예요.  
- **두 번째 옵션**을 선택해 줍니다.  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-10.png)

---

### 채널 팝업 설정  

아래처럼 **채널 팝업**이 나옵니다.  

- **Make agent available in Microsoft 365 Copilot**을 설정  
- 배포를 완료해 주세요.  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-12.png)
---

### 배포 후 에이전트 다운로드  

배포가 완료되면, 아래처럼 **Teams + Microsoft 365 배포 후 화면**이 나옵니다.  

- 에이전트를 **다운받는 다양한 방법**을 설명해 줍니다.  

| 방법           | 설명                                                |
|----------------|-----------------------------------------------------|
| **Get a Link** | 링크를 통해 직접 다운로드 가능                        |
| **Download.zip** | 에이전트 파일 자체를 압축 파일 형태로 다운로드 가능 |
| **Show in the store** | 조직과 팀메이트에게 **정식 배포** 가능 (Admin approval 필요) |

이번에는 **Copy Link** 방법을 선택할게요!  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-13.png)
---

### 에이전트 확인  

아래와 같은 화면이 나오는데, 여기서 **Agent를 다운**받아 주세요.  

- 이미 다운받았다면 **Open**으로 표시될 거예요.  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-14.png)

💡 이제 **Copilot Chat**이나 **M365 Copilot**에서 **배포된 에이전트**를 확인할 수 있어요!  

![alt text](/mwkorea/assets/images/agentschool/2_automateAgent/image-15.png)

---

### 📝 시작 프롬프트와 에이전트 토픽 설정  

사실 이렇게 보니 **에이전트 화면이 휑하다면**,  
다른 분들은 **시작 프롬프트 설정**과 **에이전트 토픽 설정**을 통해  
**에이전트를 풍부하게** 만들어 줄 수 있습니다. 한번 시도해보세요:) 

---

# H. 🎯 결론  

이번 학습에서는 **Custom Engine Agent**로  

1. **엑셀의 데이터를 받아오고**,  
2. 그 데이터를 **이메일로 보내는 방법**을 배웠어요!  

### 📚 이번 강의의 주요 포인트  

1. **Send an Email"액션을 통해 자동화하여 메시지 전달  
2. **Generative AI 설정**을 통해 Copilot 오케스트레이터가 자동으로 액션을 선택하게 설정하기
3. **테스트와 배포**를 통해 실제 사용 가능한 상태로 만들기  


---

## 🚀 다음 강의 예고  

다음 강의에서는 **Trigger 기능을 활용해**  
에이전트가 **자동으로 작동하도록 업그레이드**할 예정이에요!  

- 매일 오전마다 해당 기능이 **자동으로 작동되도록** 설정할 거예요.  

그럼 다음 시간에 만나요! 😊  

