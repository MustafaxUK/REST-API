from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route("/contacts")
def get_contacts():
    return {"email":"example@gmail.com"}