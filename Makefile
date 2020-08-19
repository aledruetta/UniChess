install:
	pip install --upgrade pip
	pip install -e .['dev']

run: export FLASK_APP=unichess/app
run: export FLASK_ENV=development
run:
	flask run

format:
	isort .
	black -l 79 -t py38 .
	flake8 setup.py unichess

clean:
	@find . -name '*.py[co]' -exec rm --force {} \;
	@find . -name '*~' -exec rm --force {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

init_db: export FLASK_APP=unichess/app.py
init_db:
	flask create-db
	flask db upgrade

test: export FLASK_ENV=test
test:
	pytest tests/ -v --cov=unichess
