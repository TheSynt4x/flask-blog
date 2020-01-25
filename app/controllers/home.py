from flask import render_template
from flask.views import MethodView

from app.models.post import Post


class HomeController(MethodView):
  def get(self):
    return render_template('home.html', posts=Post.all())
