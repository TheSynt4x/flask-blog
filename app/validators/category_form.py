from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
  name = StringField(
    label='Category name',
    validators=[
      DataRequired(message='Category name is required.'),
      Length(
        min=4,
        max=20,
        message='Category name must be between 4 and 20 characters long.',
      )
    ],
  )

  description = TextAreaField(
    label='Category description',
    validators=[
      DataRequired(message='Category description is required..'),
      Length(
        min=20,
        max=200,
        message='Description must be between 20 and 200 characters long.',
      ),
    ],
  )

  submit = SubmitField(label='Create')
