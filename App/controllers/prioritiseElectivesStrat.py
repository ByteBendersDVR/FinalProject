from App.controllers import (get_elective_courses, get_all_programCourses, get_allFoun)
from App.models import ProgramCourses, Program
from App.database import db 
from App.controllers.strategy import generateCoursePlan

def generateCoursePlan(programme):
    electiveCourses = get_elective_courses(programme.name)
    coreCourses = get_all_programCourses(programme.name)  # from programCourses
    founCorses = get_allFoun(programme.name)  # from programCourses

    requiredCourses = []
    requiredCourses.append(electiveCourses, coreCourses, founCorses) # appends in this order

    return requiredCourses