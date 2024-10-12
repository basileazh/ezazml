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
	poetry run ezazml create-mltable $(DATA_PATH) $(DATA_MLTABLE_SAVE_PATH) \
		--inputs-extension=$(DATA_INPUTS_EXTENSION) \
		--data-description "$(DATA_DESCRIPTION)" \
		--headers=$(DATA_HEADERS) \  # only for csv
		--infer-column-types \  # only for csv, is a flag, remove it not to infer column types
		# --include-path-column \  # is a flag, remove it not to include the path column
		--keep-columns $(DATA_KEEP_COLUMNS) \
		--drop-columns $(DATA_DROP_COLUMNS)

# Development

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
