from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def welcome():
    
    return "this is welcome page"

@app.route('/calc',methods=["GET"])
def calculator():
    maths = request.json["maths"]
    science=request.json["science"]
    history=request.json["history"]
    
    average_marks=(maths+science+history)/3
    
    if average_marks >= 50:
        return "average marks of the student is {} and result is pass".format(average_marks)
    else:
        return "average marks of the student is {} and result is fail".format(average_marks)


if __name__ == '__main__':
    app.run(debug=True)