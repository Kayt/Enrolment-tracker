from flask_restful import Resource, reqparse
from entrack.models.enrolment import EnrolmentModel

class Enrolment(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('student',
        type=str,
        required=True,
        help="this field cannot be left blank"
    )

    parser.add_argument('course',
        type=str,
        required=True,
        help="A student should be registered for a course"
    )

    parser.add_argument('year',
        type=str,
        required=True,
        help="Every enrolment needs a year"
    )

    def get(self):
        return {'message':'feature not supported yet'}

    def post(self):

        data = Enrolment.parser.parse_args()

        enrolment = EnrolmentModel(data['student'], data['course'], data['year'])

        try:
            enrolment.save()
        except:
            return {'message': " An error occured enrolling a student"}, 500

        return enrolment.json(), 201


class EnrolmentList(Resource):
    def get(self):
        return {'enrolments': [enrolment.json() for enrolment in EnrolmentModel.query.all()]}