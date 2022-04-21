from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'a_MagestyMemberInfo'
    
    sort = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(50))
    email = db.Column(db.String(50))
    pwd = db.Column(db.String(128))  

    def __repr__(self):
        return 'id'.format(self.id)   

class UserRegist(db.Model):
    __tablename__= 'a_MagestyMember'
    
    sort = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(50))
    group_cd = db.Column(db.String(50))
    sex_fg = db.Column(db.String(2))
    name = db.Column(db.String(50))
    add1 = db.Column(db.String(150))
    tel_no2 = db.Column(db.String(150))
    email = db.Column(db.String(50))
    pwd = db.Column(db.String(128)) 

    def __repr__(self):
        return 'id: {}'.format(self.id)       

#게시판 관련 질문 모델 ORM
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

#게시판 관련 답변 모델 ORM
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    
