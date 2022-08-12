VENV := qrcode
PYTHON := python
BIN := $(VENV)/bin

.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment with pipenv
	pipenv --three && pipenv shell

.PHONY: install
install: venv ## Install or update dependencies with pipenv
	pipenv install

freeze: ## Pin current dependencies with pipenv
	pipenv run pip freeze > requirements.txt

.PHONY: start
start: ## Run the script
	$(PYTHON) freecodecamp.py > data/freecodecamp.txt
