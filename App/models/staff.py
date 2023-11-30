from .user import User 
from App.database import db

class Staff(User):

    
    id = db.Column(db.String(10), db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(50))
    
    __mapper_args__ = {
        "polymorphic_identity": "staff"
    }

    def __init__(self, username, password, name):
        super().__init__(username, password)
        self.name = name

    def get_json(self):
        return super().get_json()

