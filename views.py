from flask import render_template, Flask
from app import app
from models import Crime, Celebrity, Charge


@app.route('/')
@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/celebrities')
def celebrities():
    celebrity_list = Celebrity.query.all()
    return render_template('celebrities.html', celebrities=celebrity_list)
     





