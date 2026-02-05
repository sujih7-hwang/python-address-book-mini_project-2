from dataclasses import dataclass
from Address import Addr

@dataclass
class CompanyAddr(Addr):
    """Addr을 상속받는 회사 동료 연락처 클래스"""
    company_name : str
    team_name : str
    level : str

    def print_info(self):
        """부모 클래스의 출력 기능을 호출한 뒤 회사 정보를 추가로 출력."""
        super().print_info()
        print(f'직급 : {self.level}')
        print(f'회사이름 : {self.company_name}')
        print(f'부서이름 : {self.team_name}')