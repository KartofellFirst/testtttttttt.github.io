from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html", text = "HELLO!", answer = "Hello!", link = "/1")

@app.route('/<int:id>')
def one(id):
    if id == 1:
        title = "HOW ARE YOU? WHATS UP?"
        answ = "I`m ok"
        linkToFolow = "/" + str(id+1)
    elif id == 2:
        title = "I ate your childrens like 2 days before"
        answ = "I ate they too"
        linkToFolow = "/" + str(id+1)
        
    return render_template("main.html", text = title, answer = answ, link = linkToFolow)

if __name__ == "__main__":
    app.run(debug=True) 