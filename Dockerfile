FROM rajcsanyiladislavit/spark_sedona_delta:latest

WORKDIR /app

# Install Project related Python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
