from enum import unique
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Contact(db.Model):
    phone_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.phone_number} - {self.name} - {self.email} "




@app.route('/')
def index():
    return "Hello World"

@app.route("/contacts")
def get_contacts():
    return {"email":"example@gmail.com"}