FROM python:3.12

# Create a non-root user
RUN useradd -m appuser

# Set work directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download wait-for-it.sh
RUN apt-get update && apt-get install -y curl && \
    curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh && \
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Copy the rest of the application
COPY . .

# Change ownership to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Define the default command
CMD ["bash", "-c", "./wait-for-it.sh db:5432 -- python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]