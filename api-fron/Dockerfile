FROM python:3

# Create working directory
RUN mkdir /code
WORKDIR /code

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Add application code
ADD . /code/

# Expose the application port
EXPOSE 5001

# Command to run the application
CMD ["python", "front.py"]
