# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.nusername = username
        self.password = password
    
    def display(self):
        print('이름 :',self.name) 
        print('아이디 :',self.nusername)

class Post:
    # TODO : 코드 구현이 필요합니다.
    pass


# ----- 코드 실행 ------
members = []
posts = []

members_1 = Member ('홍길동','hong','abc123')
members_2 = Member ('이순신','lee','abc123')
members_3 = Member ('박첨지','park','abc123')

members.append(members_1)
members.append(members_2)
members.append(members_3)

print(members) # members 리스트가 보이지는 않는 데 괜찮을까요?

for Member in members:
    print(Member.name) 

# TODO : 코드 구현이 필요합니다.
