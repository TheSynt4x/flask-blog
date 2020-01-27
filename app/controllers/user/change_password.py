from flask import render_template, redirect, url_for, flash
from flask.views import MethodView

from app.middleware import auth
from app.validators.password_form import ChangePasswordForm

from app.models.user import User


class ChangePasswordController(MethodView):
  @auth.required
  def get(self):
    """
    Displays change password form

    Returns:
      A template with the form
    """
    return render_template('user/change-password.html', form=ChangePasswordForm())

  @auth.required
  def post(self):
    """
    Processes the POST request and changes the password

    Returns:
      A redirect if validation passed else the template with the errors
    """
    form = ChangePasswordForm()

    if form.validate_on_submit():
      user = User.authenticate(self.user.username, form.current_password.data)

      if not user:
        form.current_password.errors.append('Incorrect password. Try again.')

      user.change_password(form.new_password.data)

      flash('You have changed your password.', 'success')

      return redirect(url_for('home'))

    return render_template('user/change-password.html', form=form)
