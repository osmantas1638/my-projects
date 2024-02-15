from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=56, number2=85)

@app.route("/osman")
def number():
    num1 = 56
    num2 = 44
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)



if __name__== "__main__":
    app.run(debug=True, port=30000)