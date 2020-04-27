from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class QuizSubmitForm(FlaskForm):
    question = StringField('question', validators=[DataRequired()])
    AOption = StringField('AOption', validators=[DataRequired()])
    BOption = StringField('BOption', validators=[DataRequired()])
    COption = StringField('COption')
    DOption = StringField('DOption')
    Answer = StringField('Answer', validators=[DataRequired()])
    category = StringField('category')
    quizId = StringField('quizId')
    submit = SubmitField('submit')
    
	   
class QuestionForm(FlaskForm):
    username = StringField('username')
    team = StringField('team')
    question ="["",""],["",""]"
    question = StringField('question')
    optiona = RadioField('optiona')
    optionb = RadioField('optionb')
    optionc = RadioField('optionc')
    optiond = RadioField('optiond')

class CategoryForm(FlaskForm):
    techincal = SelectField('techincal')
    about_dailmer = SelectField('about_daimler') 
    cloud = SelectField('cloud')     
    


    
    
    
    
    
