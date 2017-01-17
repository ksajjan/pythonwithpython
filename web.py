import sys
from flask import Flask , request, flash 
from flask import render_template, url_for, send_file, render_template_string, Markup
from flask_flatpages import FlatPages, pygments_style_defs, pygmented_markdown
#from flask_frozen import Freezer
#from forms import ContactForm
import cgi 


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR_II = 'TodayILearn'
POST_DIR_III = 'LearnWithPython'



app = Flask(__name__)
flatpages = FlatPages(app)
#freezer = Freezer(app)
app.config.from_object(__name__)

def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

#app.config['FREEZER_DESTINATION'] = 'gh-pages'
#app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.gitignore', 'readme.md']
#app.config['FREEZER_RELATIVE_URLS'] = True
#app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja
#app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS']= True
app.secret_key = 'secret key Never ask'


@app.route('/')
def home():
    learnwithpython_posts  = [p for p in flatpages if p.path.startswith(POST_DIR_III)]
    learnwithpython_posts.sort(key=lambda item: item['date'], reverse=True)
    til_posts = [p for p in flatpages if p.path.startswith(POST_DIR_II)]
    til_posts.sort(key=lambda item: item['date'], reverse=True)
    return render_template('base.html',learnwithpython_posts=learnwithpython_posts[:2], til_posts= til_posts) 

@app.route("/LearnWithPython/")
def LearnWithPython():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR_III)]
    posts.sort(key=lambda item: item['date'], reverse=True)
    Tags=['Machine Learning','Numpy','Configuration','SkLearn','Case Study'] 
    return render_template('learnwithpython.html', unique_tags=Tags,posts=posts)



@app.route('/LearnWithPython/<name>/')
def LearnWithPython_post(name):
    path = '{}/{}'.format(POST_DIR_III, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


@app.route('/TodayILearn/')
def TodayILearn():
    til_posts = [p for p in flatpages if p.path.startswith(POST_DIR_II)]
    til_posts.sort(key=lambda item: item['date'], reverse=True)
    return render_template('todayilearn.html', posts=til_posts)

@app.route('/TodayILearn/<name>/')
def TodayILearn_post(name):
    path = '{}/{}'.format(POST_DIR_II, name)
    til_post  = flatpages.get_or_404(path)
    return render_template('post.html', post=til_post)


@app.route('/bookshelf/')
def bookshelf():
    return render_template('bookshelf.html')


@app.route('/contact/')
def contact():
    return render_template("contact_mail.html")


if __name__ == "__main__":
    #if len(sys.argv) > 1 and sys.argv[1] == "build":
     #   freezer.freeze()
    #else:
    app.run()

