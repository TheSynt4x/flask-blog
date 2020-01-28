from datetime import datetime

import pytz

from app import db


class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer(), primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  content = db.Column(db.Text(), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
  category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'), nullable=False)
  comments = db.relationship('Comment', backref='post', lazy='dynamic')

  posted_at = db.Column(
    db.TIMESTAMP,
    nullable=False,
    default=datetime.now(tz=pytz.timezone("Europe/Stockholm")),
  )

  def __repr__(self):
    return '<Post %r>' % self.id

  @classmethod
  def create(cls, title, post_content, user_id, category_id):
    """
    Create a new post

    Args:
      title: the post title
      post_content: post content
      user_id: the user who posted it
      category_id: what category the post is in

    Returns:
      A newly created post
    """
    post = cls(title=title, content=post_content, user_id=user_id, category_id=category_id)
    db.session.add(post)
    db.session.commit()

    return post

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

  @classmethod
  def search(cls, query, page, per_page):
    """
    Get all posts matching the search query

    Args:
      page: current page
      per_page: results per page
      query: specified query for searching

    Returns:
      A list of posts that match the search query
    """
    return cls.query.filter(cls.title.like('%{0}%'.format(query))).paginate(page, per_page, True)

  @classmethod
  def delete_by_id(cls, post_id):
    """
    Delete a post by id

    Args:
      post_id: the post to be deleted

    Returns:
      void
    """
    post = cls.get_by_id(post_id)

    for comment in post.comments:
      db.session.delete(comment)

    db.session.delete(cls.get_by_id(post_id))
    db.session.commit()

  def paginate_comments(self, page, per_page):
    """
    Paginate through a post's comments

    Args:
      page: current page
      per_page: amount of results per page

    Returns:
      A paginated object of comments
    """

    return self.comments.paginate(page, per_page)

  def update(self, title, content, category_id):
    """
    Update a post and its values

    Args:
      title: new title
      content: new content
      category_id: a new category

    Returns:
      void
    """
    self.title = title
    self.content = content
    self.category_id = category_id

    db.session.commit()

  def to_dict(self):
    """
    Create a dictionary with table columns

    Returns:
      dict
    """
    return dict(title=self.title, content=self.content, posted_at=self.posted_at)
