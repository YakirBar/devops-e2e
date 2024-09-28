# # Use the official Python image as a base image
# FROM python:3.8-slim

# # Install required packages
# RUN pip install selenium

# # Set the working directory
# WORKDIR /app

# # Copy your Selenium WebDriver script into the container
# COPY . .

# # Define the command to execute your script
# CMD ["python", "google_check.py"]

# Use a base image with Python
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm chromedriver_linux64.zip

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Command to run your Selenium script
CMD ["python", "google_check.py"] # Replace with your Selenium script
