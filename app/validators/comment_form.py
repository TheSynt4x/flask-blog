from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class EditCommentForm(FlaskForm):
  comment = TextAreaField(
    label='Comment',
    validators=[
      DataRequired(message='Post content is required.'),
      Length(
        max=200,
        message='Comment length has to be 200 characters long.',
      ),
    ],
  )

  submit = SubmitField(label='Post')
