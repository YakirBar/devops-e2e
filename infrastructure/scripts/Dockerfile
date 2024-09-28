# Use the slim version of Python 3.8
FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    libxi6 \
    libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install Selenium
RUN pip install --no-cache-dir selenium

# Copy your Python script
COPY google_check.py /app/google_check.py

# Set the working directory
WORKDIR /app

# Command to run your script
CMD ["python", "google_check.py"]
