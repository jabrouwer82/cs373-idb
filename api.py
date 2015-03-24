from flask import Flask, Response, make_response, abort, jsonify, request, url_for
from models import Celebrity, Attorney, Crime, Charge
from app import app
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

  def add_items(self, *keys):
    for k in keys:
      self.json_map[k] = [item_abbrev_json(a) for a in getattr(self.obj, k)]
    return self


def celebrity_to_json(r):
  return JsonBuild(r).add_scalars('id', 'name', 'description') \
                    .add_items('attorneys', 'crimes', 'charges').json_map
                
def attorney_to_json(r):
  return JsonBuild(r).add_scalars('id', 'name', 'firm') \
                    .add_items('celebrities', 'crimes', 'charges').json_map

def crime_to_json(r):
  return JsonBuild(r).add_scalars('id', 'name') \
                    .add_items('celebrities', 'attorneys', 'charges').json_map

def charge_to_json(r):
  return JsonBuild(r).add_scalars('celebrity_id', 'attorney_id', 'crime_id', 'location') \
                    .add('date', r.date.strftime("%m-%d-%Y")).json_map



def table_name(table):
  return table.__name__.lower()

def item_func_idx(path):
  return path + '_one'

def table_func_idx(path):
  return path + '_many'



def item_abbrev_json(r):
  func_index = item_func_idx(table_name(type(r)))
  uri = url_for(func_index, elmt_id=r.id, _external=True)
  item = {'id':r.id, 'uri':uri}
  if hasattr(r, 'name'):
    item['name'] = r.name 
  return item


def make_get_table(table): 
  path = table_name(table)
  def get_table(): 
    json_list = [item_abbrev_json(a) for a in table.query.all()]
    return Response(json.dumps(json_list),  mimetype='application/json') 
  app.add_url_rule('/' + path, table_func_idx(path) , get_table, methods=['GET'])

def make_get_item(table, item_func):
  path = table_name(table)
  def get_element(elmt_id):
    match = table.query.filter(table.id == elmt_id).first()
    if match:
      return jsonify(item_func(match))
    abort(404)
  app.add_url_rule('/' + path + '/<int:elmt_id>', item_func_idx(path), get_element, methods=['GET'])


make_get_table(Celebrity)
make_get_table(Attorney)
make_get_table(Charge)
make_get_table(Crime)

make_get_item(Celebrity, celebrity_to_json)
make_get_item(Attorney, attorney_to_json)
make_get_item(Charge, charge_to_json)
make_get_item(Crime, crime_to_json)



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



