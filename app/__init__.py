from flask import Flask


def create_app():
  app = Flask(__name__, instance_relative_config=False, template_folder='../resources/views', static_folder='../public/')

  with app.app_context():
    from app import routes

    return app
