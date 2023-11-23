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

## Building pico2wav For voice response

Following this guide you can build a package called libttspico that gives access to an offline high quality text to speech application (pico2wav)

 -> https://davidjmurray.dev/pico-tts-engine-on-raspberry-pi/

![Screenshot 2023-11-23 101937](https://github.com/egrissino/offline-speech-rpi/assets/13847997/be30576e-e829-46b9-b872-8d772e7bed66)

