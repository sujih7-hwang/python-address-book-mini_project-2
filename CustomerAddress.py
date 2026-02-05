from dataclasses import dataclass
from Address import Addr

@dataclass
class CustomerAddr(Addr):
    """Addr을 상속받는 거래처 연락처 클래스"""
    costomer_name : str
    product_name : str
    level : str

    def print_info(self):
        """부모 클래스의 출력 기능을 호출한 뒤 거래처 정보를 추가로 출력."""
        super().print_info()
        print(f'직급 : {self.level}')
        print(f'거래처 이름 : {self.costomer_name}')
        print(f'품목 이름 : {self.product_name}')