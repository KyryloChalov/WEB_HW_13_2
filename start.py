import os


commands = [
    # "poetry shell",
    "poetry update package",
    "docker pull postgres",
    "docker run --name hw13-app-postgres -p 5432:5432 -e POSTGRES_PASSWORD=8032573 -d postgres",
    "python manage.py migrate",
    "python manage.py createsuperuser",
    "python manage.py loadauthors data/authors.json",
    "python manage.py loadquotes data/quotes.json",
    "python manage.py runserver",
]


def run_command(command):
    print("Running command: {}".format(command))
    os.system(command)


for command in commands:
    run_command(command)
