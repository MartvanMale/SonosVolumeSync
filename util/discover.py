from soco import discovery

# Get speaker instance based on speaker name
def Discovery(SpeakerName):
    Speaker = discovery.by_name(SpeakerName)
    return Speaker


