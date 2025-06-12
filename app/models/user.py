from ..extensions import db

class User(db.Model):
    
    __tablename__ = 'users'  # match your actual table name

    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), unique=True, nullable=False)
    last_name = db.Column(db.String(500), nullable=False)
    birthdate = db.Column(db.DateTime)

    # notes = db.relationship('Note', backref='owner', lazy=True)
