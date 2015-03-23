from flask import render_template,Flask
from app import app



@app.route('/')
@app.route('/splash')
def splash():
  return render_template('splash.html')
     





