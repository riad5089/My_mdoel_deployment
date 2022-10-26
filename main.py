from flask import Flask,request,render_template
import pickle
model=pickle.load(open("lr.pkl","rb"))
app=Flask(__name__)
@app.route("/")
def hellow():
    return render_template("index.html")

@app.route("/sub",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        Cgpa = float(request.form["Cgpa"])
        placement_exam_marks = float(request.form["placement_exam_marks"])
        result=model.predict([[Cgpa,placement_exam_marks]])
        if result ==1:
            result = "Placement"
        else:
            result="Not placement"

    # name=request.form["username"]
        # name=request.form["username"]

    return render_template("index.html",n=result)
if __name__== "__main__":
    app.run(debug=True)