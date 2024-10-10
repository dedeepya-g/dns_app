# FS/Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY fs_server.py .

RUN pip install Flask

CMD ["python", "fs_server.py"]

