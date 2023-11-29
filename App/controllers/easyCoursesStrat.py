from App.controllers import (programCourses_SortedbyRating)
from App.models import Program, ProgramCourses, Course
from App.controllers.strategy import generateCoursePlan
from App.database import db 

def generateCoursePlan(programme):
    requiredCourses = []

    requiredCourses = programCourses_SortedbyRating(programme.id)

    return requiredCourses