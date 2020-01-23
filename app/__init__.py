from flask import Flask


def create_app():
  app = Flask(__name__, instance_relative_config=False, template_folder='../resources/views', static_folder='../public/')

  app.config['APP_TITLE'] = 'Project'

  with app.app_context():
    from app import routes

    @app.context_processor
    def title():
      return dict(title=app.config['APP_TITLE'])

    return app
