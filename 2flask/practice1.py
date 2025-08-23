from flask import Flask
## WSGI
app = Flask(__name__)


## Routings

@app.route('/')
def welcome():
    return "This is Home Page"

@app.route("/index")
def index():
    return "This is index Page"


## Entery point
if __name__ == "__main__":
    app.run(debug= True)