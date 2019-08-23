#!/usr/bin/env python3

"""
  Pomme: A very basic cli pomodoro timer
"""

# Imports
import argparse
import time
import os


# Main program init function
def main():
    # Parse command line args
    args = getArgs()
    interval = args.interval
    pause = args.pause

    # Print info about current timer
    initialise(interval, pause)

    # Start the timer loop
    while True:
        try:
            # Start and repeat timers
            countInterval(interval)
            countPause(pause)
        except KeyboardInterrupt:
            # Reset the cursor and exit
            # TODO: Pretty this up a bit
            quit()
            break


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


def initialise(interval, pause):
    # Print out timer information
    print("Timer starting. Each interval will last "
          + str(interval) + " minutes, with a "
          + str(pause) + " minute pause between them.\n"
          + "\nPress Ctrl+c at any time to quit.\n")
    # Hide the cursor while the program runs
    os.system("setterm -cursor off")


def countPause(duration):
    print("Time for a " + str(duration) + " minute break")
    time.sleep(duration * 60)


def countInterval(duration):
    print(str(duration) + " minute timer is active!")
    time.sleep(duration * 60)
    # TODO: Display countdown


def quit():
    os.system("setterm -cursor on")
    print("\rTimer has been stopped!")


# Run the program
main()
