from flask import current_app, render_template
from flask.views import MethodView


class LoginController(MethodView):
  def get(self):
    return render_template('auth/login.html')

  def post(self):
    pass
