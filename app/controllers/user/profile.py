from flask import render_template
from flask.views import MethodView

from app.models.user import User


class ProfileController(MethodView):
  def get(self, username):
    """
    Displays a profile page with the requested user

    Args:
      username: requested user

    Returns:
      A template with retrieved user data
    """
    return render_template('auth/profile.html', user=User.get_by_username(username))
