---
title: "15분 걸리던 Word 계약서 Redlining을 15초로: Copilot Studio Skill 최적화"
date: 2026-07-15T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - AgentSkills
  - DocumentRedlining
  - OOXML
  - Python
  - TrackChanges
  - AgenticLoop
excerpt: "Microsoft Copilot Studio CAT가 Word 템플릿과 DOCX·PDF 제출본을 비교해 실제 Track Changes 문서를 만드는 redlining-content Skill을 공개했습니다. 에이전틱 반복으로 코드를 발견한 뒤 재사용 스크립트로 고정해 100페이지 문서 처리 시간을 약 15분에서 15초로 줄였습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 15분 걸리던 Word 계약서 Redlining을 15초로: Copilot Studio Skill 최적화

거래처가 수정한 계약서를 보내왔을 때 무엇이 달라졌는지 확인하고, Microsoft Word의 Track Changes로 모든 변경을 Accept 또는 Reject할 수 있는 문서를 만드는 일은 생각보다 어렵습니다. 원본 서식과 표를 그대로 유지하면서 실제 OOXML 변경 태그까지 삽입해야 하기 때문입니다.

Microsoft Copilot Studio Customer Advisory Team(CAT)은 새로운 Copilot Studio 오케스트레이터에서 동작하는 **redlining-content Skill**을 만들고, 첫 버전의 약 15분 처리 시간을 약 15초로 줄인 과정을 공개했습니다.

![Copilot Studio 문서 Redlining Skill](/mwkorea/assets/images/2026-07-15-CopilotStudioDocumentRedlining/image1.png)

---

## Word Track Changes의 실제 구조

`.docx` 파일은 XML 파일들을 담은 ZIP 패키지입니다. Word에서 변경 내용 추적을 켜면 텍스트를 단순히 교체하지 않고 다음 OOXML 요소로 감쌉니다.

- `<w:ins>`: 추가된 텍스트
- `<w:del>`: 삭제된 텍스트

각 요소에는 변경 작성자와 시간도 기록됩니다.

![OOXML의 w:ins와 w:del 변경 태그](/mwkorea/assets/images/2026-07-15-CopilotStudioDocumentRedlining/image2.png)

Redlining 결과는 이런 실제 변경 태그를 가진 DOCX여야 합니다. 동시에 제목 정렬, 글꼴 크기, 표, 여백 같은 원본 서식도 보존해야 합니다. 형식이 무너지면 변경 내용이 맞더라도 검토 가능한 계약서가 되지 못합니다.

## 에이전틱 반복이 코드를 발견한 4단계

![Redlining Skill을 만든 네 단계](/mwkorea/assets/images/2026-07-15-CopilotStudioDocumentRedlining/image3.png)

### 1. 코드 없이 먼저 실행

에이전트가 두 파일을 직접 비교해 Redline을 만들게 했습니다. 첫 시도는 DOCX와 PDF를 서로 변환했고, 그 과정에서 레이아웃·간격·서식이 깨졌습니다. 실제 수정이 아닌 문단 나눔과 공백까지 변경으로 표시돼 사용할 수 없는 결과가 됐습니다.

이 실패에서 얻은 원칙은 명확했습니다.

> 이미 올바른 Word 템플릿을 다른 형식으로 변환하지 않는다.

### 2. 실패를 읽고 반복하게 하기

에이전트가 직접 Python 스크립트를 작성하고 실행하도록 했습니다. `lxml` 오류, 잘못된 XML 중첩, 충돌하는 Revision ID 등을 Traceback에서 읽고 코드를 반복 수정했습니다.

약 15분의 실패·재작성 루프 끝에 Word에서 정상적으로 열리고 실제 Track Changes가 들어간 DOCX가 생성됐습니다.

### 3. 하드코딩 제거

동작하는 첫 스크립트에는 파일 경로, 문단 인덱스, 문자열, 고정 ID가 들어 있었습니다. 이를 모두 일반화했습니다.

- 특정 문단 인덱스 → 단어가 원래 속한 문단 탐색
- 고정 교체 문자열 → 템플릿과 제출본의 Diff
- 특정 파일명 → 실행 시 전달되는 입력

### 4. 재사용 스크립트로 고정

일반화한 로직을 Skill의 `scripts/redline.py`에 넣었습니다. 이후 에이전트는 매 요청마다 올바른 코드를 다시 발견하지 않고 이미 검증된 스크립트를 실행합니다.

![에이전틱 발견을 재사용 스크립트로 고정](/mwkorea/assets/images/2026-07-15-CopilotStudioDocumentRedlining/image4.png)

> 같은 결과를 약 60배 빠르게 만들었습니다. 15분의 추론 반복이 15초의 함수 호출로 바뀌었습니다.

## 런타임 제약: pip install 불가

새 Copilot Studio 런타임에서는 임의의 Python 패키지를 설치할 수 없습니다. 컨테이너에 포함된 라이브러리만 사용할 수 있습니다.

| 접근법 | 결과 |
|---|---|
| 텍스트 추출 후 DOCX 재구성 | 서식·표·정렬 손실 |
| `pdf2docx` | 런타임에 없음 |
| `pymupdf` | 런타임에 없음 |
| `python-docx`로 출력 재구성 | 추상화가 높아 원본 스타일 보존 한계 |
| `pypdfium2` 기반 재구성 | 이미지 중심 결과 |
| 원본 템플릿 + 단어 Diff | 최종 채택 |

해결책은 PDF를 Word로 변환하는 것이 아니었습니다. 사용 가능한 `pdfplumber`로 PDF의 단어를 읽고, 원본 DOCX·DOTX 템플릿에 변경 태그를 직접 삽입했습니다.

## 최종 Skill 구조

![redlining-content Skill 폴더 구조](/mwkorea/assets/images/2026-07-15-CopilotStudioDocumentRedlining/image5.png)

```text
redlining-content/
├── assets/
│   └── template.dotx
├── references/
│   ├── docx-submissions.md
│   └── pdf-submissions.md
├── scripts/
│   └── redline.py
└── SKILL.md
```

Skill은 [CAT Agent Skills Gallery의 redlining-content](https://microsoft.github.io/cat-agent-skills/skills/redlining-content/)에서 받을 수 있습니다.

## 실행 흐름

1. Skill에 포함된 DOCX 또는 DOTX 템플릿을 기준선으로 사용합니다.
2. 사용자가 DOCX 또는 PDF 제출본을 업로드합니다.
3. Word 파일은 문단 텍스트를, PDF는 `pdfplumber`로 단어를 읽습니다.
4. 제출 유형에 맞는 Reference 문서를 읽습니다.
5. `difflib.SequenceMatcher`로 두 단어 목록을 한 번 비교합니다.
6. 변경되지 않은 문단은 바이트 단위로 유지합니다.
7. 변경된 문단에만 `<w:ins>`와 `<w:del>`을 삽입합니다.
8. 변경 작성자는 `Copilot Studio AI`로 기록됩니다.
9. DOCX 표는 셀 단위로 비교하고 너비·테두리·음영을 유지합니다.
10. Track Changes가 켜진 일반 DOCX를 출력합니다.

![100페이지 이상 문서의 Redlining 결과](/mwkorea/assets/images/2026-07-15-CopilotStudioDocumentRedlining/image6.png)

## PDF와 DOCX의 품질 차이

DOCX 제출본은 단어와 표 구조가 실제로 존재하므로 높은 정확도를 기대할 수 있습니다. PDF는 레이아웃에서 텍스트를 추출한 결과를 사용하므로 문자 단위로 완벽한 비교를 보장하기 어렵습니다.

> PDF Redline은 사람이 검토해야 하는 최선의 초안으로 취급하고, 높은 정확도가 필요하면 DOCX 제출 경로를 사용해야 합니다.

## Copilot Studio와 Cowork 중 어디에 적합한가

단순히 두 문서를 한 번 비교하는 일이라면 Cowork가 더 간단할 수 있습니다. 반면 다음처럼 반복 가능한 업무 프로세스가 있다면 Copilot Studio Skill이 적합합니다.

- 항상 같은 회사 표준 템플릿을 사용합니다.
- 이메일로 들어온 제출본을 자동 수집합니다.
- 조직의 비교·승인 규칙을 적용합니다.
- 매번 같은 방식으로 Track Changes 문서를 반환합니다.

개발 과정에서는 Cowork처럼 에이전틱 반복으로 해법을 한 번 발견하고, 운영에서는 그 결과를 결정론적 Skill로 고정한 것이 이번 설계의 핵심입니다.

## 도입 체크포인트

- 계약·법률 문서 결과는 반드시 사람이 검토합니다.
- Python 런타임에서 실제 제공되는 라이브러리를 확인합니다.
- DOCX와 PDF 입력의 기대 품질을 구분해 사용자에게 안내합니다.
- 원본 템플릿의 스타일·표·머리글·바닥글 보존을 대표 문서로 테스트합니다.
- 장문 문서, 표가 많은 문서, 예상하지 못한 입력으로 평가합니다.
- 생성된 OOXML과 출력 파일을 신뢰할 수 없는 코드·문서처럼 검사합니다.

## 마무리

이 사례의 가장 중요한 교훈은 에이전트가 매번 어려운 문제를 다시 풀게 하지 않는 것입니다. 에이전틱 반복으로 올바른 코드를 발견하고, 하드코딩을 제거하고, 살아남은 해법을 Skill의 재사용 스크립트로 고정하면 속도·비용·예측 가능성을 모두 개선할 수 있습니다.

---

> **원문**: [Redlining Documents with the New Copilot Studio Experience (The Custom Engine, Microsoft Copilot Studio CAT, 2026-07-15)](https://microsoft.github.io/mcscatblog/posts/redlining-documents-new-copilot-studio-experience/)
>
> 자세한 내용은 원문을 참조하세요.
