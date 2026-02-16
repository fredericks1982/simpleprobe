FROM python:latest-slim

WORKDIR /app

COPY server.py .

ENV PORT=2982

EXPOSE 2982

CMD ["python", "server.py"]
