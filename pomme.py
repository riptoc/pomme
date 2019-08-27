#!/usr/bin/env python3

"""
  Pomme: A very basic cli pomodoro timer
"""
import argparse
import os
import time


class Pomme:
    def __init__(self, interval, pause):
        # Set the duration in minutes
        self.interval = interval
        self.pause = pause

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

        os.system('notify-send "Starting timer"')

    # The main timer interval
    def run_interval(self, interval):
        print(Colours.BLUE +
              str(interval) + " minute timer is active!"
              + Colours.RESET)
        os.system('notify-send "Timer started"')
        self.count(interval)

    # Pause between intervals
    def run_pause(self, pause):
        print(Colours.GREEN +
              "Time for a " + str(pause) + " minute break!\a"
              + Colours.RESET)
        os.system('notify-send "Your timer is complete, taking a ' + str(pause) + ' minute break"')
        self.count(pause)

    # The actual timer/countdown
    @staticmethod
    def count(duration):
        # Convert to minutes
        duration *= 60
        # Print out a timer
        while duration:
            mins, secs = divmod(duration, 60)
            counter = '{:02d}:{:02d}'.format(mins, secs)
            print(counter, end="\r")
            time.sleep(1)
            duration -= 1

    # Run when closing the timer
    @staticmethod
    def quit():
        os.system("setterm -cursor on")  # Restart terminal cursor
        print(Colours.YELLOW
              + "\rTimer has been stopped!"
              + Colours.RESET)


# Some colours for prettier display
class Colours:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RESET = '\033[0m'


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


# Main program init function
def main():
    # Parse command line args, retrieve timer settings
    args = get_args()
    interval = args.interval
    pause = args.pause

    # Initialise timer
    timer = Pomme(interval, pause)

    # Start the timer loop
    while True:
        try:
            # Main timer interval
            timer.run_interval(interval)
            # Timer pause
            timer.run_pause(pause)
        except KeyboardInterrupt:
            # Reset the cursor and exit
            timer.quit()
            break


# Run the program
main()
