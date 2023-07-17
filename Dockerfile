FROM nikolaik/python-nodejs:python3.8-nodejs14 as base

WORKDIR /var/www
COPY . .

# Install Python Dependencies
RUN ["pip", "install", "-r", "flask_react_starter/starter_app/requirements.txt"]

# Move our react build for Flask to serve
# Use cp here because we're copying files inside our working directory, not from
# our host machine.
RUN ["cp", "-r", "flask_react_starter/starter_app/app/static/static/js", "flask_react_starter/starter_app/app/static"]
RUN ["cp", "-r", "flask_react_starter/starter_app/app/static/static/css", "flask_react_starter/starter_app/app/static"]

# Setup Flask environment
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV SQLALCHEMY_ECHO=True

EXPOSE 8000

# Run flask environment
CMD gunicorn app:app
