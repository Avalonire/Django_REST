#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

until [ PGPASSWORD="avalon667788" psql -h "$host" -d "library" -U "avalon" -c '\q' ] ; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
