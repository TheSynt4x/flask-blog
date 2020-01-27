from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed, DataRequired


class AvatarForm(FlaskForm):
  avatar = FileField(
    label='Avatar',
    validators=[
      FileAllowed({'png', 'jpg', 'jpeg', 'gif'})
    ]
  )

  submit = SubmitField(label='Change')
