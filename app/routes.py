from app import app

#home page
@app.route("/")
def home():
    return open('app/home/home.html','r').read()
#    return app.send_static_file('home.html')

@app.route('/<path:path>')
def static_file(path):
    if path[-3:] == 'css':
        return app.send_static_file(path)

@app.route("/about")
def about():
    return "<h1>About Me</h1>"