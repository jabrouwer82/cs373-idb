from flask import Flask, Response, make_response, abort, jsonify, request, url_for, Blueprint
from models import Celebrity, CelebrityAlias, Crime, CrimeDescription, Charge
from sqlalchemy_searchable import parse_search_query, search
import json


class JsonBuild:
  def __init__(self, obj):
    self.obj = obj
    self.json_map = {}

  def add_scalars(self, *scalars):
    self.json_map.update({p:getattr(self.obj, p) for p in scalars})
    return self

  def add(self, k, v):
    self.json_map[k] = v
    return self

  def add_items(self, abbrev_func, k):
    self.json_map[k] = [abbrev_func(a) for a in getattr(self.obj, k)]
    return self

# TODO(jabrouwer82): Fix these to match the new models
def celebrity_to_json(r):
  return JsonBuild(r).add_scalars('id', 'name', 'description', 'twitter_handle', 'wiki_url',
                                  'imdb_url', 'picture_url', ) \
                     .add('birthday',
                          r.birthday.strftime('%m-%d-%Y') if r.birthday else None) \
                     .add_items(crime_abbrev, 'crimes') \
                     .add_items(charge_abbrev, 'charges') \
                     .add_items(alias_abbrev, 'aliases') \
                     .json_map
                
def crime_to_json(r):
  return JsonBuild(r).add_scalars('id', 'name', 'wiki_url') \
                     .add_items(celebrity_abbrev, 'celebrities') \
                     .add_items(charge_abbrev, 'charges') \
                     .add_items(crime_description_abbrev, 'descriptions') \
                     .json_map

def charge_to_json(r):
  return JsonBuild(r).add_scalars('location', 'description',
                                  'attorney', 'classification') \
                     .add('date', r.date.strftime('%m-%d-%Y') if r.date else None) \
                     .add('crime', crime_abbrev(r.crime)) \
                     .add('celebrity', celebrity_abbrev(r.celebrity)) \
                     .json_map

         

def table_name(table):
  return table.__name__.lower()



# get url of that func route to when called with ID
def url_for_call(func, ID):
  # '.' is prepended to access blueprint routes
  return url_for('.' + func, elmt_id=ID, _external=True)


# Functions to abbreviate a row in each table
def crime_abbrev(r):
  return {'id': r.id, 'uri': url_for_call('get_crime', r.id), 'name': r.name}

def celebrity_abbrev(r): 
  return {'id': r.id, 'uri': url_for_call('get_celebrity', r.id), 'name': r.name}

def charge_abbrev(r): 
  return {'id': r.id, 'uri': url_for_call('get_charge', r.id)}

def alias_abbrev(r): 
  return {'id': r.id, 'alias': r.alias}

def crime_description_abbrev(r):
  return {'id': r.id, 'location': r.location, 'description': r.description}



def table_abbrev_json(table, item_abbrev_func):
  json_list = [item_abbrev_func(a) for a in table.query.all()]
  return Response(json.dumps(json_list),  mimetype='application/json') 

def get_element(table, elmt_id, item_func):
    match = table.query.filter(table.id == elmt_id).first()
    if match:
      return jsonify(item_func(match))
    abort(404)



# Define the interface that app will register to add the api routes
apiBlueprint = Blueprint('api', __name__)
  

## Get abbreviations for tables
@apiBlueprint.route('/api/celebrity')
def get_celebrities():
  return table_abbrev_json(Celebrity, celebrity_abbrev)

@apiBlueprint.route('/api/crime')
def get_crimes():
  return table_abbrev_json(Crime, crime_abbrev)

@apiBlueprint.route('/api/charge')
def get_charges():
  return table_abbrev_json(Charge, charge_abbrev)


## Get specific elements in tables
@apiBlueprint.route('/api/celebrity/<int:elmt_id>')
def get_celebrity(elmt_id):
  return get_element(Celebrity, elmt_id, celebrity_to_json)

@apiBlueprint.route('/api/crime/<int:elmt_id>')
def get_crime(elmt_id):
  return get_element(Crime, elmt_id, crime_to_json)

@apiBlueprint.route('/api/charge/<int:elmt_id>')
def get_charge(elmt_id):
  return get_element(Charge, elmt_id, charge_to_json)


# Search
@apiBlueprint.route('/api/search')
def api_search():
  search_query = request.args.get('query')
  search_terms = search_query.split(' ')
  search_query_or = ' or '.join(search_terms)
  table_query = request.args.get('table')
  
  if table_query == 'Celebrity':
    table = Celebrity
    json_func = celebrity_to_json
    search_vector = Celebrity.search_vector | CelebrityAlias.search_vector
  elif table_query == 'Crime':
    table = Crime
    json_func = crime_to_json
    search_vector = Crime.search_vector
  elif table_query == 'Charge':
    table = Charge
    json_func = charge_to_json
    search_vector = Charge.search_vector
  else:
    abort(500)

  and_query = table.query.filter(search_vector.match(parse_search_query(search_query)))
  and_results = [json_func(item) for item in and_query]
  
  or_query = table.query.filter(search_vector.match(parse_search_query(search_query_or)))
  or_results = [json_func(item) for item in or_query]
  final_results = and_results + [item for item in or_results if item not in and_results]
  return Response(json.dumps(final_results),  mimetype='application/json')

@apiBlueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



