from flask_sqlalchemy import SQLAlchemy

Default_Image="https://pawedin.com/system/pets/default_images/default_pet.jpg"

db = SQLAlchemy()

### MODELS GO BELOW!

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ PetModel """
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    species = db.Column(db.Text,nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
    def image_url(self):
        """return pic submitted or default"""
        return self.photo_url or Default_Image

def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)