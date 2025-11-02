# Sử dụng Python làm base image
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy toàn bộ mã nguồn vào container
COPY . /app

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng (nếu chatbot chạy trên HTTP server)
EXPOSE 5000

# Lệnh chạy ứng dụng
CMD ["python", "app.py"]