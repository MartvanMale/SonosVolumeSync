# Sonos Room Volume Synchronize
This is a simple containerized script which synchronizes the volume between multiple Sonos Speakers.



## Warning: 
This program currently only works on native linux machines. like a raspberry pi or a debian linux machine. Virtualisation like WSL2 doesn't work.

## Quickstart
1. Have docker and docker compose installed.
1. Copy this repository
1. Change main.py > hostname to the room name of your host speaker.
1. Run docker-compose up
1. Volume of second machine should synchronize every time you change the volume on your host machine.


## Current limitation:
- Only works with 2 total Sonos speakers on network.
- Any virtual linux environment which creates its own virtual network breaks the SoCo discovery and the event listener.

## Detailed Installing process.
1. Docker
General: https://docs.docker.com/engine/install/

Raspberry Pi: https://phoenixnap.com/kb/docker-on-raspberry-pi

2. Docker-Compose

General: https://docs.docker.com/compose/install/

3. Git clone

Run
```bash
git clone https://github.com/MartvanMale/SonosVolumeSync.git
``` 

4. Rename host

Change the name of the host machine, this name can be found in the Sonos App. Under Products > Room name.
The name should be filled in at  main.py > "HostName"
5. Start container

Run
```bash
docker-compose up
```

The program should now be running and syncing the volume between the 2 speakers.

# Acknowledgments
The reason for this project was a video of Todd Parker in which he explained how to open up a Ikea SYMFONISK speaker and hook up the woofer output to a subwoofer.

Sonos Hack: https://www.youtube.com/watch?v=TiPPPu7j5DM&t

I hooked my SYMFONISK up to my Sonos Beam, which works great, but the volume of the subwoofer is always out of sync when using the tv remote.

### TODO: 
1. Fix discovery with more than 2 speakers on network
1. Cleanup main.py
1. Make main.py more variable.

### Commit structure
```
__Title__
Added:
- 

Changed:
- 

Removed:
- 

```
### Open container bash
```bash
docker exec -it sonosvolumesync_sonos_container_1 /bin/zsh
```
