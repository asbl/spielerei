_help:
  @just -l

# build docker container
build:
  docker compose build

# start docker container
start:
  docker compose up -d
  @echo "Open: http://localhost:1313/"

# stop docker container
stop: 
  docker compose down

# docker container logs
logs:
  docker compose logs

# docker container status
status:
  docker compose ps
