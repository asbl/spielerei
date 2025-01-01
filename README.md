# Purpose

Hugo development for website https://www.usinger-spielerei.de/

# Local development

## WSL (Windows only)
* install WSL 
```
wsl --install -d Ubuntu-24.04
```
* reboot windows after install
* open terminal app
* open new tab with Ubuntu-24.04 not Ubuntu without version
* perform initial user setup

## Install homebrew
See: https://docs.brew.sh/Homebrew-on-Linux

## Install docker
See: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

* add your user to group docker (replace <USER> with your username)
```
sudo usermod -a -G docker <USER>
```

## Install just
```
brew install just
```

# Start hugo server

* build docker container, required initially or after version or dependency changes
```
just build
```
* start docker container
```
just start
```
* open http://localhost:1313/ in browser
* for further just targets run 
```
just
```
