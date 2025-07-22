import os
from exporter.exporter import MinecraftExporter
from mcstatus import JavaServer

host = os.getenv("MC_HOST", "localhost")
port = int(os.getenv("MC_PORT", 25565))
interval = int(os.getenv("MC_INTERVAL", 30))

exporter = MinecraftExporter("localhost", 25565, interval=30)
exporter.run()

retries = 10
for attempt in range(1, retries +1):
    try:
        print(f"Attempt {attempt} to connect to {host}:{port}")
        server = JavaServer(host, port)
        status = server.status()
        print(f"Connected! {status.players.online} players online.")
        break
    except Exception as e:
        print(f"Connection attempt {attempt} failed: {e}")
        time.sleep(5)
else:
    print(f"Failed to connect to the server after {retries} attempts.")
    exit(1)