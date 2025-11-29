run:
	python3 src/fizzbuzz/fizzbuzz.py

test:
	pytest

install:
	pip3 install -r requirements.txt

lint:
	python3 -m py_compile src/fizzbuzz/*.py

help:
	@echo "make run    - run the fizzbuzz script"
	@echo "make test   - run unit tests"
	@echo "make lint   - run basic syntax lint"
	@echo "make install - install dependencies"

