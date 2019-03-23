#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE DATABASE djangoreactredux_db;
    CREATE USER djangoreactredux WITH PASSWORD 'djangoreactredux';
    ALTER ROLE djangoreactredux SET client_encoding TO 'utf8';
    ALTER ROLE djangoreactredux SET default_transaction_isolation TO 'read committed';
    ALTER ROLE djangoreactredux SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE djangoreactredux_db TO djangoreactredux;
EOSQL