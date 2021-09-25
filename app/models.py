from app import db


class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.String())    
    price = db.Column(db.Float)
    transmission = db.Column(db.Boolean)
    img_url_1 = db.Column(db.String(128))
    img_url_2 = db.Column(db.String(128))
    img_url_3 = db.Column(db.String(128))
    img_url_4 = db.Column(db.String(128))
    in_rent_or_free = db.Column(db.Boolean, default=False)