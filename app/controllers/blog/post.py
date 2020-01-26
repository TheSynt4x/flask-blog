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
    page = request.args.get('page', 1, type=int)
    per_page = 5

    post = Post.get_by_id(post_id)
    comments = post.paginate_comments(page, per_page)

    return render_template('blog/show.html', post=post, comments=comments)


class EditPostController(MethodView):
  def get(self):
    pass
