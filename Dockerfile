FROM python:latest-slim

WORKDIR /app

COPY server.py .

ENV PORT=1982

EXPOSE 1982

CMD ["python", "server.py"]
