FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

COPY . .

# Mở cổng 5000 cho Flask
EXPOSE 5000

ENV FLASK_ENV=production

# Lệnh để chạy ứng dụng Flask
CMD ["python", "app.py"]
