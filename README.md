# python-address-book-mini_project-2
dataclass를 활용한 객체지향 기반 연락처 관리 시스템 (CRUD 실습)

# SmartPhone Address Book System

파이썬의 객체지향 프로그래밍(OOP)을 연습하기 위해 제작한 연락처 관리 프로그램입니다.
`dataclass`를 사용하여 데이터 구조를 정의하고, 기능별로 클래스를 분리하여 관리 효율성을 높였습니다.

## 🌟 주요 기능
* **연락처 등록**: 이름, 전화번호, 이메일, 주소, 그룹 정보 저장
* **연락처 조회**: 저장된 모든 데이터 출력 및 이름 기반 검색
* **연락처 수정/삭제**: 특정 사용자를 찾아 데이터 업데이트 및 삭제

## 📂 파일 구조
* `Address.py`: 사용자 정보를 담는 `Addr` 데이터 클래스
* `SmartPhone.py`: 데이터 추가, 삭제, 검색 등 실제 비즈니스 로직 처리
* `SmartPhoneMain.py`: 메뉴 UI 출력 및 프로그램 실행 (Entry Point)

---

## 🚀 실행 방법

```bash
# 1. 저장소 클론 (내 컴퓨터로 코드 복사)
git clone [https://github.com/sjhwang/python-address-book.git](https://github.com/sjhwang/python-address-book.git)

# 2. 프로젝트 폴더로 이동
cd python-address-book

# 3. 프로그램 실행
python SmartPhoneMain.py

# ---------------------------------------------------------
# 📝 학습 포인트 (Learning Points)
# ---------------------------------------------------------
# - dataclass를 활용한 데이터 모델링 및 객체 지향 구조 설계
# - 리스트와 enumerate()를 이용한 데이터 탐색 및 인덱스 제어
# - 클래스 간 import/export를 통한 모듈화 실습
