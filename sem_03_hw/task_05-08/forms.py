from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^(?=.*?[a-zA-Z])(?=.*?[0-9]).{8,}$',
                                                                            message='Password should contain at least '
                                                                                    'one letter and one digit')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    agreement = BooleanField('Consent to personal data processing', default=True, validators=[DataRequired()])
