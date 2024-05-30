FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    mysql-client \
    libmysqlclient-dev \
    pkg-config \
    build-essential

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Create working directory
RUN mkdir /code
WORKDIR /code

# Install Python dependencies
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Add application code
ADD . /code/

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "backend.py"]
