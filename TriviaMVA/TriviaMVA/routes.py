from flask import Flask,url_for;
from app import app;


# server/ (URL)
@app.route('/')
def hello():
    #return "Hello World!"
    createLink = "<a href='" + url_for('create') + "'>Create a question</a>";
    return """<html>
                       <head>
                               <title>Hello, world</title>
                       </head>
                       <body>
                                <h1>Hello,Joey</h1>
                                """ + createLink + """
                       </body>
                   </html>"""

# server/create
#@app.route('/create')
@app.route('/joey')
def create():
    return '<h2>This is the create page!</h2>'

#server/question/<title>
@app.route('/question/<title>')
def question(title):
    return '<h2>' + title + '</h2>'

