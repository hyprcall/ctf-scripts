# Manages the arguments passed by the user
import argparse
# Parsing System
def init_parser():
    parser = argparse.ArgumentParser(prog="breach")
    parser.add_argument("category", nargs="?")
    parser.add_argument("module", nargs="?")
    args, remaining = parser.parse_known_args()
    return args, remaining
