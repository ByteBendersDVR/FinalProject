from App.database import db


class CoursePlanCourses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planId = db.Column(db.ForeignKey('course_plan.planId'))
    code = db.Column(db.ForeignKey('course.courseCode'))
    plan_option = db.Column(db.Integer)
    
    # associated_coursePlan = db.relationship('CoursePlan', back_populates='students', overlaps="coursePlan")
    # associated_course = db.relationship('Course', back_populates='planIds', overlaps="courses")

    def __init__(self, plan, courseCode):
        self.planId = plan
        self.code = courseCode
        self.plan_option = plan
        

    def get_json(self):
        return{
            'Course Plan ID': self.planId,
            'Course': self.code
        }

