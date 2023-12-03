from App.controllers import (programCourses_SortedbyRating)


def generateCoursePlan(programme):
    requiredCourses = []

    requiredCourses = programCourses_SortedbyRating(programme.id)

    return requiredCourses