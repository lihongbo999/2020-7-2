


from flask import Flask,redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy  # 导入 SQLAlachamy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lyu19910409@localhost:3306/lab'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s!' % name
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

# ----------------------------------
# post 方法

@app.route('/success/<name>/<password>')
def success(name,password):
    return 'welcome {} {}' .format(name,password)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        return redirect(url_for('success',name = user,password = password))
    else:
        user = request.args.get('user')
        password = request.args.get('password')
        return redirect(url_for('success',name = user,password = password))

#---------------------------------------------
# 数据库测试


class BaseModel(db.Model):
    __abstract__ = True # 抽象类，可以将其他数据表中的公共字段存放在这个类中，然后继承该类
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)

Article_Tag =db.Table(
    "acticle_tag",
    db.Column("id",db.Integer,primary_key=True,autoincrement=True),
    db.Column("article_id",db.Integer,db.ForeignKey("article.id")),
    db.Column("tag_id",db.Integer,db.ForeignKey("tag.id"))
) # 创建多对多表

class Article(BaseModel):
    __tablename__ = "article"
    title = db.Column(db.String(20))
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    tag = db.relationship(
        "Tag", # 定义关联的数据表，正向查询时使用“tag”进行查询
        secondary=Article_Tag, # 多对多关系中关联的中间表
        lazy="dynamic", # 指定sqlalchemy数据库何时加载数据
        backref=db.backref("article",lazy="dynamic") # 指定反向查询时使用的名称和何时加载数据
    )

class Tag(BaseModel):
    __tablename__ = "tag"
    name = db.Column(db.String(20))

class User(BaseModel):
    __tablename__ = "user"
    username = db.Column(db.String(10))
    phone = db.Column(db.String(11))
    article = db.relationship(
        "Article",
        backref = "Author"
    )

db.create_all() # 在数据库中生成数据表
#db.drop_all() 删除数据库中的数据表


if __name__ == '__main__':
    app.run(debug=True)
