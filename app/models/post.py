from datetime import datetime
import pytz
from app import db


class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer(), primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  content = db.Column(db.Text(), nullable=False)
  category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'), nullable=False)

  posted_at = db.Column(
    db.DateTime,
    nullable=False,
    default=datetime.now(tz=pytz.timezone("Europe/Stockholm")),
  )

  def __repr__(self):
    return '<Post %r>' % self.id

  @classmethod
  def all(cls):
    """
    Get all posts

    Returns:
      A list of posts
    """
    return cls.query.all()

  @classmethod
  def paginate(cls, page=1, per_page=5):
    """
    Paginate through all posts

    Args:
      page: current page
      per_page: how many items displayed per page

    Returns:
      A paginated object
    """
    return cls.query.order_by(cls.posted_at.desc()).paginate(page, per_page, False)

  @classmethod
  def get_by_id(cls, post_id):
    """
    Get a post by id

    Args:
      post_id: specified post id

    Returns:
      The first post that matches by id
    """
    return cls.query.filter_by(id=post_id).first_or_404()

  @classmethod
  def get_recent_posts(cls, limit=5):
    """
    Get all latest posts with a limit

    Args:
      limit: the limit of results to be displayed

    Returns:
      A list of posts with the specified limit
    """
    return cls.query.order_by(cls.posted_at.desc()).limit(limit).all()

  def to_dict(self):
    """
    Create a dictionary with table columns

    Returns:
      dict
    """
    return dict(title=self.title, content=self.content, posted_at=self.posted_at)
