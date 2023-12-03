# from App.models import FastestGraduation, EasyCourses, PrioritizeElectives
from App.database import db
from App.controllers.easyCoursesStrat import generateCoursePlanEasy
from App.controllers.fastestGraduationStrat import generateCoursePlanFastest
from App.controllers.prioritiseElectivesStrat import generateCoursePlanElectives
# think this is how it should work
def setStrategy(planOption, programme):
   strategy = None

   if planOption == "fastest":
      strategy = generateCoursePlanEasy(programme)
   if planOption == "easy":
      strategy = generateCoursePlanEasy(programme)
   if planOption == "electives":
      strategy = generateCoursePlanElectives(programme)
   
   return strategy

