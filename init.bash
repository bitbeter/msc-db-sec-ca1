#!/bin/bash

echo "[INIT] Rebuilding Database"
# Rebuild Database
psql -h localhost -U postgres -f ./sql/rebuild-database.sql
echo "[INIT] Databse with name dbsecca1 has been created"

# Create Tables
psql -h localhost -U postgres dbsecca1 < ./sql/create-tables.sql
echo "[INIT] Tables initiated"

# First data insertion
psql -h localhost -U postgres dbsecca1 < ./sql/first-insert.sql
echo "[INIT] First Data Insertion"

# Test data insertion
psql -h localhost -U postgres dbsecca1 < ./sql/test-insert.sql
echo "[INIT] Test Data Insertion"

# Install python packages
pip install -r requirements.txt
echo "[INIT] Python3 requiermetns has been installed"