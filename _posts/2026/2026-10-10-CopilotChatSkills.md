---
title: "Copilot Chat에 Skills 도입, 작업별 지침을 직접 만들고 Cowork와 공유한다"
date: 2026-10-10T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot Chat
  - Skills
  - Plugins
  - Cowork
  - Agent Store
excerpt: "Microsoft 365 Copilot Chat에 작업별 지침과 파일·스크립트를 묶은 Skills가 도입됩니다. 사용자가 만들고 공유하며, 관리자는 Microsoft 365 admin center에서 배포·차단할 수 있고 Cowork에서도 함께 쓸 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Chat에 Skills 도입, 작업별 지침을 직접 만들고 Cowork와 공유한다

Microsoft 365 Copilot Chat에 **Skills**가 도입됩니다. Skill은 특정 작업을 위한 지침과, 필요하면 보조 파일이나 스크립트를 묶은 단위입니다. Copilot은 요청이 해당 skill과 관련 있다고 판단하면 지침을 자동으로 적용해 업무 정확도를 높입니다. 사용자는 이 자동 호출을 끌 수도 있습니다.

최종 사용자는 skill을 만들고 편집·업로드·공유할 수 있고, 관리자는 admin center에서 skill이 담긴 plugin을 배포하거나 차단할 수 있습니다. Chat과 Copilot Cowork가 같은 skill과 plugin을 공유한다는 점이 핵심입니다.

---

## 새로운 점

### 최종 사용자용 Skills
- skill 생성·편집, 기존 skill 업로드, 다른 사람과 공유
- 관리자가 배포한 skill 및 ISV(독립 소프트웨어 공급업체)가 공개한 skill 사용
- 자동 호출 허용 여부 선택, 또는 Context IQ의 새 **"Agents and Skills"** 섹션에서 직접 선택 (Context IQ 경험은 MC1479519 참조)

### 관리자 배포
- Microsoft 365 admin center에서 skill과 plugin(skill·커넥터 포함)을 배포·설치·차단
- 배포된 plugin은 Copilot Chat과 Copilot Cowork 양쪽에서 사용 가능
- **Tools** 보기에서 사용자가 만든 skill 전체를 검토

### Agent Store에 plugin 포함
- Chat의 Agent Store에서 에이전트, skill, skill 포함 plugin을 탐색
- 커넥터만 있는 plugin은 이번 릴리스에 포함되지 않으며 후속 추가 예정. 그때까지 커넥터는 Chat의 Data Sources 메뉴로 사용

### Chat과 Cowork 간 사용
- Chat에서 만든 skill은 Cowork에서도 사용 가능
- Cowork에서 만든 skill은 **공유한 경우에만** Chat에서 사용 가능

### 개발자 도구
WIQ Dev Tools 또는 Agents Toolkit으로 만든 skill·plugin도 Copilot Chat에서 사용할 수 있습니다.

## Information Barriers 테넌트
Information Barriers를 사용하는 테넌트에는 **11월**에 롤아웃됩니다. 이 테넌트에서는 개인용 skill 생성, 관리자 배포 skill과 ISV 공개 skill 사용이 가능하지만, **사용자가 만든 skill의 공유는 아직 지원되지 않으며** 향후 정책에 맞춰 지원될 예정입니다.

## 일정
- 일반 공급(GA, Worldwide): **2026년 10월** 롤아웃 시작, **11월 중순** 완료 예상

## 도입 체크포인트
- skill이 담긴 plugin 배포: Microsoft 365 admin center > Agents > Tools > Upload에서 plugin 앱 패키지를 업로드한 뒤 대상 사용자·그룹에 게시 또는 설치
- 사용자가 만든 skill은 Tools의 skill·plugin 인벤토리에서 정기적으로 검토
- 이 기능은 상위 서비스의 데이터 거주·처리 약속을 따르고 RBAC를 지원하며, 사용자·그룹 단위로 접근을 제어할 수 있습니다.
- 사내에서 자주 반복되는 업무 지침(보고서 양식, 응대 규칙 등)을 skill 후보로 정리하면 도입 효과를 빨리 확인할 수 있습니다.

> **출처**: 원문 ID **MC1493223** · [mc.merill.net 원문](https://mc.merill.net/message/MC1493223) · [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
