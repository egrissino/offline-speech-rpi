from vosk import Model, KaldiRecognizer
import pyaudio
import kasa
import asyncio
import time
import os
import weather

def turnOn(dev_name):
    '''
    Turn device on
    '''
    #dev_name = dev_name.replace(' ','')
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
    print(f'Turing off : {dev_name}')
    for dev in devices:
        if dev_name in devices[dev].alias.lower():
            print(dev_name)
            print(devices[dev].alias)
            try:
                asyncio.run(devices[dev].turn_off())
                #time.sleep(1)
            except:
                pass

def processCmd(text):
    '''
    Process voice command
    '''

    command = text[:-3].replace('alexa ', '')
    print(command)

    if 'turn' in command:
        # check for turn on/off commands
        if 'turn on' in command:
            dev_name = command.replace('turn on the ', '')
            turnOn(dev_name)
        elif 'turn off' in command:
            dev_name = command.replace('turn off the ', '')
            turnOff(dev_name)

    if ('what is the ' in command) or ("what's the " in command):
        # Answer querys
        query = command.replace('what is the', '')
        query = query.replace("what's the ", '')

        if 'weather in ' in query:
            # Get wheather in location if avilable
            area = query.replace('weather in ','')
            weather.readWeather(area)
        

    if 'connect' in command:
        # Try blue tooth conenction
        
        pass

devices = {}
def updateDeviceList():
    '''
    Update device list from kasa
    '''
    global devices
    devices = asyncio.run(kasa.Discover.discover())

MAX_ERRS = 100
err = 0

if __name__ == "__main__":
    
    updateDeviceList()

    print(os.path.abspath(__file__))
    app_root = os.path.abspath(os.getcwd())
    model_dir = app_root + r"/vosk-model-small-en-us-0.15"
    model = Model(model_dir)
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192) , input_device_index=2)
    stream.start_stream()

    text = ""
    while err < MAX_ERRS:
        try:
            err = 0
            data = stream.read(8192, exception_on_overflow=False)
        
            if recognizer.AcceptWaveform(data):
                text += recognizer.Result()

                if "alexa" in text:
                    #stream.stop_stream()
                    #print(text)
                    processCmd(text[text.index('alexa'):])
                    text = ""
                    #stream.start_stream()
                else:
                    if len(text) > 41:
                        text = text[-40:]
                    
        except Exception as e:
            if err == 0:
                print(e)
            err += 1
            break
        
