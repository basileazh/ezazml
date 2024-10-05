install-dependencies:
	echo "Installing dependencies..."
	poetry install

.PHONY: create-datastore
create-datastore: install-dependencies
	echo "Creating datastore..."
	poetry run aml create-or-update-adls-datastore

.PHONY: run-tests
run-tests: install-dependencies
	echo "Running tests..."
	poetry run pytest tests/ -v -s

.PHONY: run-tests-cov
run-tests-cov: install-dependencies
	echo "Running tests with coverage..."
	poetry run pytest tests/ -v -s --cov=src --cov-report=term-missing

.PHONY: clean-tests-files
clean-tests-files:
	echo "Cleaning tests files..."
	rm -rf tests/__pycache__/
	rm -rf tests/.pytest_cache/
	rm -rf tests/.coverage
	rm -rf tests/temp/
	rm -rf "tests/temp/"
