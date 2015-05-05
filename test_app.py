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
  tests = [t for t in functions_in(TestIDB) if t.startswith('test')]
  return stream_response(test_runner(tests))

@test_app.route('/api/tests/fail')
def stream_with_fail():
  tests = [t for t in functions_in(TestIDB) if t.startswith('test')]
  fail_tests = [t for t in functions_in(TestIDB) if t.startswith('failtest')]
  for f in fail_tests:
    tests.insert(len(tests) // 2, f)
  return stream_response(test_runner(tests))

def stream_response(generator):
  main_app_url = os.environ.get('MAIN_URL', 'http://celebrapsheet.tk')
  response = Response(encode(generator), mimetype="text/event-stream")
  response.headers['Access-Control-Allow-Origin'] = main_app_url
  response.headers['Access-Control-Allow-Credentials'] = 'true'
  return response

def test_runner(test_names):
  # Throw away result
  runner = unittest.TextTestRunner(StringIO())
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

# This will break if g contains \n\n
def encode(gen):
    return ("data: " + g + "\n\n" for g in gen)

def make_suite(test_name):
    suite = unittest.TestSuite()
    suite.addTest(TestIDB(test_name))
    return suite

def functions_in(a_class):
  return (t for t in dir(a_class) if callable(getattr(a_class, t)))
