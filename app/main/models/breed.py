from .. import db
from app.main.models import specie

class Breed(db.Model):
    __tablename__ = "breed"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    breed_name = db.Column(db.String(100), unique=True)
    
    specie_id = db.Column(db.String, db.ForeignKey("specie.public_id"), nullable=False)

    def __repr__(self):
        return "<breed '{}'>".format(self.breed_name)