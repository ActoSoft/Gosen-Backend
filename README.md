# Gosen-Backend
Repository with the Backend App of Gosen Project

# Run in Locally
1. Clone the repo
2. Create a python virtual environment and activate it
3. cd to gosenProject/ folder that contains all the the Django project
4. Run pip ```install -r requirements.txt``` to install all the python packages used in this project.
5. Create a .env into the root gosenProject folder, copy the .env.example file and paste it into .env, config your own environment variables
5. Create a superuser with ```./manage.py createsuperuser``` to access to Django Admin Panel
6. Open another terminal tab and run ```rabbitmq-server``` used as broker of Celery
7. open another terminal tab, active the virualenv and ```run celery -A gosenProject worker --loglevel=info``` to run Celery worker
8. Run ```./manage.py runserver``` in the main terminal tab to run the Django local server