# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port (8000) and Streamlit port (8501)
EXPOSE 8000
EXPOSE 7860

# Command to run FastAPI and Streamlit concurrently
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/visualizer.py --server.port 7860 --server.address 0.0.0.0"]
