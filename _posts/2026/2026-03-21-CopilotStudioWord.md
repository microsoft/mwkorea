---
title: "코파일럿 스튜디오에서 워드파일을 참조할 때 도움이 될 팁"
date: 2026-03-21T00:00:00 KST
categories:
  - CopilotStudio
tags:
  - CopilotStudio
  - Word
  - Agent
  - Tips
excerpt: "코파일럿 스튜디오에서 워드 파일을 참조할 때 어떤 형식이 정확한 답변으로 이어지는지, 5가지 유형 비교 테스트 결과를 공유합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 코파일럿 스튜디오에서 워드파일을 참조할 때 도움이 될 팁

이전 포스트 **"코파일럿 스튜디오에서 엑셀파일을 참조할 때 도움이 될 팁"** 에 이은 내용입니다. 해당 포스트를 읽고 오시면 이해하시는 데 도움이 될 것 같습니다.

이전 포스트의 핵심을 요약하면 다음과 같습니다.

- 엑셀파일의 내용은 인간이 보기에는 구조적이다.
- 그런데 코파일럿 스튜디오에서 엑셀의 내용을 사용할 때는 그냥 평문 텍스트로 쭈욱 뽑아서 쓴다.
- 그래서 그 엑셀을 참조시키면 잘못된, 엉뚱한 답변이 나온다.
- 그걸 해결하려면 엑셀로부터 뽑아져 나온 텍스트를 구조화된 것처럼 힌트를 좀 더해준다.

![엑셀 팁 포스트 요약](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image1.png)

그런데, **워드 문서는 어떨까?** 가 이 포스트의 주제입니다.

---

## 5가지 워드 문서 형식 비교 테스트

이왕 테스트하는 김에 5가지 유형으로 워드 문서를 만들어서 테스트를 해봤습니다.

- 워드에 **표** 형식
- 워드에 **평문** 형식
- 워드에 **평문이지만 콤마로 구분**한 형식
- 워드에 **불릿** 형식
- 워드에 **불릿으로 구분하고 콤마로 구분**한 형식

---

### 1형식 — 표

![5가지 워드 문서 유형 예시](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image2.png)

---

### 2형식 — 평문

![워드 표 형식 예시](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image3.png)

---

### 3형식 — 평문 + 콤마

![워드 평문 형식 예시](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image4.png)

---

### 4형식 — 불릿

![워드 평문 + 콤마 형식 예시](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image5.png)

---

### 5형식 — 불릿 + 콤마

![워드 불릿 형식 예시](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image6.png)

---

## 테스트 결과

결과부터 이야기하면 아래와 같습니다.

| 형식 | 내용 | 테스트 결과 |
|------|------|------------|
| 1형식 | 표 | 💀 가끔 잘못되고 엉뚱한 답변 |
| 2형식 | 평문 | 💀 가끔 잘못되고 엉뚱한 답변 |
| 3형식 | 평문 + 콤마 | 💀 가끔 잘못되고 엉뚱한 답변 |
| **4형식** | **불릿** | **✅ 제대로 된 답변** |
| 5형식 | 불릿 + 콤마 | 💀 가끔 잘못되고 엉뚱한 답변 |

**불릿(bullet) 형식만이 일관되게 정확한 답변을 반환했습니다.**

![테스트 결과 전체 비교](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image7.png)

## 각 형식별 결과 상세

### 1형식 — 💀 가끔 잘못되고 엉뚱한 답변

![각 형식별 에이전트 응답 화면](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image8.png)

---

### 2형식 — 💀 가끔 잘못되고 엉뚱한 답변

![1형식 테스트 결과 화면](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image9.png)

---

### 3형식 — 💀 가끔 잘못되고 엉뚱한 답변

![2형식 테스트 결과 화면](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image10.png)

---

### 4형식 — ✅ 제대로 된 답변

![3형식 테스트 결과 화면](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image11.png)

---

### 5형식 — 💀 가끔 잘못되고 엉뚱한 답변

![4형식 테스트 결과 화면 — 정확한 답변](/mwkorea/assets/images/2026-03-22-CopilotStudioWord/image12.png)

---

## 정리

워드 파일을 코파일럿 스튜디오 에이전트의 참조 자료로 사용할 때는 **불릿(bullet) 형식**으로 데이터를 정리하는 것이 가장 효과적입니다.

| 구분 | 권장 여부 | 이유 |
|------|----------|------|
| 표 형식 | ❌ 비권장 | 셀 구조가 평문 텍스트로 추출될 때 구분이 사라짐 |
| 평문 | ❌ 비권장 | 행 간 구분이 없어 데이터 혼동 발생 |
| 평문 + 콤마 | ❌ 비권장 | 행 구분이 여전히 불명확 |
| **불릿** | **✅ 권장** | **각 항목이 명확히 구분되어 LLM이 올바르게 인식** |
| 불릿 + 콤마 | ❌ 비권장 | 오히려 노이즈가 추가되어 정확도 저하 |

엑셀 팁과 마찬가지로, **코파일럿 스튜디오가 워드 파일을 평문 텍스트로 변환해서 LLM에 전달한다**는 점을 기억하면 이해가 쉽습니다. 불릿 형식은 텍스트로 변환된 후에도 각 항목 간 경계가 명확하게 유지되기 때문에 정확한 답변으로 이어집니다.
