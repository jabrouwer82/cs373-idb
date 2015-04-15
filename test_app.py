from tests import TestIDB 
from io import StringIO
import unittest
from flask import Flask, Response
import json
import os

test_app = Flask(__name__)
test_app.debug = True


@test_app.route('/api/tests')
def stream():
  main_app_url = os.environ.get('MAIN_URL', 'http://celebrapsheet.tk')
  response = Response(encode(test_runner()), mimetype="text/event-stream")
  response.headers['Access-Control-Allow-Origin'] = main_app_url
  response.headers['Access-Control-Allow-Credentials'] = 'true'
  return response

def test_runner():
  test_names = [t for t in dir(TestIDB) if callable(getattr(TestIDB,t)) and t.startswith('test')]
  runner = unittest.TextTestRunner(StringIO()) # throw away result
  yield json.dumps({'return_code':'num_tests', 'message':str(len(test_names))})
 
  for t in test_names:
    result = runner.run(make_suite(t))
    return_code = ''
    if result.errors != []:
      return_code = 'error'
    elif result.failures != []:
      return_code = 'failure'
    else:
      return_code = 'success'
    yield json.dumps({'return_code':return_code, 'message':t})

# This will break if g contain \n\n
def encode(gen):
    return ("data: " + g + "\n\n" for g in gen)

def make_suite(test_name):
    suite = unittest.TestSuite()
    suite.addTest(TestIDB(test_name))
    return suite

