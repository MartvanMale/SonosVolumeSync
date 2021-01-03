from datetime import datetime
from util import util
from queue import Empty

from soco.events import event_listener
from soco import SoCo

# Fill in name of Host and Slave speaker
HostName = "Woonkamer"
SlaveName = "SubWoofer"

# Discover devices based on name of speakers.
def Discover(HostName, SlaveName):
    global Speaker_Host, Speaker_Slave
    Speaker_Host = util.Discovery(HostName)
    Speaker_Slave = util.Discovery(SlaveName)
    print(f'Speaker_Host found, name = {Speaker_Host.player_name} @ ipadress = {Speaker_Host.ip_address}')
    print(f'Speaker_Slave found, name = {Speaker_Slave.player_name} @ ipadress = {Speaker_Slave.ip_address}')
    return Speaker_Host, Speaker_Slave

# Setup listener for changes on speaker control
def Listener(Speaker_Host, Speaker_Slave):
    sub = Speaker_Host.renderingControl.subscribe(auto_renew=True)
    while True:
        try:
            sub.events.get(timeout=1)
            now = datetime.now()
            now = now.strftime("%H:%M:%S")
            print(now)
            Volume(Speaker_Host, Speaker_Slave)
        except Empty:
            pass

        except KeyboardInterrupt:
            sub.unsubscribe()
            event_listener.stop()
            break

# Set volume correct on change host
def Volume(Speaker_Host, Speaker_Slave):
    status = util.Active(Speaker_Slave)   
    if status == 'Playing':
        Speaker_Slave.volume = Speaker_Host.volume
        print(f'Status = {status}')
        print(f'Set volume to {Speaker_Host.volume}')
        print(' ')
    else:
        print(f'Status = {status}')
        print(' ')


# Run if main program
if __name__ == "__main__":
    Discover(HostName, SlaveName)
    Listener(Speaker_Host, Speaker_Slave)
