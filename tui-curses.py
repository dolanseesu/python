# Test program for curses


import curses
from curses import wrapper

'''
# the standard screen (named after the C variable)
stdscr = curses.initscr()

# turn off character output and allow input without pressing enter
curses.noecho()
curses.cbreak()

# turn off echoing of keys and allow input without pressing enter
# allow input from the keypad
stdscr.keypad(True)

stdscr.addstr(0,0, 'Hello World', curses.A_BOLD)
stdscr.refresh()

cmd = stdscr.getch()

stdscr.addch(cmd, curses.A_ITALIC)
stdscr.refresh()

curses.napms(1000)

# before closing the curses program, all settings need to be reversed
curses.echo()
curses.nocbreak()
stdscr.keypad(False)

# then, the screen can be closed
curses.endwin()

print(type(cmd))
'''

def main(stdscr):
    stdscr.addstr('Hello')
    stdscr.refresh()

    curses.napms(2000)

wrapper(main)