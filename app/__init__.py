from flask import Flask, app, render_template, redirect, request

app = Flask(_name_)

@app.route('/')
def load():
    try:
        return render_template('initialPage.html')
    except:
        return render_template('error.html')

@app.route('/home')
def home():
    try:
        return render_template('home.html', title="home")
    except:
        return render_template('error.html')

@app.route('/about')
def about():
    try:
        return render_template('about.html', title="about")
    except:
        return render_template('error.html')