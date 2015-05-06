#! /bin/bash
# Usage: ./server.sh [start | stop | restart]
# User must have superuser privilages to run this script.

base="/tmp/server/"
archive="archive/"
apppidfile="uwsgi.pid"
applogfile="app.log"
testpidfile="test_uwsgi.pid"
testlogfile="test.log"
apppid="$base""$apppidfile"
applog="$base""$applogfile"
testpid="$base""$testpidfile"
testlog="$base""$testlogfile"


opt=$1
if [ "$opt" = "start" ]; then
  # both $apppid and $testpid must not exist or must be empty
    if [ ! -s "$apppid" ] && [ ! -s "$testpid" ]; then
    if [ ! -d "$base""$archive" ]; then
      sudo mkdir -p "$base""$archive"
    fi
    if [ ! -f "$testpid" ]; then
      sudo touch "$testpid"
    fi
    if [ ! -f "$apppid" ]; then
      sudo touch "$apppid"
    fi
    if [ ! -f "$testlog" ]; then
      sudo touch "$testlog"
    else
      echo "Moving old log files to $base$archive"
      sudo mv "$testlog" "$base""$archive"$(date +"%m-%d-%y-%T")"-$testlogfile"
      sudo touch "$testlog"
    fi
    if [ ! -f "$applog" ]; then
      sudo touch "$applog"
    else
      sudo mv "$applog" "$base""$archive"$(date +"%m-%d-%y-%T")"-$applogfile"
      sudo touch "$applog"
    fi
    echo "Creating pid and log files in $base"

  sudo chmod a+w "$testlog"
  sudo chmod a+w "$applog"
  sudo chmod a+w "$testpid"
  sudo chmod a+w "$apppid"
  
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
  if [ -s "$apppid" ] || [ -s "$testpid" ]; then
    pid=$(cat "$apppid")
    echo "Killing prod uwsgi server"
    sudo kill -s SIGINT "$pid"
    sudo rm "$apppid"
    echo "Killing test uwsgi server"
    pid=$(cat "$testpid")
    sudo kill -s SIGINT "$pid"
    sudo rm "$testpid"
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
