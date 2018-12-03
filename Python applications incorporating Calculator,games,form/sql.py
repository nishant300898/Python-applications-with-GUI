from sqlite3 import *
def g(a,b,c,d,e):
        print(a)
        conn = connect('form.db')
        r = conn.cursor()
        r.execute("INSERT INTO form(First_name,Last_name,user_name,password,email) VALUES(?,?,?,?,?)",(a,b,c,d,e))
        conn.commit()
        conn.close()
