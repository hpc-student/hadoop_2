from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
#from project.models import User


class HadoopForm(FlaskForm):
    javaClass = StringField('class', validators=[DataRequired(), Length(min=1, max=100)])
    dataInput = StringField('input', validators=[DataRequired(), Length(min=1, max=100)])
    dataOutput = StringField('output', validators=[DataRequired(), Length(min=1, max=100)])
    #confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('start job')
'''
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
'''
#    def validate_output(self,dataInput):


'''
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
'''
