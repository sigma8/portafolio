from . import db

class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.String(120))
    subject = db.Column("subject", db.String(120))
    email = db.Column("email", db.String(120), unique=True)
    message = db.Column("message", db.Text())

    def __init__(self, name, subject, email, message):
        self.name = name
        self.subject = subject
        self.email = email
        self.message = message
