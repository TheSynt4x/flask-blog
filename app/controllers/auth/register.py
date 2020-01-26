import os
import uuid

from flask import render_template, flash, redirect, url_for, current_app as app, request
from flask.views import MethodView
from werkzeug import secure_filename

from app.middleware import auth
from app.models.user import User
from app.validators.register_form import RegisterForm


class RegisterController(MethodView):
  @auth.optional
  def get(self):
    return render_template('auth/register.html', form=RegisterForm())

  @auth.optional
  def post(self):
    form = RegisterForm()

    if form.validate_on_submit():
      form.validate_username(form.username)

      unique_filename = ''

      if 'avatar' in request.files and request.files['avatar']:
        file = secure_filename(form.avatar.data.filename)
        extension = os.path.splitext(file)[1]

        unique_filename = str(uuid.uuid4()) + extension

        form.avatar.data.save(os.path.join(
          app.static_folder, 'images', unique_filename
        ))

      avatar = unique_filename if 'avatar' in request.files and request.files['avatar'] else 'no-image.png'

      User.create(form.username.data, form.password.data, avatar)

      flash('Your account has been created. You may now login.', 'info')

      return redirect(url_for('login'))

    return render_template('auth/register.html', form=form)
