#! /bin/bash
export TEST_API_URL="http://celebrapsheet.tk/api/tests"
pidfile="uwsgi.pid"

opt=$1
if [ "$opt" = "start" ]; then
  nohup uwsgi --socket 127.0.0.1:5000 --wsgi-file run.py --master --processes 4 --threads 2 --stats 127.0.0.1:5001 --callable app --pidfile "$pidfile" > app.log &
elif [ "$opt" = "stop" ]; then
  pid=$(cat "$pidfile")
  kill -s SIGINT "$pid"
fi
