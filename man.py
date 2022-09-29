from user import User
from post import Post
app_user_one = User("mosaku@gmail.com", "Michael", "Pw1", "Developer")
app_user_one.get_user_info()

app_post_one = Post("in a twinkle of an eye", app_user_one.name)
app_post_one.get_post_info()