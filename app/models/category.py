from app import db


class Category(db.Model):
  __tablename__ = 'categories'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  description = db.Column(db.Text(), nullable=False)
  posts = db.relationship('Post', backref='category', lazy='dynamic')

  def __repr__(self):
    return '<Category %r>' % self.name

  @classmethod
  def all(cls):
    """
    Get all categories

    Returns:
      A list of categories
    """
    return cls.query.all()

  @classmethod
  def get_by_id(cls, category_id):
    """
    Get a category by id

    Args:
      category_id: the specified category id

    Returns:
      The first category that matches by id
    """
    return cls.query.filter_by(id=category_id).first_or_404()

  @classmethod
  def limit(cls, limit=5):
    """
    Get a certain amount of categories

    Args:
      limit: specified limit of results

    Returns:
    A list of retrieved categories
    """
    return cls.query.limit(limit).all()

  @classmethod
  def get_posts(cls, category_id, page, per_page):
    """
    Get posts for a specific category

    Args:
      category_id: specified category
      page: current page
      per_page: results per page

    Returns:
      dict
    """
    category = cls.get_by_id(category_id)

    return dict(category=category, posts=category.posts.paginate(page, per_page, True))
