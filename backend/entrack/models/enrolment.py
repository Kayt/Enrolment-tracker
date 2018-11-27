from entrack import db

class EnrolmentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(200), db.ForeignKey('student_model.name'))
    course_name = db.Column(db.String(200), db.ForeignKey('course_model.name'))
    year = db.Column(db.String(200))

    def __init__(self, student_name, course_name, year):
        self.student_name = student_name
        self.course_name = course_name
        self.year = year

    def json(self):
        return {'student':self.student_name, 'course':self.course_name, 'year':self.year }

    def list(self):
        return [self.student_name, self.course_name, self.year]

    @classmethod
    def find_enrolment(cls, student_name, course_name):
        return cls.query.filter(student_name=student_name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()