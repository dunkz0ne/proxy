# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy the rest of the application code to the working directory
COPY . .

# Set the entrypoint command to run the WSGI server with HTTP
CMD gunicorn --bind 0.0.0.0:$PORT app:app
