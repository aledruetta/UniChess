install:
	pip install -e .['dev']


format:
	isort **/*.py
	black -l 79 **/*.py
	flake8 **/*.py
