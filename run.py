from exporter.exporter import MinecraftExporter

exporter = MinecraftExporter("10.15.15.4", 25565, interval=10)
exporter.run()