from flask import Flask, request, render_template, redirect, session, escape, url_for
import mengo

app=Flask(__name__)
@app.route("/", methods=["GET","POST"])
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if mengo.authenticate(username,password):
            session['username'] = request.form['username']  
            return redirect(url_for('restricted'))
        else:
            return redirect(url_for('login'))
    

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if new_user(username,password):
            return redirect(url_for('register_success'))
        else:
            return redirect(url_for('register_failure'))


@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/unrest")
def unrest():
    return render_template("unrestricted.html")

@app.route("/secret")
def secret():
    return render_template("secret.html")

@app.route("/restricted")
def restricted():
    if 'username' in session:
        username = escape(session['username'])
        password = 'd'
        studentid = 'd'
        pizza = 'd'
        return render_tempalte("restricted.html", username=username, password=password, studentid=studentid, pizza=pizza)
    else:
        return redirect(url_for('login'))
    
@app.route("/register_success")
def register_success():
    return render_tempalte("register_success.html")
    
@app.route("/register_failure")
def register_failure():
    return render_tempalte("register_failure.html")

if __name__=="__main__":
    app.debug=True
    app.run()
    

