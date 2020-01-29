from flask import request, redirect, url_for, session, flash
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


class EditCommentController(MethodView):
  @auth.required
  def get(self, post_id, comment_id):
    return 'ok'

  @auth.required
  def post(self, post_id, comment_id):
    pass


class DeleteCommentController(MethodView):
  @auth.required
  def get(self, post_id, comment_id):
    is_deleted = Comment.delete_by_id(post_id, comment_id, self.user.id)

    if is_deleted:
      flash('Your comment has been successfully deleted.', 'success')
      return redirect(url_for('blog.post', post_id=post_id))
    else:
      flash('That is not your comment.', 'error')
      return redirect(url_for('blog.post', post_id=post_id))
