# Use official Python slim image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /aiogrambot

# Update the package manager and install necessary build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other files to the working directory
COPY . /aiogrambot

# Clean up build dependencies to reduce image size
RUN apt-get purge -y --auto-remove build-essential

# Run the bot using python
ENTRYPOINT [ "python3", "run.py" ]
