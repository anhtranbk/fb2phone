# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required binary packages
RUN apt-get update -y
RUN apt-get install -y gcc

# Install any needed packages specified in requirements.txt
RUN pip install -U pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run run.sh when the container launches
CMD ["bash", "/bin/docker-web"]
