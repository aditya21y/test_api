from enum import unique
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# class login(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(100),unique=True,nullable=False)
#     password = db.Column(db.String(100),nullable=False)


#     def __repr__(self):
#         return f"{self.username} - {self.password}"

class register(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.String(100),nullable=False)
    username = db.Column(db.String(100),unique=True,nullable=False)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f"{self.username} - {self.password}"
@app.route('/registered_usr')
def list_user():
    log = register.query.all()
    user=[]
    for usr in log:
        log_data = {"fullname":usr.fullname,"username":usr.username,"password":usr.password,"email":usr.email}
        user.append(log_data)
    return{"users":user}


# @app.route('/login/<id>')
# def get_user(id):
#     user = login.query.get_or_404(id)
#     return {"username":user.username,"password":user.password}

@app.route('/login',methods=['POST'])
def add_user():
    user = register(username=request.json['username'],password=request.json['password'])
    log = register.query.all()
    for usr in log:
        if  user.username == usr.username:
            return {'status':"ok",
            'token':'<TOKEN_JWT>'}
        else:
            return {'status':"not ok",
            'token':'<TOKEN_JWT>'}

@app.route('/register',methods=['POST'])
def add_userRegister():
    user = register(fullname=request.json['fullname'],username=request.json['username'],password=request.json['password'],email=request.json['email'])
    db.session.add(user)
    db.session.commit()
    # return{'id':user.id}
    return {'status':"ok",
    'message':'akun berhasil dibuat'}



if __name__ == "__main__":
    app.run(debug=True)