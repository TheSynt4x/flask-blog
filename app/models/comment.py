from app import db


class Comment(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key=True)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  comment = db.Column(db.Text(), nullable=False)
  posted_at = db.Column(
    db.TIMESTAMP,
    nullable=False,
    default=db.func.current_timestamp(),
  )

  def __init__(self, user_id, post_id, comment):
    self.user_id = user_id
    self.post_id = post_id
    self.comment = comment

  def __repr__(self):
    return '<Comment %r>' % self.id

  @classmethod
  def get_by_post(cls, post_id, comment_id):
    """
    Get a comment by post id and comment id

    Args:
      post_id: the post comment belongs to
      comment_id: comment id

    Returns:
      Retrieved comment or 404 if not found.
    """
    return cls.query.filter_by(post_id=post_id).filter_by(id=comment_id).first_or_404()

  @classmethod
  def delete_by_id(cls, post_id, comment_id, user_id):
    """
    Delete a comment by post id and comment id

    Args:
      user_id:
      post_id: the post comment belongs to
      comment_id: comment id

    Returns:
      boolean
    """
    comment = cls.get_by_post(post_id, comment_id)

    if comment.user_id == user_id:
      db.session.delete(cls.get_by_post(post_id, comment_id))
      db.session.commit()
      return True
    else:
      return False
