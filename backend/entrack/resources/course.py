from flask_restful import Resource, reqparse
from entrack.models.course import CourseModel

class Course(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="this field cannot be left blank"
    )

    parser.add_argument('description',
        type=str,
        required=True,
        help="Describe the course first"
    )

    def get(self, name):
        course = CourseModel.find_by_name(name)
        if course:
            return course.json()
        return {'message': 'course not found'}, 404

    def post(self, name):

        if CourseModel.find_by_name(name):
            return {'message': 'course with name {} already exists'.format(name)}, 400
        
        data = Course.parser.parse_args()

        course = CourseModel(data['name'], data['description'])

        try:
            course.save()
        except:
            return {'message': 'An error occured while creating a course'}, 500

        return course.json(), 201

    def delete(self, name):
        course = CourseModel.find_by_name(name)
        if course:
            course.delete()

        return {'message': 'course deleted'}


class CourseList(Resource):
    def get(self):
        return {'courses': [course.json() for course in CourseModel.query.all()]}