import os
import uuid

from flask import current_app as app
from werkzeug.utils import secure_filename


def remove(avatar_filename):
  """
  Delete an avatar from the images/avatar folder.

  Args:
    avatar_filename: the avatar filename

  Returns:
    null
  """
  os.remove(os.path.join(
    app.static_folder, 'images/avatars', avatar_filename,
  ))


def save(avatar_data):
  """
  Save an uploaded image to the avatar folder

  Args:
    avatar_data: the avatar form field

  Returns:
    A unique filename
  """
  file = secure_filename(avatar_data.filename)
  extension = os.path.splitext(file)[1]

  unique_filename = str(uuid.uuid4()) + extension

  avatar_data.save(os.path.join(
    app.static_folder, 'images/avatars', unique_filename
  ))

  return unique_filename
