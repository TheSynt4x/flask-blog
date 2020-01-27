from flask import render_template, request, flash, redirect, url_for
from flask.views import MethodView

from app.services import avatar_service
from app.middleware import auth
from app.validators.avatar_form import AvatarForm


class ChangeAvatarController(MethodView):
  @auth.required
  def get(self):
    """
    Displays change avatar form

    Returns:
      A template with the form
    """
    return render_template('user/change-avatar.html', form=AvatarForm())

  @auth.required
  def post(self):
    """
    Processes the POST request and updates the user avatar

    Returns:
      A redirect if the validation passes else the template with the form
    """
    form = AvatarForm()

    if form.validate_on_submit():
      if self.user.avatar != 'no-image.png':
        avatar_service.remove(self.user.avatar)

      avatar = avatar_service.save(form.avatar.data)

      self.user.change_avatar(avatar)

      flash('You have changed your avatar.', 'info')

      return redirect(url_for('home'))

    return render_template('user/change-avatar.html', form=form)
