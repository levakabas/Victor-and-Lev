from flask import Flask, request, render_template, redirect,session



@app.route("/")
def index():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/unrest")
def unrest();
    return render_template("unrestricted.html")

@app.route("/secret")
def secret():
    return render_template("secret.html")

@app.route("/restricted")
def restricted():
    return render_tempalte("restricted.html")

if __name__=="__main__":
    app.debug=True
    app.run()
    

