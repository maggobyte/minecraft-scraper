from prometheus_client import Gauge, Info

# Define Prometheus metrics
mc_online = Gauge("minecraft_server_online", "Is the Minecraft server online?, (1 = yes, 0 = no)")
mc_latency = Gauge("minecraft_server_latency", "Latency of the Minecraft server in milliseconds")
mc_players_online = Gauge("minecraft_server_players_online", "Number of players online in the Minecraft server")

mc_info = Info("minecraft_server_info", "Information about the Minecraft server")