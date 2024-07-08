# [미션] 비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
import hashlib

# ----- Member 코드 정의 ------


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        # [미션] b는 (normally bytes) using the
        self.password = hashlib.sha256(b"password").hexdigest()
        # https://docs.python.org/ko/3/library/hashlib.html

    def display(self):
        print('이름 :', self.name)
        print('아이디 :', self.username)


# ----- Post 코드 정의 ------

class Post():  # Post 기본틀
    def __init__(self, title, content, username):

        self.title = title
        self.content = content
        self.author = username

    def display_post(self):
        print(f"<제목: {self.title}> by {self.author}")
        print(f"{self.content}")


# [미션] Input을 이용하여 Post를 생성하게 해주세요.
def post_writing():
    while True:

        id_check = str(input("아이디: "))
        if any(member.username == id_check for member in members):
            post_title = str(input("글 제목을 입력하세요: "))
            post_content = str(input("글 내용을 입력하세요: "))

            result = Post(post_title, post_content, id_check)
            posts.append(result)

        else:
            print(f"{id_check}는 존재하지 않는 아이디입니다. 다시 입력하세요.")
            continue

        rewrite_option = str(input("더 작성하시겠습니까?(Y/N) : ")).lower()
        if rewrite_option != 'y':
            return False
        else:
            continue


# ----- Member 코드 실행 ------

members = []
posts = []

# [미션] 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요

members_1 = Member('홍길동', 'hong', 'abc123')
members_2 = Member('이순신', 'lee', 'abc123')
members_3 = Member('박첨지', 'park', 'abc123')

members.append(members_1)
members.append(members_2)
members.append(members_3)


# [미션] input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.

name = input("이름: ")
username = input("아이디: ")
password = input("패스워드: ")
members.append(Member(name=name, username=username, password=password))

# [미션] members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요

for Member in members:
    print(Member.name)


# ----- Post 코드 실행 ------

# [미션] 각각의 회원이 게시글을 3개 이상 작성하는 코드를 만들고 'posts'에 append로 저장해주세요 (총 9개 게시글)
post_1 = Post("길동의 일기", "오늘 날씨가 좋다", "hong")
post_2 = Post("길동의 노래", "아버지를 아버지라 부르지 못하고", "hong")
post_3 = Post("길동의 소설", "해피엔딩", "hong")
post_4 = Post("순신의 일기", "어제 날씨가 흐렸다", "lee")
post_5 = Post("순신의 노래", "내 재채기를 알리지 말라", "lee")
post_6 = Post("순신의 소설", "새드엔딩", "lee")
post_7 = Post("첨지의 일기", "내일 날씨는 더울것이다", "park")
post_8 = Post("첨지의 노래", "에헤라디야", "park")
post_9 = Post("첨지의 소설", "애매한엔딩", "park")

for i in range(1, 10):
    posts.append(globals()[f'post_{i}'])


# 게시글 작성 시작
question_post = str(input("게시글을 작성하시겠습니까?(Y/N) : ")).lower()
if question_post == "y":
    post_writing()
else:
    print(("게시글 작성 취소를 선택하셨습니다."))


# [미션] for 문을 돌면서 특정 유저 / 특정 단어가 포함된 게시글의 제목을 모두 프린트 해주세요
try:

    print("----게시글 검색 시작----")

    while True:

        question_keyword = str(
            input("'멤버ID' 또는 '특정 단어'를 입력해주세요 (종료'N'/전체글'All') :  ")).lower()

        if question_keyword == "all":
            for post in posts:
                post.display_post()
            break

        elif question_keyword == "n":
            print("게시글 검색을 취소하셨습니다")
            break

        else:
            if all(question_keyword not in post.content and question_keyword not in post.author for post in posts):
                print("검색결과가 없습니다")
            else:
                for post in posts:
                    if question_keyword in post.content or question_keyword in post.author:
                        print(f"글제목: {post.title} / 글쓴이: {post.author}")

# 예외처리
except Exception:
    print("예기치 못한 문제가 발생했습니다.")


print("프로그램을 종료합니다. 감사합니다!")
