install-requirements:
	pip install -r requirements.txt


migrate:
	python manage.py migrate


format: ## Format code
	isort --recursive .
	black .


populate-db:
	cat cards/scripts.py | python manage.py shell


runserver:
	python manage.py runserver