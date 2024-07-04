members = []

class Member() :
    
    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password
        
    def display(self):
        print(f"▶ 유저이름: {self.name}")
        print(f"   유저ID: {self.username}")
        

def info_set():
    a = str(input("이름을 적으시오 : "))
    b = str(input("원하는 아이디 입력하시오 : "))
    c = str(input("원하는 비밀번호를 만드시오 : "))
    
    return Member(a,b,c)


##### 회원가입 실행 #####
while True:
    sign_in = str(input("계정을 생성하시겠습니까?(Y/N) : ")).lower()
    if sign_in == 'y':
        user_sign = info_set()
        members.append(user_sign)
    else:
        print("회원가입을 종료합니다")
        break

print("-----현재까지 가입된 멤버의 정보입니다-----")
for member in members:
    member.display()



class Post() : 
    def __init__(self,title,content,Member):
        
        self.title = title
        self.content = content
        self.username = Member.username
        
    def display_post(self):
        print(f"<제목: {self.title}>")
        print(f"{self.content} by {self.username}")


Many_post = Post("Many's word", "냉정과 열정 사이", Many)
Tony_post = Post("Tony's word", "점프 투 파이썬", Tony)
Kona_post = Post("Kona's word", "점심 메뉴를 고민중입니다", Kona)

posts.append(Many_post)
posts.append(Tony_post)
posts.append(Kona_post)

for y in posts:
    y.display_post()






