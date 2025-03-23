# Use the official Python image from the Docker Hub
FROM python:3.13.2-alpine3.21

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install build tools
RUN apk update && apk add --no-cache gcc musl-dev

# Copy the requirements file
COPY ./src/requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY ./src /app