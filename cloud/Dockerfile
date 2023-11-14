FROM python:3.9

# Install Nginx for serving the UI
RUN apt-get update && apt-get install -y nginx

# Copy the UI HTML file into the container
COPY index.html /usr/share/nginx/html/index.html

# Copy the requirements.txt file into the container
COPY requirements.txt /app/requirements.txt

# Install any dependencies for your API
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the API code
COPY app.py /app/

# Expose both the UI and API ports
EXPOSE 80
EXPOSE 5000

# Start Nginx and your API when the container starts
CMD service nginx start && python /app/app.py

