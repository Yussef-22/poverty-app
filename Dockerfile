# ----------------------------------------------------------
# Base Image: Slim Python for smaller final image
# ----------------------------------------------------------
FROM python:3.10-slim

# ----------------------------------------------------------
# Working directory inside container
# ----------------------------------------------------------
WORKDIR /app

# ----------------------------------------------------------
# Install system-level dependencies for XGBoost & Pandas
# ----------------------------------------------------------
# Comment: libgomp1 is required for XGBoost's runtime.
# Comment: gcc/g++ allow loading compiled model objects.
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------------------------------------
# Copy requirements first for Docker layer caching
# ----------------------------------------------------------
COPY requirements.txt .

# ----------------------------------------------------------
# Install Python dependencies
# ----------------------------------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# ----------------------------------------------------------
# Copy the application code (app.py + models + utils)
# ----------------------------------------------------------
COPY . .

# ----------------------------------------------------------
# Expose Streamlit port (internal)
# ----------------------------------------------------------
EXPOSE 8600

# ----------------------------------------------------------
# Start Streamlit app inside the container
# ----------------------------------------------------------
# Comment: We explicitly force the port to 8600.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

