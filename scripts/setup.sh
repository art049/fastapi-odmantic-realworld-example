#!/bin/bash
set -e
poetry install
poetry run pre-commit install
echo -e "\e[1mProject has been setup successfully\e[0m"
