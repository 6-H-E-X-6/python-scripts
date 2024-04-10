import argparse
import curses
from curses import wrapper
from time import sleep


parser = argparse.ArgumentParser(prog='Stopwatch',
                                 description='A basic timer and stopwatch')

parser.add_argument('-u', '--up', dest='up', action='store_true',  help='''
                    Counts up from zero instead of down and overrwrites the 
                    --time flag.''')

parser.add_argument('-t', '--time', dest='time',  help='''An integer number 
                    representing seconds or a
                    string input formatted as minutes:seconds.''')

args = parser.parse_args()

stdscr = curses.initscr()
curses.curs_set(0)
CENTER_Y, CENTER_X = curses.LINES // 2, curses.COLS // 2


def convert_to_seconds(input):
    """ Converts any input into seconds."""

    # If the input isn't in minutes:seconds...
    if ':' not in input:
        return int(input)

    # Else, split the minutes and seconds at the colon symbol
    split_numbers = input.split(':')

    # Check for invalid input
    if len(split_numbers[1]) > 2 or int(split_numbers[1]) > 60:
        return TypeError

    minutes = int(split_numbers[0])
    seconds = int(split_numbers[1])
    return (minutes * 60) + seconds


def print_time(stdscr, minutes, seconds):
    """Displays time after formatting it appropriately."""

    if args.up is True:
        timer_text = 'TIME ELAPSED'
    else:
        timer_text = 'TIME REMAINING'

    stdscr.clear()

    # Add a zero to the variables if they have no tens place.
    if minutes < 10:
        minutes = f'0{minutes}'
    if seconds < 10:
        seconds = f'0{seconds}'

    time = f'{minutes}:{seconds}'

    # Output the time on a constantly updating line.
    stdscr.addstr(CENTER_Y, CENTER_X - len(time) // 2, time)
    stdscr.addstr(CENTER_Y - 3, CENTER_X - len(timer_text) // 2, timer_text)
    stdscr.refresh()


def count(time_in_seconds):
    """Takes time_in_seconds as input and either increments or decrements it based on flags"""

    while time_in_seconds >= 0:

        # Convert time_in_seconds into minutes and seconds.
        minutes = (time_in_seconds // 60)
        seconds = (time_in_seconds % 60)

        print_time(stdscr, minutes, seconds)
        sleep(1)

        if args.up is True:
            time_in_seconds += 1
            continue

        time_in_seconds -= 1

    print('All done!')


def main(stdscr):
    if args.up is True:
        count(0)
        pass
    else:
        total_seconds = convert_to_seconds(args.time)
        count(total_seconds)
    print('Input out of range.')


try:
    wrapper(main)
except KeyboardInterrupt:
    print("Exited!")
