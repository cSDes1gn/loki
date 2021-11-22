# Loki Python

Modified: 2021-10

Sandbox environment for testing custom grafana images with preconfigured dashboards and configuring loki logging handlers for a python microservice.

## Quickstart
Startup the services
```bash
docker compose up
```

Open the grafana dashboard at http://localhost:3000 login with default username: `admin` and password: `loki`

To teardown the demo:
```bash
docker compose down
```