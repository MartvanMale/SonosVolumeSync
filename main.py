from time import sleep
from datetime import datetime
from util import active, volume
from queue import Empty
import re

from soco.events import event_listener
from soco import SoCo, discovery


HostName = "Woonkamer"

# Get Ip + name of both devices
Speakers = list(discovery.discover())
Speaker1 = Speakers[0]
Speaker2 = Speakers[1]

# return Device_Host, Device_Slave
if Speaker1.player_name == HostName:
    Speaker_Host = Speaker1
    Speaker_Slave = Speaker2
else: 
    Speaker_Host = Speaker2
    Speaker_Slave = Speaker1

# Set volume correct on change host
def Volume(Speaker_Host, Speaker_Slave):
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    status = active.Active(Speaker_Slave)
    relative_volume = volume.Get_RelativeVolume(Speaker_Host, Speaker_Slave)
    print(now)
    if status == 'Playing':
        print('Status = ' + status)
        if  relative_volume == 0:     
            print('Volume is equal')
            print(' ')
        else:
            volume.Set_Volume(Speaker_Slave, relative_volume)
            print('Set volume to ' + str(Speaker_Host.volume))
            print(' ')
    else:
        print('Status = ' + status)
        print(' ')

# Setup listener for changes on speaker control
sub = Speaker_Host.renderingControl.subscribe()

while True:
    try:
        event = sub.events.get(timeout=1)
        Volume(Speaker_Host, Speaker_Slave)
    except Empty:
        pass

    except KeyboardInterrupt:
        sub.unsubscribe()
        event_listener.stop()
        break