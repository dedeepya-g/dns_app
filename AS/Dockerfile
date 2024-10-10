# AS/Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY as_server.py .

RUN pip install Flask

CMD ["python", "as_server.py"]

