FROM python:3.10.8-slim-buster

# Update and install dependencies
RUN apt update && apt upgrade -y && apt install -y git

# Set working directory first
WORKDIR /FILTER-BOT

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the bot
CMD ["python", "bot.py"]
