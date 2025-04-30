from app import db

class Ejksdzb(db.Model):
    __tablename__ = 'ejksdzb'
    hospitalno = db.Column(db.String(30), primary_key=True)
    hospitalname = db.Column(db.String(60))
    deptcodelevel2 = db.Column(db.String(20))
    deptnamelevel2 = db.Column(db.String(60))
    deptcodelevel1 = db.Column(db.String(20))
    deptcodelevel1 = db.Column(db.String(60))
    bz = db.Column(db.String(20))
    isdeleted = db.Column(db.Integer)
    sj = db.Column(db.DateTime)