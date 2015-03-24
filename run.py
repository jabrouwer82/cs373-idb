# Usage: python3 run.py [(-p | --port) <port nunmber to use>]
# Example: python3 run.py -p 5050
# -p or --port to specify the port to run the server on (default 5000)

from app import app
import getopt
import sys

# load the url routing functions
from views import *
from api import *

# CMD opts handling
opts = getopt.getopt(sys.argv[1:], 'p:', ['port='])
port = 5000
for opt, arg in opts[0]:
  if opt in ('-p', '--port'):
    port = int(arg)


app.run(host='0.0.0.0', port=port,  debug=True)

