from flask import render_template
from flask.views import MethodView


class RegisterController(MethodView):
  def get(self):
    return render_template('auth/register.html')

  def post(self):
    pass
