# Uses a base image of Python 3.11
FROM python:3.11

# Sets the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the /app directory
COPY requirements.txt /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Flask
RUN pip install requests
RUN pip install openai
# pip install openai==0.28 (sometimes it asks to specify the openai version, you can try with this version)


# Copy the app.py file to the /app directory (if it is located in a different folder)
COPY app.py /app

# Exposes port 8080
EXPOSE 8080

# Specifies the start command to run the Python application.
CMD ["python", "/app/app.py"]

