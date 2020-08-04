install:
	pip install --upgrade pip
	pip install -e .['dev']


format:
	isort **/*.py
	black -l 79 **/*.py
	flake8 **/*.py


run: export FLASK_APP = xadrez.app
run: export FLASK_ENV = development
run:
	flask run
