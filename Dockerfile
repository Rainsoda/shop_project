# Pull from base image
FROM python:3.10.11-slim-bullseye

# Update and install applications
RUN apt-get update && apt-get install -y \
    neovim \
    tree \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /usr/src/app/online_shop

# Install dependencies
COPY ./online_shop/requirements.txt .
RUN python -m pip install --no-cache-dir --requirement requirements.txt

# Copy all files
COPY ./online_shop .
