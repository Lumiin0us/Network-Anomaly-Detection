FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run your anomaly detection script
CMD ["python", "network_anomaly_forecasting/models/isolation_forest.py"]

