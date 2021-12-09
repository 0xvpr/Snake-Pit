#!/usr/bin/env python3

"""
Creator:    VPR
Created:    December 4, 2021
Updated:    December 4, 2021

Description:
    Command & Control.
"""

import sys
# import os

from flask import Flask
from flask import ( request,
                    render_template )

app = Flask(__name__)

HOST = "127.0.0.1"
PORT = 5901

@app.route("/")
def index():
    host = request.url_root
    return render_template("index.html", host=host)

if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv

    if argc == 3:
        HOST = str(argv[1])
        PORT = int(argv[2])

    app.debug = False
    app.run(host=HOST, port=PORT)