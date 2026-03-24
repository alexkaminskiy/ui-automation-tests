# Use the official Python image as a base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app


# Install OS-level dependencies required by Playwright browsers
# (this is required even when using `playwright install --with-deps`)
RUN apt-get update && apt-get install -y wget gnupg unzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

# Copy the rest of the application code
COPY . .

# Ensure run.sh is executable
RUN chmod +x run.sh

# Command to run tests
CMD ["./run.sh"]