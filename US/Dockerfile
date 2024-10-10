# US/Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY us_server.py .

RUN pip install Flask requests

CMD ["python", "us_server.py"]

