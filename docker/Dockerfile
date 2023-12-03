# Use an official base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /usr/app/src

# Copy the files to working directory
COPY requirements.txt ./
COPY py_test_api ./framework/py_test_api

# Install any required system dependencies
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install --no-cache-dir -r requirements.txt






