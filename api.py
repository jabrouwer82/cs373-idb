#!flask3/bin/python

from flask import Flask, Response, make_response, jsonify, abort
from models import *
import json


# json helpers
def jsonify_table(table):
  json_list = [a.to_json() for a in table.query.all()]
  return Response(json.dumps(json_list),  mimetype='application/json') # cause jsonify doesn't like arrays

def jsonify_id_in_table(ID, table):
  match = table.query.filter(table.id == ID).first()
  if match:
    return jsonify(match.to_json())
  abort(404)


##### API functions #######
@app.route('/celebrities', methods=['GET'])
def get_celebrities():
  return jsonify_table(Celebrity)

@app.route('/celebrities/<int:celeb_id>', methods=['GET'])
def get_celebrity(celeb_id):
  return jsonify_id_in_table(celeb_id, Celebrity)

@app.route('/attorneys', methods=['GET'])
def get_attorneys():
  return jsonify_table(Attorney)
  
@app.route('/attorneys/<int:attorney_id>', methods=['GET'])
def get_attorney(attorney_id):
  return jsonify_id_in_table(attorney_id, Attorney)

@app.route('/crimes', methods=['GET'])
def get_crimes():
  return jsonify_table(Crime)

@app.route('/crimes/<int:crime_id>', methods=['GET'])
def get_crime(crime_id):
  return jsonify_id_in_table(crime_id, Crime)


@app.route('/charges', methods=['GET'])
def get_charges():
  return jsonify_table(Charge)

@app.route('/charges/<int:charge_id>', methods=['GET'])
def get_charge(charge_id):
  return jsonify_id_in_table(charge_id, Charge)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
  


