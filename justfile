_help:
  @just -l

# build docker container
docker-build:
  docker compose --profile do-not-start build

build:
  docker compose run --rm hugo hugo

# start docker container
start:
  docker compose up -d
  @echo "Open: http://localhost:8080/"

# stop docker container
stop: 
  docker compose down

# docker container logs
logs:
  docker compose logs

# docker container status
status:
  docker compose ps

# Erstellt eine neue Event-Datei mit Hugo und einem python-skript.
# DATE: Datum im Format YYYY-MM-DD
# TYPE: Art der Veranstaltung (z.B. gemeindehaus, schafferei, wochenende-merzhausen)
event DATE TYPE:
    python new-event.py {{DATE}} {{TYPE}}