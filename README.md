# ![RealWorld FastAPI + ODMantic App](logo.png)

<div align="center">

<!---
[![CircleCI](https://circleci.com/gh/......)](https://circleci.com/gh/...)
[![codecov](https://codecov.io/gh/.../........)](https://codecov.io/gh/.....)
[![Maintainability](https://api.codeclimate.com/v1/badges/......)](https://codeclimate.com/repos/....)
-->

![Python: 3.11](https://img.shields.io/badge/python-3.11-informational.svg)
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

- [Install Docker](https://docs.docker.com/engine/install/)
- Build and run: docker-compose up api

### :bulb: Useful scripts

- Unit tests: docker-compose up unit-tests
- Integration tests: docker-compose up integration-tests
- Linting and other tests: docker-compose up pre-commit

## Coming Soon

- [ ] Articles with details on every single step required to build this app
- [ ] Unit Testing
- [ ] Deployment on AWS with MongoDB Atlas
