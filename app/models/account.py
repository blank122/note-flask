from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Account(db.Model):
    
    __tablename__ = 'accounts'  # match your actual table name

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)