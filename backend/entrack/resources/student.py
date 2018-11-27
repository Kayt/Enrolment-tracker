from flask_restful import Resource, reqparse
from entrack.models.student import StudentModel

class Student(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="this field cannot be left blank"
    )

    parser.add_argument('surname',
        type=str,
        required=True,
        help="Add the students surname"
    )

    def get(self, name):
        student = StudentModel.find_by_name(name)
        if student:
            return student.json()
        return {'message': 'student not found'}, 404

    def post(self, name):
        if StudentModel.find_by_name(name):
            return {'message': 'student with name {} already exists'.format(name)}, 400
        
        data = Student.parser.parse_args()

        student = StudentModel(data['name'], data['surname'])

        try:
            student.save()
        except:
            return {'message': 'An error occured while creating a student'}, 500

        return student.json(), 201

    def delete(self, name):
        student = StudentModel.find_by_name(name)
        if student:
            student.delete()

        return {'message': 'student deleted'}


class StudentList(Resource):
    def get(self):
        return {'students': [student.json() for student in StudentModel.query.all()]}