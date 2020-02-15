from app import app
from flask import request, session
import app.blog_helpers as BH
import app.database_access as DB

#home page
@app.route("/")
def home():
    return static_file("index.html")

@app.route("/edit/<view_name>", methods=['GET', 'POST'])
def edit(view_name):
    if not ('user_name' in session):
        return static_file('404')
    ## For when we're ready to start editing stuff
    if request.method == 'POST':
        PageName = view_name
        PageType = 'html'
        if '.' in view_name:
            view_name = view_name.split('.')
            PageName = view_name[0]
            PageType = view_name[1]
        DB.save_page(PageName, PageType, request.form['text'])
        
    edit_page = static_file(view_name)
    page = static_file('edit').replace('LOAD',edit_page.replace('/', '\/').replace('`', '\`'))

    return page
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    page = static_file('login')
    if 'user_name' in session:
        page += "<script>alert('Already logged in as " + session['user_name'] + "')</script>"
    if request.method == 'POST':
        if 'user_name' in request.values:
            session['user_name'] = request.values['user_name']
    return page

@app.route("/all")
def all():
    page = static_file('all')
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
    if '.' in view_name:
        pname, ptype = view_name.split('.')
        TPage = DB.get_page(pname, ptype)
    else:
        TPage = DB.get_page(view_name, 'html')
    return TPage