# Pull official base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc python3-dev libmagic1 libffi-dev netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY ../requirements ./requirements
RUN pip install --upgrade pip \
    && pip install -r ./requirements/local.txt

# Copy all project files
COPY ../ /app