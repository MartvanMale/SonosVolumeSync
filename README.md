# Sonos Room Volume Synchronize
This is a simple containerized script which synchronizes the volume between two Sonos Speakers.

## Quickstart
1. Have docker and docker compose installed.
1. Copy this repository
1. Change HostName and SlaveName to name of your speakers.
1. Run docker-compose up
1. Volume of second machine should synchronize every time you change the volume on your host machine.

## Warning
This program currently only works on native linux machines. like a raspberry pi or a debian linux machine. Virtualisation like WSL2 doesn't work, because virtual linux environments create their own virtual network, which breaks the SoCo discovery and the event listener.


## Detailed Installing process
**Step 1. Install Docker and Docker-Compose**

General: https://docs.docker.com/engine/install/

Raspberry Pi: https://phoenixnap.com/kb/docker-on-raspberry-pi

**Step 2. Install Docker-Compose**

General: https://docs.docker.com/compose/install/

**Step 3. Clone Repository**

Run
```bash
git clone https://github.com/MartvanMale/SonosVolumeSync.git
``` 

**Step 4. Rename speakers**

Change the name of the host and the slave devies, these names can be found in the Sonos App. Under Products > Room name.
The name should be filled in at  main.py > "HostName" "SlaveName"

**Step 5. Start container**

Run
```bash
docker-compose up
```

The program should now be running and syncing the volume between the 2 speakers.

# Acknowledgments
The inspiration for this project was a video of [Todd Parker](https://www.youtube.com/user/toddparker000) in which he explained how to open up a Ikea SYMFONISK speaker and hook up the woofer output to a subwoofer. [Video](https://www.youtube.com/watch?v=TiPPPu7j5DM&t)

I hooked my SYMFONISK up to my Sonos Beam, which works great, but the volume of the subwoofer is always out of sync when using the tv remote.

This program is written using the [SoCo Python library](https://github.com/SoCo/SoCo)

### Open container terminal
```zsh
docker exec -it sonosvolumesync_sonos_container_1 /bin/zsh
```

### Open container log
```zsh
bash openlog.sh
```

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