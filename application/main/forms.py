from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User
from application import db

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=2)])
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=2)])
    username = StringField('pseudo_', validators=[DataRequired(), Length(min=2)])
    profession = SelectField('professional_background', choices=[('software', 'Software Developer'),
                                        ('devops', 'Devops')], 
                                        validators=[DataRequired()], default='software')
    date_of_birth = DateField('Year of Birth', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(min=2)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=2), EqualTo('password', message="passwords must match")])
    submit = SubmitField('Submit')

    # custom validation to remove intergrity error
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username is taken, please choose another!')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is taken, please choose another!')
        

