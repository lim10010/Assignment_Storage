# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.nusername = username
        self.password = password
    
    def display(self):
        print('이름 :',self.name) 
        print('아이디 :',self.nusername)
    
    # def append(self): 멤버스 리스트에 인스턴스를 넣는 방식모르겠어요,,

a = Member ('홍길동','hong','abc123')
b = Member ('이순신','lee','abc123')
c = Member ('박첨지','park','abc123')

a.display() # 메서드확인용



class Post:
    # TODO : 코드 구현이 필요합니다.
    pass


# ----- 코드 실행 ------
members = []
posts = []

# TODO : 코드 구현이 필요합니다.
