from app import db

class OPIncome(db.Model):
    __tablename__ = 'opincome'
    __table_args__ = {'schema': 'kb_datamining'}
    hospitalno = db.Column(db.String(30), primary_key=True)
    hospitalname = db.Column(db.String(60))
    statisticsdate = db.Column(db.DateTime, primary_key=True)
    deptcode = db.Column(db.String(40), primary_key=True)
    deptname = db.Column(db.String(80))
    deptcodeleve1 = db.Column(db.String(40))
    deptnameleve1 = db.Column(db.String(80))
    chargecategorycode = db.Column(db.String(10))
    chargecategoryname = db.Column(db.String(80))
    ybname = db.Column(db.String(20))
    totalmoney = db.Column(db.Numeric)
    zdtotalmoney = db.Column(db.Numeric)
    zdhctotalmoney = db.Column(db.Numeric)



