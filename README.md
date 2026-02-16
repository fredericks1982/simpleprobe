# Simple Probe

A minimal HTTP probe that serves a "Hello World" page. Useful for verifying network connectivity, testing reverse proxies, or checking that a tunnel (e.g. Cloudflare) is working.

## Local Install

Copy `server.py` to your machine, then run:

```sh
SIMPLEPROBE_PORT=9090 python server.py
```

Open `http://localhost:9090` in your browser. You should see a "Hello World" page.

The `SIMPLEPROBE_PORT` environment variable controls which port the probe listens on. If omitted, it defaults to `9090`.

## Container Install

1. Create a folder and copy these three files into it:
   - `server.py`
   - `Dockerfile`
   - `docker-compose.yml`

2. Start the container:

```sh
docker compose up -d
```

The probe will be available on port `2982` (mapped to `9090` inside the container). Open `http://localhost:2982` to verify.

To stop the container:

```sh
docker compose down
```

## Configuration

| Variable | Default | Description |
|---|---|---|
| `SIMPLEPROBE_PORT` | `9090` | Port the probe listens on inside the container (or locally) |

The `docker-compose.yml` maps external port `2982` to internal port `9090`. Edit the `ports` section if you need a different external port.
