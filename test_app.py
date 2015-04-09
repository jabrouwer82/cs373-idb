from tests import TestIDB 
from io import StringIO
import unittest
import filters
from flask import Flask, jsonify
from types import FunctionType

test_app = Flask(__name__)
test_app.debug = True
'''
test_app.jinja_env.autoescape = False
# Auto imports all functions in filters.py to be jinja filters
for func_name in dir(filters):
  func = getattr(filters, func_name, None)
  if isinstance(func, FunctionType):
    test_app.jinja_env.filters[func_name] = func

test_app.config['tipfyext.jinja2'] = {
    'environment_args': {
         'autoescape': False,
    } 
}

'''

@test_app.route('/api/tests')
def run_tests():
  stream = StringIO()
  runner = unittest.TextTestRunner(stream)
  runner.run(unittest.makeSuite(TestIDB))
  stream.seek(0)
  return jsonify({'message':stream.getvalue()})



# Usage: python3 run.py [(-p | --port) <port nunmber to use>]
# Example: python3 run.py -p 5050
# -p or --port to specify the port to run the server on (default 5000)

# Be sure to run 'sudo ufw allow <port num>' to enable the port you are using
# for external facing servers.
import getopt
import sys

if __name__ == '__main__':

  # CMD opts handling
  opts = getopt.getopt(sys.argv[1:], 'p:', ['port='])
  port = 5000
  for opt, arg in opts[0]:
    if opt in ('-p', '--port'):
      port = int(arg)


  test_app.run(host='0.0.0.0', port=port,  debug=True)




  
'''
def wrap_data(gen):
  return ("data: " + g for g in gen)

def test_runner():
  test_names = [t for t in dir(TestIDB) if callable(getattr(TestIDB,t)) and t.startswith('test')]
  runner = unittest.TextTestRunner(StringIO()) # throw away report
  num_run = 0
  num_successes = 0
   
  start = time.time()
  for t in test_names:
    result = runner.run(make_suite(t))
    num_run += 1
    if result.errors == [] and result.failures == []:
      num_successes += 1
    yield str((num_successes, num_run))
  end = time.time()

  yield "Ran " + str(num_run) + " tests in " + "{0:.2f}s".format(end - start)
      
 
def make_suite(test_name):
  suite = unittest.TestSuite()
  suite.addTest(TestIDB(test_name))
  return suite
  
 
@test_app.route("/progress")
def progress():
  debug_template = """
            <!DOCTYPE html>
            <html>
            <head>
              <meta charset="utf-8" />
            </head>
            <body>
              <script>
                var source = new EventSource('tests');

                document.body.innerHTML += '<p>smug bug </p>' + '<br>';
                source.onopen = function () {
                  document.body.innerHTML = '<p>onopen</p>' + '<br>';
                };

                source.onerror = function () {
                  document.body.innerHTML = '<p>onerror</p>' + '<br>';
                };

                source.onmessage = function (event) {
                  document.body.innerHTML = '<p>' + event.data + '</p>' + '<br>';
                };


              </script>
            </body>
            </html>
    

    """

  return(debug_template) 

'''
