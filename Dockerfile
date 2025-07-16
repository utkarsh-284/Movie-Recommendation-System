FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install system dependencies for FAISS
RUN apt-get update && \
    apt-get install -y libopenblas-dev libgomp1 && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements first for better cache
COPY app/requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application code
COPY app/ ./

# Create /data directory and copy the model file
RUN mkdir -p /data \
    && cp /app/data/movie_recommender_v02.joblib /data/movie_recommender_v02.joblib

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]