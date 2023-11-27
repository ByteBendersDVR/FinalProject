from App.database import db
from .strategy import Strategy

class CoursePlanGenerator(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    strategy = db.Column(db.Integer, db.ForeignKey("Strategy.id"))
    
    # __init__(self, strategy):
    #     self.strategy = strategy
        