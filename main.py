from flask import Flask, request

import pandas as pd
app = Flask(__name__)
 
@app.route("/")
def hello():
    main = '<!DOCTYPE html><html><head></head><body><style>body{background-color: #007acc; text-align:center;} h1{border: 2px solid; background-color: white;} form{background-color: white;}input{display: block; margin:auto;}</style><h1>Where Do U Stand?</h1><form action="/gpa" method="POST"><label>Course 1</label><input name="course1"> <label>Course 2</label><input name="course2"> <label>Course 3</label><input name="course3">'
    main +='<label>Course 4</label><input name="course4"> <label>Course 5</label><input name="course5"> <label>Course 6</label><input name="course6">'
    main+='<label>Course 7</label><input name="course7"><label>Course 8</label><input name="course8"><label>Course 9</label><input name="course9">'
    main+='<label>Course 10</label><input name="course10"><label>Course 11</label><input name="course11"><label>Course 12</label>'
    main+='<input name="course12"><input type="submit" value="Submit"></form></body></html>'
    return main
 
@app.route("/gpa", methods=['POST'])
def gpa(): 
    grades = pd.DataFrame({request.form['course1'], request.form['course2'], request.form['course3'], request.form['course4'], request.form['course5'], request.form['course6'], request.form['course8'],request.form['course9'] , request.form['course10'], request.form['course11'], request.form['course12']})
    grades.to_csv('input.csv')
    return ""

 
if __name__ == "__main__":
    app.run()