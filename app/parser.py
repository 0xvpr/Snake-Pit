from argparse import ArgumentParser
from typing import Tuple

def handle_command_line() -> Tuple[str, str]:
    parser = ArgumentParser()
    parser.add_argument(
        "-H", "--host",
        dest="host",
        default="127.0.0.1",
        help="Specify host address.",
        type=str
    )
    parser.add_argument(
        "-p", "--port",
        dest="port",
        default=5901,
        help="Specify port number.",
        type=int
    )

    args = parser.parse_args()

    return args.host, args.port
