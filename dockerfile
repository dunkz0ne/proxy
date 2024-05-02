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

# Expose the port on which the Flask app will run
EXPOSE 5000


# Set the entrypoint command to run the WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]