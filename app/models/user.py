from app import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String(255), nullable=False)
  avatar = db.Column(db.String(255), nullable=False, default='no-image.png')
  posts = db.relationship('Post', backref='user', lazy='dynamic')
  comments = db.relationship('Comment', backref='user', lazy='dynamic')

  def __init__(self, username, password, avatar):
    self.username = username
    self.password = password
    self.avatar = avatar

  def __repr__(self):
    return '<User %r>' % self.username

  @classmethod
  def get_by_id(cls, user_id):
    """
    Get a user by id

    Args:
      user_id: user's id

    Returns:
       The retrieved user
    """
    return cls.query.filter_by(id=user_id).first_or_404()

  @classmethod
  def get_by_username(cls, username):
    """
    Get a user by username

    Args:
      username: user's username

    Returns:
      The retrieved user
    """
    return cls.query.filter_by(username=username).first_or_404()

  @classmethod
  def create(cls, username, password, avatar):
    """
    Create a new user

    Args:
      username: user input
      password: user input
      avatar: user's avatar

    Returns:
      A newly created user
    """
    user = cls(username=username, password=generate_password_hash(password + username), avatar=avatar)

    db.session.add(user)
    db.session.commit()

    return user

  @classmethod
  def authenticate(cls, username, password):
    """
    Authenticate a user.

    Args:
      username: user input
      password: user input

    Returns:
      bool
    """
    user = cls.query.filter_by(username=username).first()

    if user:
      if check_password_hash(user.password, password + username):
        return user

    return False

  def change_password(self, new_password):
    """
    Change user password

    Args:
      new_password: the new password

    Returns:
      void
    """
    self.password = generate_password_hash(new_password + self.username)
    db.session.commit()

  def change_avatar(self, new_avatar):
    """
    Change user avatar

    Args:
      new_avatar: the uploaded avatar

    Returns:
      void
    """
    self.avatar = new_avatar
    db.session.commit()

  def to_dict(self):
    return dict(id=self.id, username=self.username)
