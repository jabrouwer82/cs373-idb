
# Usage: python3 run.py [(-p | --port) <port nunmber to use>]
# Example: python3 run.py -p 5050
# -p or --port to specify the port to run the server on (default 5000)

# Be sure to run 'sudo ufw allow <port num>' to enable the port you are using
# for external facing servers.
import getopt
import sys 
from test_app import test_app

if __name__ == '__main__':

  # CMD opts handling
  opts = getopt.getopt(sys.argv[1:], 'p:', ['port='])
  port = 5050
  for opt, arg in opts[0]:
    if opt in ('-p', '--port'):
      port = int(arg)


  test_app.run(host='0.0.0.0', port=port,  debug=True)
