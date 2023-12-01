#!/bin/sh
# wait-for-mysql.sh
set -e
host="$1"
shift
cmd="$@"
until MYSQL_PASSWORD="Veneberg!255724" mysql -h "$host" -d "db_library" -U "veneberg" -c '\q';>
  >&2 echo "Mysql is unavailable - sleeping"
  sleep 1
done
>&2 echo "Mysql is up - executing command"
exec $cmd

