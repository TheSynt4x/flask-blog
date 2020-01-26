from flask import render_template, request
from flask.views import MethodView

from app.models.post import Post


class PostController(MethodView):
  def get(self, post_id):
    """
    Display a single post based on the id

    Args:
      post_id: the specified post id

    Returns:
      Single blog template with a dynamic post
    """
    return render_template('blog/show.html', post=Post.get_by_id(post_id))


class EditPostController(MethodView):
  def get(self):
    pass
