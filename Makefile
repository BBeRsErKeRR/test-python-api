test:
	pip install -r requirements/test.txt
	python -B -m pytest --flake8 --cov-report=xml
	bandit --verbose --exclude tests --recursive

build:
	docker build -t 'test-rest-api'