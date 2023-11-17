# Use the official Python 3.9 image as the base image
FROM python:3.9

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Expose port 8000 for Nginx
EXPOSE 8000
EXPOSE 5000
# Create a directory for your application
WORKDIR /app

# Copy your Python application files into the container
COPY app.py /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Configure Nginx to serve your application on port 8000
RUN echo "server {" > /etc/nginx/sites-available/app \
    && echo "    listen 8000;" >> /etc/nginx/sites-available/app \
    && echo "    server_name localhost;" >> /etc/nginx/sites-available/app \
    && echo "    location / {" >> /etc/nginx/sites-available/app \
    # && echo "        proxy_pass http://127.0.0.1:8001;" >> /etc/nginx/sites-available/app \
    && echo "        root /var/www/html;" >> /etc/nginx/sites-available/app \
    && echo "    }" >> /etc/nginx/sites-available/app \
    && echo "}" >> /etc/nginx/sites-available/app \
    && ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/

# Remove the default Nginx configuration
RUN rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Copy your HTML file to the default Nginx document root
COPY index.html /var/www/html/index.html

# Start Nginx and your Python application
CMD service nginx start && python app.py


