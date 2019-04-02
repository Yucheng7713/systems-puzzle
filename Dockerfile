# Use an official Python runtime as a parent image
FROM python:3

# For showing docker log in python environment
ENV PYTHONUNBUFFERED 1

# Create the working directory : /opt/services/flaskapp/src
RUN mkdir -p /opt/services/flaskapp/src

# Copy requirements.txt to the working directory (image)
COPY requirements.txt /opt/services/flaskapp/src

# Set the working directory to /app
WORKDIR /opt/services/flaskapp/src

# Install required python libraries : Flask, psycopg2, SQLAlchemy, Flask-WTF
RUN pip install -r requirements.txt

# Copy the current directory contents (including installed packages) into the container at /opt/services/flaskapp/src
COPY . /opt/services/flaskapp/src

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Run app.py when the container launches
CMD ["python", "app.py"]
