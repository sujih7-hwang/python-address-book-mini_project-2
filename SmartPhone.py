from CompanyAddress import CompanyAddr
from CustomerAddress import CustomerAddr

class SmartPhone:
    """
    연락처 리스트를 관리하며 등록, 검색, 삭제, 수정 기능을 제공하는 클래스
    """
    def __init__(self):
        # 메모리 효율을 위해 필요한 시점에 리스트에 객체를 담습니다.
        self.contact = []

    def inputAddCompanyData(self):
        """사용자로부터 회사 정보를 입력받아 CompanyAddr 객체를 생성합니다."""
        print('#연락처 등록(회사)')
        name = input("이름: "); phone = input("전화번호: ")
        email = input("이메일: "); address = input("주소: ")
        birth = input("생일: "); level = input("직급: ")
        company_name = input("회사이름: "); team_name = input("부서이름: ")
        return CompanyAddr(name, phone, email, address, birth, level, company_name, team_name)

    def inputAddCustomerData(self):
        """사용자로부터 거래처 정보를 입력받아 CustomerAddr 객체를 생성합니다."""
        print('#연락처 등록(거래처)')
        name = input("이름: "); phone = input("전화번호: ")
        email = input("이메일: "); address = input("주소: ")
        birth = input("생일: "); level = input("직급: ")
        customer_name = input("거래처이름: "); product_name = input("품목이름: ")
        return CustomerAddr(name, phone, email, address, birth, level, customer_name, product_name)

    def addAddr(self, contact_obj):
        """리스트에 연락처 객체를 추가"""
        self.contact.append(contact_obj)
        print(f'>>>{contact_obj.name}님의 데이터가 저장되었습니다.')

    def printAllAddr(self):
        """모든 연락처 출력"""
        if not self.contact:
            print("데이터가 없습니다.")
            return
        for i, person in enumerate(self.contact):
            print(f'[{i+1}]')
            person.print_info()
            print("-" * 20)

    def searchAddr(self):
        """이름으로 연락처 검색"""
        name = input('검색할 이름: ')
        for person in self.contact:
            if person.name == name:
                person.print_info()
                return
        print('검색 결과가 없습니다.')

    def deleteAddr(self):
        """이름으로 연락처를 찾아 삭제"""
        name = input('삭제할 이름: ')
        for person in self.contact:
            if person.name == name:
                self.contact.remove(person)
                print(f'{name} 삭제 완료.')
                return
        print('삭제할 대상이 없습니다.')

    def editAddr(self):
        """기존 연락처를 수정합니다."""
        name = input('수정할 이름: ')
        for i, person in enumerate(self.contact):
            if person.name == name:
                choice = int(input('1.회사 2.거래처: '))
                self.contact[i] = self.inputAddCompanyData() if choice == 1 else self.inputAddCustomerData()
                print("수정 완료.")
                return
        print('대상을 찾을 수 없습니다.')