FROM ubuntu

# Install required system dependencies
RUN apt update && apt -y upgrade && apt install -y python3-pip python3-venv libpq-dev

# Create virtual environment
RUN python3 -m venv venv

# Copy application files
COPY app app
COPY frontend frontend
COPY tests tests
COPY requirements.txt .

# Install dependencies inside virtual environment
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose FastAPI default port
EXPOSE 8000

# Ensure ENTRYPOINT executes correctly
CMD ["./venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
