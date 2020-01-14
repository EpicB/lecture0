from flask import Flask,render_template,request,session
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"]= "filesystem"
Session(app)

@app.route("/", methods=["POST","GET"])
def hello():
    
    if request.method == "POST":
        session['notes']=[]
        note=request.form.get("notes")
        session['notes'].append(note)
        return render_template("main.html",notes=session['notes'])
    else:
        return render_template("main.html",notes=session['notes'])