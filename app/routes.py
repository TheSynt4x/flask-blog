from flask import current_app as app
from app.controllers.home import HomeController
from app.controllers.blog.post import PostController
from app.controllers.blog.search import SearchController
from app.controllers.blog.category import CategoryController
from app.controllers.auth.login import LoginController
from app.controllers.auth.logout import LogoutController

from app.controllers.auth.register import RegisterController

app.add_url_rule('/', view_func=HomeController.as_view('home'))

app.add_url_rule('/search', view_func=SearchController.as_view('blog.search'))
app.add_url_rule('/blog/post-<int:post_id>', view_func=PostController.as_view('blog.post'))
app.add_url_rule('/category/<int:category_id>', view_func=CategoryController.as_view('blog.category'))

app.add_url_rule('/login', view_func=LoginController.as_view('login'))
app.add_url_rule('/logout', view_func=LogoutController.as_view('logout'))
app.add_url_rule('/register', view_func=RegisterController.as_view('register'))
