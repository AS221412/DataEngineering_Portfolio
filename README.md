# Datenimport mit Docker und MongoDB
Dieses Projekt demonstriert den Import von Daten aus einer CSV-Datei in eine MongoDB-Datenbank mithilfe von Docker.

# Voraussetzungen
Vor dem Starten der Anwendung müssen Docker und Docker-Compose auf Ihrem System installiert sein.

# Anwendung starten
 Öffnen Sie ein Terminal und navigieren Sie zum Verzeichnis dieses Projekts.

 Führen Sie den Befehl docker-compose up aus, um die Anwendung zu starten.

 Die Anwendung startet zwei Container: einen für die Python-Anwendung und einen für MongoDB. Sie können den Fortschritt im Terminal beobachten.

Nachdem die Container gestartet wurden, wird das Python-Skript ausgeführt. Dieses Skript liest die Daten aus der Datei iot_telemetry_data.csv ein und speichert sie in der MongoDB-Datenbank.

Der Importvorgang wird im Terminal protokolliert, und Sie sehen die Meldung "Import completed.", wenn der Vorgang abgeschlossen ist.

# Dateistruktur
pyapp/: Dieser Ordner enthält die Python-Anwendung und die benötigten Dateien.
main.py: Das Hauptskript, das die Daten aus der CSV-Datei liest und in die MongoDB-Datenbank importiert.
iot_telemetry_data.csv: Die CSV-Datei mit den zu importierenden Daten.
Dockerfile: Das Dockerfile für die Python-Anwendung.
docker-compose.yml: Die Docker-Compose-Datei, die die Konfiguration für das Starten der Anwendung enthält.

# Hinweise
Stellen Sie sicher, dass die Datei iot_telemetry_data.csv im gleichen Verzeichnis wie die main.py liegt. Andernfalls kann das Python-Skript die Datei nicht finden.
Überprüfen Sie das Terminalprotokoll, um sicherzustellen, dass der Datenimport erfolgreich abgeschlossen wurde.
