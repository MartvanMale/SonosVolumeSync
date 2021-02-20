from soco import core, discovery
from re import search

# util file for main program

# Get speaker instance based on speaker name
def Discovery(SpeakerName):
    Speaker = discovery.by_name(SpeakerName)
    return Speaker

# Check if Device is playing
def Active(Device):
    playstate = Device.get_current_transport_info()['current_transport_state']
    playing = search('PLAYING', str(playstate))  
    if playing is None:
        Status = "Not_Playing"
        return Status
    else:
        Status = "Playing"
        return Status
        
def Mute(Speaker_Host, Speaker_Slave):
    if Speaker_Host.mute != Speaker_Slave.mute:
        if Speaker_Host.mute == True:
            Speaker_Slave.mute = True
            print(f'Set {Speaker_Slave.player_name} to Muted')
        else:
            Speaker_Slave.mute = False 
            print(f'Set {Speaker_Slave.player_name} to Unmuted') 

        