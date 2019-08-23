#!/usr/bin/env python3

"""
  Pomme: A very basic cli pomodoro timer
"""

# Imports
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(
    description="Pomme, a super simple pomodoro CLI.")
parser.add_argument('timer',
                    type=int,
                    nargs='?',
                    default=25,
                    help='How long the timers last before a pause')
parser.add_argument('pause',
                    type=int,
                    nargs='?',
                    default=3,
                    help='How long the pauses last between timers')
args = parser.parse_args()
