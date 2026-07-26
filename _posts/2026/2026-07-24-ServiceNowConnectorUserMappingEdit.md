---
title: "ServiceNow 커넥터, 이제 연결을 지우지 않고 사용자 매핑·쿼리 필터를 수정한다"
date: 2026-07-24T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotConnectors
  - ServiceNow
  - GraphConnectors
  - Admin
  - Roadmap
excerpt: "ServiceNow 커넥터를 운영하다 사용자 매핑이나 쿼리 필터를 바꾸려면 연결을 다시 만들어야 했던 번거로움이 사라집니다. 이제 기존 연결에서 바로 사용자 매핑과 쿼리 필터를 편집할 수 있습니다. 관리자 관점의 의미를 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# ServiceNow 커넥터, 이제 연결을 지우지 않고 사용자 매핑·쿼리 필터를 수정한다

Microsoft 365 Copilot과 Microsoft Search에 ServiceNow 데이터를 색인하는 **ServiceNow용 Copilot 커넥터**는, 사내 IT 서비스 관리(ITSM) 데이터를 검색과 Copilot 답변의 근거로 끌어오는 대표적인 통로입니다. 인시던트, 지식 문서, 요청 항목 등을 색인해 직원들이 한곳에서 찾고 활용하게 해 줍니다.

그런데 그동안 운영 관리자들의 작은 불편이 있었습니다. **사용자 매핑(user mapping)** 이나 **쿼리 필터(query filter)** 를 바꾸려면 기존 연결을 편집할 수 없어, 사실상 연결을 다시 구성해야 하는 경우가 있었죠. 이번 로드맵 항목(RM503590)은 바로 이 지점을 해소합니다.

이 기능은 이미 **출시(Launched)** 되었으며, **2026년 2월 미리 보기, 2026년 3월 GA** 로 전 세계(Worldwide) 대상 제공되는 것으로 표기되어 있습니다.

---

## 무엇이 달라지나요?

기존 ServiceNow 연결을 유지한 채로, 아래 두 가지를 **편집**할 수 있게 됩니다.

- **사용자 매핑(User mapping)**: ServiceNow의 사용자 ID를 Microsoft Entra(Azure AD) 사용자에 대응시키는 규칙. 이 매핑이 정확해야 항목 수준 권한(ACL)이 제대로 적용되어, 직원이 **볼 수 있는 데이터만** 검색·Copilot 결과에 노출됩니다.
- **쿼리 필터(Query filter)**: ServiceNow에서 어떤 레코드를 색인할지 걸러 내는 조건. 예를 들어 특정 상태·카테고리·테이블만 가져오도록 범위를 좁히는 설정입니다.

이제 이 두 설정을 **연결을 삭제·재생성하지 않고 그 자리에서 수정**할 수 있습니다.

## 왜 중요한가요?

- **재색인 리스크 감소**: 연결을 다시 만들면 전체 재색인이 발생하고, 그동안 검색 품질이 흔들리거나 일시적으로 결과가 비는 상황이 생길 수 있습니다. 인플레이스 편집은 이런 운영 리스크를 줄여 줍니다.
- **거버넌스 대응 속도**: 조직 개편, 권한 정책 변경, ServiceNow 구성 변경이 생겼을 때 사용자 매핑을 **즉시 조정**해 정보 노출 범위를 빠르게 맞출 수 있습니다.
- **색인 범위 최적화**: 불필요한 레코드까지 색인되던 상황을 쿼리 필터 편집으로 손쉽게 좁혀, 색인 용량과 노이즈를 관리하기 쉬워집니다.

## 관리자 활용 시나리오

- **권한 정합성 유지**: 신규 부서 신설·통합 후 ServiceNow ↔ Entra 사용자 매핑을 갱신해 접근 권한이 어긋나지 않도록 유지합니다.
- **점진적 색인 확장**: 처음에는 특정 테이블·카테고리만 색인하다가, 검증 후 쿼리 필터를 넓혀 색인 범위를 단계적으로 확장합니다.
- **오분류 정리**: 불필요하게 노출되던 레코드가 발견되면 쿼리 필터를 조정해 즉시 색인 대상에서 제외합니다.

## 도입 체크포인트

- **권한(ACL) 우선 검증**: 사용자 매핑을 바꾸면 곧바로 검색 결과의 가시성에 영향을 줍니다. 변경 후 대표 계정으로 접근 권한이 의도대로 적용되는지 반드시 확인하세요.
- **변경 이력 관리**: 매핑·필터 수정은 검색 결과 범위에 직접 영향을 주므로, 변경 사유와 시점을 사내 운영 문서에 기록해 두는 것을 권장합니다.
- **색인 상태 모니터링**: 필터 변경 후 색인 항목 수와 색인 오류를 Copilot 커넥터 관리 화면에서 모니터링하세요.
- **최소 권한 원칙**: 쿼리 필터로 색인 범위를 필요한 만큼만 좁혀, 민감한 ITSM 데이터가 과도하게 노출되지 않도록 관리합니다.

---

## 마무리

이번 개선은 겉으로는 소소해 보이지만, 커넥터를 **실제로 운영해 본 관리자라면 반가울** 변화입니다. "설정 하나 바꾸려고 연결을 통째로 다시 만드는" 비효율이 사라지기 때문입니다. ServiceNow 커넥터로 ITSM 데이터를 Copilot에 연결해 두었다면, 사용자 매핑과 쿼리 필터를 주기적으로 점검하는 운영 루틴을 마련해 두시길 권합니다.

---

> **출처**: Microsoft 365 Message Center 항목 **RM503590** — *Admins can now edit user mappings and query filters for ServiceNow Connector*
> - Message Center 아카이브: [https://mc.merill.net/message/RM503590](https://mc.merill.net/message/RM503590)
> - Microsoft 365 Roadmap: [https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=503590](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=503590)
> - 상태: 출시됨(Launched) · 미리 보기 2026년 2월 · GA 2026년 3월 · Worldwide
>
> 위 내용은 Microsoft 365 로드맵/메시지 센터 정보를 바탕으로 정리한 것으로, **실제 출시 일정·기능은 변경될 수 있습니다.**
