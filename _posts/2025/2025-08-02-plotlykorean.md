---
title: "코파일럿 그래프에 한글이 깨져요. plotly로 해결하세요."
date: 2025-08-02T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - Agent
excerpt: "코파일럿에서 그래프를 그릴 때 한글이 깨지는 문제는 오랜 숙제였습니다. 문서 외 파일 업로드가 불가능해 기존 해결책이 적용되지 않았지만, plotly를 사용하니 한글이 완벽하게 표시되었습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  #actions:
  #  - label: "원문보기"
  #    url: "https://www.microsoft.com/en-us/power-platform/blog/2025/07/21/agent-costs-controls/?msockid=3535fcba82d669720766ed1c8358686d"
toc: false
toc_sticky: true
classes: wide
author: 이영서
---

# Plotly로 해결한 한글 깨짐 문제

코파일럿에서 matplotlib나 seaborn을 이용해 그래프를 그릴 때, 한글이 "ㅁㅁㅁ"처럼 깨져 보이는 현상이 자주 발생했습니다. 이는 기본 폰트 설정이 한글을 지원하지 않기 때문인데, 해결을 위해서는 일반적으로는 한글 폰트를 직접 설치하고 경로를 지정해주는 복잡한 작업이 필요했습니다. 하지만 코파일럿은 문서 타입 외의 파일 업로드를 허용하지 않기 때문에, 폰트 파일을 업로드해서 적용하는 방식은 사용할 수 없었습니다.

## 리서치 결과: 챗GPT도 동일한 문제

문제 해결을 위해 구글링을 해보니, 챗GPT에서도 동일한 문제가 발생하고 있다는 것을 알게 되었습니다. 많은 사용자들이 matplotlib에서 한글을 표시하기 위해 NanumGothic이나 Malgun Gothic 폰트를 설치하고 설정하는 방법을 공유하고 있었지만, 코파일럿 환경에서는 적용이 어려웠습니다.

![image](/mwkorea/assets/images/20250802/image01.png) 

---

**해결의 실마리: **

이전부터 알고 있던 지식을 활용해서 문제를 깔끔하게 해결할 수 있었습니다. 그 마법의 주문은 바로:

```
plotly를 이용해
```

![image](/mwkorea/assets/images/20250802/image02.png) 

---

plotly는 웹 기반 인터랙티브 그래프를 생성하는 라이브러리로, 브라우저에서 렌더링되기 때문에 시스템 폰트에 의존하지 않고 한글을 자연스럽게 표시할 수 있습니다. 실제로 plotly를 사용해 그래프를 그려보니, 아무런 추가 설정 없이도 한글이 깨지지 않고 잘 나타났습니다.


## 결론

그래프에서 한글이 깨지는 문제는 오랫동안 많은 사용자들을 괴롭혀왔지만, plotly를 사용하면 매우 간단하게 해결할 수 있습니다. 앞으로 코파일럿에서 시각화를 할 때는 plotly를 적극 활용해보세요. 
