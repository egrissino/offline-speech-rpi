import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

input_devs = {}
output_devs = {}

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        input_devs[i] = p.get_device_info_by_host_api_device_index(0, i)
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
        output_devs[i] = p.get_device_info_by_host_api_device_index(0, i)


print(f"Input Devices found : {len(input_devs)}")
for devID in input_devs:
    print("Input Device id ", devID, " - ", input_devs[devID].get('name'))

print(f"Output Devices found : {len(output_devs)}")
for devID in output_devs:
    print("Output Device id ", devID, " - ", output_devs[devID].get('name'))
