import pyaudio

pa = pyaudio.PyAudio()

def list_devices():
    info = pa.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(numdevices):
        if pa.get_device_info_by_index(i)["maxInputChannels"] > 0:
            print(pa.get_device_info_by_index(i)["index"], "-", pa.get_device_info_by_index(i)["name"])

list_devices()

