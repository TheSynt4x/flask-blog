from flask import redirect, url_for, session, flash
from flask.views import MethodView

from app.middleware import auth


class LogoutController(MethodView):
  @auth.required
  def get(self):
    """
    Logout a user

    Returns:
      Flask Response
    """
    session.pop('user_id', 0)

    flash('You have been logged out', 'success')
    return redirect(url_for('home'))
