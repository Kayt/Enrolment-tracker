from entrack import db 

class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))
    enrolled_courses = db.relationship('EnrolmentModel', backref='student_model', lazy='dynamic')

    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname

    def json(self):
        return {'name':self.name, 'surname':self.surname}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()