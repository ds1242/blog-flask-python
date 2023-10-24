from flask import Flask, render_template
from post import Post
import requests
# setting up the initial flask sever
app = Flask(__name__)

posts = requests.get('https://api.npoint.io/2fe1152e54348485537b').json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["date"], post['author'])
    post_objects.append(post_obj)



@app.route("/")
def home():
    return render_template("index.html", posts=post_objects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/sample-post")
def contact():
    return render_template("sample-post.html")


@app.route('/post/<int:num>')
def post(num):
    request_post = None
    for blog_post in post_objects:
        if blog_post.id == num:
            request_post = blog_post
    return render_template("post.html", post_num=num, blog_post=request_post)


if __name__ == "__main__":
    app.run(debug=True)