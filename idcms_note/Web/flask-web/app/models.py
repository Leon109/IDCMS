#coding=utf-8

from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager

class User(UserMixin, db.Model):
    '''为了使用flask-login用户模型需要继承UserMixin'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    '''这是个回调函数接收(理论上该方法放在任何一个被导入的模块中都可以，
    @login_manager.user_loader会将这个方法注册到程序中去，类似蓝本通过
    __init__ 导入,放在models，方便管理)
    以Unicode字符串形式表示的用户标识符，如果能找到用户，这个函数必须返
    回用户对象；否则应该返回None
    user_id 就是用User模型表里的id,通过id确定用户是否存在
    '''
    return User.query.get(int(user_id))