# Installation

.PHONY: install-dependencies
install-dependencies:
	echo "Installing dependencies..."
	poetry install

# Azure ML Workspace Setup

.PHONY: create-or-update-adls-datastore
create-or-update-adls-datastore: install-dependencies
	echo "Creating datastore..."
	poetry run ezazml create-or-update-adls-datastore

.PHONY: create-mltable
create-mltable: install-dependencies
	echo "Creating MLTable..."
	poetry run ezazml create-mltable $(DATA_PATH) \
		--mltable-save-path=$(DATA_MLTABLE_SAVE_PATH) \
		--inputs-extension=$(DATA_INPUTS_EXTENSION) \
		--data-description "$(DATA_DESCRIPTION)" \
		--headers=$(DATA_HEADERS) \
		--infer-column-types \
		--keep-columns $(DATA_KEEP_COLUMNS) \
		--drop-columns $(DATA_DROP_COLUMNS)
# --include-path-column \  # is a flag, remove it not to include the path column

# Development

.PHONY: clean-pycache

.PHONY: clean-tests-files
clean-tests-files:
	echo "Cleaning tests files..."
	rm -rf tests/__pycache__/
	rm -rf tests/.pytest_cache/
	rm -rf tests/.coverage
	rm -rf tests/temp/
	rm -rf "tests/temp/"

clean-pycache:
	echo "Cleaning pycache files..."
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name ".pytest_cache" -exec rm -rf {} +
	pytest --cache-clear

.PHONY: run-tests
run-tests: install-dependencies clean-tests-files clean-pycache
	echo "Running tests..."
	poetry run pytest tests/ -v -s

.PHONY: run-tests-cov
run-tests-cov: install-dependencies clean-tests-files clean-pycache
	echo "Running tests with coverage..."
	poetry run pytest tests/ -v -s --cov=src --cov-report=term-missing
