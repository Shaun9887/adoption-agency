from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, Length


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
