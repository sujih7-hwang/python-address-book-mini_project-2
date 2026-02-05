from SmartPhone import SmartPhone

class SmartPhoneMain:
    """메뉴를 화면에 출력하고 사용자 선택에 맞춰 기능을 실행하는 클래스"""
    
    def __init__(self):
        """기능 클래스인 SmartPhone을 가져와 준비함"""
        self.smartphone = SmartPhone()
    
    def print_menu(self):
        """화면에 작업 메뉴판 출력"""
        print('\n주소관리 메뉴')
        print('-------------------')
        print('1. 연락처 등록')
        print('2. 모든 연락처 출력')
        print('3. 연락처 검색')
        print('4. 연락처 삭제')
        print('5. 연락처 수정')
        print('6. 프로그램 종료')
        print('-------------------')

    def start(self):
        """입력을 받아 적절한 기능을 연결해주는 반복 루프"""
        while True:
            self.print_menu()
            choice = input('원하는 작업을 선택하세요 (1 ~ 6) : ')

            if choice == '1':
                item = self.smartphone.inputAddData()
                self.smartphone.addAddr(item)
            elif choice == '2':
                self.smartphone.printAllAddr()
            elif choice == '3':
                name = input('검색할 이름을 입력하세요 : ')
                self.smartphone.searchAddr(name)
            elif choice == '4':
                name = input('삭제할 이름을 입력하세요 : ')
                self.smartphone.deleteAddr(name)
            elif choice == '5':
                name = input('수정할 이름을 입력하세요 : ')
                print('-----새로운 연락처 정보를 입력하세요-----')
                new_item = self.smartphone.inputAddData()
                self.smartphone.editAddr(name, new_item)
            elif choice == '6':
                print('프로그램을 종료합니다.')
                break
            else:
                print('잘못된 입력입니다. 다시 선택해주세요.')

if __name__ == "__main__":
    app = SmartPhoneMain()
    app.start()
