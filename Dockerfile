# Use the base Python image
FROM python:3.8-slim-buster

# Create and set the working directory
WORKDIR /app

# Copy requirements.txt to the container and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your source code into the container
COPY . .

# Expose the port on which your Flask app will run (optional)
EXPOSE 8080

# Set the command to activate the virtual environment and run your Flask app
# ... (previous Dockerfile instructions)

# Set the command to activate the virtual environment and run your Flask app
CMD ["bash", "-c", "source /app/devspace-env/Scripts/activate && flask run --host=0.0.0.0 --port=5000"]


