from app import db
from datetime import datetime


class Condenser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.String())    
    length = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    fan = db.Column(db.String(128))
    number_fan = db.Column(db.Integer)
    air_flow = db.Column(db.Integer)
    noise = db.Column(db.Integer)
    low_noise = db.Column(db.Boolean)
    img_url_1 = db.Column(db.String(128))
    img_url_2 = db.Column(db.String(128))
    capacity_ = db.relationship('Capacity', backref='condenser')

class Capacity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condenser_id = db.Column(db.Integer, db.ForeignKey('condenser.id'))
    max_temp = db.Column(db.Integer)
    min_temp = db.Column(db.Integer)
    capacity_point = db.Column(db.Float)
    delta_temp = db.Column(db.Integer)
    check_name = db.Column(db.String(128), unique=True, )
    

class New_Capacity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condenser_id = db.Column(db.Integer, db.ForeignKey('condenser.id'))
    max_temp = db.Column(db.Integer)
    min_temp = db.Column(db.Integer)
    capacity_point = db.Column(db.Float)
    delta_temp = db.Column(db.Integer)
   
    