FROM python:latest-slim

WORKDIR /app

COPY server.py .

ENV SIMPLEPROBE_PORT=9090

EXPOSE 9090

CMD ["python", "server.py"]
