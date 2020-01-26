from flask import Flask
from flask_dotenv import DotEnv
from flask_sqlalchemy import SQLAlchemy

env = DotEnv()
db = SQLAlchemy()


def create_app():
  app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder='../resources/views',
    static_folder='../public/'
  )

  env.init_app(app, env_file='.env', verbose_mode=True)
  db.init_app(app)

  with app.app_context():
    from app import routes
    from app.utils import jinja

    from app.models.category import Category
    from app.models.post import Post
    from app.models.user import User
    from app.models.comment import Comment

    db.create_all()

    return app
