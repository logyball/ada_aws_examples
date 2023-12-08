venv:
	python3 -m virtualenv venv

install:
	pip install -r ./requirements.txt

run:
	python main.py
