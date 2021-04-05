SHELL := /bin/bash

.PHONY: build
build:
	python3 -m pip install -r requirements.txt
	python3 -m pip install --upgrade build
	python3 -m build

.PHONY: publish
publish:
	python3 -m twine upload --skip-existing dist/*

.PHONY: test
test:
	python setup.py pytest

