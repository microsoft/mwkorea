---
title: "잘 만든 영업 에이전트 설정을 다른 팀으로: 복제·공유의 범위와 한계"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365Sales
  - SalesDevelopmentAgent
  - Governance
excerpt: "Sales Development agent의 플레이북·지침·가드레일·설정을 파일로 내보내 다른 에이전트에 적용하는 기능이 안내됐습니다. 일회성 스냅샷이며 지식 소스는 포함되지 않는다는 점이 중요합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 잘 만든 영업 에이전트 설정을 다른 팀으로: 복제·공유의 범위와 한계

조직의 영업 방침과 가드레일을 에이전트마다 다시 입력하면 시간이 들고 설정 편차도 생깁니다. Sales Development agent는 한 번 구성한 내용을 내보내 여러 팀에 배포하는 기능을 안내했습니다.

다만 **설정 복제와 지속적인 중앙 동기화는 다릅니다.** 원문이 명시한 전달 범위를 이해해야 운영 중 혼선을 줄일 수 있습니다.

---

## 내보내기와 가져오기

Teams에서 원본 에이전트에 `Export your configuration`처럼 요청해 설정을 파일로 묶습니다. 새 에이전트에 그 파일을 첨부한 뒤 해당 설정을 적용하도록 요청합니다.

공유 대상은 플레이북, 지침, 가드레일과 설정입니다. 영업 조직의 표준 구성을 다른 사업부에 전달하는 출발점으로 사용할 수 있습니다.

## 복제되지 않는 것

복사본은 **일회성 스냅샷**이며 원본의 이후 변경이 대상 에이전트에 자동 적용되지 않습니다. 업로드한 문서, FAQ, URL 같은 **지식 소스도 내보내기 파일에 포함되지 않으므로** 가져온 뒤 대상에 직접 추가해야 합니다.

표준 설정을 업데이트했을 때 배포 대상을 추적하고, 팀별 지식 소스와 접근 권한을 확인하는 운영 절차가 필요합니다.

## 일정과 시작하기

로드맵은 프리뷰 **2026년 8월**, GA 목표 **2027년 4월**로 표기합니다. 현재 단계와 환경별 지원 여부는 [설정 복사 문서](https://learn.microsoft.com/en-us/dynamics365/sales/sales-dev-agent/copy-configuration)를 확인하세요. 관리자 등이 최종 사용자용으로 활성화하는 기능입니다.

> 출처: 원문 ID **RM576637**, [MC 아카이브](https://mc.merill.net/message/RM576637), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576637). 실제 출시 일정·기능은 변경될 수 있습니다.
