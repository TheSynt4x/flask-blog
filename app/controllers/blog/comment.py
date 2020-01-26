from app import db
from flask import request, redirect, url_for, session
from flask.views import MethodView

from app.models.post import Post
from app.models.comment import Comment


class CommentController(MethodView):
  def post(self, post_id):
    comment = request.form.get('comment')

    post = Post.get_by_id(post_id)
    post.comments.append(Comment(session.get('user_id'), post.id, comment))

    db.session.commit()

    return redirect(url_for('blog.post', post_id=post_id))
