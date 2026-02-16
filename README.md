# Simple Probe

Minimal HTTP probe serving a "Hello World" page. Used to verify Cloudflare tunnel connectivity.

## Usage

### Run locally

```sh
python server.py
```

### Custom port

```sh
PORT=9090 python server.py
```

### Devcontainer

Open the project in VS Code and select **Reopen in Container**. The probe starts automatically on port 1982.

## Configuration

Set the `PORT` environment variable in `.env` (default: `1982`).
