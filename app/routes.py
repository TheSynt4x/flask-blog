from flask import current_app as app
from app.controllers.home import HomeController
from app.controllers.blog.post import PostController

app.add_url_rule('/', view_func=HomeController.as_view('home'))
app.add_url_rule('/blog/post-<int:post_id>', view_func=PostController.as_view('blog.post'))
