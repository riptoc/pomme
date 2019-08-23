#!/usr/bin/env python3

"""
  Pomme: A very basic cli pomodoro timer
"""

# Imports
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(
    description="Pomme: A super simple pomodoro CLI.")
parser.add_argument('interval',
                    type=int,
                    nargs='?',
                    default=25,
                    help='How long the intervals last before a pause')
parser.add_argument('pause',
                    type=int,
                    nargs='?',
                    default=3,
                    help='How long the pauses last between intervals')
args = parser.parse_args()


# Main program loop
def main():
    print("Timer starting. Each interval will last "
          + str(args.interval) + " minutes, with a "
          + str(args.pause) + " minute pause between them.\n")


# Run the program
main()
