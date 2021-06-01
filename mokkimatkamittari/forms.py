from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, ValidationError, InputRequired


class InputIntValidator:
    def __init__(self):
        self.message = None


    def __call__(self, form, field):
        # print(field.data)
        try:
            tst = int(field.data)
        except ValueError:
            raise ValidationError("Anna tiedot kokonaislukuina!")
        if tst <=0 or tst > 10000:
            raise ValidationError('Sallitut arvot 1 - 10000 !')



class TripDataForm(FlaskForm):
    car = RadioField('Auton tyyppi*', choices=[('A', "carA.png"), ('B', 'carB.png'), ('C', 'carC.png')], validators=[DataRequired('Valitse automalli!')])
    dist = StringField('Matkan pituus km*', validators=[DataRequired('Syötä matkan pituus'), InputIntValidator()])
    speed1 = StringField('Käytetty keskinopeus 1*', validators=[DataRequired('Syötä nopeus 1'), InputIntValidator()])
    speed2 = StringField('Käytetty keskinopeus 2*', validators=[DataRequired('Syötä nopeus 2'), InputIntValidator()])
    submit = SubmitField('Laske')
