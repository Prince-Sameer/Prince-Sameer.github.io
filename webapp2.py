from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def nm():
    return render_template("nw2.html")
@app.route("/f1",methods=["GET","POST"])
def f1():
    if request.method=="POST":
        k=request.form.get("name")
    return render_template("nw1.html",name=k)
@app.route("/king",methods=["GET","POST"])
def dish():
    if request.method=="POST":
        u=request.form.get("food")
    if u=="Biryani":
        return render_template("Biryani.html")
    else:
        return render_template("Pulao.html")
