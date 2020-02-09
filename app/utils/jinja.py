from datetime import datetime

from flask import current_app as app, session, url_for, request

from app.models.category import Category
from app.models.post import Post
from app.models.user import User


@app.context_processor
def site_globals():
  return dict(title=app.config['APP_TITLE'], base_url=app.config['BASE_URL'])


def url_for_other_page(page, **kwargs):
  """
  Creates a url_for link with existing url parameters

  Args:
    page: page query parameter
    **kwargs: more query parameters

  Returns:
    A url_for links with the wished query parameters.
  """
  args = request.view_args.copy()
  args['page'] = page

  new_args = {**kwargs, **args}

  return url_for(request.endpoint, **new_args)


app.jinja_env.globals['url_for_other_page'] = url_for_other_page


@app.context_processor
def utility_processor():
  def recent_posts():
    return Post.get_recent_posts(5)

  def categories():
    return Category.limit(5)

  def current_user():
    if session.get('user_id'):
      return User.get_by_id(session.get('user_id'))
    return False

  return dict(recent_posts=recent_posts, categories=categories, current_user=current_user)


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
      return str(int(second_diff)) + " second{0} ago".format('s' if int(second_diff) > 1 else '')
    if second_diff < 120:
      return "a minute ago"
    if second_diff < 3600:
      return str(int(second_diff / 60)) + " minute{0} ago".format('s' if int(second_diff / 60) > 1 else '')
    if second_diff < 7200:
      return "an hour ago"
    if second_diff < 86400:
      return str(int(second_diff / 3600)) + " hour{0} ago".format('s' if int(second_diff / 3600) > 1 else '')
  if day_diff == 1:
    return "yesterday"
  if day_diff < 7:
    return str(day_diff) + " days ago"
  if day_diff < 31:
    return str(int(day_diff / 7)) + " week{0} ago".format('s' if int(day_diff / 7) > 1 else '')
  if day_diff < 365:
    return str(int(day_diff / 30)) + " month{0} ago".format('s' if int(day_diff / 30) > 1 else '')
  return str(int(day_diff / 365)) + " year{0} ago".format('s' if int(day_diff / 365) > 1 else '')


@app.template_filter('ucfirst')
def ucfirst(text):
  """
  Template filter for capitalizing the first letter of a word

  Args:
    text: the text to be modified

  Returns:
    A string with the first letter uppercase.
  """
  return text[0].upper() + text[1:]
