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
        

def sign_in():
    
    while True:
                
        if question_signin == 'y':
            name = str(input("이름을 적으시오 : "))
            username = str(input("원하는 아이디 입력하시오 : "))
            password = str(input("원하는 비밀번호를 만드시오 : "))
            
            user = Member(name, username, password)
            members.append(user)
        
        
            resignin_option = str(input("더 가입하시겠습니까?(Y/N) : ")).lower()
            if resignin_option != 'y':
                break
            else:
                continue
                
        else:
            print("회원가입을 종료합니다")
            break        
        
    return 


# 게시글 (Post)
class Post() : 
    def __init__(self,title,content,username):
        
        self.title = title
        self.content = content
        self.author = username
        
    def display_post(self):
        print(f"<제목: {self.title}> by {self.author}")
        print(f"{self.content}")
        

# Post 작성 수행 함수
def post_writing() :
    while True: 
        id_check = str(input("아이디: "))
        if any(member.username == id_check for member in members):
            b = str(input("글 제목을 입력하세요: "))
            c = str(input("글 내용을 입력하세요: "))
                    
            result = Post(b, c, id_check)
            posts.append(result)
                    
        else:
            print(f"{id_check}는 존재하지 않는 아이디입니다. 다시 입력하세요.")
            continue
                
        rewrite_option = str(input("더 작성하시겠습니까?(Y/N) : ")).lower()
        if rewrite_option != 'y':
            return False
        else:
            continue




##### 1. Member - 회원가입 실행 및 출력 #####
    
question_signin = str(input("계정을 생성하시겠습니까?(Y/N) : ")).lower()
if question_signin == "y":
    sign_in()  
else:
    print("회원가입을 취소하셨습니다")

# Member 출력
print("-----현재 등록된 Member-----")
for i in members:
    i.display()
print("-----회원가입 절차완료 / 게시글 작성 시작-----")



##### 2. Post - 게시글 작성 실행 및 출력 #####

question_post = str(input("게시글을 작성하시겠습니까?(Y/N) : ")).lower()
if question_post == "y":
    post_writing()
else:
    print(("게시글 작성 취소를 선택하셨습니다."))

# Post 출력 (+ 특정 단어 검색)

try:

    print("게시글 열람 시작. 어떤 단어가 포함된 게시글을 보시겠습니까? ")
    print("(검색 결과가 없을 시, 다른 검색어로 검색하십시오.)")

    while True:

        question_keyword = str(input("검색어 (종료'N'/전체글'All') :  ")).lower()
        
        if question_keyword == "all":
            for post in posts:
                post.display_post()
            break
        
        elif question_keyword == "n":
            print("게시글 열람을 취소하셨습니다")
            break
        
        else:
            if all(question_keyword not in post.content for post in posts) :
                print("검색결과가 없습니다")
            else:
                for post in posts:
                    if question_keyword in post.content:
                        post.display_post()

##### 3. 예외처리 #####        
except Exception:
    print("예기치 못한 문제가 발생했습니다. 프로그램을 종료합니다")
    

print("프로그램을 종료합니다. 감사합니다!")