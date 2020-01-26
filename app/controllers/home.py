from flask import render_template, request
from flask.views import MethodView

from app.models.post import Post


class HomeController(MethodView):
  def get(self):
    """
    Displays a home page with a list of posts.

    Returns:
      Home template with dynamic posts
    """
    page = request.args.get('page', 1, type=int)
    per_page = 5

    return render_template('home.html', posts=Post.paginate(page, per_page))
