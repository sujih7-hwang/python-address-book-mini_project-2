from SmartPhone import SmartPhone

class SmartPhoneMain:
    """
    프로그램의 메뉴를 출력하고 제어하는 메인 컨트롤러 클래스
    """
    def __init__(self):
        self.addrbook = SmartPhone()

    def start(self):
        """메인 루프를 실행합니다."""
        while True:
            print('\n--- 주소관리 메뉴 ---')
            print('1.회사등록 2.거래처등록 3.전체출력 4.검색 5.삭제 6.수정 7.종료')
            try:
                user = int(input('선택: '))
                if user == 1: self.addrbook.addAddr(self.addrbook.inputAddCompanyData())
                elif user == 2: self.addrbook.addAddr(self.addrbook.inputAddCustomerData())
                elif user == 3: self.addrbook.printAllAddr()
                elif user == 4: self.addrbook.searchAddr()
                elif user == 5: self.addrbook.deleteAddr()
                elif user == 6: self.addrbook.editAddr()
                elif user == 7: break
            except ValueError:
                print("숫자만 입력해 주세요.")

if __name__ == "__main__":
    app = SmartPhoneMain()
    app.start()