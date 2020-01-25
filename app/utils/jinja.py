from flask import current_app as app

from app.models.category import Category
from app.models.post import Post


@app.context_processor
def site_globals():
  return dict(title=app.config['APP_TITLE'], base_url=app.config['BASE_URL'])


@app.context_processor
def utility_processor():
  def recent_posts():
    return Post.get_recent_posts(5)

  def categories():
    return Category.limit(5)

  return dict(recent_posts=recent_posts, categories=categories)
