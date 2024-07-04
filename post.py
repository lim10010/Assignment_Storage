class Post:  # 클래스 선언
    def __init__(self, title, content, username):  # 생성자 정의
        self.title = title  # author, content 등은 클래스의 속성
        self.content = content
        self.author = username

    def display_post(self): # 디스플레이
        print(f'제목 : {self.title}')
        print(f'닉네임 : {self.author}')
        print(f'글 내용 : {self.content}')