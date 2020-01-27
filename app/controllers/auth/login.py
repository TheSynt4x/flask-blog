from flask import render_template, request, flash, redirect, url_for, session
from flask.views import MethodView

from app.middleware import auth
from app.models.user import User


class LoginController(MethodView):
  @auth.optional
  def get(self):
    """
    Renders the login template

    Returns:
      The login template
    """
    return render_template('auth/login.html')

  @auth.optional
  def post(self):
    """
    Processes the POST request and checks if credentials match against the database

    Returns:
      A redirect
    """
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.authenticate(username, password)

    if not user:
      flash('Invalid credentials. Please try again.', 'error')
      return redirect(url_for('login'))

    session['user_id'] = user.id

    flash('You have been logged in.', 'success')

    return redirect(url_for('home'))
