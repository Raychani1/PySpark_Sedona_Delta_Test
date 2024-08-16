FROM rajcsanyiladislavit/local_geo_analysis:DB_12.2_LTS_ML

WORKDIR /app

# Install Project related Python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
