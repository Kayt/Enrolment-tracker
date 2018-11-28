import csv
import celery

from flask import render_template, redirect

from . import api, app
from entrack.resources.course import Course, CourseList
from entrack.resources.enrolment import Enrolment, EnrolmentList
from entrack.resources.student import Student, StudentList
from flask_restful import Resource


api.add_resource(Student, '/student/<string:name>')
api.add_resource(StudentList, '/students')
api.add_resource(Course, '/course/<string:name>')
api.add_resource(CourseList, '/courses')
api.add_resource(Enrolment, '/enrolment')
api.add_resource(EnrolmentList, '/enrolments')

@app.route('/')
def index():
    return render_template('index.html')

@celery.task
def create_csv(data):
    enrolments = Enrolment.query.all()
    with open('enrolments.csv', mode='w') as csv_file:
        enrolment_writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        for entry in enrolments:
            enrolment_writer.writerow(entry.list())

