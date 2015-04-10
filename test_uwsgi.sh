#! /bin/bash

pidfile="test_uwsgi.pid"

opt=$1
if [ "$opt" = "start" ]; then
  nohup uwsgi --socket 127.0.0.1:5050 --wsgi-file test_run.py --master --processes 2 --threads 2 --stats 127.0.0.1:5051 --callable test_app --pidfile "$pidfile" > test.log &
elif [ "$opt" = "stop" ]; then
  pid=$(cat "$pidfile")
  kill -s SIGINT "$pid"
fi
