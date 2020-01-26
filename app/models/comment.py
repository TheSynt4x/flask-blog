from app import db
import pytz
from datetime import datetime


class Comment(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key=True)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  comment = db.Column(db.Text(), nullable=False)
  posted_at = db.Column(
    db.TIMESTAMP,
    nullable=False,
    default=datetime.now(tz=pytz.timezone("Europe/Stockholm")),
  )

  def __init__(self, user_id, post_id, comment):
    self.user_id = user_id
    self.post_id = post_id
    self.comment = comment

  def __repr__(self):
    return '<Comment %r>' % self.id
