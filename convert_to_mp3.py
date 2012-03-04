#!/usr/bin/python

import os
from subprocess import call

def convert(filename):
    new_filename = filename.split(".")[0] + ".mp3"
    call(["ffmpeg", "-i", filename, new_filename])

if __name__ == '__main__':
    files = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].split('\n')
    for filename in files:
        convert(filename)
