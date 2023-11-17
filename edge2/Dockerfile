# FROM python:3.9

# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# COPY app.py /app/

# RUN chmod +x app.py

# CMD python app.py

# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run your Python application when the container starts
CMD ["python", "app.py", "&"]
