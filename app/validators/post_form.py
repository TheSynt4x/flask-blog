from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
  title = StringField(
    label='Title',
    validators=[
      DataRequired(message='Post title is required.'),
      Length(min=4, max=40, message='Post title is either too long or too short.'),
    ]
  )

  post_content = TextAreaField(
    label='Post content',
    validators=[
      DataRequired(message='Post content is required.'),
      Length(
        min=20,
        max=2000,
        message='Content length has to be between 20 and 2000 characters long.',
      ),
    ],
  )

  submit = SubmitField(label='Post')


