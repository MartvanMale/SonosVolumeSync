from soco import SoCo, discovery

def Discovery():
    Speakers = list(discovery.discover())
    Device_Host = Speakers[0]
    Device_Slave = Speakers[1]
    print(Device_Host.player_name)
    print(Device_Slave.player_name)
    return Device_Host, Device_Slave
