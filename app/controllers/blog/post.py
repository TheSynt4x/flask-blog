from flask import current_app as app, render_template, request, redirect, url_for, flash
from flask.views import MethodView

from app.middleware import auth
from app.models.post import Post
from app.validators.post_form import PostForm


class PostController(MethodView):
  def get(self, post_id):
    """
    Display a single post based on the id

    Args:
      post_id: the specified post id

    Returns:
      Single blog template with a dynamic post
    """
    page = request.args.get('page', 1, type=int)
    per_page = 5

    post = Post.get_by_id(post_id)
    comments = post.paginate_comments(page, per_page)

    return render_template('blog/show.html', post=post, comments=comments)


class CreatePostController(MethodView):
  @auth.required
  def get(self):
    """
    Display create post form

    Returns:
      Create post template
    """
    return render_template('blog/create.html', form=PostForm())

  @auth.required
  def post(self):
    """
    Handles POST request and creates a new post

    Returns:
      A redirect if the validation passed else the form
    """
    form = PostForm()

    if form.validate_on_submit():
      post = Post.create(
        title=form.title.data,
        post_content=form.post_content.data,
        user_id=self.user.id,
        category_id=request.form.get('category'),
      )

      flash('Your post has been published.', 'success')

      return redirect(url_for('blog.post', post_id=post.id))

    return render_template('blog/create.html', form=form)


class EditPostController(MethodView):
  def get(self, post_id):
    """
    Displays the edit form

    Args:
      post_id: the post id from the url

    Returns:
      Edit post template
    """
    form = PostForm()
    form.submit.label.text = 'Edit'
    return render_template('blog/edit.html', post=Post.get_by_id(post_id), form=form)

  def post(self, post_id):
    """
    Handles the POST request and updates the blog post

    Args:
      post_id: the post id from the url

    Returns:
      A redirect if the validation passed else the form
    """
    form = PostForm(request.form)

    form.submit.label.text = 'Edit'

    if form.validate_on_submit():
      post = Post.get_by_id(post_id)
      post.update(title=form.title.data, content=form.post_content.data, category_id=request.form.get('category'))

      flash('Your post has been updated.', 'success')

      return redirect(url_for('blog.post', post_id=post.id))

    app.logger.info(form.is_submitted() and form.validate())

    return render_template('blog/edit.html', post=Post.get_by_id(post_id), form=form)


class DeletePostController(MethodView):
  def get(self, post_id):
    """
    Delete a post by id

    Args:
      post_id:

    Returns:

    """
    Post.delete_by_id(post_id)

    flash('Your post has been successfully deleted', 'success')

    return redirect(url_for('home'))
