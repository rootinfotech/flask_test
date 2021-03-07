from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/flaskdemo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)

class Student(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(20))
    saddr = db.Column(db.String(30))

@app.route('/stu', methods=['GET','POST'])
def homeview():
    s = Student(sname='vishnu', saddr='pune')
    db.session.add(s)
    print(s.sid)
    db.session.commit()
    print(s.sid)
    s.saddr = 'mumbai'
    db.session.commit()
    stulist = Student.query.all()
    return render_template('stu_list.html', studentlist=stulist)

@app.route('/')
def m1():
    s = Student(sname='vishnu', saddr='karvenagar')
    s1 = Student(sname='ketan', saddr='wardha')
    s2 = Student(sname='vaibhav', saddr='pune')
    db.session.add_all([s, s1, s2])
    db.session.commit()
    s1.sname='sagar'
    stulist = Student.query.all()
    return render_template('base.html', stulist=stulist)

@app.route("/update/<int:id>/")
def m2(id):
    x=Student.query.get(id)
    x.sname='nishit'
    x.saddr='nagpur'
    db.session.commit()
    return redirect('/')
@app.route('/delete/<int:id>/')
def m3(id):
    db.session.delete(id)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)