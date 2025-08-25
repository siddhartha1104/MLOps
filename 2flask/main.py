from flask import Flask, render_template, request

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

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
