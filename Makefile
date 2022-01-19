all: lint test

test:
	make -C ./tests/

lint:
	flake8
