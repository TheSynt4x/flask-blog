from flask import render_template, request, flash, redirect, url_for, session
from flask.views import MethodView

from app.models.user import User


class LoginController(MethodView):
  def get(self):
    return render_template('auth/login.html')

  def post(self):
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.authenticate(username, password)

    if not user:
      flash('Invalid credentials. Please try again.', 'error')
      return redirect(url_for('login'))

    session['user_id'] = user.id

    flash('You have been logged in.', 'success')

    return redirect(url_for('home'))
