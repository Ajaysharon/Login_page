import sqlite3

db=sqlite3.connect("login.db")
cursor= db.cursor()


def execute_query(sql_query):
    with sqlite3.connect('login.db') as db:
        csr=db.cursor()
        result=csr.execute(sql_query)
        db.commit()
    return result

#sql_query="""create table login(username varchar(20),password varchar(20))"""
#sql_query="""insert into login values('20ad04','kcg1234')"""
sql_query="""SELECT * FROM login"""

#sql_query="""create table details(username varchar(20),Name varchar(20),Dob varchar(20),Mail_id varchar(20),
#               phone_number integer,Address varchar(20)) """

#sql_query="""insert into details values('20ad04',"AJAY",'10-11-2001','20ad04@kcgcollege.com',9489693949,'kanyakumari')"""

sql_query="""SELECT * FROM details"""

RESULT=execute_query(sql_query)
print(RESULT.fetchall())



