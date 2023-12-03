from App.controllers import (programCourses_SortedbyRating)


def generateCoursePlanEasy(programme):
    requiredCourses = []

    requiredCourses = programCourses_SortedbyRating(programme.id)

    return requiredCourses