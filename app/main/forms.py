from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField, SelectField, RadioField, StringField, PasswordField, BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms.validators import Required

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
