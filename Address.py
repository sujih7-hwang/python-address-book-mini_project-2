from dataclasses import dataclass

@dataclass
class Addr:
    """주소 정보를 저장하는 기본 클래스"""
    name : str
    phone : str
    email : str
    address : str
    birth : str
    level : str

    def print_info(self):
        """기본 인적 사항을 출력."""
        print(f'이름 : {self.name}')
        print(f'전화번호  : {self.phone}')
        print(f'이메일 : {self.email}')
        print(f'주소 : {self.address}')
        print(f'생일 : {self.birth}')
        print(f'직급 : {self.level}')