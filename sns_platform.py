# [완료] 비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
import hashlib

# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.nusername = username
        self.password = hashlib.sha256(b"password").hexdigest()  # [완료] b는 (normally bytes) using the
        # https://docs.python.org/ko/3/library/hashlib.html
    
    def display(self):
        print('이름 :',self.name) 
        print('아이디 :',self.nusername)

class Post:
    def __init__(self, title, content, Member):
        self.title = title
        self.content = content
        self.username = Member

    def display_post(self):
        print(f"<제목: {self.title}>")
        print(f"{self.content} by {self.username}")


# ----- 코드 실행 ------
members = []
posts = []

# [완료] 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요

members_1 = Member ('홍길동','hong','abc123')
members_2 = Member ('이순신','lee','abc123')
members_3 = Member ('박첨지','park','abc123')

members.append(members_1)
members.append(members_2)
members.append(members_3)

# Many_post = Post("Many's word", "냉정과 열정 사이", members_1)
# Tony_post = Post("Tony's word", "점프 투 파이썬", members_2)
# Kona_post = Post("Kona's word", "점심 메뉴를 고민중입니다", members_3)

# posts.append(Many_post)
# posts.append(Tony_post)
# posts.append(Kona_post)

# [완료] input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
name = input("이름: ")
username = input("아이디: ")
password = input("패스워드: ")
members.append(Member(name=name, username=username, password=password))

# [완료] members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
for Member in members:
    print(Member.name)

#### 

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
