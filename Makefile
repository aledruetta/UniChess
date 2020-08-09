install:
	pip install --upgrade pip
	pip install -e .['dev']


run: export FLASK_APP = xadrez.app
run: export FLASK_ENV = development
run:
	flask run


format:
	isort .
	black -l 79 -t py38 .
	flake8 setup.py xadrez
