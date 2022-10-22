seed:
	python data_seeding.py

test:
	pytest

install: 
	pip3 install -r requirements.txt

start_database:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

run_project:
	python3 manage.py run
