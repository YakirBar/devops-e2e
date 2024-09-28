# Use the official Python image as a base image
FROM python:3.8-slim

# Install required packages
RUN pip install selenium

# Set the working directory
WORKDIR /app

# Copy your Selenium WebDriver script into the container
COPY google_check.py .

# Define the command to execute your script
CMD ["python", "google_check.py"]