#! /bin/bash
# Usage: sudo ./server.sh
# MUST BE SUPER USER TO COMPLETE


apppid="uwsgi.pid"
applog="app.log"
testpid="test_uwsgi.pid"
testlog="test.log"

opt=$1
if [ "$opt" = "start" ]; then
  # both $apppid and $testpid must not exist
  if [ ! -r "$apppid" ] && [ ! -r "$testpid" ]; then
    echo "Copying nginx config to /etc/nginx/sites-enabled/default"
    cp nginx.conf /etc/nginx/sites-enabled/default
    echo "Checking is nginx is running"
    if [ -r "/run/nginx.pid" ]; then
      echo "Nginx is running."
      echo "Reloading nginx"
      nginx -s reload
    else
      echo "Nginx is not running."
      echo "Starting nginx."
      nginx
    fi
    echo "Starting prod uwsgi server on port 5000, logs located at $applog"
    nohup uwsgi --socket 127.0.0.1:5000 --wsgi-file run.py --master --processes 4 --threads 2 --stats 127.0.0.1:5001 --callable app --pidfile "$apppid" &> "$applog" &
    echo "Starting test uwsgi server on port 5050, logs located at $testlog"
    nohup uwsgi --socket 127.0.0.1:5050 --wsgi-file test_run.py --master --processes 4 --threads 2 --stats 127.0.0.1:5051 --callable test_app --pidfile "$testpid" &> "$testlog" &
    echo "Success, the server is now running."
  else
    echo "Server already running, please run [sudo ./server.sh restart] to quit and restart the server"
  fi
elif [ "$opt" = "stop" ]; then
  if [ -r "$apppid" ] || [ -r "$testpid" ]; then
    pid=$(cat "$apppid")
    echo "Killing prod uwsgi server"
    kill -s SIGINT "$pid"
    rm "$apppid"
    echo "Killing test uwsgi server"
    pid=$(cat "$testpid")
    kill -s SIGINT "$pid"
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
  sleep 1s
  ./server.sh start
fi
