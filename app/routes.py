from flask import current_app as app

from app.controllers.auth.login import LoginController
from app.controllers.auth.logout import LogoutController
from app.controllers.user.profile import ProfileController
from app.controllers.auth.register import RegisterController
from app.controllers.blog.category import CategoryController
from app.controllers.blog.comment import CommentController
from app.controllers.blog.post import PostController, CreatePostController, EditPostController, DeletePostController
from app.controllers.blog.search import SearchController
from app.controllers.home import HomeController
from app.controllers.user.change_password import ChangePasswordController
from app.controllers.user.change_avatar import ChangeAvatarController

app.add_url_rule('/', view_func=HomeController.as_view('home'))

app.add_url_rule('/search', view_func=SearchController.as_view('blog.search'))
app.add_url_rule('/blog/make-post', view_func=CreatePostController.as_view('blog.post.create'))
app.add_url_rule('/blog/post-<int:post_id>', view_func=PostController.as_view('blog.post'))
app.add_url_rule('/blog/post-<int:post_id>/make-comment', view_func=CommentController.as_view('blog.post.comment'))
app.add_url_rule('/blog/post-<int:post_id>/edit', view_func=EditPostController.as_view('blog.post.edit'))
app.add_url_rule('/blog/post-<int:post_id>/delete', view_func=DeletePostController.as_view('blog.post.delete'))

app.add_url_rule('/category/<int:category_id>', view_func=CategoryController.as_view('blog.category'))
app.add_url_rule('/profile/<string:username>', view_func=ProfileController.as_view('profile'))

app.add_url_rule('/ucp/password', view_func=ChangePasswordController.as_view('password'))
app.add_url_rule('/ucp/avatar', view_func=ChangeAvatarController.as_view('avatar'))

app.add_url_rule('/login', view_func=LoginController.as_view('login'))
app.add_url_rule('/logout', view_func=LogoutController.as_view('logout'))
app.add_url_rule('/register', view_func=RegisterController.as_view('register'))
