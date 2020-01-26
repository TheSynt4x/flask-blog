from app import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String(255), nullable=False)

  def __init__(self, username, password):
    self.username = username
    self.password = password

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
    return cls.query.filter_by(id=user_id).first()

  @classmethod
  def create(cls, username, password):
    """
    Create a new user

    Args:
      username: user input
      password: user input

    Returns:
      A newly created user
    """
    user = cls(username=username, password=generate_password_hash(password + username))

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

  def to_dict(self):
    return dict(id=self.id, username=self.username)
