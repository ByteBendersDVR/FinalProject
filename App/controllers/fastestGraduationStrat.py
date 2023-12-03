from App.controllers import (get_all_programCourses, get_allFoun)

# fastest graduation, no electives 
def generateCoursePlanFastest(programme):
    coreCourses = get_all_programCourses(programme.name)  # from programCourses
    founCorses = get_allFoun(programme.name)  # from programCourses

    requiredCourses = []
    requiredCourses.append(coreCourses, founCorses)

    return requiredCourses

