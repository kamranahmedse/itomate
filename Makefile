.PHONY: setup

setup:
	python -m venv venv
	source venv/bin/activate
	pip install --upgrade setuptools wheel twine

install:
	pip install -e .

build:
	rm -rf build dist
	python setup.py sdist bdist_wheel

publish:
	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
