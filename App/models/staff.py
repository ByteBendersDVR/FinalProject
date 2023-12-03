from .user import User 
from App.database import db

class Staff(User):

    id = db.Column(db.ForeignKey('user.id'), primary_key=True)
    staff_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    
    __mapper_args__ = {
        "polymorphic_identity": "staff"
    }

    def __init__(self, staff_id, username, password, name):
        super().__init__(username, password)
        self.name = name
        self.staff_id = staff_id

    def get_json(self):
        return super().get_json()

