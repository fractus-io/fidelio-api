#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "root" --dbname "root" <<-EOSQL
    CREATE DATABASE incubator;
    GRANT ALL PRIVILEGES ON DATABASE incubator TO root;
EOSQL
