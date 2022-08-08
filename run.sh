#!/bin/bash

exec python3 ./init_db.py &
exec python3 ./app.py