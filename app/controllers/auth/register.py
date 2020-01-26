from flask import render_template, flash, redirect, url_for
from flask.views import MethodView

from app.validators.register_form import RegisterForm
from app.models.user import User


class RegisterController(MethodView):
  def get(self):
    return render_template('auth/register.html', form=RegisterForm())

  def post(self):
    form = RegisterForm()

    if form.validate_on_submit():
      form.validate_username(form.username)

      User.create(form.username.data, form.password.data)

      flash('Your account has been created. You may now login.', 'info')

      return redirect(url_for('login'))

    return render_template('auth/register.html', form=form)
