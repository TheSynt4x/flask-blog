from app import db


class Comment(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key=True)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  comment = db.Column(db.Text(), nullable=False)

  def __init__(self, user_id, post_id, comment):
    self.user_id = user_id
    self.post_id = post_id
    self.comment = comment

  def __repr__(self):
    return '<Comment %r>' % self.id

  @classmethod
  def create(cls, user_id, post_id, comment):
    """
    Create a new comment

    Args:
      user_id: logged in user id
      post_id: current post
      comment: the actual comment

    Returns:
      A newly created comment
    """
    comment = cls(user_id, post_id, comment)

    db.session.add(comment)
    db.session.commit()

    return comment

  @classmethod
  def paginate(cls, page, per_page):
    """
    Paginate comments for a post

    Args:
      page: current page
      per_page: results per page

    Returns:
      A paginated object of comments
    """
    return cls.query.order_by(cls.posted_at.desc()).paginate(page, per_page, False)
