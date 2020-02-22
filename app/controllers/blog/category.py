from flask import render_template, request, flash, redirect, url_for
from flask.views import MethodView

from app.models.category import Category
from app.validators.category_form import CreateCategoryForm


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


class CreateCategoryController(MethodView):
  def get(self):
    """
    Render create category template.

    Returns:
      A template with the create category form.
    """
    return render_template('blog/category/create.html', form=CreateCategoryForm())

  def post(self):
    """
    Validates form and creates a new category if validation passed

    Returns:
      A template or a flask redirect.
    """
    form = CreateCategoryForm()

    if form.validate_on_submit():
      category = Category.create(form.name.data, form.description.data)

      flash('Category {0} has been created.'.format(category.name), 'success')
      return redirect(url_for('blog.category', category_id=category.id))

    return render_template('blog/category/create.html', form=form)


class EditCategoryController(MethodView):
  def get(self):
    pass

  def post(self):
    pass


class DeleteCategoryController(MethodView):
  def get(self):
    pass

  def post(self):
    pass
