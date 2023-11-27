from App.database import db

class CoursePlanGenerator(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    strategy = db.Column(db.ForeignKey("strategy.id"))
    
    __init__(self, strategy):
        self.strategy = strategy
        