from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Email, Optional

class AddPetForm(FlaskForm):
    name = StringField("Pet's Name",validators=[
        InputRequired(message="Dog's name can't be blank")])
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )
    photo_url = StringField("Pet's Photo URL",validators=[Optional()])
    age = IntegerField("Age",validators=[Optional()])
    notes = StringField("Note",validators=[Optional()])
    available = BooleanField("Still Available?",validators=[
        InputRequired(message="Availability can't be left blank")])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    name = StringField("Pet's Name",validators=[
        InputRequired(message="Dog's name can't be blank")])

    photo_url = StringField(
        "Photo URL",
        validators=[Optional()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional()],
    )

    available = BooleanField("Still Available?")