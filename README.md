# ![RealWorld FastAPI + ODMantic App](logo.png)

<div align="center">

<!---
[![CircleCI](https://circleci.com/gh/......)](https://circleci.com/gh/...)
[![codecov](https://codecov.io/gh/.../........)](https://codecov.io/gh/.....)
[![Maintainability](https://api.codeclimate.com/v1/badges/......)](https://codeclimate.com/repos/....)
-->

![Python: 3.10](https://img.shields.io/badge/python-3.10-informational.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![mypy: checked](https://img.shields.io/badge/mypy-checked-informational.svg)](http://mypy-lang.org/)
[![Manager: poetry](https://img.shields.io/badge/manager-poetry-blueviolet.svg)](https://poetry.eustace.io/)

</div>

> ### [FastAPI](https://github.com/tiangolo/fastapi) + [ODMantic](https://github.com/art049/odmantic) codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld) spec and API.

[![CI](https://github.com/art049/fastapi-odmantic-realworld-example/actions/workflows/ci.yml/badge.svg)](https://github.com/art049/fastapi-odmantic-realworld-example/actions/workflows/ci.yml)
[![Realworld Tests](https://github.com/art049/fastapi-odmantic-realworld-example/actions/workflows/realworld-tests.yml/badge.svg)](https://github.com/art049/fastapi-odmantic-realworld-example/actions/workflows/realworld-tests.yml)

## Getting Started

### :hammer: Installation

- [Install Docker](https://docs.docker.com/engine/install/) (necessary to run a local MongoDB instance)
- Make sure Python 3.10 is available on your system
- Install [poetry](https://poetry.eustace.io/)
- Setup the environment `./scripts/setup.sh`

### :bulb: Useful scripts

- Start the MongoDB instance `./scripts/start-mongo.sh`
- Stop the MongoDB instance `./scripts/stop-mongo.sh`
- Start the FastAPI server `./scripts/start.sh`
- Format the code `./scripts/format.sh`
- Manually run the linter `./scripts/lint.sh`
- Manually run the tests `./scripts/test.sh`

## Coming Soon

- [ ] Articles with details on every single step required to build this app
- [ ] Testing
- [ ] Deployment on AWS with MongoDB Atlas
