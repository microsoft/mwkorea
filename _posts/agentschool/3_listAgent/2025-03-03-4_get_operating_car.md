---
title: "차량 렌탈 시스템 에이전트를 만들기 (4)"
date: 2025-03-03T00:00:00 KST
categories:
  - AgentSchool
tags:
  - AI
  - Agent
  - Copilot
excerpt: "이번 시간에는 get_operating_car 액션을 만들어 운용 가능한 차량만 필터링하여 불러오는 방법을 배울 거예요."
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

# 🛹 A. 이전 학습 복습하기

지난 시간에는  
✅**Copilot Agent의 Instruction**이 무엇인지,  
✅**프롬프팅 엔지니어링**을 활용하여 **Instruction을 정교하게 작성하는 방법**에 대해 배웠어요!

---

</br>
</br>

# 🚀 B. 이번 학습 내용
이번 시간에는 **get_operating_car** 액션을 만들어 **운용 가능한 차량만 필터링하여 불러오는 방법**을 배울 거예요.  
이 과정을 통해 **SharePoint List 아이템들을 필터링하여 가져오는 방법**을 익혀볼게요! 🚗

---

</br>
</br>

# 🛸 C. 주의사항
이번 학습부터는 **create_car**를 만들 때 익혔던 **Custom Engine Agent에서 Flow를 생성하고 이를 Declarative Agent에서 불러오는 과정**을 익혔다고 가정하고 설명할 거예요.  
헷갈리는 부분이 있다면 **create_car 학습 내용을 참고**해 주세요!  
만약 **create_car 과정을 건너뛰었다면, 꼭 학습한 후 이번 과정으로 넘어와 주세요!**  

---

</br>
</br>

# 🎉 D. get_operating_car 만들기 

## 목표
✅ **get_operating_car 액션을 통해 SharePoint에서 운용 가능한 차량만 불러오는 것**이 목표예요.  
- 즉, **SharePoint `car_list`에서 `is_operating`이 `true`인 차량만 필터링**하는 거죠!  
- 우리가 만들 **최종 목표 Flow는 아래 캡처와 같아요.**  

![.](/mwkorea/assets/4_get_operating_car/1.png)



##  사전 진행 사항
- **Custom Engine Agent에서 Power Automate Flow 액션을 생성해주세요!**  
  → **create_car에서 진행한 것과 동일한 방식으로** 진행해주시면 된답니다:)  
- **Power Automate 화면에서 부터 설명을 하겠습니다!**  
  → 아래 Custom Engine 에이전트에서 Flow를 생성한 아래 화면까지 진행해주시고 설명을 따라와주세요:) 

![.](/mwkorea/assets/4_get_operating_car/2.png)




##  Run a Flow From Copilot
- **지난 시간에 배웠던 `Run a Flow from Copilot`의 역할**, 기억하시죠?  
  → **Flow 실행에 필요한 입력값을 유저로부터 받는 역할**을 해요.  
- 하지만 이번에는 **입력값이 필요 없기 때문에 따로 설정할 필요 없어요!**  
  → **설정 없이 그대로 두면 됩니다.** 👍  

---

##  Get Items 설정하기

### 1️⃣ Get Items 추가하기
- `Run a Flow from Copilot`과 `Respond to Copilot` **사이에** **`Get Items`를 추가**해주세요.  
- 아래 캡처처럼 항목을 검색하여 선택하면 돼요!  


![.](/mwkorea/assets/4_get_operating_car/3.png)

### 2️⃣ SharePoint와 List 연결하기
- **create_car과 동일하게**  
  - 접근할 **SharePoint Page와 List를 설정**해주세요.  
  - 첫 학습에서 만든 **Page와 `car_list`를 선택**하면 됩니다.  

### 3️⃣ SharePoint 필터 설정하기
- 목표는 **`car_list` 중에서 `is_operating`이 `yes`인 차량만 가져오는 것**이에요.  
- 여기서 주의해야 할 점!  
  - **SharePoint에서 `yes/no` 데이터 타입을 만들었지만, 필터에서는 `1/0`으로 설정해야 해요.**  
    - `yes` → `1`  
    - `no` → `0`  

- **Get Items 설정 화면에서**  
  - `Advanced Parameters` → `Filter Query`를 클릭!  
  - 필터를 설정할 수 있는 입력란이 보일 거예요.  
  - 클릭시 아래 처럼 Filter Query가 나타나게 됩니다. 
  - 저는 Top Count까지 선택하고, 값들을 채워놨어요! 여러분들은 빈 Filter Query 나타나는게 정상입니다:) 

![.](/mwkorea/assets/4_get_operating_car/4.png)
---

### 4️⃣ Filter Query 작성하기
- 필터는 다음 형식으로 작성하면 돼요.  
  ```plaintext
  {Column의 시스템 명칭} eq {원하는 값}
  ```
- 위 Query는 **OData 형식**을 따르기에, 다양한 조건을 설정할 수도 있어요!  
  → **더 알고 싶다면 "OData Query 문법"을 검색해보세요!** 🔎  

---

##  Column의 시스템 명칭 찾기 (중요!)
- **Filter Query에서는 Column명을 직접 입력해야 해요!**  
  → 보통 `/`를 눌러 원하는 Dynamic Content를 선택하면 되지만,  
     **Filter Query에서는 이 방법을 사용할 수 없어요.**  
  → 따라서, **Column의 시스템 명칭을 직접 찾아야 합니다.**  
  
### 1️⃣ **'Filter array'를 추가**  
   - `+` 버튼을 눌러 **'Filter array'** 추가  
   - `Filter Query`의 `Choose a value`란에서 `/` 입력 후 Dynamic Content 선택  
   - `See more` 클릭 → 원하는 변수명인 `is_operating` 선택  

![.](/mwkorea/assets/4_get_operating_car/5.png)

*⚠️주의*:  위의 사진처럼 filter array만 골라도 For Each가 자동적으로 생길 수 있는데요. 
Get items때문에 각 아이템을 순회해야 되서 생긴것이지만 어짜피 시스템 명칭만 알아내고 삭제 할테니 큰 상관없습니다. 

### 2️⃣ **변수명 확인**
   - `is_operating`을 추가한 후 **해당 변수명을 드래그하여 메모장에 복사**  
   - 보통 시스템 명칭은 아래와 같은 형식으로 나올 거예요.  
     ```plaintext
     field_5
     ```
   - **아래 화면의 괄호 안의 영역이 Column의 시스템 명칭**입니다.  

![.](/mwkorea/assets/4_get_operating_car/6.png)

### 3️⃣ **For Each와 Filter Array 삭제**
   - **자동 생성된 `For Each`와 시스템 명칭만을 알아내기 위해 만든 `Filter Array`는 삭제해주세요!**  
   - 그럼 시스템 명칭도 알아냈으니 `Get Items`로 돌아가서 필터 입력해줄까?  
   - **True 값 필터링을 위해 아래처럼 입력**해주세요  
     ```plaintext
     field_5 eq 1
     ``` 
   - 여러분의 시스템 명칭은 저와 다를 수 있어요. 여러분의 시스템 명칭을 적용해 주시면 됩니다!
   - **Top Count(최대 불러올 아이템 수) 설정**  
     - 기본적으로 너무 많은 데이터를 불러오면 속도가 느려지니 **10개 정도**가 적절해요.  

![.](/mwkorea/assets/4_get_operating_car/4.png)

✅ **이제 Get Items 설정이 완료되었습니다!** 🎉  
다음 단계로 넘어가 볼까요?



## Respond to Copilot
- `Get Items`를 사용해서 아이템들을 불러오는 것까지 성공했다면, 이제 불러온 값들을 **Copilot Agent에게 전달**해야 해요.  
- 아래와 같이 **Output을 설정**해주세요.  
  - `'body/value'`는 `/`를 누른 후 **Dynamic Content를 클릭하여 추가**하면 됩니다.  
  - 저는 **Output이 어떤 정보인지 설명하는 문장을 Description에 추가**했어요!  

  ```plaintext
  "This is raw content. Copilot should organize this result before showing to user."
  ```


![.](/mwkorea/assets/4_get_operating_car/7.png)

✅ **이제 Flow 설정이 완료되었습니다! 🎉**  

---

## 사후 진행 사항  
**create_car에서 했던 것과 동일한 절차를 진행해 주세요!**  
기억이 안 나신다면 **create_car 학습을 참고**해 주세요.  
create_car를 완벽하게 익혔다면 **그대로 따라 진행하면 됩니다.**  

1️⃣ **Power Automate 편집창에서 Flow 이름 변경**  
   - `"Run Flow from Copilot"` → `"get_operating_car"`  

2️⃣ **Flow 저장 및 배포**  
   - `Save` 클릭 후 `Publish`  

3️⃣ **Custom Engine Agent에서 Flow 불러오기 & 추가**  
   - (불러오는 데 시간이 걸릴 수 있어요. 새로고침 시도!)  

4️⃣ **Custom Engine Agent 코드 에디터에서 코드 복사**  

5️⃣ **Declarative Agent에서 Dummy 액션 생성 후 코드 붙여넣기**  
   - Power Automate Action의 Flow로 덮어쓰기  

6️⃣ **Declarative Agent Overview에서 액션 이름 변경**  
   - `"get_operating_cars"`로 변경  

✅ **여기까지 완료하면, Copilot Agent가 `get_operating_cars`를 통해 운용 중인 차량을 불러와 고객에게 제공할 수 있습니다!** 🚘  
이제 테스트를 진행해볼까요?  

---

</br>
</br>

# 🚆 E. 테스트해보기 
**create_car와 동일한 방식으로 Overview 화면의 오른쪽에서 테스트를 진행할게요.**  

## 1️⃣ 테스트 데이터 넣어보기  
![.](/mwkorea/assets/4_get_operating_car/8.png)

- 저는 테스트를 위해 **`car_list`에 더미 데이터를 채워 넣었습니다.**  
- 여러분도 테스트하려면,  
  - **직접 데이터를 수기로 입력**하거나,  
  - **GPT에게 CSV 형식 데이터를 요청한 후 업로드하면 대량의 더미 데이터로 쉽게 테스트 가능해요!**  



## 2️⃣ 테스트 실행 & 결과 확인  
![.](/mwkorea/assets/4_get_operating_car/9.png)
- **테스트 결과:**  
  - `is_operating`이 `yes`인 차량들만 **정확하게 필터링되어 가져와졌어요!** 🎯  
- 추가적으로, `"운용 중인 차량을 불러와서 표로 보여줘"`라고 질문하면,  
  → **Copilot이 표로 정리하여 결과를 제공해줍니다!** 📊  

---

</br>
</br>

# 🎯 D. 결론 
다들 따라오시느라 수고많으셨습니다. 시스템 변수 부분이 좀 어렵죠?  
하지만 그부분을 뺴면 이번 학습은 무난했던것 같습니다. 
이번 강의를 랩업 하자면 저희는  **get_operating_cars**를 통해 다음을 배웠어요.  

✅ **`Get Items`를 활용하여 SharePoint List에서 아이템을 불러오는 방법**  
✅ **Filter Query를 사용해 특정 조건을 만족하는 데이터만 필터링하는 방법**  

🚀 **다음 학습 예고:**  
- 차량이 특정 시간에 예약 가능한지 확인하는 **`check_reservation`**  
- 차량 예약을 생성하는 **`create_car_reservation`**  

**다음 시간에는 난이도가 높아집니다!**  
복잡한 로직을 **Power Automate을 활용하여 구현하면서, Power Automate Flow를 완전 정복해볼게요!** 💪🔥  
