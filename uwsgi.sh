#! /bin/bash

opt=$1
if [ "$opt" = "start" ]; then
  nohup uwsgi --socket 127.0.0.1:5000 --wsgi-file run.py --master --processes 4 --threads 2 --stats 127.0.0.1:5050 --callable app --pidfile uwsgi.pid &
elif [ "$opt" = "stop" ]; then
  pidfile="uwsgi.pid"
  pid=$(cat "$pidfile")
  kill -s SIGINT "$pid"
fi
