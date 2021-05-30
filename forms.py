from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired


# class InputValidator:
#     def __init__(self):
#         self.message = "Anna tiedot kokonaislukuina!"
#
#
#     def __call__(self, form, field):
#         print(field.data)
#         try:
#             int(field.data)
#         except ValueError:
#             raise ValidationError(self.message)


class TripDataForm(FlaskForm):
    car = RadioField('Auto*', choices=[('A', '- S'), ('B', '- M'), ('C', '- L')])  #, validators=[DataRequired()])
    dist = StringField('Matkan pituus km*', validators=[DataRequired('Täytä tämä kenttä')])  #, InputValidator()])
    speed1 = StringField('Käytetty keskinopeus 1*', validators=[DataRequired('Täytä tämä kenttä')])  #, InputValidator()])
    speed2 = StringField('Käytetty keskinopeus 2*', validators=[DataRequired('Täytä tämä kenttä')])  #, InputValidator()])
    submit = SubmitField('Laske')

