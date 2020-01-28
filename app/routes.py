from app import app
from app.blog_helpers import render_page
from app.blog_helpers import page_exists

#home page
@app.route("/")
def home():
    return render_page('index.html')

@app.route('/<view_name>')
def static_file(view_name):
    if page_exists(view_name + '.html'):
        return render_page(view_name + '.html')
    return render_page('404.html')