from vosk import Model, KaldiRecognizer
import pyaudio
import kasa
import asyncio
import time
import os
import weather
import speak
import listen

def turnOn(dev_name):
    '''
    Turn device on
    '''
    dev_name = dev_name.replace(' ','')
    print(f'Turing on : {dev_name}')
    for dev in devices:
        if dev_name in devices[dev].alias.lower():
            print(dev_name)
            print(devices[dev].alias)
            try:
                asyncio.run(devices[dev].turn_on())
                #time.sleep(1)
            except:
                pass

def turnOff(dev_name):
    '''
    Turn device on
    '''
    attempted = 0
    completed = 0
    dev_name = dev_name.replace(' ','')
    print(f'Turing off : {dev_name}')
    for dev in devices:
        if dev_name in devices[dev].alias.lower():
            #print(dev_name)
            attempted += 1
            print(devices[dev].alias)
            try:
                asyncio.run(devices[dev].turn_off())
                #time.sleep(1)
            except Exception as e:
                print(e)
                completed += 1
                #speak.error()
                pass

    return completed

def processCmd(text):
    '''
    Process voice command
    '''

    command = text.replace('alexa', '')
    print(command)

    if 'turn' in command:
        # check for turn on/off commands
        if 'turn on' in command:
            dev_name = command.replace('turn on ', '')
            dev_name = dev_name.replace('the ', '')
            turnOn(dev_name)
            speak.success()
            return
        elif 'turn off' in command:
            dev_name = command.replace('turn off ', '')
            dev_name = dev_name.replace('the ', '')
            turnOff(dev_name)
            speak.success()
            return

    if ('what is ' in command) or ("what's " in command):
        # Answer querys
        query = command.replace('what is ', '')
        query = query.replace("what's ", '')
        query = query.replace("the ", '')

        if 'weather in ' in query:
            # Get wheather in location if avilable
            area = query.replace('weather in ','')
            weather.readWeather(area)
            speak.success()
            return

    if 'connect' in command:
        # Try blue tooth conenction
        speak.success()
        return

    print(command)
    speak.error()

devices = {}
def updateDeviceList():
    '''
    Update device list from kasa
    '''
    global devices
    new_devices = asyncio.run(kasa.Discover.discover())

    for dev in new_devices:
        if not (dev in devices):
            # Need deep copy
            devices[dev] = new_devices[dev]
            print(f'Added new device from home: {devices[dev]}')

    if len(devices) == 0:
        print("No devices found!")

MAX_ERRS = 100
err = 0

if __name__ == "__main__":
    # Update kasa device list
    updateDeviceList()

    # Get root dirs setup
    print(os.path.abspath(__file__))
    app_root = os.path.abspath(os.getcwd())
    model_dir = app_root + r"/vosk-model-small-en-us-0.15"

    listener = listen.Listener()
    listener.loadModel(model_dir)
    listener.startStream()


    '''
    # Check for model file or exit
    if not (os.path.exists(model_dir)):
        print("Please download vosk-model-small-en-us-0.15 and unzip folder to this directory")
        exit()

    model = Model(model_dir)
    recognizer = KaldiRecognizer(model, RATE)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16,
 rate=RATE,
 channels=1,
 input=True,
 frames_per_buffer=bufferSize ,
 input_device_index=inputDevIdx)

    stream.start_stream()
    '''


    text = ""
    while err < MAX_ERRS:
        text += listener.checkforText()
        if "alexa" in text:
            #stream.stop_stream()
            #print(text)
            processCmd(text[text.index('alexa'):])
            text = ""
            #stream.start_stream()
        else:
            if len(text) > 41:
                text = text[-40:]
