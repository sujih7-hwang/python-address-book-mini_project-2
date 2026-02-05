from Address import Addr

class SmartPhone:
    """연락처 데이터의 실제 처리 로직을 담당하는 클래스"""
    
    def __init__(self):
        # 주소록 데이터를 저장할 리스트 객체
        self.contact = []

    def inputAddData(self):
        """사용자로부터 연락처 정보를 입력받아 Addr 객체 생성"""
        name = input('이름: ')
        phone = input('전화번호: ')
        email = input('이메일: ')
        address = input('주소: ')
        group = input('그룹: ')
        return Addr(name, phone, email, address, group)

    def addAddr(self, person):
        """리스트의 끝에 새로운 연락처 정보를 추가 (append)"""
        self.contact.append(person)
        print('정상적으로 저장되었습니다.')

    def printAllAddr(self):
        """저장된 모든 데이터를 순차적으로 출력"""
        if not self.contact:
            print('저장된 연락처가 없습니다.')
            return
            
        for person in self.contact:
            person.print_info()
            print('-' * 20)

    def searchAddr(self, name):
        """이름 기반의 선형 검색 수행"""
        for person in self.contact:
            if person.name == name:
                person.print_info()
                return
        print(f'[{name}]님을 찾을 수 없습니다.')

    def deleteAddr(self, name):
        """
        enumerate()로 데이터의 순서(index)와 값(person)을 동시에 추출.
        삭제할 위치를 정확히 파악하여 del 키워드로 메모리에서 제거.
        """
        for index, person in enumerate(self.contact):
            if person.name == name:
                # del: 특정 인덱스의 요소를 리스트에서 완전히 제거
                del self.contact[index]
                print(f'[{name}]님의 정보를 삭제했습니다.')
                return
        print(f'삭제하려는 [{name}]님이 목록에 없습니다.')

    def editAddr(self, name, new_person):
        """입력받은 인덱스(index)의 기존 데이터를 새 데이터로 덮어쓰기"""
        for index, person in enumerate(self.contact):
            if person.name == name:
                # 찾은 위치(index)에 새로운 객체를 대입
                self.contact[index] = new_person
                print(f'[{name}]님의 정보를 수정 완료했습니다.')
                return
        print(f'수정하려는 [{name}]님을 찾지 못했습니다.')
