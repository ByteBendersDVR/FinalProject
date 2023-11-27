from App.models import User  
from App.database import db

class Student(User):
    id = db.Column(db.ForeignKey('user.id'), primary_key=True)
    student_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    program_id = db.Column(db.ForeignKey('program.id'))
    
    associated_program = db.relationship('Program', back_populates='students', overlaps="program")
    courses = db.relationship('StudentCourseHistory', backref='student', lazy=True)
    
    __mapper_args__ = {
        "polymorphic_identity": "student"
    }

    def __init__(self, student_id, username, password, name, program_id):
        super().__init__(username, password)
        self.student_id = student_id
        self.name = name
        self.program_id = program_id

    def get_json(self):
        return{'student_id': self.id,
            'name': self.name,
            'program' : self.program_id
            
        }

