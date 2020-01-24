from flask import Flask
from flask_dotenv import DotEnv

env = DotEnv()


def create_app():
  app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder='../resources/views',
    static_folder='../public/'
  )

  env.init_app(app, env_file='.env', verbose_mode=True)

  with app.app_context():
    from app import routes

    @app.context_processor
    def site_globals():
      return dict(title=app.config['APP_TITLE'], base_url=app.config['BASE_URL'])

    return app
