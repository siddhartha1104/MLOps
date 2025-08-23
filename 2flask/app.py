from flask import Flask

'''
It will create an instance of the Flask class, 
which will be our WSGI (web server gateway interface) application.
'''
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome Sid. My name is Nishant as well. Hahah, Heheh"

@app.route('/index')
def index():
    return "This is Index route"

if __name__ == "__main__":
    app.run(debug=True)
     
 