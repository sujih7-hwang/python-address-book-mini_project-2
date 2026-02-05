from dataclasses import dataclass

@dataclass
class Addr:
    """사용자 정보를 담는 기본 데이터 구조"""
    name: str
    phone: str
    email: str
    address: str
    group: str

    def print_info(self):
        """저장된 상세 정보를 포맷에 맞춰 출력"""
        print(f'이름 : {self.name}')
        print(f'전화번호 : {self.phone}')
        print(f'이메일 : {self.email}')
        print(f'주소 : {self.address}')
        print(f'그룹(친구/가족) : {self.group}')
