#!/bin/bash
poetry run uvicorn --app-dir ./src/ api:app
