'''

Speach and sound effects

'''

import subprocess
import sys
import os

## Settings

# Get deivce hw:<card id>,<device id>
# raspberian command `arecord -l`
outputDev = "hw:0,0"

# Appliocation directory
app_root = os.getcwd()

# Sucess file
successWav = app_root + '/wav/success.wav'

# error file
errorWav = app_root + '/wav/error-2.wav'

def speakText(text):
  '''
  '''
  # put report into command
  print(text)

  # Call espeak and buffer in subprocess PIPE
  # Mode 1 - espeak
  #ps = subprocess.Popen(('espeak', '--stdout', '-ven+f1', '-s205', '-p2', '-g2', f'"{text}"'), stdout=subprocess.PIPE)

  # Mode 2 - pico tts
  #Send to local alias for stdout /var/local/pico2wave.wav <- `ln -s /dev/stdout /var/local/pico2wave.wav`
  ps = subprocess.Popen(('pico2wave','-len-US', '-w/var/local/pico2wave.wav', f'"{text}"'), stdout=subprocess.PIPE)

  # Send PIPE to aplay to speak through device
  output = subprocess.check_output(('aplay', f'-D{outputDev}', '--rate=22050'), stdin=ps.stdout)
  ps.wait()


def success():
  '''
  Play Success sound to indicate completed command
  '''
  output = subprocess.check_output(('aplay', f'-D{outputDev}', successWav))


def error():
  '''
  Play error sound to indicate failed command
  '''
  output = subprocess.check_output(('aplay', f'-D{outputDev}', errorWav))


if __name__ == "__main__":
  print(sys.argv)
  if len(sys.argv) > 1:
    print(sys.argv)
    speakText(sys.argv[1])
    success()
  else:
    success()
    error()
    speakText("Self Test Complete")
