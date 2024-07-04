members = []
posts = []

class Member() :
    
    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password
        
    def display(self):
        print(f"▶ 유저이름: {self.name}")
        print(f"▶ 유저ID: {self.username}")
        

def info_set():
    a = str(input("이름을 적으시오 : "))
    b = str(input("원하는 아이디 입력하시오 : "))
    c = str(input("원하는 비밀번호를 만드시오 : "))
    
    return Member(a,b,c)



class Post() : 
    def __init__(self,title,content,username):
        
        self.title = title
        self.content = content
        self.author = username
        
    def display_post(self):
        print(f"<제목: {self.title}>")
        print(f"{self.content} by {self.author}")
        


def post_writing() :
    while True: 
        
        while True:
            id_check = str(input("아이디를 입력하세요: "))
            if any(id.username == id_check for id in members):
                break
            else:
                print(f"{id_check}는 존재하지 않는 아이디입니다. 다시 입력하세요.")
                continue
        
        b = str(input("글 제목을 입력하세요: "))
        c = str(input("글 내용을 입력하세요: "))
        
        result = Post(b, c, id_check)
        posts.append(result)
        
        rewrite_option = str(input("더 작성하시겠습니까? : ")).lower()
        if rewrite_option != 'y':
            break
        
    return


##### 회원가입 실행 및 출력 #####
while True:
    sign_in = str(input("계정을 생성하시겠습니까?(Y/N) : ")).lower()
    if sign_in == 'y':
        user_sign = info_set()
        members.append(user_sign)
    else:
        print("회원가입을 종료합니다")
        break
    
for i in members:
    i.display()

##### 게시글 작성 실행 및 출력 #####
post_writing()

for y in posts:
    y.display_post()