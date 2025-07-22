## Minecraft Exporter for Prometheus

A lightweight Prometheus exporter that collects metrics from a Minecraft server using [mcstatus](https://github.com/py-mine/mcstatus).


## 🔧 Docker compose usage

```yaml
services:
  minecraft_scraper:
    image: ghcr.io/maggobyte/minecraft-scraper:latest
    restart: unless-stopped
    environment:
      MC_HOST: "localhost" #Ip or hostname of the Minecraft server
      MC_PORT: "25565" #Minecraft server port (default 25565)
      MC_INTERVAL: "30" #Seconds between each status query
    ports:
      - "8000:8000"
```

## 🔧 Prometheus Config Example
```yaml
scrape_configs:
  - job_name: 'minecraft'
    static_configs:
      - targets: ['localhost:8000']

```
