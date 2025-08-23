from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return 'This is main Page '

@app.route('/index')
def index():
    return render_template('index1.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
