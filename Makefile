install:
	@pip install -r requirements.txt

test:
	@python -m unittest discover -s helm/tests -p "test_*.py" -v

clean-pycache:
	@find . -name "__pycache__" -exec rm -r {} +

lint:
	@flake8 helm/

test-coverage:
	@coverage run -m unittest discover -s helm/tests -p "test_*.py" -v
	@coverage report -m