FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Both web server and bot running via background subshell
CMD python3 web.py & exec python3 main.py
