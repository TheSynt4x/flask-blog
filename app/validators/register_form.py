from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from app.models.user import User


class RegisterForm(FlaskForm):
  username = StringField(
    label='Username',
    validators=[
      DataRequired(message='Username is required.'),
      Length(
        min=4,
        max=15,
        message='Username is either too short or too long.',
      ),
    ],
  )

  password = PasswordField(
    label='Password',
    validators=[
      DataRequired(message='Password is required.'),
      Length(
        min=8,
        max=100,
        message='Password is either too short or too long.',
      ),
      EqualTo(
        fieldname='confirm_password',
        message='Passwords do not match.',
      )
    ],
  )

  confirm_password = PasswordField(
    label='Confirm Password',
    validators=[
      DataRequired(message='Confirm password is required.'),
      EqualTo(fieldname='password', message='Passwords do not match.')
    ],
  )

  submit = SubmitField(label='Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()

    if user is not None:
      raise ValidationError('That username is already taken.')
