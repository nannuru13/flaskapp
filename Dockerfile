# Use the official Python image for ARM64 as the base image
FROM python:3.9-slim-bullseye AS base

# Set the working directory inside the container
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Expose the port that the Flask application will run on
EXPOSE 8080

# Set the environment variables
ENV MYSQL_HOST=host.docker.internal
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=Nskr@5411
ENV MYSQL_DATABASE=my

# Use the base image as the runtime image
FROM base AS runtime

# Run the Flask application
CMD ["python", "app.py"]
