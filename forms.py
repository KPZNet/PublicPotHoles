from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm ( FlaskForm ) :
    name = StringField ( "Name: ", validators=[DataRequired ()] )
    email = StringField ( "Email: ", validators=[Email ()] )
    message = TextAreaField ( "Message", validators=[DataRequired ()] )
    submit = SubmitField ( "Submit" )


class ContactFormXY ( FlaskForm ) :
    name = StringField ( "Name: ", validators=[DataRequired ()] )
    email = StringField ( "Email: ", validators=[Email ()] )
    message = TextAreaField ( "Message", validators=[DataRequired ()] )
    submit = SubmitField ( "Submit" )

class AEPotHoleForm ( FlaskForm ) :
    streetAddress = StringField ( "Street:", validators=[DataRequired ()] )
    district = StringField ( "District:", validators=[DataRequired ()] )
    location = StringField ( "Location:", validators=[DataRequired ()] )
    severity = StringField ( "Severity:", validators=[DataRequired ()] )
    size = StringField ( "Size:", validators=[DataRequired ()] )
    submit = SubmitField ( "Submit" )

