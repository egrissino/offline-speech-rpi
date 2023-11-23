#!/bin/bash
pico2wave -l en-US -w /var/local/pico2wave.wav "It's currently a temp of 77 and mostly sunny in Chattanooga Tennessee!" | aplay -Dhw:0,0

