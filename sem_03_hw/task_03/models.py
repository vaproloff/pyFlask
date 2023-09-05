from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    grades = db.relationship('Grade', backref='student', lazy=True)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, email: {self.email}, группа: {self.group}.'


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f'{self.subject} - {self.grade}'
