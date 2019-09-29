format: ## Format code
	isort --recursive .
	black .


runserver:
	python manage.py runserver