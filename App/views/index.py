from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import (create_course, create_staff,createCoursesfromFile)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_staff(1, "adminpass","999", "admin")
    createCoursesfromFile('testData/courseData.csv')
    create_user('bob', 'bobpass')
    create_program("Computer Science Major", 69, 15, 9)
    create_student(816, "boo", "boopass", "Boon", "Computer Science Major")
    create_staff(123,"admin", "adminstaff", "Jones")
    return jsonify(message='staff created, courses created, db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
