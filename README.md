
# Swe_t.py's Celebrity Rap Sheet Website

## Overview
This project is a webite with information on celebrities and their alleged crimes.

## Ways to start the website
### Start server for debugging
The website may be run for debugging purposes in flask without starting an nginx server. The server will listen to port 5000 by default, but a specific port may be provide with the -p option, as in the following command

```python3 run.py -p <port number>```

The port must be enabled to be accessed by external servers. It is not enabled run:

```sudo ufw allow <port num>```

