from mcstatus import JavaServer

class MinecraftQuerier:
    def __init__(self, host, port=25565):
        self.server = JavaServer(host, port)

    def get_status(self):
        try:
            status = self.server.status()
            motd = status.description
            # Handle legacy vs modern MOTD format
            if isinstance(motd, dict) and "text" in motd:
                motd = motd["text"]
            else:
                motd = str(motd)

            return {
                "online": True,
                "latency": status.latency,
                "players_online": status.players.online,
                "version": status.version.name,
                "motd": motd,
            }
        except Exception as e:
            print(f"[Error] Failed to query server: {e}")
            return {
                "online": False,
                "latency": 0,
                "players_online": 0,
                "version": "",
                "motd": "",
            }
