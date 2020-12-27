from time import sleep
from datetime import datetime
from util import active, volume, discover
from queue import Empty
import re

from soco.events import event_listener
from soco import SoCo, discovery

# Fill in name of Host and Slave speaker
HostName = "Woonkamer"
SlaveName = "SubWoofer"

# Get Ip of devices based on names above
Speaker_Host = discover.Discovery(HostName)
Speaker_Slave = discover.Discovery(SlaveName)
print(Speaker_Host)
print(Speaker_Slave)

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