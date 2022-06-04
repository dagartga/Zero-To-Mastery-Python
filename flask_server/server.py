from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./index.html')

@app.route('/about.html')
def about():
    return render_template('./about.html')

@app.route('/blog')
def blog():
    return 'This is the blog page'


@app.route('/blog/2020')
def blog2020():
    return 'This is the blog page for 2020'
