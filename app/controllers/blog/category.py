from flask import render_template, request
from flask.views import MethodView

from app.models.category import Category


class CategoryController(MethodView):
  def get(self, category_id):
    """
    Display a category by id

    Args:
      category_id: the specified category id

    Returns:
      A template with the category and its posts.
    """
    page = request.args.get('page', 1, type=int)
    per_page = 2

    category = Category.get_posts(category_id, page, per_page)

    return render_template('blog/category/show.html', category=category['category'], posts=category['posts'])
