#!/usr/bin/env python3

"""
  Pomme: A very basic cli pomodoro timer
"""

# Imports
import argparse


# Main program init function
def main():
    # Parse command line args
    args = getArgs()
    interval = args.interval
    pause = args.pause

    # Print info about current timer
    printInfo(interval, pause)


def getArgs():
    # Parse command line arguments and set up
    # options/help etc.
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
    return parser.parse_args()


def printInfo(interval, pause):
    # Print out timer information
    print("Timer starting. Each interval will last "
          + str(interval) + " minutes, with a "
          + str(pause) + " minute pause between them.\n")


# Run the program
main()
