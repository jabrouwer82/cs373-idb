from flask import Response, request, render_template, Flask, send_from_directory, Blueprint
from models import Crime, Celebrity, CelebrityAlias, Charge
from sqlalchemy_searchable import parse_search_query, search
import json
import os
import re
import urllib

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

@viewsBlueprint.route('/superheroes')
@viewsBlueprint.route('/superheroes/')
def superheroes():
    supers = list()
    r = urllib.request.urlopen('http://104.239.165.88/api/characters')
    supers_id = json.loads(r.read().decode("utf-8"))
    for super_id in supers_id:
        super_id_url = urllib.request.urlopen('http://104.239.165.88/api/characters/' + str(super_id['id']))
        supers.append(json.loads(super_id_url.read().decode("utf-8")))
    return render_template('superheroes.html', supers=supers)
    

@viewsBlueprint.route('/tests')
@viewsBlueprint.route('/tests/')
def tests():
  test_route = '/api/tests'
  test_url = os.environ.get('TEST_URL', 'http://celebrapsheet.tk') + test_route
  return render_template('tests.html', test_url=test_url)


@viewsBlueprint.route('/tests/fail')
@viewsBlueprint.route('/tests/fail/')
def tests_fail():
  test_route = '/api/tests/fail'
  test_url = os.environ.get('TEST_URL', 'http://celebrapsheet.tk') + test_route
  return render_template('tests.html', test_url=test_url)


@viewsBlueprint.route('/search')
@viewsBlueprint.route('/search/')
def search():
  search_query = request.args.get('query')
  search_terms = search_query.split(' ')
  search_query_or = ' or '.join(search_terms)
  table_query = request.args.get('table')
  
  if table_query == 'Celebrity':
    table = Celebrity
    item_mapper = celeb_item_mapper
    search_vector = Celebrity.search_vector # | CelebrityAlias.search_vector
  elif table_query == 'Crime':
    table = Crime
    item_mapper = crime_item_mapper
    search_vector = Crime.search_vector
  elif table_query == 'Charge':
    table = Charge
    item_mapper = charge_item_mapper
    search_vector = Charge.search_vector
  else:
    abort(500)

  and_query = table.query.filter(search_vector.match(parse_search_query(search_query)))
  and_results = and_query.all()  
  or_query = table.query.filter(search_vector.match(parse_search_query(search_query_or)))
  or_results = or_query.all()  
  final_results = and_results + [item for item in or_results if item not in and_results]
  items = [item_mapper(item, search_terms) for item in final_results]
  #items = [item_mapper(item, search_terms) for item in and_results]
  return render_template('search.html', items=items, query=search_query, table=table_query)

def celeb_item_mapper(celeb, search_terms):
  item = {}
  item['name'] = celeb.name
  item['description'] = highlighter(' '.join([val for val in [celeb.name, celeb.description, celeb.twitter_handle, celeb.wiki_url, celeb.imdb_url] + [alias.alias for alias in celeb.aliases] if val is not None]), search_terms)
  item['href'] = '/celebrities/{id}'.format(id=celeb.id)
  return item

def crime_item_mapper(crime, search_terms):
  item = {}
  item['name'] = crime.name
  item['description'] = highlighter(' '.join([val for val in [crime.name, crime.description, crime.wiki_url] if val is not None]), search_terms)
  item['href'] = '/crimes/{name}'.format(name=crime.name)
  return item

def charge_item_mapper(charge, search_terms):
  item = {}
  item['name'] = charge.celebrity.name + ', ' + charge.crime.name + ', ' + date_formatter(charge.date)
  item['description'] = highlighter(' '.join([val for val in [charge.description, charge.attorney, charge.classification] if val is not None]), search_terms)
  item['href'] = '/charges/{id}'.format(id=charge.id)
  return item

def highlighter(description, terms):
  for term in terms:
    description = re.sub('({term})'.format(term=term),
                         r'<mark>\1</mark>',
                         description,
                         flags=re.IGNORECASE)

  description = re.sub('</mark>(.{20})(.*?)(.{20})<mark>',
                       r'</mark>\1...\3<mark>',
                       description)
  description = re.sub('(.*?)(.{20})<mark>(.*)',
                       r'...\2<mark>\3',
                       description)
  description = re.sub('(.*)</mark>(.{20})(.*)',
                       r'\1</mark>\2...',
                       description)
  return description

def date_formatter(d):
  return '{month} {day}, {year}'.format(month=d.strftime('%B'), day=d.day, year=d.year)

