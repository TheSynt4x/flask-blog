from flask import request, redirect, url_for, session
from flask.views import MethodView

from app import db
from app.middleware import auth
from app.models.comment import Comment
from app.models.post import Post


class CommentController(MethodView):
  @auth.required
  def post(self, post_id):
    """
    Create a new comment for a post

    Args:
      post_id: specified post

    Returns:
      Flask response
    """
    comment = request.form.get('comment')

    post = Post.get_by_id(post_id)
    post.comments.append(Comment(session.get('user_id'), post.id, comment))

    db.session.commit()

    return redirect(url_for('blog.post', post_id=post_id))
