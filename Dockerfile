# Use the official Python image as a base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# # Install Allure CLI
# RUN apt-get update && \
#     apt-get install -y openjdk-11-jre && \
#     curl -o allure-commandline.zip -L https://github.com/allure-framework/allure2/releases/download/2.21.0/allure-2.21.0.zip && \
#     unzip allure-commandline.zip -d /opt/ && \
#     ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure
# RUN sudo playwright install 

# Copy the rest of the application code
COPY . .

# Ensure run.sh is executable
RUN chmod +x run.sh

# Command to run tests
CMD ["./run.sh"]