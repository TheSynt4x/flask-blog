from flask import current_app as app

from app.models.category import Category
from app.models.post import Post

from datetime import datetime

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


@app.template_filter('humanize')
def humanize_time(time):
  """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
  now = datetime.now()
  diff = now - time
  second_diff = diff.seconds
  day_diff = diff.days

  if day_diff < 0:
    return ''

  if day_diff == 0:
    if second_diff < 10:
      return "just now"
    if second_diff < 60:
      return str(int(second_diff)) + " seconds ago"
    if second_diff < 120:
      return "a minute ago"
    if second_diff < 3600:
      return str(int(second_diff / 60)) + " minutes ago"
    if second_diff < 7200:
      return "an hour ago"
    if second_diff < 86400:
      return str(int(second_diff / 3600)) + " hours ago"
  if day_diff == 1:
    return "yesterday"
  if day_diff < 7:
    return str(day_diff) + " days ago"
  if day_diff < 31:
    return str(int(day_diff / 7)) + " weeks ago"
  if day_diff < 365:
    return str(int(day_diff / 30)) + " months ago"
  return str(int(day_diff / 365)) + " years ago"

