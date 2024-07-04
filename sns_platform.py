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
        

Many = Member("Many","lim10010","qwe123")
Tony = Member("Tony","Ton20020","qwe456")
Kona = Member("Kona","Kon30030","qwe789")

members.append(Many)
members.append(Tony)
members.append(Kona)


for i in members:
    i.display()



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






