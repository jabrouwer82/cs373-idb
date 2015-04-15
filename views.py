from flask import render_template, Flask, send_from_directory, Blueprint
from models import Crime, Celebrity, Charge
import os
import urllib
import json

# Define the interface that app will register to views routes
viewsBlueprint = Blueprint('views', __name__)


@viewsBlueprint.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(viewsBlueprint.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@viewsBlueprint.route('/')
@viewsBlueprint.route('/splash')
def splash():
    return render_template('splash.html')

@viewsBlueprint.route('/celebrities')
@viewsBlueprint.route('/celebrities/')
def celebrities():
    celebrity_list = Celebrity.query.all()
    return render_template('celebrities.html', celebrities=celebrity_list)
    
# Poor implementation of sorting, will fix in next phase.
@viewsBlueprint.route('/celebrities/alph')
def alphCelebrities():
    celebrity_list = Celebrity.query.all()
    celebrity_list.sort(key = lambda celebrity: celebrity.name)
    return render_template('celebrities.html', celebrities=celebrity_list)

@viewsBlueprint.route('/celebrities/bday')
def bdayCelebrities():
    celebrity_list = Celebrity.query.all()
    celebrity_list.sort(key = lambda celebrity: celebrity.birthday)
    return render_template('celebrities.html', celebrities=celebrity_list)

@viewsBlueprint.route('/crimes/alph')
def alphCrimes():
    crime_list = Crime.query.all()
    crime_list.sort(key = lambda crime: crime.name)
    return render_template('crimes.html', crimes=crime_list)

@viewsBlueprint.route('/charges/alph')
def alphCharges():
    charge_list = Charge.query.all()
    charge_list.sort(key = lambda charge: charge.celebrity.name)
    return render_template('charges.html', charges=charge_list, date_formatter=date_formatter)

    
@viewsBlueprint.route('/celebrities/<int:celebrity_id>')
def getCelebrity(celebrity_id):
  celebrity_info = Celebrity.query.filter(Celebrity.id== celebrity_id).first()
  return render_template('celebrity.html', celebrity=celebrity_info, date_formatter=date_formatter)

@viewsBlueprint.route('/crimes')
@viewsBlueprint.route('/crimes/')
def crimes():
	crime_list = Crime.query.all()
	return render_template('crimes.html', crimes=crime_list)

@viewsBlueprint.route('/crimes/<crime>')
def getCrime(crime):
    crime_info = Crime.query.filter(Crime.name == crime).first()
    return render_template('crime.html', crime=crime_info)

@viewsBlueprint.route('/charges')
@viewsBlueprint.route('/charges/')
def charges():
	charge_list = Charge.query.all()
	return render_template('charges.html', charges=charge_list, date_formatter=date_formatter)
@viewsBlueprint.route('/charges/<int:charge_id>')
def getCharge(charge_id):
    charge = Charge.query.filter(Charge.id == charge_id).first()
    return render_template('charge.html', charge=charge, date_formatter=date_formatter)

@viewsBlueprint.route('/about_us')
@viewsBlueprint.route('/about_us/')
def about_us():
    return render_template('about_us.html')


@viewsBlueprint.route('/tests')
@viewsBlueprint.route('/tests/')
def tests():
  test_route = '/api/tests'
  test_url = os.environ.get('TEST_URL', 'http://celebrapsheet.tk') + test_route
  return render_template('tests.html', test_url=test_url)



def date_formatter(d):
  return '{month} {day}, {year}'.format(month=d.strftime('%B'), day=d.day, year=d.year)

