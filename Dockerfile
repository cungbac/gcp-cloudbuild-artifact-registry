# Getting python 3.9
FROM python:3.9.18-alpine

# Copying my app to the image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies from requirements.txt
RUN pip install -r requirements.txt

# Startup command to serve our app
CMD exec gunicorn --bin :$PORT --workers 1 --threads 8 main:app