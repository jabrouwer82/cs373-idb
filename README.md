
# Swe_t.py's Celebrity Rap Sheet Website

## Overview
This project is a website with information on celebrities and their alleged crimes.

## Get the Project

```git clone https://github.com/plberg/cs373-idb.git```

```cd cs373-idb```

## Install Dependencies
To install dependencies run 

```chmod +x install.sh```

```sudo ./install.sh```

## Create Postgres user and database

Make current unix user a postres superuser

```sudo -u postgres createuser --superuser $USER```

Get into postgres prompt

```sudo -u postgres psql```

Make a password, within the postgres prompt the unix username must be entered manually

``` postgres=# \password <USER>```

After entering a password, enter '\q' to exit the prompt.

Make a new database called 'celebsdb'

```sudo -u postgres createdb celebsdb```


## Initialize the database

Before starting the website server, the database must be initialized, to do this run:

```python3 initialize_db.py```

Once the database has been initialized, run this:

```sudo ./server.sh start```

And let the script handle the rest of the nginx and uwsgi startup/configuration.



### Starting the debugging server
The website may be run for debugging purposes in flask without starting an nginx server. The server will listen to port 5000 by default, but a specific port may be provide with the -p option, as in the following command. Be sure that the database is initialized before starting server (explained above)

```python3 run.py -p <port number>```

The port must be enabled to be accessed by external servers. If it is not enabled run:

```sudo ufw allow <port num>```


### Running the tests
To run the unit tests execute the command

``` python3 tests.py```

