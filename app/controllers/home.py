from flask import render_template
from flask.views import MethodView


class HomeController(MethodView):
  def get(self):
    return render_template('home.html')
