from ..extensions import db

class Note(db.Model):
    
    __tablename__ = 'notes'  # match your actual table name

    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)