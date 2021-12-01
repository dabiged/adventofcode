SHELL := /usr/bin/env bash
PYLINT = pylint

PYTHONFILES = $(shell find  -name '*.py' | grep -v 'template'| grep -v filehelper)

#######
# Help
#######

.DEFAULT_GOAL := help
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: run
run: ## Run all code specified in main.py
	python main.py

.PHONY: test
test: ## Run All tests
	python -m pytest

.PHONY: pylint
pylint: ## Run pylint on all python files
	python -m pylint $(PYTHONFILES)

%.pylint: ## Run pylint on one file: i.e. make day01.pylint
	python -m pylint $*.py	

.PHONY: pyclean
pyclean: ## Run py3clean to remove __pycache__ and *.pyc files
	py3clean .
