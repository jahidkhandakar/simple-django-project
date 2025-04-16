# Use an official Python image as the base image
FROM python:3.11-slim-bullseye AS build

# Set environment variables to prevent Python from writing .pyc files and to buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100

# Set the working directory in the container
WORKDIR /app

# Install system dependencies needed to build Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    gcc \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    default-libmysqlclient-dev \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Final image: Use a clean, minimal image
FROM python:3.11-slim-bullseye AS runtime

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy installed Python packages from the build stage
COPY --from=build /usr/local /usr/local

# Copy the rest of the application files into the container
COPY . .

# Expose port 8000 to allow access to the Django app
EXPOSE 8000

# Run the Django development server (replace with production server in actual deployment)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
