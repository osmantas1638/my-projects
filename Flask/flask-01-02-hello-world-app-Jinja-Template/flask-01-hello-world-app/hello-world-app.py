from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello from flask !!!"

@app.route('/second')
def second():
    return "bize her yer gaziantep !!!"



@app.route('/third/subthird')
def third():
    return "this is the subpage of third page !!!"













if __name__ == '__main__':
    app.run(debug=True,port=2000)