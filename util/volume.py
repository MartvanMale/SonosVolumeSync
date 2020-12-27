from soco import core 

# Set relative volume
def Set_Volume(Device, Volume):
    Device.set_relative_volume(Volume)

# Gets volume of device 
def Get_Volume(Device):
    Volume = Device.volume
    return Volume

# Gets relative volume of 2 devices
def Get_RelativeVolume(Device_Host, Device_Slave):
    Relative_Volume = Device_Host.volume - Device_Slave.volume
    return Relative_Volume