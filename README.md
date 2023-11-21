# offline-speech-rpi
Offline capable speech assistant for #RPI 

## Compatability
This is designed with Kasa smart plugs connected on the local wifi network. The router does not need to have internet connectivity.

Speech recognition is for english only. You could modify the commands and use a different recognition model for other langugages.
see https://alphacephei.com/vosk/models for list of compatible languages.

## Installation

1. Clone repository
2. Download vosk model from
       https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
3. unzip model folder to repository
4. run python ./offline-speech.py from terminal on RPi 
