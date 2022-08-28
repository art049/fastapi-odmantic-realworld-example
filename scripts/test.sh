#!/bin/bash
# pytest -n auto -s -c pytest.ini
export APIURL=http://localhost:8000
./realworld/api/run-api-tests.sh
