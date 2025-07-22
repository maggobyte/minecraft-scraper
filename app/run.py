import os
from exporter.exporter import MinecraftExporter

host = os.getenv("MC_HOST", "localhost")
port = int(os.getenv("MC_PORT", 25565))
interval = int(os.getenv("MC_INTERVAL", 30))

exporter = MinecraftExporter("10.15.15.4", 25565, interval=10)
exporter.run()