from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired


class InputIntValidator:
    def __init__(self):
        self.message = "Tiedot positiivisina kokonaislukuina!"


    def __call__(self, form, field):
        # print(field.data)
        try:
            if int(field.data) <=0:
                raise ValidationError(self.message)
        except ValueError:
            raise ValidationError(self.message)



class TripDataForm(FlaskForm):
    car = RadioField('Auton tyyppi*', choices=[('A', "carA.png"), ('B', 'carB.png'), ('C', 'carC.png')], validators=[DataRequired()])
    dist = StringField('Matkan pituus km*', validators=[DataRequired(), InputIntValidator()])
    speed1 = StringField('Käytetty keskinopeus 1*', validators=[DataRequired(), InputIntValidator()])
    speed2 = StringField('Käytetty keskinopeus 2*', validators=[DataRequired(), InputIntValidator()])
    submit = SubmitField('Laske')
