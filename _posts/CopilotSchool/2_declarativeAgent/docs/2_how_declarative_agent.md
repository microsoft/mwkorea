안녕하세요, MW Technical Specialist 인턴 조항우입니다😊  
오늘도 저번시간에 이어서 Copilot의 Declarative Agent를 만들면서 익혀볼게요.    

# ⚒️ 만들면서 Declarative 에이전트를 익혀보아요(2)

### **학습 목표:** ###  
저번 강의에 이어 문서를 참조하고, 해당 문서를 기반으로 답변하는 챗봇 만들기를 진행하면서 **Declarative 에이전트의 기능**에 대해 소개해 드릴게요.  


이번 학습을 통해 다음과 같은 내용을 익힐 수 있어요!
- **액션이란 무엇인가**
- **Knowledge를 활용해 문서를 참조하는 법**  
- **에이전트의 테스트 방법**  
- **에이전트 배포 및 활용법** 


이번 학습은 Declarative 에이전트 기능소개(1) 에 이어서 진행되므로, 꼭 첫 번째 학습을 완수해주세요!  
---


![alt text](../assets/2_how_declarative_agent/function_finish_2.png)  

위 화면에서부터 다시 시작해보겠습니다.  
초기 설정한 내용들이 그대로 적용되어 있을 거예요.  
그런데 초기 설정에서 보지 못한 기능들이 몇 개 보이네요?  

---

## 1️⃣ 액션 (Action)  

1번 기능인 액션이란 **에이전트의 기능을 확장하여 다양한 작업을 수행할 수 있도록 하는 기능**이에요.  
이를 통해 **외부 시스템과 통합하거나, 데이터를 처리하거나, 자동화된 워크플로우를 실행**하는 등 여러 작업을 수행할 수 있습니다.  

Copilot Studio에서는 **Connector, Flow** 등 다양한 액션을 지원해요.  

액션이 없다면 **Declarative 에이전트는 기존에 있는 자료를 바탕으로 답변하거나 LLM 역할**밖에 수행하지 못해요.  
하지만 **액션을 활용하면** 다음과 같은 작업이 가능해집니다:  
✅ 기상청 API를 호출해 날씨 정보를 받아오기  
✅ 회사의 API에 접근해서 최신 데이터를 불러오기  
✅ 데스크톱을 자동화하여 반복적인 작업 수행  

이번 기능 소개에서는 액션을 사용하지 않아요.  
하지만, 곧 업데이트될 **핸즈온 학습**에서는 다양한 액션을 직접 사용해볼 예정입니다.  

---

## 2️⃣ Test 팝업  

![alt text](../assets/2_how_declarative_agent/testing_2.png)  

2번 기능에는 **Test 팝업**에서는 우리가 만든 에이전트를 **배포 전에 미리 테스트**할 수 있습니다.  
상단에는 우리가 적용한 시작 프롬프트들이 보이네요.  
굳이 배포하지 않아도 테스트할 수 있다는 점에서 **개발자들에게 매우 유용한 기능**입니다.  

---

## 3️⃣ Knowledge에 참고 문헌 추가하기  

이제 **Knowledge에 문헌을 추가하여** Copilot이 파일을 기반으로 답변하도록 만들어볼게요.  
이를 위해서는 **참고할 문서**를 먼저 준비해야 합니다.  
저는 이미 **짱구 명대사 PDF 파일**을 준비해 놓았어요.  
이제 이 파일을 **SharePoint**에 업로드해야 합니다.  


> **SharePoint 페이지를 만들고 파일을 업로드하는 법**  
> 많은 분들이 익숙하겠지만, 익숙하지 않은 분들을 위해 정우 멘토님께서 작성한 가이드를 공유할게요.  
> [👉 쉐어포인트 페이지 만들기 & 파일 업로드 방법](https://lanslote.github.io/copilot/agent-HOL/31)  

---

위 내용을 따라 SharePoint 페이지를 만들고 파일을 업로드했다면, 이제 아래 화면의 **Knowledge** 부분에서 `Add` 버튼을 눌러주세요.  
저는 미리 추가해 놓아서 Knowledge가 등록된 상태지만, 여러분의 화면에는 등록된 Knowledge가 없을 거에요.  

![knowledge_add](../assets/2_how_declarative_agent/knowledge_add.png)  

버튼을 클릭하면 아래와 같은 화면이 나타납니다.  
이제 **SharePoint를 선택**해주세요!  

![alt text](../assets/2_how_declarative_agent/add_knowledge.png)  

하이라이트된 부분에 참고할 문서의 **SharePoint URL을 입력**해주세요.  
저는 **짱구 명대사 PDF 파일의 링크**를 입력하겠습니다.  
아니면 `Browse file`을 통해 직접 조직의 SharePoint에서 문서를 찾아서 업로드할 수도 있어요.  

이제 `Add` 버튼을 눌러 추가해볼까요?  

![alt text](../assets/2_how_declarative_agent/sharepoint_link.png)  

✅ **이제 에이전트가 파일을 참조할 수 있게 되었어요!**  

---

## 4️⃣ 테스트 실행  

이제 아까 설명드린 **테스트 환경**에서 제대로 문서를 참고하는지 확인해볼게요.  
![alt text](../assets/2_how_declarative_agent/testing_2.png)  

오, 잘 불러와지네요! 😃  

---

## 5️⃣ 배포하기  

이제 마지막으로 배포(Publish)를 해봅시다.  
위 화면에서 우측 상단의 `Publish` 버튼을 눌러주세요!  

![alt text](../assets/2_how_declarative_agent/publish_1.png)  

그럼 다음 화면으로 이동할 거예요.  
여기서 **하단의 `Publish` 버튼을 한 번 더 눌러주세요.**  

![alt text](../assets/2_how_declarative_agent/publish_2.png)  

✅ **위 화면처럼 표시되면 배포가 완료된 것입니다!**  

---

## 6️⃣ 배포된 에이전트 활용하기  

배포된 Declarative 에이전트는 **3가지 방식**으로 사용할 수 있습니다.  

1️⃣ **링크 공유**  
   - 공유된 링크를 통해 Copilot에서 사용할 수 있습니다.  

2️⃣ **User Access 배포**  
   - **Teammates 및 특정 사용자**에게 배포 가능해요! 
   - **조직 전체 배포 시, Admin 승인이 필요**합니다.

3️⃣ **ZIP 파일로 Export**  
   - 에이전트의 코드와 설정을 `.zip` 파일로 다운로드 가능해요.
   - 로컬 환경에서 백업 및 별도 관리 가능해요.

---

## ✅ 마무리  

이제 간단한 RAG 챗봇을 만들면서 **Declarative 에이전트의 모든 기능**을 살펴봤어요!  
어떤가요? Declarative 에이전트가 어떤 개념인지 감이 좀 오시나요?  

처음 접하시는 분들은 다소 생소할 수 있지만,  
더 자세히 공부하고 싶다면 아래 **공식 문서**를 참고해보세요.  

📖 **[https://learn.microsoft.com/copilot-studio](https://learn.microsoft.com/copilot-studio)**  

---

### 🔜 다음 시간 예고  
다음 강의에서는 **Custom Engine 에이전트**를 살펴볼 예정입니다.  
Declarative 에이전트와의 차이점이 무엇인지 비교하면서 학습해봐요! 🚀
