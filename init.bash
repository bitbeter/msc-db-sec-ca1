#!/bin/bash

echo "[INIT] Building Database"
# Rebuild Database
psql -h localhost -U postgres -f ./sql/rebuild-database.sql
echo "[INIT] Databse with name dbsecca1 has been created"

# Create Tables
psql -h localhost -U postgres dbsecca1 < ./sql/create-tables.sql
echo "[INIT] Tables initiated"

# Install python packages
pip install -r requirements.txt