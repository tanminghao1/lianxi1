from flask import Flask
app = Flask(__name__)

@app.route("/login",methods=['GET','POST'])
def login():
    return {"username":"tann"}


if __name__ == '__main__':
    app.run()