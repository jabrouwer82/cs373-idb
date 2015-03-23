from flask import Flask, Response, make_response, abort, jsonify
from models import Celebrity, Attorney, Crime, Charge
from app import app
import json

def make_get_table(path, table): 
  def get_table(): 
    json_list = [a.to_json() for a in table.query.all()]
    return Response(json.dumps(json_list),  mimetype='application/json') 
  app.add_url_rule('/' + path, path + '_many' , get_table, methods=['GET'])

def make_get_element(path, table): 
  def get_element(elmt_id):
    match = table.query.filter(table.id == elmt_id).first()
    if match:
      return jsonify(match.to_json())
    abort(404)
  app.add_url_rule('/' + path + '/<int:elmt_id>', path + '_one', get_element, methods=['GET'])

make_get_table('celebrities', Celebrity)
make_get_table('attorneys', Attorney)
make_get_table('charges', Charge)
make_get_table('crimes', Crime)

make_get_element('celebrity', Celebrity)
make_get_element('attorney', Attorney)
make_get_element('charge', Charge)
make_get_element('crime', Crime)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



