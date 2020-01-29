from app import app
import app.blog_helpers as BH

#home page
@app.route("/")
def home():
    return BH.render_page('index.html')

@app.route("/edit/<view_name>", methods=['GET', 'POST'])
def edit(view_name):
    edit_page = static_file(view_name)
    page = static_file('edit').replace('LOAD',edit_page)

    ## For when we're ready to start editing stuff
#    if request.method == 'POST':
#        pass

    return page
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
#        session['user_name'] = request.values['user_name']
    return ""

@app.route("/all")
def all():
    page = BH.render_page('all.html')
    # Get all pages
    files = BH.get_page_files()
    insert = ""
    for n in files:
        path = '/' + n
        if n.endswith('index.html'):
            path = '/'
        elif n.endswith('.html'):
            path = '/' + n[:n.rfind('.')]
        insert += "<tr>"
        insert += "<th>" + n + "</th>"
        insert += "<th><a href='" + path + "'>" + path + "</a></th>"
        insert += "</tr>"
    page = page.replace("<!--FILL-->", insert)
    return page

@app.route('/<view_name>')
def static_file(view_name):
    if view_name.endswith('.css'):
        if BH.page_exists(view_name, 'styles'):
            return BH.render_page(view_name, 'styles')
    elif BH.page_exists(view_name + '.html'):
        return BH.render_page(view_name + '.html')
    return BH.render_page('404.html')