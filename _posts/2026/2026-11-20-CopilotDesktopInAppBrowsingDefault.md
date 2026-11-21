---
title: "Copilot 데스크톱 앱의 링크, 이제 앱 안에서 기본으로 열립니다"
date: 2026-11-20T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftCopilot
  - Desktop
  - Windows
  - Mac
  - InAppBrowsing
  - Policy
excerpt: "Windows와 Mac용 Microsoft Copilot 데스크톱 앱의 인앱 브라우징이 2027년 1월부터 기본 활성화될 예정입니다. 대화와 웹 콘텐츠를 나란히 보는 경험과 BrowsingEnabled 정책 등 관리자가 확인할 사항을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 데스크톱 앱의 링크, 이제 앱 안에서 기본으로 열립니다

Copilot이 알려 준 웹사이트를 확인할 때 앱과 브라우저를 오가면 대화 맥락이 끊기기 쉽습니다. 인앱 브라우징은 Copilot 대화 옆에서 웹 콘텐츠를 바로 확인하도록 돕는 기능입니다.

Message Center 공지 MC1560922는 **Windows와 Mac용 Microsoft Copilot 데스크톱 앱에서 인앱 브라우징을 기본 활성화**한다고 안내합니다. 새 기능을 처음 도입한다기보다, 앞서 선택적으로 제공하던 경험의 기본값이 바뀌는 업데이트입니다.

---

## 사용자에게 달라지는 점

Copilot 채팅에서 공유된 웹사이트가 기본적으로 데스크톱 앱 내부에서 열립니다. 사용자는 대화와 웹페이지를 나란히 볼 수 있어, 응답의 근거를 확인하거나 내용을 비교할 때 앱 전환을 줄일 수 있습니다.

![Copilot 대화 옆에서 웹페이지를 확인하는 인앱 브라우징 화면](/mwkorea/assets/images/2026-11-20-CopilotDesktopInAppBrowsingDefault/image1.png)

이 공지의 대상은 **Windows와 Mac의 Microsoft Copilot 데스크톱 앱**입니다. 모든 브라우저나 다른 Microsoft 제품에서 링크 처리 방식이 일괄 변경된다는 의미는 아닙니다.

## 일정: 2027년 1월 순차 적용

원문 기준 전 세계 GA 배포는 **2027년 1월 초 시작, 1월 말 완료 예상**입니다. 공지의 관리자 대응 기한인 **Act by는 2027년 1월 3일**로 표시되어 있습니다.

기능을 사용할 조직은 별도로 활성화할 필요가 없습니다. 아무 설정도 변경하지 않으면 인앱 브라우징이 기본 활성화 상태로 유지됩니다.

## 사용을 막거나 관리하려면

원문은 인앱 브라우징을 비활성화하려는 조직에 다음 설정을 안내합니다.

```text
정책: BrowsingEnabled
값: Off
```

조직의 디바이스 관리 시스템을 통해 정책을 적용하는 방식입니다. 위 내용은 공지에 나온 정책 이름과 값이며, 실행할 PowerShell 명령어가 아닙니다.

이 밖에도 새로운 인앱 브라우징 정책으로 다음 영역을 관리할 수 있다고 설명합니다.

- 보안, 개인정보 보호 및 접근
- 인증과 네트워크 동작
- 다운로드와 권한

다만 원문은 이들 정책의 세부 이름이나 설정 경로를 모두 제공하지 않으며, 문서를 추후 업데이트하겠다고 안내합니다. 추정한 레지스트리 경로나 배포 명령어를 사용하기보다는 업데이트된 관리 문서를 확인해야 합니다.

## 조직에서 준비할 사항

다음은 운영상 권고입니다. 외부 사이트 로그인, 사내 네트워크 접근, 파일 다운로드가 인앱 환경에서 조직의 정책과 맞게 동작하는지 점검하고, 헬프데스크에는 기본 링크 동작이 바뀐다는 점을 알려 두세요.

기존 외부 브라우저 사용을 유지해야 하는 조직은 배포 시점 전에 비활성화 정책과 적용 범위를 확인하는 편이 좋습니다. 공지에 별도 컴플라이언스 고려사항이 식별되지 않았더라도, 조직별 보안 검토를 대신하는 것은 아닙니다.

## 마무리

사용자에게는 앱 전환을 줄이는 변화지만, 관리자에게는 **기본으로 켜지는 기능의 경계를 점검해야 하는 변화**입니다. 편의성과 함께 인증·다운로드·네트워크 통제를 확인하는 것이 핵심입니다.

> **출처:** Message Center **MC1560922**, [Microsoft Copilot: In-app browsing will be enabled by default in the desktop app](https://mc.merill.net/message/MC1560922). 선행 공지: [MC1474455](https://mc.merill.net/message/MC1474455). [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap)에서 관련 업데이트를 확인할 수 있습니다. 이 공지에는 개별 Roadmap ID가 명시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
