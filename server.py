from flask import Flask, render_template,request
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")
 

@app.route('/login', methods=["POST"])
def login():

    if request.method == 'POST':
        from login import login
        login(request.form['user'], request.form['pass'])

    return render_template('index.html')

if __name__ == "__main__":
    app.env = "DEVELOPMENT"
    app.debug = True
    app.run()