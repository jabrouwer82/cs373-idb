from tests import TestIDB 
from io import StringIO
import unittest
import filters
from flask import Flask, jsonify
from types import FunctionType

test_app = Flask(__name__)
test_app.debug = True

@test_app.route('/api/tests')
def run_tests():
  stream = StringIO()
  runner = unittest.TextTestRunner(stream)
  runner.run(unittest.makeSuite(TestIDB))
  stream.seek(0)
  return jsonify({'message':stream.getvalue()})

