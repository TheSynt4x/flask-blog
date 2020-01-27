from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class ChangePasswordForm(FlaskForm):
  current_password = PasswordField(
    label='Current Password',
    validators=[
      DataRequired(message='Current password cannot be blank.'),
      Length(
        min=8,
        max=100,
        message='Password is either too short or too long. Try again.'
      ),
    ]
  )

  new_password = PasswordField(
    label='New Password',
    validators=[
      DataRequired(message='New password cannot be blank.'),
      Length(
        min=8,
        max=100,
        message='New Password is either too short or too long. Try again.',
      ),
      EqualTo(
        fieldname='confirm_new_password',
        message='Passwords must match.'
      )
    ]
  )
  confirm_new_password = PasswordField(
    label='Confirm New Password',
    validators=[
      DataRequired(message='Current password cannot be blank.'),
      Length(
        min=8,
        max=100,
        message='Password is either too short or too long. Try again'
      ),
      EqualTo(
        fieldname='new_password',
        message='Passwords must match'
      )
    ]
  )

  submit = SubmitField(label='Change')
