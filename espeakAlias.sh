#!/bin/bash
espeak --stdout "Testing, 1, 2, 3" | aplay -Dhw:0,0
