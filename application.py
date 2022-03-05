from enum import unique
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Contact(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.id} - {self.phone_number} - {self.name} - {self.email} "

@app.route("/contacts")
def get_contacts():
    contacts = Contact.query.all()
    output = []
    for contact in contacts:
        contact_data = {"phone_number": contact.phone_number, "name": contact.name, "email": contact.email}
        output.append(contact_data)

    return {"My Contacts":output}

@app.route("/contacts/<id>")
def get_contact(id):
    contact = Contact.query.get_or_404(id)
    return {"Mobile": contact.phone_number, "Name": contact.name, "Email": contact.email}
