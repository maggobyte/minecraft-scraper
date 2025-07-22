import time
from prometheus_client import start_http_server
from exporter.server_query import MinecraftQuerier
import exporter.metrics as metrics

class MinecraftExporter:
    def __init__(self, host, port=25565, interval=30):
        self.querier = MinecraftQuerier(host, port)
        self.interval = interval
    
    def update_metrics(self):
        while True:
            data = self.querier.get_status()
            metrics.mc_online.set(1 if data["online"] else 0)
            metrics.mc_latency.set(data["latency"])
            metrics.mc_players_online.set(data["players_online"])
            metrics.mc_info.info({
                "version": data["version"],
                "motd": data["motd"]
            })

            time.sleep(self.interval)
    
    def run(self):
        start_http_server(8000)
        self.update_metrics()
            
