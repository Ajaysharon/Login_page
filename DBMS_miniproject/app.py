from flask import Flask,render_template,request
from distutils.log import debug
import sqlite3

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route("/",methods=["POST", "GET"])
def login():
    if request.method == "GET":
        print("a")
        return render_template("hello.html")
    else:
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        #register=request.form['register']
        name = request.form['loginUser']
        password= request.form['loginPassword']

        query="select * from login where username='"+name+"' and password = '"+password+"'"
        cursor.execute(query)
        result = cursor.fetchall()

        if len(result)!=0:
            query="select name,dob,Mail_id,phone_number,Address from details where username='"+name+"'"
            cursor.execute(query)
            details=cursor.fetchall()[0]
            return render_template("psdetail.html",name=details[0],dob=details[1],mail=details[2],
                        phone=details[3],address=details[4],user=name)
        else:
            return render_template("hello.html")

        
@app.route("/psdetails")
def home():
    return render_template("psdetail.html")

@app.route("/Register",methods=["POST", "GET"])
def register():
    if request.method == "GET":
        print("a")
        return render_template("Register.html")
    else:
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        name = request.form['loginUser']
        dob= request.form['DOB']
        mail=request.form['mail']
        phone=request.form['phone']
        address=request.form['addr']
        password=request.form['loginPassword']
        user=request.form['username']
        query="insert into details values('"+user+"','"+name+"','"+dob+"','"+mail+"','"+phone+"','"+address+"')"
        cursor.execute(query)
        query="insert into login values('"+user+"','"+password+"')"
        cursor.execute(query)
        db.commit()
        print("Added Successfully")
        return render_template("hello.html")

if __name__ == "__main__":
    app.run(debug=True)
