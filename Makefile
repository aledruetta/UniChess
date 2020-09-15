install:
	pip install --upgrade pip
	pip install -e .['dev'] --use-feature=2020-resolver
	pip check

run: export FLASK_APP=unichess/app
run: export FLASK_ENV=development
run:
	flask run

lint:
	isort .
	black -l 79 -t py38 --exclude migrations .
	flake8 setup.py unichess
	# shellcheck scripts/*

clean:
	@find . -name '*.py[co]' -exec rm --force {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm --force {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

initdb:
	FLASK_APP=unichess.app flask dropdb
	FLASK_APP=unichess.app flask db upgrade

test:
	FLASK_ENV=test pytest tests/ -v --cov=unichess
