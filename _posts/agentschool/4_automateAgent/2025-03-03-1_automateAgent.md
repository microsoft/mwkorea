---
title: "Custom Engine Agent 만들기 1"
date: 2025-03-03T00:00:00 KST
categories:
  - AgentSchool
tags:
  - AI
  - Agent
  - Copilot
excerpt: "커스텀 엔진 에이전트를 만들어 봅시다 1"
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

# 🚗 A. Business Scenario 

## 커스텀 엔진 Agent야, 길인턴을 구해줘!  

무한상사 PR팀의 길인턴, 하루는 유부장님으로부터 난감한 부탁을 받습니다.

> 유부장: "길인턴, 우리 제품에 대한 인터넷 반응이 궁금하네. 매일 종류별로 리뷰를 필터링해서 보내고 코멘트도 남겨줄 수 있겠나?"

> 길인턴: "넵! (하지만 어떻게요...?)" 

길인턴은 IT팀에서 매일 리뷰를 크롤링해 엑셀에 적어 놓는다는 사실을 알게 됩니다.  
하지만, 매일 보내는 것도 부담스러운데 리뷰 필터링에 분석까지 요구받은 길인턴은 **Agent 구축**을 통해 이 문제를 해결하고 싶어지는데요. 

과연 길인턴은 에이전트의 도움으로 미션을 완수할 수 있을까요?

---

</br>
</br>

# 🎯 B. Objective  

이번 프로젝트의 목표는 **커스텀 엔진 에이전트**를 사용해, **엑셀로부터 원하는 정보를 필터링하고, 이를 분석해 자동으로 이메일을 보내는 것**이에요!

 ❓**왜 Declarative가 아니라 Custom Engine에이전트를 써야할까요?**

   Declarative 에이전트와 커스텀 에이전트의 차이중 하나는 Trigger라 불리는 액션 자동 실행 기능을 사용할 수 있냐 없냐도 있어요. 
 
   이번 프로젝트에서는 3번쨰 학습에서 Trigger를 사용해 이메일을 원하는 시간에 보내도록 스케줄링 해줄것이기 때문에 Custom Engine 에이전트를 사용해 주어야해요! 

 ✅ **SharePoint의 엑셀을 에이전트에 연결해** 원하는 정보만 필터링해 가져올 수 있어요.  

 ✅ **엑셀에서 추출한 정보를 분석해** 자동으로 대상자에게 이메일을 보낼 수 있어요.  


 ✅ 이메일을 매일 오전 원하는 시간에 보내도록 스케줄링 할 수 있어요
---

</br>
</br>


# 💡 C. 커스텀 엔진 에이전트란?  

이번 시간에는 **커스텀 엔진 에이전트**를 다뤄볼 거예요.  
왜 커스텀 엔진 에이전트르 

1강에서 배웠듯이 **커스텀 엔진 에이전트**는 **Declarative 에이전트**와 달리, **Orchestration 모델을 커스텀할 수 있는 자유도**가 높아요.  

| 에이전트 유형  | 특징 |
|----------------|-------|
| Declarative 에이전트 | Flow 사용, 규칙 기반, 제한적 |
| 커스텀 엔진 에이전트 | Trigger사용가능, Orchestration 모델 커스텀 가능, 높은 자유도 |

궁금하시다면 1강으로 돌아가시면 상세히 설명되어 있어요.  
이전까지는 **Declarative 에이전트**를 주로 다뤘지만, 이번 강의에서는 **커스텀 엔진 에이전트**로 에이전트를 만들어봅시다!  

> 💡 **Tip:**  
> 커스텀 엔진 에이전트를 사용하면, Declarative 에이전트에서 Flow를 사용했을 때와 달리, **복잡한 절차 없이 바로 적용**할 수 있어요!

---

</br>
</br>

# 📂 D. 고객 댓글 데이터베이스를 담은 엑셀 만들기  

본격적으로 **커스텀 에이전트**를 만들기 전에, **고객 댓글을 담은 DB**부터 만들어줘야 해요.  

DB를 만들어서 **SharePoint**에 올려두면 에이전트가 해당 엑셀에 접근할 수 있어요.  
저는 아래 형식대로 엑셀에 테이블을 만들어볼게요.  

### 🗂️ 엑셀 테이블 형식  

| 인덱스 | 작성자 이름 | 작성일 | 평점 | 댓글내용 | 감정 분석 결과 |
|--------|-------------|--------|-------|-----------|-----------------|
| 1 | 홍길동 | 2024-03-01 | 5 | "좋아요!" | 긍정 |

![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image.png) 

IT팀에서 해당 양식으로 PR 댓글들을 쌓아준다고 가정해보겠습니다.  
이제 **SharePoint**에 올려줘야 에이전트가 해당 엑셀에 접근할 수 있어요.  

저는 `User_Feedback`이라는 SharePoint 사이트를 만들고, Document에 해당 엑셀 파일을 올려두겠습니다.  

![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-2.png)

> 📝 **참고:**  
> SharePoint 사이트 만드는 법이나, 문서 업로드 방법이 궁금하시다면 2강의 학습 1번을 참조하세요!  
> 우리 팀 **정우님**께서 작성하신 링크도 함께 공유해두었습니다.  

---

</br>
</br>


# E. 커스텀 에이전트를 만들어보자. 

커스텀 에이전트를 만들기 위해서는 코파일럿 스튜디오의 **세 번째 탭**으로 이동해주자.  
커스텀 에이전트를 만드는 방법과 자세한 내용은 **1강**에서 자세히 설명했으니,  
다른 방법이 궁금한 분들은 **1강을 참고**해 주세요.  

### 📌 에이전트 생성 단계  

1. **+NEW AGENT** 클릭  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-3.png)

2. **대화창 방식으로 에이전트를 생성하는 화면**이 나타나면 **Skip**을 눌러주세요.  
   그러면 아래와 같이 **에이전트를 직접 설정하는 창**이 나타납니다.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-4.png)

3. 아래와 같이 설정해 줄게요.  

| 항목        | 설정값                                                 |
|-------------|---------------------------------------------------------|
| **Name**        | Auto_Report_Agent                                       |
| **Description** | This agent reads Excel and sends reports to personnel. |
| **Instructions** | 시스템 프롬프트 및 역할 설명 (아래 내용 참고)           |


```plaintext
시스템 프롬프트: Auto_Report_Agent


역할:  
당신은 온라인 엑셀 데이터를 자동으로 읽어 분석하고, 분석 결과를 관련 담당자에게 이메일로 전송하는 AI 에이전트입니다.

기능

데이터 읽기 및 분석:
온라인 Excel 파일의 데이터를 직접 읽어와 분석합니다.
필요한 데이터만 추출하고, 주요 정보를 요약합니다.
자동 이메일 전송:
분석된 데이터를 기반으로 간결하고 정확한 이메일을 생성합니다.
관련 담당자에게 자동으로 이메일을 발송합니다.
오류 감지 및 보고:
데이터 읽기 및 이메일 전송 과정에서 오류가 발생하면 자동으로 관리자에게 알립니다.

사용 예시

"주간 보고서 데이터를 읽어 분석하고 이메일로 보내줘"
"프로젝트 현황을 온라인 엑셀에서 읽어와 담당자에게 전달해줘"

```
> 💡 **Tip:**  
> 원래 **Instructions** 부분을 **마크다운 형식**으로 설정하면 성능이 훨씬 좋아져요.  
> 하지만 이번에는 간단하게 **줄글 형식**으로 설정할게요.  
> 물론, 마크다운으로 작성하고 싶으신 분들은 자유롭게 사용해도 됩니다!  

3가지 설정 사항을 모두 입력했다면, **Create 버튼**을 눌러줍시다.  
그러면 에이전트 생성이 **완료**돼요! 🎉  
---

</br>
</br>

# 📂 F. Excel Action을 만들어보자!  

생성한 에이전트에 들어간 후,  
아래 화면처럼 **네 번째 탭 Actions**로 이동해서 **Add an Action**을 클릭해 주세요.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-5.png)

그 후 **+ New Action**을 선택하고, **New Power Automate flow**를 클릭해 주세요.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-6.png)

이제 아래와 같이 **New Power Automate** 화면이 나타날 거예요.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-7.png)

---

### 📊 엑셀 모듈 추가하기  

1. **가운데 + 버튼**을 누릅니다.  
2. **List rows present in a table**을 검색하고 추가해 주세요.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-8.png)

> 💡 **Excel Online 모듈 그룹**을 통해 엑셀 파일에 접근하고 정보를 컨트롤할 수 있어요.  
> 엑셀과 관련된 다양한 유용한 기능들이 많으니 꼭 살펴보세요!  

---

## ⚙️ List rows present in a table 설정하기  

이제 해당 모듈이 **SharePoint**와 **엑셀 파일**을 찾을 수 있게 설정해 봅시다.  
아래와 같이 설정하면 돼요.  

![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-9.png)

| 설정 항목            | 설정 방법                                                                                   |
|----------------------|---------------------------------------------------------------------------------------------|
| **Location**         | 엑셀 파일을 올린 **SharePoint** 선택 (OneDrive도 가능, 제 경우에는 **User_Feedback**)      |
| **Document Library** | 파일이 올라가 있는 **라이브러리** 선택 (자동으로 옵션이 나타나요)                            |
| **File**             | 업로드한 **엑셀 파일** 선택                                                                 |
| **Table**            | PR 데이터가 들어있는 **엑셀 내 테이블**을 선택                                              |  

위와 같이 설정했다면, **엑셀 모듈 설정은 완료**된 거예요!  
이제 가져온 **엑셀 정보**를 **Copilot 에이전트**에게 전달할 차례입니다.  

---

</br>
</br>

# 🤖 G. Respond to Copilot 설정하기  

**Copilot 에이전트**에게 **엑셀 정보**를 전달하려면 **파라미터 설정**이 필요해요.  

1. 아래 화면처럼 **텍스트 파라미터**를 선택해 만들어 줍니다.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-10.png)

| 항목        | 설정값                                                               |
|-------------|-----------------------------------------------------------------------|
| **Name**    | Rows                                                                  |
| **Content** | **/**를 눌러 **다이나믹 컨텐츠**를 설정하고, **엑셀 모듈의 body/value**를 입력 |
| **Description** | 에이전트가 이해할 수 있도록 간략히 설명 (`Get rows from the excel table`) |



## 💾 저장하고 Publish하기  

모든 설정을 완료했다면, 항상 해야 할 중요한 작업이 있어요.  
바로 **저장하고 Publish**하기입니다!  

1. **이름을 Get_Comments_Info**로 이해하기 쉽게 변경해 주세요.  
2. **Save Draft**를 누른 다음, **Publish** 버튼을 눌러주세요.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-11.png)

> 🛠️ **팁:**  
> 이 글은 **Instruction**이기에 처음부터 쭉 진행했지만,  
> 오른쪽 상단의 **Test 버튼**을 활용해 **중간중간 테스트**해 보는 것도 좋아요!

---

# 🚦 H. 에이전트에 만든 Action 등록하기  

1. **Publish**를 완료했다면, 다시 **에이전트 Add Action 화면**으로 돌아갑니다.  
2. **3-dot 버튼**을 눌러 **Flow를 선택**하고, 우리가 만든 **get_comments_info**를 확인해 주세요.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-12.png)

3. 클릭해서 선택한 후, 아래 화면처럼 **Add Action**을 눌러 마무리해 줍니다.  
![alt text](/mwkorea/assets/images/agentschool/1_automateAgent/image-13.png)

> 🎯 여기까지 완료했다면, Action에 **get_comments_info**가 성공적으로 등록된 거예요!

---

</br>
</br>

# 🧾 I. 결론  

오늘은 **Power Automate**에서 **Excel 모듈**을 활용해,  
**SharePoint**에 업로드된 **엑셀 파일의 테이블 정보**를 가져오는 Flow를 만들어 보았어요.  

### 📌 오늘의 주요 학습 내용  

1. **엑셀 모듈을 활용해 데이터 불러오기**  
2. **SharePoint와 엑셀 파일 연결 설정하기**  
3. **Power Automate에서 Flow 생성 및 테스트하기**  

---

### ⏭️ 다음 시간에는?  

다음 시간에는 **불러온 엑셀 정보를 자동으로 이메일로 보내는 시스템**을 구축할 거예요.  
또한, **Generative Orchestrator 설정**을 통해 AI가 자동으로 해당 기능을 실행할 수 있게 해 볼게요! 🚀  
