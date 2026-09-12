FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Background me Web Server aur Bot dono ek saath chalane ke liye
CMD python web.py & python main.py

