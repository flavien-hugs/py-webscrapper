VENV := qrcode
PYTHON := python
BIN := $(VENV)/bin
SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

.PHONY: qrcode
qrcode: ## Make a new virtual environment with pip
	python3 -m venv $(VENV)
	source $(BIN)/activate
	python3 -m pip install --upgrade pip

.PHONY: pip-install
pip-install: ## Make venv and install requerements with pip
	$(BIN)/pip install --upgrade -r requirements.txt

.PHONY: venv
venv: ## Make a new virtual environment with pipenv
	pip3 install pipenv
	pipenv --three && pipenv shell

.PHONY: install
install: venv ## Install or update dependencies with pipenv
	pipenv install

freeze: ## Pin current dependencies with pipenv
	pipenv lock -r > requirements.txt

.PHONY: test
test: ## Run tests
	flake8 --statistics

.PHONY: start
start: ## Run the script
	$(PYTHON) start.py > data/data.html
