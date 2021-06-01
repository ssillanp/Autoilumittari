from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired


class InputIntValidator:
    def __init__(self):
        self.message = "Anna tiedot positiivisina kokonaislukuina!"


    def __call__(self, form, field):
        # print(field.data)
        try:
            if int(field.data) <=0:
                raise ValidationError(self.message)
        except ValueError:
            raise ValidationError(self.message)



class TripDataForm(FlaskForm):
    car = RadioField('Auton tyyppi*', choices=[('A', "carA.png"), ('B', 'carB.png'), ('C', 'carC.png')], validators=[DataRequired('Valitse automalli!')])
    dist = StringField('Matkan pituus km*', validators=[DataRequired('Syötä matkan pituus'), InputIntValidator()])
    speed1 = StringField('Käytetty keskinopeus 1*', validators=[DataRequired('Syötä nopeus 1'), InputIntValidator()])
    speed2 = StringField('Käytetty keskinopeus 2*', validators=[DataRequired('Syötä nopeus 2'), InputIntValidator()])
    submit = SubmitField('Laske')
