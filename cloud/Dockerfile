FROM python:3.11-slim
WORKDIR /app
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY cloud.py /app/cloud.py
CMD ["python", "/app/cloud.py"]