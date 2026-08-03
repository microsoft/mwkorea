---
title: "매일 아침 안 읽는 뉴스레터, 출근길 팟캐스트로 바꾸기 — Copilot Studio Skill 실전"
date: 2026-07-28T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Skills
  - AzureAISpeech
  - SSML
  - TextToSpeech
  - Agent
  - Teams
  - M365Copilot
excerpt: "Copilot Studio Skill과 Azure AI Speech 커넥터를 조합해, 매일 받는 뉴스레터를 두 명의 진행자가 대화하는 6분짜리 팟캐스트 오디오로 바꾸는 에이전트를 만드는 방법입니다. Skill을 쓰는 이유, 멀티보이스 SSML의 함정, Teams 모바일 배포까지 실제 구현 세부사항을 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 매일 아침 안 읽는 뉴스레터, 출근길 팟캐스트로 바꾸기 — Copilot Studio Skill 실전

![Podcast Script Skill](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image1.jpg)

매일 아침 메일함에 뉴스 클리핑이 도착합니다. 헤드라인 15개, 각각 세 문단. 정성껏 큐레이션된 자료입니다. 그리고 매일 아침, 열어서 4초 만에 맨 아래까지 스크롤하고는 "나중에 제대로 읽어야지"라고 스스로에게 말합니다. **물론 나중에 제대로 읽는 일은 없습니다.**

Microsoft Copilot Studio Customer Advisory Team(CAT) 블로그의 이번 글은 바로 이 문제에서 출발합니다. 눈은 바쁘지만 귀는 한가한 40분(출퇴근길, 러닝머신 위, 요리할 때)이 매일 있는데, 그 시간에 쓸 수 있는 형식이 없다는 것이죠.

그래서 저자는 **메일을 받아 팟캐스트 에피소드로 돌려주는 에이전트**를 만들었습니다. 진행자 두 명이 실제로 대화하는, 약 6분 분량의 오디오가 이어폰으로 재생됩니다. 이 글에서는 그 구현 과정을 한국의 Copilot Studio 메이커 관점에서 정리합니다.

> **전제조건**: 이 구현은 **GitHub Copilot harness**가 필요합니다. Skill은 Standard harness가 아니라 여기에 존재하며, 전체 구조가 Skill 위에 얹혀 있습니다. 아직 이 환경을 쓰고 있지 않다면 이 글은 빌드 가이드보다는 미리보기에 가깝습니다.

---

## 왜 "요약"이 아니라 "팟캐스트"인가

먼저 목표를 정확히 해야 합니다. **"메일 요약해 줘"는 답이 아닙니다.**

에이전트에게 뉴스 클리핑을 요약시키면 불릿 리스트가 돌아옵니다. 읽기에는 훌륭한 산출물이지만 **듣기에는 최악**입니다. 불릿을 소리 내어 읽으면 화재 대피 방송처럼 들립니다.

들을 만한 콘텐츠를 만드는 건 **두 사람 사이의 마찰**입니다. 한 명이 숫자를 말하면, 다른 한 명이 "잠깐, 그거 어떤 기준으로 계산한 건데?"라고 되묻습니다. 이 주고받음이 사실을 머릿속에 남깁니다. NotebookLM의 오디오 오버뷰 형식이 빠르게 자리 잡은 이유이기도 합니다.

그래서 이 에이전트는 세 가지 산출물을 만듭니다.

| 산출물 | 용도 |
|--------|------|
| `<slug>_Podcast_Script.txt` | 사람이 읽는 대본. `NOVA:` / `MILES:` 라벨이 붙어 있어 들을 내용을 미리 훑어볼 수 있음 |
| `<slug>_Podcast.ssml` | 기계용 산출물. 멀티보이스 SSML만 담겨 있으며 TTS 서비스에 바로 전달 가능 |
| `<slug>_Podcast.wav` | 실제 나레이션 오디오 (요청 시 생성) |

입력 소스는 거의 무엇이든 가능합니다. 뉴스레터, 프레스 리뷰, 채팅에 붙여넣은 기사 묶음, PDF, 문서. 심지어 소스 없이 **주제만 주고 에피소드를 만들 수도** 있습니다. 저자는 회의 전에 검토해야 했던 12페이지짜리 아키텍처 문서에 이걸 써 봤고, 대충 훑어보는 것보다 훨씬 나은 준비가 되었다고 합니다.

![Copilot Studio 테스트 창에서 실행된 팟캐스트 에이전트 — 세그먼트 요약 표와 생성된 오디오 파일](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image2.png)

다이제스트를 붙여넣으면 세그먼트 분해 결과가 나오고, 오디오 생성에 "예"라고 답하면 `.wav`가 나옵니다. 전체 루프가 **하나의 대화** 안에서 끝납니다.

---

## Part 1. Azure AI Speech 리소스 준비

에이전트가 실제로 음성을 합성할 곳이 필요합니다. Azure AI Speech 리소스이고, 만드는 데 3분 정도 걸립니다.

### Speech 리소스 만들기

Azure 포털에서 **Speech service** 리소스를 생성합니다. 실질적으로 중요한 선택은 두 개뿐입니다.

- **리전(Region)**: 가까운 곳을 고르고 **짧은 코드를 적어 두세요**. 커넥터는 표시 이름이 아니라 `westeurope`, `eastus` 같은 **short code**로 리전을 요구합니다.
- **가격 책정 계층**: 무료 계층에도 월간 뉴럴 TTS 문자 할당량이 포함되어 있어, 커밋 전에 전체 동작을 검증하기에 충분합니다. **6분짜리 에피소드는 대략 5,000자** 정도입니다.

![Azure 포털에서 Speech service 리소스 생성](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image3.png)

### 키와 리전 확보

배포가 끝나면 리소스에서 **Resource Management → Keys and Endpoint**로 이동합니다. 필요한 값은 **KEY 1**과 **Location/Region** 두 개뿐입니다. **엔드포인트 URL은 커넥터가 요구하지 않습니다.**

![Speech 리소스의 Keys and Endpoint 블레이드](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image4.png)

> **보안 주의**: 키는 다른 자격 증명과 똑같이 다뤄야 합니다. **Power Platform 연결(connection)에만** 들어가야 하며, Skill 파일이나 지침, 변수에 넣으면 안 됩니다. 키를 아예 다루고 싶지 않다면, 커넥터는 리소스 ID 기반의 **Microsoft Entra ID 인증**도 지원합니다. 개인 데모를 넘어서는 용도라면 이쪽이 더 나은 답입니다.

### 음성이 해당 리전에 있는지 확인

기본 캐스트는 `en-US-AvaMultilingualNeural`과 `en-US-AndrewMultilingualNeural`을 씁니다. 둘 다 표준 뉴럴 음성이지만 **리전별로 제공 여부가 다르므로**, 선택한 리전의 지원 음성 목록을 미리 확인하는 것이 좋습니다.

---

## Part 2. 커넥터를 에이전트에 연결

Copilot Studio로 넘어갑니다. 에이전트에서 **Tools → Add a tool → Connector**로 이동해 **Azure Text to speech**를 검색합니다.

![Copilot Studio 에이전트에 Azure Text to speech 커넥터를 도구로 추가](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image5.png)

커넥터는 세 개의 작업을 제공하지만, **필요한 건 하나뿐**입니다.

**Convert text to speech with SSML** 액션을 추가하세요. 이게 핵심입니다. 형제 격인 *Convert text to speech*는 평범한 문자열과 단일 음성 이름만 받기 때문에, 진행자 한 명이 단조롭게 읽어 주는 결과가 나옵니다. **SSML 작업이라야 두 명의 화자, 줄 단위 prosody, 통제된 일시정지를 얻을 수 있습니다.**

연결 생성 시 **API Key** 인증을 선택하고 Azure 포털에서 가져온 두 값을 입력합니다.

| 필드 | 값 |
|------|-----|
| Account Key | Speech 리소스의 Key 1 |
| Region | 리전 **짧은 코드**, 예: `westeurope` |

![Account Key와 Region으로 Azure Text to speech 연결 생성](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image6.png)

필드는 두 개지만, **리전에서 실수하는 사람이 많습니다.** 친숙한 표시 이름이 아니라 짧은 코드입니다.

이 커넥터를 습관으로 삼기 전에 알아 둘 두 가지가 있습니다.

- **프리미엄 커넥터**입니다. 일반적인 Power Platform 라이선싱 규칙이 적용됩니다.
- **연결당 60초에 100회 호출로 스로틀링**됩니다. 하루 한 편이면 무관하지만, 문서 묶음에 일괄 적용하려 한다면 매우 중요한 제약입니다.

도구를 추가한 뒤에는 에이전트의 도구 목록에서 **설명(description)이 여전히 말이 되는지** 확인하세요. 에이전트는 설명을 보고 도구를 고르고, Skill은 이 도구를 이름으로 지목합니다. 설명을 크게 고쳐 쓰면 연결이 깨집니다.

![에이전트의 Tools 탭에 등록된 Convert text to speech with SSML 도구](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image7.png)

---

## Part 3. Skill 추가하기

배관 작업이 끝났으니, 이제 흥미로운 부분인 **지침(instructions)** 차례입니다.

### 왜 프롬프트가 아니라 Skill인가

이 모든 걸 에이전트 지침 블록 하나에 몰아 쓸 수도 있습니다. 저자도 시도했지만 **나쁜 생각**이라고 결론 내렸습니다. 이유는 두 가지입니다.

**첫째, 지침이 너무 깁니다.** 소스 자료 파싱, 항목의 편집적 순위 매기기, 대화체 작성, 합성기를 위한 숫자 풀어쓰기, 유효한 멀티보이스 SSML 생성 — 다 합치면 수천 단어의 매우 구체적인 절차가 됩니다. 이게 에이전트 지침에 들어가면 **누군가 그냥 "안녕"이라고 말한 턴에서도 매번 컨텍스트에 실립니다.**

**둘째, 상황 의존적입니다.** 이 에이전트가 하는 일의 대부분은 팟캐스트와 무관합니다. CAT 블로그의 Skill 원칙이 이를 잘 정리합니다.

> **모든 대화에서 참인 지침이면 instructions에, 특정 시나리오에만 적용되면 Skill에 넣는다.**

팟캐스트 생성은 시나리오 특화의 극단적인 사례입니다.

### 내려받아 업로드하기

이 Skill은 처음부터 직접 쓸 필요가 없습니다. **CAT skill library**에 [Podcast Script Generator](https://microsoft.github.io/cat-agent-skills/skills/generating-podcast-script/)로 공개되어 있습니다.

Skill은 세 개 파일을 담은 폴더 구조입니다.

```text
generating-podcast-script/
├── SKILL.md        # front matter + 11단계 절차
├── README.md       # 사람이 읽는 설명
└── metadata.json   # 이름, 설명, 태그, 버전
```

폴더를 zip으로 압축해 에이전트의 **Skills 탭 → Add a Skill → Upload**에서 업로드합니다. 단독 `SKILL.md`도 동작하지만, zip으로 하면 README와 metadata가 함께 따라다닙니다.

![Copilot Studio Skills 탭에서 팟캐스트 Skill zip 업로드](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image8.png)

라우팅 신호는 front matter의 `description`이며, 후속 요청까지 의도적으로 명시합니다.

```yaml
name: generating-podcast-script
description: >
  Use this skill whenever the user asks to write, generate, or create a
  podcast script or podcast episode, from a topic, or from source material
  such as a news digest, newsletter, email review, or set of articles, and
  optionally convert it to audio with Azure Text-to-Speech. Handles the
  initial request and every follow-up refinement (source, topic, length,
  cast, narration) in the same task.
```

**마지막 문장이 핵심입니다.** 이 문장이 없었을 때, Skill은 "이걸 팟캐스트로 만들어 줘"에는 깔끔하게 반응했지만, "아, 좀 더 짧게 해 줘"라고 하는 순간 조용히 컨텍스트에서 빠졌고 에이전트는 아무 규칙도 적용하지 않은 대본을 즉흥적으로 만들어 냈습니다. **"이 Skill이 후속 요청까지 담당한다"고 명시적으로 적어야** 해결됩니다. Skill 지침을 쓰는 분들이 반드시 기억할 만한 노하우입니다.

![에이전트의 Skills 탭에 등록된 팟캐스트 Skill](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image9.png)

이름과 설명만 라우팅 메타데이터로 상시 노출되고, **나머지는 팟캐스트 요청이 들어올 때만 로드**됩니다.

---

## Skill이 실제로 하는 일: 11단계

흥미로운 부분은 "팟캐스트를 생성한다"가 아니라 **순서**입니다. Skill은 에이전트를 11단계로 이끄는데, 이 순서가 결과물이 뭉개지는 것을 막습니다.

**1. 쓰기 전에 파싱한다.** 소스 자료가 주어지면 첫 패스에서 개별 항목을 전부 추출합니다. 헤드라인, 매체명, 날짜, 핵심 사실 주장, 수치나 인용, 그리고 "그래서 뭐(so what)". 같은 사건을 다룬 중복은 병합합니다. 푸터, 면책 조항, 수신거부 문구, 이미지 캡션은 버립니다. **실제 뉴스레터의 약 30%가 보일러플레이트**이기 때문에, 이 단계 하나로 결과물의 사용성이 갈립니다.

**2. 편집적 판단을 내린다.** 남은 항목을 뉴스 가치와 영향도로 순위를 매깁니다. 상위 **4~6개**가 정식 세그먼트를 받고, 나머지는 하나의 **rapid-fire 라운드**로 묶입니다. 에피소드와 목록의 차이가 여기서 갈리며, 원샷 프롬프트로 시도할 때 대부분 생략하는 단계이기도 합니다.

**3. 눈이 아니라 입을 위해 쓴다.** 축약형을 적극 사용하고, 대부분의 문장은 30단어 미만입니다. 긴 설명은 2~3턴으로 쪼개 다른 진행자가 끼어들 수 있게 합니다. 복잡한 개념마다 구체적인 비유를 하나씩 답니다. 한 진행자가 정기적으로 순진한 질문을 던져 다른 진행자가 풀어 설명하도록 합니다.

**가드레일도 있고, 이게 중요합니다.**

- 사실에 대한 반응은 괜찮습니다("그 숫자 진짜 대단한데").
- **인물·기업·정치에 대한 의견을 지어내는 것은 금지**입니다.
- 확인되지 않은 주장은 소리 내어 표시합니다("보고서는 그 부분을 미확인이라고 조심스럽게 표현합니다").
- **헤드라인을 그대로 읽지 않고** 말로 풀어 씁니다.
- 출처는 이름으로 명시합니다.

**4. 길이를 실제 목표로 관리한다.** 분당 **약 150단어** 기준으로 계산합니다. Short 약 450단어, Medium 약 900단어, Long 약 1,800단어이며 **오차 10% 이내**로 맞춥니다. 고정된 출퇴근 시간에 습관을 만들려면 "6분이면 정말 6분"이어야 하기 때문입니다.

### 진행자 캐스트

항상 동일한 성격의 두 진행자가 등장합니다.

- **Nova** — 리드 진행자. 따뜻하고 호기심 많고 빠릅니다. 의제를 이끌고, 청취자가 생각할 만한 질문을 던지고, 전문 용어를 평범한 말로 바꿉니다.
- **Miles** — 분석가. 차분하고 건조하고 정확합니다. 맥락, 숫자, 단서 조항, 2차 함의를 제공합니다. 가끔 Nova에게 반론을 폅니다.

**둘 다 나레이터가 아닙니다.** 마이크가 아니라 서로에게 말합니다. "팟캐스트에 오신 것을 환영합니다"도 없고, 채널 브랜딩도, 음악 큐도 없습니다. **에피소드는 자료에서 가장 인상적인 사실 하나로 차갑게 시작**합니다.

물론 전부 덮어쓸 수 있습니다. 다른 이름, 다른 음성, 단일 진행자, 다른 언어. Nova와 Miles는 결정을 미루기 위한 기본값일 뿐입니다.

### 실행하기

다이제스트를 붙여넣고 이렇게 요청합니다.

```text
Here's this morning's press review. Make it a six-minute episode
and give me the audio.
```

에이전트는 파싱하고, 순위를 매기고, 두 파일을 쓴 뒤, **오디오 생성 여부를 묻기 전에** 대략적인 길이가 표시된 세그먼트 표를 보여 줍니다.

![오디오 생성 전에 세그먼트별 요약 표를 보여 주는 에이전트](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image10.png)

**이 검토 단계를 반드시 유지하세요.** 합성 이후에 고치는 것보다 텍스트 상태에서 구성 순서를 바꾸는 것이 훨씬 저렴합니다.

"예"라고 답하면 에이전트가 SSML을 `ConvertTextToSpeechWithSSML`에 `outputFormat: riff-24khz-16bit-mono-pcm`으로 넘기고, base64 응답을 디코딩해 다운로드 가능한 `.wav` 파일로 씁니다.

---

## Part 4. 휴대폰까지 배달하기

데모를 습관으로 바꾸는 부분이자, 이걸 일회성 프롬프트가 아니라 **에이전트로 만들 가치가 있는 이유**입니다.

에이전트를 게시한 뒤 **Channels**에서 **Microsoft 365 Copilot**과 **Microsoft Teams** 채널을 활성화합니다.

![에이전트에 Teams와 Microsoft 365 Copilot 채널 활성화](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image11.png)

여기서 얻는 결과가 핵심입니다. **Teams 모바일은 반환된 `.wav`를 재생 가능한 첨부 파일로 렌더링**합니다. 그래서 평일 아침이 이렇게 됩니다.

1. 휴대폰의 Teams에서 에이전트에게 프레스 리뷰를 전달하거나 붙여넣는다
2. 휴대폰을 주머니에 넣고 외투를 입는다
3. 현관에 도착할 때쯤 오디오가 채팅에 도착해 있다
4. 재생을 누르고, 이어폰을 끼고, 걷는다

![Teams 모바일에서 재생 가능한 첨부 파일로 표시된 팟캐스트 에피소드](/mwkorea/assets/images/2026-07-28-PodcastScriptSkill/image12.jpg)

> **주의**: **오디오 재생 동작은 채널마다 다릅니다.** Teams 모바일은 첨부 파일을 잘 처리하지만, 다른 표면에서는 플레이어 대신 다운로드가 제공될 수 있습니다. 아침 루틴을 설계하기 전에 **실제로 사용할 채널에서 먼저 테스트**하세요.

---

## 소리의 품질을 결정하는 부분: SSML 디테일

여기까지가 배관과 편집이라면, 이 부분은 기계적이고 **처음 열두 번의 시도가 무너진 지점**입니다.

### 합성기가 망칠 만한 건 전부 풀어 쓴다

TTS 엔진은 기호에 대해 **자신 있게 틀립니다.** 그래서 숫자나 약어는 발화 텍스트에 그대로 남기지 않습니다.

- `2026`이 아니라 "twenty twenty-six"
- `$3.2B`가 아니라 "three point two billion dollars"
- `~15%`가 아니라 "about fifteen percent"
- 약어는 첫 등장에서 풀어 쓰고 이후 축약
- 철자 단위로 읽는 약어는 `<say-as interpret-as="characters">API</say-as>`
- 특이한 고유명사는 `<sub alias="phonetic spelling">Name</sub>`
- 영어 문장 안의 프랑스어 구절은 `<lang xml:lang="fr-FR">`로 감싸기

**스마트 따옴표, em dash, 별표, 밑줄, URL은 전부 금지**입니다. 원치 않는 방식으로 읽히거나, 조용히 XML을 깨뜨립니다.

### 턴당 voice 요소는 하나 — 가장 큰 함정

저자가 가장 많은 시간을 쏟은 규칙입니다.

> 멀티보이스 SSML 문서에서 **두 `<voice>` 요소 사이에 직접 놓인 `<break>` 요소는 유효하지 않으며 합성이 실패합니다.** "이상하게 들린다"가 아니라 **실패**합니다.

턴 **사이**에 원하는 일시정지는 **앞 턴 텍스트의 끝**, 그 턴의 `<prosody>` 안에 넣어야 합니다. 두 `<voice>` 요소는 사이에 아무것도 없이 맞붙어야 합니다.

```xml
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="http://www.w3.org/2001/mstts"
       xml:lang="en-US">
  <voice name="en-US-AvaMultilingualNeural">
    <mstts:express-as style="excited">
      <prosody rate="+8%" pitch="+3%">Okay, so the number that stopped me cold
      this morning was forty percent. <break time="300ms"/> Forty percent, in one
      quarter. <break time="250ms"/></prosody>
    </mstts:express-as>
  </voice>
  <voice name="en-US-AndrewMultilingualNeural">
    <mstts:express-as style="chat">
      <prosody rate="-2%" pitch="-4%">Right, and the part everyone's skipping is
      that it's off a very small base. <break time="250ms"/> Context matters
      here. <break time="700ms"/></prosody>
    </mstts:express-as>
  </voice>
</speak>
```

끝에 붙은 break를 눈여겨보세요. **250ms는 다음 턴 전의 간격**, **700ms는 다음 세그먼트 전의 더 긴 간격**입니다. 두 `<voice>` 요소 사이에는 아무것도 없습니다.

### 딜리버리를 변주하지 않으면 밋밋해진다

문서 전체에 단일 `rate`와 `pitch`를 적용하면 **공항 안내방송**처럼 들립니다. Skill은 진행자별 기준선을 설정합니다.

| 진행자 | 기준 prosody |
|--------|--------------|
| Nova | `rate="+6%" pitch="+2%"` |
| Miles | `rate="-2%" pitch="-4%"` |

그런 다음 문장의 감정에 맞춰 줄 단위로 미세 조정합니다.

`<mstts:express-as>`가 나머지를 담당합니다. 잡담에는 `chat`, 설명에는 `friendly`, 기사의 사실 핵심에는 `narration-professional`, 콜드 오픈에는 아껴서 `excited`를 씁니다. **스타일은 구조적 요소가 아니라 의도적으로 선택적**입니다. 지원되지 않는 스타일은 서비스가 조용히 무시하기 때문에, `excited`를 지원하지 않는 음성으로 바꿔도 색채만 조금 잃을 뿐 **에피소드 전체가 날아가지는 않습니다.**

`<emphasis level="moderate">`는 세그먼트당 한두 개 핵심 용어에만 씁니다. 그보다 많으면 강조의 의미가 사라집니다.

> **디버깅 팁**: Copilot Studio에서 뭔가를 디버깅하기 전에, 생성된 SSML을 Speech Studio의 **Audio Content Creation**에 붙여넣어 보세요. 어느 줄이 잘못됐는지 정확히 알려 줍니다. 커넥터는 알려 주지 않습니다.

---

## 솔직한 트레이드오프

**즉시 나오지 않습니다.** 6분짜리 에피소드를 파싱·순위·작성·합성하는 것은 실제 작업량이 있습니다. 채팅 응답이 아니라 **"실행해 놓고 신발 신으러 가는"** 성격의 작업입니다.

**긴 에피소드는 분할이 필요합니다.** SSML은 **40,000자 미만**으로 유지됩니다. 단일 합성 호출이 감당할 수 있는 길이를 넘으면, 에이전트가 세그먼트 경계에서 나누고 각 부분을 합성한 뒤 디코딩된 오디오를 순서대로 이어 붙입니다. 동작하지만 움직이는 부품이 늘어납니다.

**편집적 판단은 여전히 판단입니다.** 순위 매기기는 소스 자료에서 무엇이 중요한지에 대한 에이전트의 의견입니다. 대체로 합리적이지만 가끔 틀립니다. 그래서 Skill이 나레이션 전에 세그먼트 표를 보여 주는 것입니다. 동의하지 않으면 순서를 바꾸면 됩니다.

**쓰레기를 넣으면 자신만만한 쓰레기가 나옵니다.** 소스 자료가 빈약하면 별것 없는 내용에 두 사람이 열정적인 6분이 나옵니다. Skill은 시간을 채우려고 사실을 지어내지는 않지만, **당신의 뉴스레터가 지루했다고 알려 주지도 않습니다.**

---

## 다음 단계와 국내 적용 아이디어

저자가 꼽은 확장 방향은 **사람을 루프에서 완전히 빼는 것**입니다. 메일함에 자율 트리거를 걸어 프레스 리뷰가 도착하면 Skill이 실행되고, `.wav`가 휴대폰이 이미 동기화하는 OneDrive 폴더에 떨어지는 구조입니다.

또 다른 방향은 **뉴스가 아닌 소스 자료**입니다. 자주 챙겨 보지 않는 제품의 릴리스 노트, 가끔 기여하는 리포지토리의 체인지로그, 아무도 읽지 않은 그 아키텍처 문서. **정보는 정말 유용한데 형식이 정말 매력 없는** 모든 것 — 업무 메일함에 쌓이는 상당수가 여기에 해당합니다.

국내 조직이라면 이런 응용을 생각해 볼 수 있습니다.

- **경영진 일일 브리핑**: 사내 대시보드 리포트를 출근길 5분 오디오로
- **주간 릴리스 노트**: 개발팀 변경사항을 비개발 부서가 들을 수 있는 형태로
- **교육 콘텐츠**: 긴 정책 문서나 규정 개정 사항을 대화형 오디오로

다만 기본 캐스트가 영어 음성이라는 점을 감안해, **한국어 뉴럴 음성으로 캐스트를 교체**하고 숫자·단위 풀어쓰기 규칙을 한국어 발화 기준으로 다시 정의하는 작업이 필요합니다. Skill 지침은 덮어쓸 수 있게 설계되어 있으므로 이 부분이 국내 적용의 첫 번째 커스터마이징 지점이 됩니다.

---

## 마무리

이 Skill이 흥미로운 이유는 팟캐스트를 만들어서가 아닙니다. **하나의 Skill 안에서 편집 작업, 창작 글쓰기, 엄격한 XML 생성을 동시에 요구**하고, 각각의 제약이 서로 조금씩 충돌한다는 점 때문입니다. 저자는 "잘 동작하는 Skill들보다 이 Skill이 어디서 삐걱대는지를 지켜본 것이 Skill 지침 작성에 대해 더 많이 가르쳐 줬다"고 말합니다.

Copilot Studio에서 Skill을 설계하고 있다면, 이 사례에서 얻을 수 있는 실질적인 교훈은 세 가지입니다.

1. **상시 지침과 시나리오 지침을 분리하라** — 컨텍스트 비용은 매 턴 발생한다
2. **Skill 설명에 후속 요청 처리를 명시하라** — 안 하면 두 번째 턴에서 조용히 빠진다
3. **합성·실행 전에 사람이 검토할 지점을 만들어라** — 되돌리는 비용이 훨씬 싸다

그리고 마지막으로 저자의 질문을 그대로 옮깁니다. **"매번 읽어야지 하면서 안 읽는 그 메일, 무엇인가요?"** 그게 이걸 가장 먼저 겨눌 대상입니다.

---

> **출처**: *Turn Your Daily Digest Into a Podcast You'll Actually Listen To* — MCSCAT Blog (The Custom Engine, Microsoft Copilot Studio Customer Advisory Team)
> - 원문: [https://microsoft.github.io/mcscatblog/posts/podcast-script-skill/](https://microsoft.github.io/mcscatblog/posts/podcast-script-skill/)
> - Skill 다운로드: [Podcast Script Generator — CAT Agent Skills](https://microsoft.github.io/cat-agent-skills/skills/generating-podcast-script/)
>
> 자세한 내용은 원문 참조.
