from flask import Flask, render_template, request, redirect, url_for
import random
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import func
from itertools import product
import random




############# 데이터베이스 구현 ##############

# 플라스크와 데이터베이스 연결
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

# 테이블 생성 코드
class RockPaperSissor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    com = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(100), nullable=False)

    def __rerp__(self):
        return f'사용자 : {self.user} 컴퓨터 : {self.com} 결과 : {self.result}'

with app.app_context():
    db.create_all()



############# 코드 구현 ##############

@app.route("/", methods=['GET', 'POST'])
def home():

    # 초기값 세팅
    case = ["가위", "바위", "보"]
    computer = "대기중"
    player = "대기중"
    result = None

    if request.method == 'POST':
        player = request.form['player_choice']
    else:
        player = "대기중"


    # 가위바위보 승패판정 로직
    def rsp_result(player,computer):
        event = (player,computer) # (플레이어,컴퓨타) 듀플로 묶기 -> 밑에 product가 생성한 경우의 수와 비교
        for x, y in enumerate(product(case, case), 1): # 가위바위보 모든 경우의 수 생성
            if event == y:
                if x in [1,5,9]: # 승패판정
                    return "무"
                elif x in [3,4,8]:
                    return "패"
                else:
                    return "승"


    # player 사용자 선택이 있어야 실행 조건
    if player != "대기중":
        computer = str(random.choice(case))
        result = rsp_result(computer,player)
    
        # 결과 database에 추가
        result_history = RockPaperSissor(com=computer, user=player, result=result)
        db.session.add(result_history)
        db.session.commit()


    # 결과 히스토리 출력
    db_value = db.session.query(RockPaperSissor).all()


    # 결과 통계표 출력
    win = db.session.query(func.count(RockPaperSissor.result)).filter(RockPaperSissor.result == "승").scalar()
    lost = db.session.query(func.count(RockPaperSissor.result)).filter(RockPaperSissor.result == "패").scalar()
    same =  db.session.query(func.count(RockPaperSissor.result)).filter(RockPaperSissor.result == "무").scalar()

    db_report = {
        "win": win,
        "lost":lost,
        "same":same,
        "com":computer,
        "user":player,
        "result":result,
    }

    return render_template("game.html", report=db_report, historys=db_value)


# 리셋 라우트
@app.route('/reset', methods=['POST'])
def reset_database():
    try:
        db.drop_all()
        db.create_all()
        return redirect(url_for('home'))
    except Exception as e:
        return f"예기치 못한 오류 발생: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
