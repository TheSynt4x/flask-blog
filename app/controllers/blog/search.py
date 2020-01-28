from flask import render_template, request
from flask.views import MethodView

from app.models.post import Post


class SearchController(MethodView):
  def get(self):
    """
    Display results based on the query

    Returns:
      A template with the search results
    """
    query = request.args.get('query', type=str)
    page = request.args.get('page', 1, type=int)

    posts = Post.search(query, page=page, per_page=5)

    return render_template('blog/search/show.html', query=query, posts=posts)
