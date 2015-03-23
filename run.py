#!../flask3/bin/python

from app import app

# load the url routing functions

from views import *
from api import *


app.run(debug=True)
