from App.controllers import (get_all_programCourses, get_allFoun)
from App.models import Course, FastestGraduation
from App.database import db 

# fastest graduation, no electives 
def generateCoursePlan(programme):
    coreCourses = get_all_programCourses(programme.name)  # from programCourses
    founCorses = get_allFoun(programme.name)  # from programCourses

    requiredCourses = []
    requiredCourses.append(coreCourses, founCorses)

    return requiredCourses

