from flask import *
import sql
app=Flask(__name__)
@app.route('/send1',methods=['GET','POST'])
def sen():
    if request.method=='POST':
        a=request.form['a']
        b=request.form['b']
        c=request.form['c']
        d=request.form['d']
        e=request.form['e']
        sql.g(a,b,c,d,e)
        return render_template("0.html")
    return render_template('my_form1.html')
if __name__=='__main__':
    app.run(debug=True)
