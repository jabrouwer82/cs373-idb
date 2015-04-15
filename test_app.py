from tests import TestIDB 
from io import StringIO
import unittest
import filters
from flask import Flask, jsonify, Response, url_for
from types import FunctionType
import json
import os

test_app = Flask(__name__)
test_app.debug = True


@test_app.route('/api/tests')
def stream():
  main_app_url = os.environ.get('MAIN_URL', 'http://23.253.252.30:9898')
  response = Response(encode(test_runner()), mimetype="text/event-stream")
  response.headers['Access-Control-Allow-Origin'] = main_app_url
  response.headers['Access-Control-Allow-Credentials'] = 'true'
  return response

def encode(gen):
  for g in gen:
    yield "data: " + g + "\n\n"

def test_runner():
  test_names = [t for t in dir(TestIDB) if callable(getattr(TestIDB,t)) and t.startswith('test')]
  runner = unittest.TextTestRunner(StringIO())
  yield json.dumps({'return_code':'num_tests', 'message':str(len(test_names))})
 
  for t in test_names:
    result = runner.run(make_suite(t))
    return_code = ''
    if result.errors == [] and result.failures == []:
      return_code = 'success'
    else:
      return_code = 'failure'
    yield json.dumps({'return_code':return_code, 'message':t})

      
 
def make_suite(test_name):
    suite = unittest.TestSuite()
    suite.addTest(TestIDB(test_name))
    return suite
    





