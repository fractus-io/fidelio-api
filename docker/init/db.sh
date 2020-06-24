#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "root" --dbname "root" <<-EOSQL
    CREATE DATABASE fidelio;
    GRANT ALL PRIVILEGES ON DATABASE fidelio TO root;
EOSQL
