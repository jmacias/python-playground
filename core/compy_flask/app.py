from flask import Flask, render_template

app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello World',
        'content': 'This is my first post'
    }
}


@app.route('/')
def home():
    return 'Hello World'


@app.route('/post/<int:post_id>')
def post(post_id):
    p = posts.get(post_id)
    # return f"Post {p['title']} content:\n\n {p['content']}"
    if not p:
        return render_template('404.jinja2', message='POST NOT FOUND')

    return render_template('post.jinja2', post=p)


if __name__ == "__main__":
    app.run(debug=True)
