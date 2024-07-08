'''
가상환경 세팅 후에 터미널에서 아래 두 코드 실행하시면 됩니다!!
pip install flask
pip install flask_sqlalchemy
'''


from flask import Flask, render_template, request
import random
from flask_sqlalchemy import SQLAlchemy
import os



#########################################################
############# 파이썬 코드로 데이터베이스 다루기###################

# 플라스크와 데이터베이스 연결
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

# 테이블 생성 코드
class RockPaperSissor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    com = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(100), nullable=False)

    def __rerp__(self):
        return f'사용자 : {self.user} 컴퓨터 : {self.com} 결과 : {self.result}'
    

with app.app_context():
    db.create_all()

#################################################################
##################################################################

@app.route("/")
def home():
    db_value = db.session.query(RockPaperSissor).all()
    return render_template("game.html", historys=db_value)

    ####### 코드 작성 ############


    return render_template("game.html")

if __name__ == '__main__':
    app.run(debug=True)
