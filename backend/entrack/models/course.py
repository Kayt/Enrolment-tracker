from entrack import db

class CourseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    description = db.Column(db.Text)
    enroled_students = db.relationship('EnrolmentModel', backref='course_model', lazy='dynamic')

    def __init__(self, name, description):
        self.name = name 
        self.description = description

    def json(self):
        return {'name':self.name, 'description':self.description}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()