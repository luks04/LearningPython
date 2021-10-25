from flask_learning.database import db

class User(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    phone = db.Column(db.Integer())

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
