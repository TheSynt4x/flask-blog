from flask import flash, redirect, session, url_for

from app.models.user import User


def optional(func):
  def wrapper(self, *args, **kwargs):
    if session.get('user_id'):
      flash('You\'re already logged in.', 'info')
      return redirect(url_for('home'))
    else:
      return func(self, *args, **kwargs)

  return wrapper


def required(func):
  def wrapper(self, *args, **kwargs):
    if not session.get('user_id'):
      flash('You\'re not logged in.', 'info')
      return redirect(url_for('login'))
    else:
      self.user = User.query.get(session.get('user_id'))
      return func(self, *args, **kwargs)

  return wrapper
