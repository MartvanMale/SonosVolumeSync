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
# TODO test function errback
def Listener(Speaker_Host, Speaker_Slave):
    def errback(exception):
        print("Rewenal error happened")
        Start()    

    sub = Speaker_Host.renderingControl.subscribe(auto_renew=True)
    sub.auto_renew_fail=errback   
    # sub = Speaker_Host.renderingControl.subscribe(auto_renew=True, requested_timeout=60)
    while True:
        try:
            sub.events.get(timeout=1)
            now = datetime.now()
            day = now.strftime("%D")
            time = now.strftime("%H:%M:%S")
            print(f"Time = {day} : {time}")
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
        util.Mute(Speaker_Host, Speaker_Slave)
        print(f'Status = {status}')
        print(f'Set volume to {Speaker_Host.volume}')
        print(' ')
    else:
        print(f'Status = {status}')
        print(' ')


def Start():
    Discover(HostName, SlaveName)
    Listener(Speaker_Host, Speaker_Slave)


# Run if main program
if __name__ == "__main__":
    Start()

