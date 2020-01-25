from app import db


class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  content = db.Column(db.Text(), nullable=False)

  def __repr__(self):
    return '<Post %r>' % self.id

  @classmethod
  def all(cls):
    return cls.query.all()

  def to_dict(self):
    return dict(title=self.title, content=self.content)