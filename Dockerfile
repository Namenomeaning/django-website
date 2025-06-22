# Dockerfile for running the e-commerce Django project on Python 3.8

FROM python:3.8-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirement.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirement.txt

# Copy application code
COPY . .

# Expose Django default port
EXPOSE 8000

# Run migrations and start development server by default
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]


scp -i "C:\Users\pvaqu\Downloads\test.pem" -r "C:\Users\pvaqu\Downloads\django-website-main.zip" 
