# Use an official Python runtime as a base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    --no-install-recommends

# Add Chrome repository and install Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Set display port to avoid crash in headless mode
ENV DISPLAY=:99

# Copy the current directory contents into the container
WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip install selenium

# Run the Selenium script
CMD ["python", "./selenium_script.py"]
