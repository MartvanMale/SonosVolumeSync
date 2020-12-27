from soco import SoCo
import re

# Check if Device is playing
def Active(Device):
    playstate = Device.get_current_transport_info()['current_transport_state']
    playing = re.search('PLAYING', str(playstate))  
    if playing is None:
        Status = "Not_Playing"
        return Status
    else:
        Status = "Playing"
        return Status