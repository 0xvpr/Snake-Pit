#!/usr/bin/env python3

import os
import errno

named_pipe = "/tmp/data"
try:
    os.mkfifo(named_pipe)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

while True:
    print("Opening FIFO...")
    with open(named_pipe) as pipe:
        print("FIFO opened")
        while True:
            data = pipe.read()
            if len(data) == 0:
                print("Writer closed")
                break

            print(f'Read: "{data}"')
