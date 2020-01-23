from flask import current_app as app
from app.controllers.home import HomeController

app.add_url_rule('/', view_func=HomeController.as_view('home'))