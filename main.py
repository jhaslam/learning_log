# Required by Google App Engine.

# By default, app engine looks for a WSGI-compatible object 
# called "app" inside main.py, which should be located at
# the project root. 

# In this case, we are using the application object in 
# learning_log/wsgi.py without additional configuration.

# Alternatively, we can add a custom entrypoint field in our 
# app.yaml file as such:
# entrypoint: gunicorn -b :$PORT mysite.wsgi

from learning_log.wsgi import application

app = application