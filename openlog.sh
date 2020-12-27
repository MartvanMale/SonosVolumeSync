#!/bin/zsh
# Small script which opens the logs of the Sonos container service
ID=$(docker ps -q -f name=sonosvolumesync_sonos_container_1)

docker logs --follow $ID