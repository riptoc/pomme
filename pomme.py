#!/usr/bin/env python3

"""
  Pomme: A very basic cli pomodoro timer
"""

# Imports
import argparse
import os
import time


# Main program init function
def main():
    # Parse command line args
    args = get_args()
    interval = args.interval
    pause = args.pause

    # Print info about current timer
    initialise(interval, pause)

    # Start the timer loop
    while True:
        try:
            # Start and repeat timers
            count_interval(interval)
            count_pause(pause)
        except KeyboardInterrupt:
            # Reset the cursor and exit
            # TODO: Pretty this up a bit
            quit_timer()
            break


def get_args():
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
    print(Colours.GREEN
          + "Timer starting. Each interval will last "
          + str(interval) + " minutes, with a "
          + str(pause) + " minute pause between them.\n"
          + Colours.YELLOW
          + "\nPress Ctrl+c at any time to quit.\n"
          + Colours.RESET)
    # Hide the cursor while the program runs
    os.system("setterm -cursor off")


def count_pause(duration):
    print(Colours.GREEN +
          "Time for a " + str(duration) + " minute break!"
          + Colours.RESET)
    create_timer(duration)


def count_interval(duration):
    print(Colours.BLUE +
          str(duration) + " minute timer is active!"
          + Colours.RESET)
    create_timer(duration)


# Create a timer that counts down to 0 from specified duration
def create_timer(duration):
    duration *= 60
    while duration:
        mins, secs = divmod(duration, 60)
        counter = '{:02d}:{:02d}'.format(mins, secs)
        print(counter, end="\r")
        time.sleep(1)
        duration -= 1


def quit_timer():
    os.system("setterm -cursor on")
    print(Colours.YELLOW
          + "\rTimer has been stopped!"
          + Colours.RESET)


# Some colours for prettier display
class Colours:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RESET = '\033[0m'


# Run the program
main()
