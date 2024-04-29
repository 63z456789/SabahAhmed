# Use an official Python runtime as a parent image
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir nltk

# Download NLTK data (uncomment if NLTK is used for stop word removal)
# RUN python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python", "./app.py"]
