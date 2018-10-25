from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    usernum = StringField('UserNumber', validators=[DataRequired()])
    usercity = StringField('UserCity', validators=[DataRequired()])
    submit = SubmitField('Join')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
