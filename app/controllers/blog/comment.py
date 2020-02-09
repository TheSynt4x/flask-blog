from flask import request, redirect, url_for, session, flash, render_template
from flask.views import MethodView

from app import db
from app.middleware import auth
from app.models.comment import Comment
from app.models.post import Post
from app.validators.comment_form import EditCommentForm


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
    return render_template(
      'blog/comments/edit.html',
      comment=Post.get_by_comment(post_id, comment_id),
      form=EditCommentForm(),
    )

  @auth.required
  def post(self, post_id, comment_id):
    comment = Post.get_by_comment(post_id, comment_id)

    form = EditCommentForm()

    if form.validate_on_submit():
      comment.comment = form.comment.data
      db.session.commit()

      flash('Your comment has been updated.', 'info')

      return redirect(url_for('blog.post', post_id=post_id))

    return render_template('blog/comments/edit.html', comment=comment, form=form)


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
