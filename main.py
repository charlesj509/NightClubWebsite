# app.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #images=['picture1.jpg','picture3.jpg','picture4.jpg','picture5.jpg','picture6.jpg','picture7.jpg']
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
