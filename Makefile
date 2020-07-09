VERSION := $(shell git rev-parse --abbrev-ref HEAD | sed -E 's/^.*?([0-9][.][0-9]+[.][0-9]+).*$$/\1/g')

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

test:
	pip install -U -r requirements/test.txt
	python -B -m pytest -v --cov-report=xml --flake8
	bandit --verbose --exclude tests,.git,requirements .

build: clean-pyc
	grep -rlI '\^__VERSION__\^' ./ | xargs sed -i 's/\^__VERSION__\^/${VERSION}/g'
	docker build -t test-rest-api:${VERSION} .

version:
	@echo ${VERSION}