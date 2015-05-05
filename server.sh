#! /bin/bash
# Usage: ./server.sh [start | stop | restart]
# User must have superuser privilages to run this script.

base="/tmp/server/"
apppid="$base""uwsgi.pid"
applog="$base""app.log"
testpid="$base""test_uwsgi.pid"
testlog="$base""test.log"

if [ ! -f "$testpid" ]; then
  sudo install -Dv /dev/null "$testpid"
fi
if [ ! -f "$apppid" ]; then
  sudo install -Dv /dev/null "$apppid"
fi
if [ ! -f "$testlog" ]; then
  sudo install -Dv /dev/null "$testlog"
fi
if [ ! -f "$applog" ]; then
  sudo install -Dv /dev/null "$applog"
fi

sudo chmod a+w "$testlog"
sudo chmod a+w "$applog"
sudo chmod a+w "$testpid"
sudo chmod a+w "$apppid"

opt=$1
if [ "$opt" = "start" ]; then
  # both $apppid and $testpid must not exist or must be empty
  if [ ! -s "$apppid" ] && [ ! -s "$testpid" ]; then
    echo "Copying nginx config to /etc/nginx/sites-enabled/default"
    sudo cp nginx.conf /etc/nginx/sites-enabled/default
    echo "Checking is nginx is running"
    if [ -r "/run/nginx.pid" ]; then
      echo "Nginx is running."
      echo "Reloading nginx"
      sudo nginx -s reload
    else
      echo "Nginx is not running."
      echo "Starting nginx."
      sudo nginx
    fi
    echo "Starting prod uwsgi server on port 5000, logs located at $applog"
    nohup uwsgi --socket 0.0.0.0:5000 --wsgi-file run.py --master --processes 4 --threads 2 --stats 0.0.0.0:5001 --callable app --pidfile "$apppid" &> "$applog" &
    echo "Starting test uwsgi server on port 5050, logs located at $testlog"
    nohup uwsgi --socket 0.0.0.0:5050 --wsgi-file test_run.py --master --processes 1 --threads 1 --stats 0.0.0.0:5051 --callable test_app --pidfile "$testpid" &> "$testlog" &
    echo "Success, the server is now running."
  else
    echo "Server already running, please run [sudo ./server.sh restart] to quit and restart the server"
  fi
elif [ "$opt" = "stop" ]; then
  if [ -r "$apppid" ] || [ -r "$testpid" ]; then
    pid=$(cat "$apppid")
    echo "Killing prod uwsgi server"
    sudo kill -s SIGINT "$pid"
    rm "$apppid"
    echo "Killing test uwsgi server"
    pid=$(cat "$testpid")
    sudo kill -s SIGINT "$pid"
    rm "$testpid"
    echo "Success, killed both prod and test uwsgi servers."
  else
    echo "Failed to kill uwsgi servers."
    echo "Could not locate pidfiles for prod or test servers."
    echo "Please run 'pgrep uwsgi' to locate processes related to uwsgi."
    echo "Then run 'kill -s SIGINT <pid>' to kill them."
    echo "Kill the lowest pid first, then re-run the above commands until all processes are dead."
  fi
elif [ "$opt" = "restart" ]; then
  ./server.sh stop
  sleep 2s
  ./server.sh start
fi
