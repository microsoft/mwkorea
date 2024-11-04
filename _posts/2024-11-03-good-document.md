---
title: Copilot 활용법. 탐색 기능으로 답변의 정확도를 높이는 법!
date: 2024-11-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - 문서구조화
  - 탐색기능
  - MS_Teams
  - 효율적인작업
  - 프롬프트최적화
excerpt: Copilot을 활용할 때, 문서가 탐색 기능으로 구조화되어 있는지 확인하는 것이 사용자가 원하는 정확한 답변을 얻는 데 필수적입니다.
header:
  overlay_image: /assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  #caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  #actions:
  #  - label: "원문 보기"
  #    url: "https://www.microsoft.com/en-us/microsoft-365/blog/2024/10/28/streamline-collaboration-with-the-new-chat-and-channels-experience-in-microsoft-teams/"
toc: false
toc_sticky: true
classes: wide
author: 최원영
---

# Copilot 활용법. 탐색 기능으로 답변의 정확도를 높이는 법!

문서에서 Copilot 을 통하여 자신이 원하는 답변을 찾아오지 못하면, 프롬프트의 문제라고 생각하여 여러 번 프롬프트를 변경하여 작성하여도 자신이 원하는 답변을 받지 못하는 경우가 종종 있습니다. 이런 경우에는 자신의 문서가 탐색 기능으로 구조화가 되어 있는지를 확인하는 것이 중요합니다. 
{: .notice--info}

## 1. 탐색 기능으로 구조화가 되지 않은 일반 문서에서의 호출

탐색 기능으로 구조화가 되지 않은 일반 문서에서 프롬프트로 “MS Teams 미팅 업데이트를 확인해줘”를 요청하면, 미팅 업데이트 부분만 확인하여 답변을 주는 것이 아니라 문서 전체에서 “”MS Teams”, 미팅” 과 “업데이트” 키워드로 탐색하여 나온 단어와 문장들을 기반으로 작성을 한 가공된 답변을 제공합니다. (하기의 Copilot의 답변 결과를 확인해보면, MS Teams 미팅 업데이트 위주의 내용 보다는 MS Teams의 전체 문서 기준으로 답변이 제공된 것을 확인할 수 있습니다.)

![에이전트](/mwkorea/assets/images/20241103/pic1.png)

(탐색 기능으로 구조화가 되지 않은 일반 문서)

![에이전트](/mwkorea/assets/images/20241103/pic2.png)

(탐색 기능으로 구조화가 되지 않은 일반 문서에서 미팅 업데이트를 호출하였을 때 받은 답변)

## 2. 탐색 기능으로 구조화가 된 문서에서의 호출

탐색 기능을 이용하여 구조화된 문서를 작성하였을 경우에, 동일한 프롬프트인 “MS Teams 미팅 업데이트를 확인해줘”를 요청하면 문서에서 “MS Teams 미팅 업데이트”의 목차를 확인하여 MS Teams 미팅 업데이트 내용만 정확하게 답변을 제공하는 것을 확인할 수 있습니다.

![에이전트](/mwkorea/assets/images/20241103/pic3.png)

(탐색 기능으로 구조화하여 작성된 문서)

![에이전트](/mwkorea/assets/images/20241103/pic4.png)
 
(탐색 기능으로 구조화가 된 문서에서 미팅 업데이트를 호출하였을 때 받은 답변)

이를 통하여 프롬프트도 매우 중요하지만, 호출하는 문서가 탐색 기능으로 구조화되었을 경우에 사용자가 원하는 정확한 답변을 제공할 수 있다는 것을 알게 되었습니다! 😊
