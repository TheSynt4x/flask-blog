from flask import render_template
from flask.views import MethodView


class PostController(MethodView):
  def get(self, post_id):
    return render_template('blog/show.html')


class EditPostController(MethodView):
  def get(self):
    pass
