from pybo import db

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gubun = db.Column(db.String(10), nullable=False)
    service = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    roc = db.Column(db.String(100), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id',ondelete='CASCADE'))
    list = db.relationship('List', backref=db.backref('comments_set',cascade='all, delete-orphan' ))
    comment = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)