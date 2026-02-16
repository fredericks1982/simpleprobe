FROM python:3.13-slim
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
RUN useradd --create-home probe
USER probe
WORKDIR /home/probe/app
