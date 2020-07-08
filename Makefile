
venv:
	virtualenv venv

test: venv
	venv/bin/pip install -r requirements/test.txt
	venv/bin/python -B -m pytest --flake8 --cov-report=xml
	venv/bin/bandit --verbose --exclude venv,tests --recursive

build:
	docker build -t 'test-rest-api'