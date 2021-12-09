#!/usr/bin/env python3

"""
Creator:    VPR
Created:    December 4, 2021
Updated:    December 4, 2021

Description:
    Command & Control.
"""

from app import create_app
from app.parser import handle_command_line

if __name__ == "__main__":
    host, port = handle_command_line()

    app = create_app()
    app.run(host=host, port=port)
