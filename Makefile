clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

test:
	pip install -r requirements/test.txt
	python -B -m pytest --flake8 --cov-report=xml
	bandit --verbose --exclude tests --recursive

build: clean-pyc
	docker build -t 'test-rest-api'