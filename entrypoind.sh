#!/usr/bin/env bash
# data=`sqlite3 ./db.sqlite3 "SELECT id FROM auth_user WHERE username='admin'"`
# echo $data
# if [[ $data ]]; then
#     echo "test"
# fi

# if [ `sqlite3 ./db.sqlite3 "SELECT id FROM auth_user WHERE username='admin'"` ]; then
#     echo "test"
# fi

FILE=./db.sqlite3

if ! test -f "$FILE"; then
    python manage.py migrate
    echo "migrate"
fi

# if [ `sqlite3 ./db.sqlite3 "SELECT id FROM auth_user WHERE username='admin'"` ]; then
#     echo "test"
# fi

