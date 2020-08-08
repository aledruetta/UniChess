install:
	pip install --upgrade pip
	pip install -e .['dev']


run: export FLASK_APP = xadrez.app
run: export FLASK_ENV = development
run:
	flask run


format:
	isort **/*.py
	black -l 79 **/*.py
	flake8 **/*.py
