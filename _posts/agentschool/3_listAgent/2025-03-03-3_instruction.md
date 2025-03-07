---
title: "차량 렌탈 시스템 에이전트 만들기 (3)"
date: 2025-03-03T00:00:00 KST
categories:
  - AgentSchool
tags:
  - AI
  - Agent
  - Copilot
excerpt: "이번 시간에는 Instruction을 활용하여 Copilot Agent를 고도화하고 개선하는 방법을 배워볼 거예요.  "
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

# 🚀 A. 이전 학습 돌아보기
이전 학습에서는 **`create_car`** 액션을 구현하면서, 다음 개념들을 배웠어요.  

1️⃣ **Action과 Power Automate Flow의 개념**  
2️⃣ **Customer Engine Agent에서 Flow를 만들고 옮기는 법**  
3️⃣ **Copilot Agent가 Action을 호출하고 파라미터를 추출하는 원리**  

---

</br>
</br>

이번 시간에는 **Instruction을 활용하여 Copilot Agent를 고도화하고 개선하는 방법**을 배워볼 거예요.  

### 질문:  왜 배우는 걸까요?  
앞으로 **Action을 추가하면서 Agent의 기능 복잡도가 올라갈수록** 다음과 같은 문제가 발생할 수 있어요.  
- Action 호출의 정확도가 떨어짐  
- Output의 품질이 원하는 대로 제어되지 않음  

💡 이를 해결하기 위해 **Instruction을 활용하여 Agent에게 명확한 지침을 주고 컨트롤하는 방법을 익혀야 합니다.**  

---

</br>
</br>

# C. Instruction 추가해보기  
## 📌 Instruction 추가 방법  
Instruction을 작성하는 방법을 배우기 전에, **추가하는 법부터 익혀볼까요?**  

💡 정말 간단합니다!  

![only](/mwkorea/assets/images/agentschool/3_instruction/instructions.png)

1️⃣ **Declarative 에이전트 화면에서 `Edit` 버튼 클릭**  
2️⃣ **Instructions 입력 후 `Save` 버튼 클릭**  

🚀 끝! 너무 쉽죠?  
*(우리가 다루고 있는 Agent는 **Copilot for M365** 안의 **Declarative 에이전트**라는 것, 잊지 마세요!)*  

---

</br>
</br>

#  D. Instruction과 프롬프트 엔지니어링  
## 🔍 Instruction이 왜 중요할까요?  
**Instruction이 중요한 이유는 모델의 작동 방식을 결정하기 때문이에요.**  

**중요**: **Copilot에서는 Instruction**이라고 부르지만, 다른 LLM 모델에서는 **시스템 프롬프트**라는 개념이 존재해요.  
- 이는 우리가 GPT를 사용할 때 입력하는 **User Prompt**와는 달라요.  
- 모델의 **행동 방식, 응답 스타일, 제한 사항**을 미리 정의하는 역할을 합니다.  
- 즉, **Agent의 행동 방식과 응답 스타일을 제어하고 싶다면, Instruction을 구체적으로 작성하는 것이 필수적!**  

## 🏗️ 프롬프트 엔지니어링이란?  
프롬프트 엔지니어링은 **모델이 원하는 방식으로 응답하도록 입력을 설계하는 기술**이에요.  

✔️ 단순히 질문을 던지는 것이 아니라,  
✔️ **어떤 단어를 사용하고, 어떤 맥락을 제공하며, 어떤 형식을 요구하는지**에 따라  
✔️ Copilot Agent의 **응답 품질이 크게 달라집니다!**  

예를 들어,  
❌ `"이 코드 설명해줘"` → 일반적인 답변  
✅ `"이 코드를 한 줄씩 분석해주고, 실행 흐름을 설명해줘"` → 단계적이고 구체적인 답변  
**프롬프트 엔지니어링을 활용하여 Copilot Agent에게 명확한 지시를 내리고, 원하는 결과를 구체적으로 정의해야 합니다.**  
Knowledge가 많아지고, Action이 고도화될수록 **Instruction의 중요성은 더욱 커집니다.**  
</br>
</br>
#  E. Instruction 프롬프트 적용과 분석  
## 🛠️ 사용할 프롬프트  
차량 렌탈 시스템에 사용할 **Instruction 프롬프트**는 아래와 같아요.  
💡 **아래 내용을 복사 & 붙여넣기하여 적용해 주세요!**  

📌 **프롬프트는 Markdown 형식**으로 작성되었습니다.  
- 일부에서는 **플레인 텍스트**를 선호하기도 하지만,  
- 저는 **Markdown 형식으로 작성하는 것이 훨씬 효과적**이라고 생각해요!  
</br>
</br>

---

  <프롬프트 시작>차량 렌탈 시스템 에이전트 Instruction   

   A. 역할 (Role)**  
   - 당신은 **회사 차량 렌탈 시스템**의 **AI 에이전트**입니다.  
   - 사용자의 요청을 분석하고 적절한 **액션 함수**를 호출하여 요청을 처리합니다.  
   - **쉐어포인트 권한이 필요한 경우, 먼저 권한을 요청한 후 액션을 실행합니다.**  
   - 액션 호출 후, 반드시 **응답 데이터를 반영하여 사용자에게 결과를 전달**합니다.  
   - 시스템은 다음 두 개의 변수를 정확하게 인식해야 합니다:  
      1. `user_reserved_start` - 예약 시작 시간을 나타냅니다. **이 값은 항상 `user_reserved_end`보다 빠른(이전) 시간이어야 합니다.**  
      2. `user_reserved_end` - 예약 종료 시간을 나타냅니다. **이 값은 항상 `user_reserved_start`보다 늦은(이후) 시간이어야 합니다.**  



   B. 중요 규칙 (Critical Rules)  
   - **두 변수 이름을 변경하거나 서로 바꾸지 마세요.**  
   - **항상 `user_reserved_start`는 시작 시간, `user_reserved_end`는 종료 시간으로 사용해야 합니다.**  
   - **사용자가 입력하는 시간은 한국 시간(KST, UTC+9) 기준입니다. 하지만 UTC 변환을 수행하지 않고, 입력된 값을 그대로 `Z` 형식으로 저장해야 합니다.**  
      - 예: 사용자가 `"10월 1일 오후 3시"`라고 입력하면, **`2025-10-01T15:00:00Z`**로 저장해야 합니다.  
      - 잘못된 예: `2025-10-01T06:00:00Z` (UTC로 변환되었으므로 잘못되었습니다)  



   C. 동작 원칙 (Operational Principles)  
   1. **간결하고 명확한 응답 제공**  
      - 요청 처리 후 **결과를 사용자에게 직관적으로 전달**합니다.  



   D. 호출 가능한 액션 목록 (Available Actions)  
   **1. 차량 등록 (create_car)**
   - **기능:** 새로운 차량을 시스템에 등록합니다.
   - **입력 정보:**  
     - car_num: 차량 번호판 (텍스트)  
     - car_size: 차량 크기 (예: 소형, 중형, 대형)  
     - car_name: 차량 모델명  
     - seating_num: 탑승 가능 인원 (숫자)  
     - is_operating: 운용여부 (True/False)
   - **주의사항**  
     1. is_operating은 운용중이면 TRUE 아니면 FALSE



   **2. 운용 중인 차량 조회 (get_operating_cars)**
   - **기능:** 쉐어포인트에서 현재 운용 중인 차량 목록을 불러옵니다.
   - **주의사항:** 해당 액션은 운용 가능한 차량의 목록을 불러옵니다.
   - **출력 정보:**  
     - 운용 가능한 차량 목록 (Raw data)



   **3. 차량 예약 가능 여부 확인 (check_reservation)**
   - **기능:** 특정 차량이 지정된 시간에 예약이 가능한지 확인합니다.
   - **입력 정보:**  
     - car_id: 차량 ID  
     - reservation_time: 예약 희망 시간 (예: 2025-11-19 15:00~18:00)  
   - **출력 정보:**  
     - 예약 가능 여부 (True/False)  
     - 예약 요청 시간  
   - **필수 행동:**  
     - 액션 실행 후, **예약 가능 여부를 사용자에게 반드시 전달**합니다.



   **4. 차량 예약 생성 (create_reservation)**
   - **기능:** 특정 차량을 요청한 시간에 예약합니다.
   - **출력 정보:**  
     - 예약 결과: 성공 여부 (True/False)


   **5. 내 예약 목록 조회 (get_my_reservations)**
   - **기능:** 사용자의 기존 예약 목록을 불러옵니다.
   - **출력 정보- json에서 대응되는 키값, 꼭 아래 정보들을 모두 제공하시오**  
     - 예약 ID-ID  
     - 차량 ID-Title  
     - 예약 시작 시간-field_3  
     - 예약 종료 시간-field_4  
   - **주의사항:** 자체적으로 정보를 생성하지 말고, 꼭 Action을 통해서 받아온 body의 'my_reservations'에 근거해서 답변을 제공해줘.


   **6. 예약 취소 (delete_reservation)**
   - **기능:** 특정 예약을 취소합니다.
   - **입력 정보:**  
     - reservation_id: 예약 ID  
   - **출력 정보:**  
     - 예약 삭제 결과: 성공 여부 (True/False)

 
  **E. 예제 (Usage Examples)**

   | **사용자 요청** | **호출 액션** |
   |----------------|--------------|
   | "차량 추가하고 싶어요" | create_car |
   | "운용 중인 차량 리스트 보여줘" | get_operating_cars |
   | "car_id 18이 2025년 11월 19일 15시부터 18시까지 예약 가능한지 확인해줘" | check_reservation |
   | "car_id 18을 2025년 11월 19일 15시부터 18시까지 예약해줘" | create_reservation |
   | "내 예약 목록 알려줘" | get_my_reservations |
   | "예약 ID 187번 취소해줘" | delete_reservation |  
   
---

</br>
</br>

# F. 프롬프트의 구조  

이번에 작성한 **프롬프트**는 아래와 같은 구성으로 설계했어요.  

### ✅ 프롬프트 구조  
1. 역할(Role)  
2. 중요 규칙(Critical Rules)  
3. 동작 원칙(Operational Principles)  
4. 호출 가능한 액션 목록(Available Actions)  
5. 예제(Usage Examples)  

💡 **프롬프트 구조는 다양한 방식으로 설계할 수 있습니다.**  
이에 관련된 연구와 책들도 많으니, **유튜브나 서점에서 "프롬프트 엔지니어링"을 검색해보면** 도움이 될 거예요!  
이제 각 요소가 어떤 역할을 하는지 살펴볼까요?  

---

## 🏗️ 1. 역할 (Role) 작성법  
Copilot이 어떤 역할을 수행하는지 **명확하게 정의**하는 것이 중요해요.  

###  1️⃣ 어떤 시스템에서 작동하는지 설명하기  
- Copilot이 **어떤 맥락에서 작동하는지**를 분명하게 적어야 해요.  
- 예: `"회사 차량 렌탈 시스템의 AI 에이전트"`처럼 **도메인과 역할**을 명확히 기술해야 합니다.  

###  2️⃣ 주요 기능을 구체적으로 명시하기  
- Copilot이 수행해야 할 핵심 기능을 정리해야 해요.  
- 예: `"사용자의 요청을 분석하고 적절한 액션을 호출하여 처리"`  

###  3️⃣ 제약 사항을 포함하기  
- Copilot이 특정한 절차를 따라야 한다면, 이를 명확히 설명해야 해요.  
- 예: `"쉐어포인트 권한이 필요할 경우, 먼저 권한을 요청한 후 액션을 실행해야 합니다."`  

---

## ⚠️ 2. 중요 규칙 (Critical Rules) 작성법  
Copilot이 올바르게 작동하기 위해 **반드시 지켜야 할 규칙**을 정해야 해요.  

### 1️⃣ 핵심 변수에 대한 규칙 정하기  
- Copilot이 사용하는 변수의 의미가 **변경되지 않도록** 해야 해요.  
- 예: `"user_reserved_start는 예약 시작 시간을 나타내며, 항상 user_reserved_end보다 이전이어야 합니다."`  

### 2️⃣ 데이터 변형 방지  
- AI가 **자체적으로 데이터를 수정하지 않도록** 주의해야 해요.  
- 예: `"Copilot은 액션을 통해 받아온 데이터를 기반으로 응답해야 하며, 자체적으로 정보를 생성하지 말아야 합니다."`  

### 3️⃣ 작업 순서 명확히 하기  
- 특정 작업이 선행되어야 한다면 이를 명확하게 기술해야 해요.  
- 예: `"쉐어포인트 권한이 필요한 경우, 먼저 권한 요청 후 액션을 실행해야 합니다."`  

---

## ⚙️ 3. 동작 원칙 (Operational Principles) 작성법  
Copilot이 **답변을 생성할 때 따라야 할 기본적인 원칙과 응답 스타일**을 설정해야 해요.  

###  1️⃣ 응답 스타일을 정의하기  
- Copilot이 간결하게 답변할지, 상세한 정보를 포함할지 설정하는 것이 중요해요.  
- 예: `"요청 처리 후 결과를 사용자에게 직관적으로 전달해야 합니다."`  

###  2️⃣ 데이터 처리 방식 정리하기  
- Copilot이 다루는 데이터가 **어떤 형식으로 저장되거나 처리되어야 하는지** 명확하게 설명해야 해요.  
- 예: `"사용자가 입력하는 시간은 한국 시간(KST, UTC+9) 기준이며, UTC 변환 없이 ‘Z’ 형식으로 저장해야 합니다."`  

---

##  D. 호출 가능한 액션 목록 (Available Actions) 작성법  
Copilot이 실행할 수 있는 액션을 정리하고, **필요한 입력값과 출력값을 명확히 기술**해야 해요.  

### 1️⃣ 각 액션의 역할 설명하기  
- 액션이 **어떤 기능을 수행하는지 간단명료

### 2️⃣ 입력값과 출력값 정의하기  
- Copilot이 액션을 호출할 때 **필요한 입력값과 반환값을 명확히 지정**해야 해요.  
- 예: `"차량 등록 액션(create_car)에는 차량 번호판, 크기, 모델명, 탑승 가능 인원, 운용 여부(True/False) 등의 입력값이 필요하다."`  

### 3️⃣ 주의사항 추가하기  
- 액션을 사용할 때 반드시 지켜야 할 조건이 있다면, 이를 명확히 작성해야 해요.  
- 예: `"예약 목록 조회 시, Copilot은 데이터를 자체 생성하지 말고 반드시 액션을 통해 받은 응답을 기반으로 사용자에게 제공해야 합니다."`  

---

## 📖 E. 예제 (Usage Examples) 작성법  
Copilot Agent가 올바르게 동작하는지 검증하기 위해 **실제 사용 예시를 포함하는 것이 중요해요.**  

### 1️⃣ 사용자 요청과 액션을 매핑하기  
- 사용자가 입력할 요청 문장과 실행할 액션을 **일대일로 정리**해야 해요.  

| **사용자 요청** | **호출 액션** |
|----------------|--------------|
| "차량 추가하고 싶어요" | `create_car` |
| "운용 중인 차량 리스트 보여줘" | `get_operating_cars` |
| "car_id 18이 2025년 11월 19일 15시부터 18시까지 예약 가능한지 확인해줘" | `check_reservation` |
| "car_id 18을 2025년 11월 19일 15시부터 18시까지 예약해줘" | `create_reservation` |
| "내 예약 목록 알려줘" | `get_my_reservations` |
| "예약 ID 187번 취소해줘" | `delete_reservation` |

### 2️⃣ 실제 요청 문장 형식 맞추기  
- Copilot이 실제 상황에서 **어떻게 동작할지 자연스러운 요청 문장을 예제로 제공**하면 좋아요.  
- 예: `"car_id 18이 2025년 11월 19일 15시부터 18시까지 예약 가능한지 확인해줘"` → `check_reservation` 실행  

---

</br>
</br>

# 🛹 G. 결론  
이번 학습에서는 다음 내용을 배웠어요!  

✅ **Instruction을 추가하는 방법**  
✅ **Instruction 작성 시 적용되는 프롬프트 엔지니어링 개념**  
✅ **프롬프트 구조와 각 요소별 작성법**  

🚀 **에이전트의 목적이나 구동 방식에 따라 Instruction 내용은 달라질 수 있지만, 위 구성을 지키면 원하는 대로 LLM이나 Agent를 효과적으로 구동할 수 있습니다.**  

💡 **이제 Instruction을 탄탄하게 작성했으니, 다음 시간부터는 `get_operating_car`를 구현해볼까요?**  