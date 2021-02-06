'''
todo-app that uses a kanban principle

There will be 3 areas:
    - backlog
    - in progress
    - done

'''

import curses
import sys

'''
def main(stdscr):
    pass

curses.wrapper(main)
'''

is_window = False

# initialize screen
stdscr = curses.initscr()

# set tui parameters
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

height, width = stdscr.getmaxyx()
if height < 50 or width < 50:
    quit()


def initialize():

    global height, width
    stdscr.clear()
    stdscr.addstr(0, 0, '---KANBAN PLANNING TOOL---', curses.A_BOLD)
    stdscr.addstr(1, 0, 'Please enter a command (\'h\' for help, \'q\' to quit).')
    stdscr.addstr(height -1, 0,  'STATUS BAR')
    stdscr.refresh()

def display_help():

    # if a window is displayed, clear the screen first
    if is_window:
        stdscr.clear()
    stdscr.addstr(3, 0, 'a - add new task')
    stdscr.addstr(4, 0, 'd - delete selected task')
    stdscr.addstr(5, 0, 's - save kanban list to file')
    stdscr.addstr(6, 0, 'q - quit')
    stdscr.addstr(8, 0, 'Press a key to continue...')
    stdscr.refresh()
    stdscr.getkey()

    # remove later
    initialize()

def quit_program():
    curses.echo()
    curses.nocbreak()
    stdscr.keypad(False)

    curses.endwin()
    sys.exit()

def generate_board():
    global is_window
    is_window = True
    board = curses.newwin(50, 100, 2, 0)
    board.addstr(0, 0, "Hello from 0,0")
    board.addstr(4, 4, "Hello from 4,4")
    board.addstr(5, 5, "Hello from 5,15 with a long string")
    board.refresh()
    

#Start program
initialize()

cmd = None
# ord() returns the unicode of a caracter
# chr() returns the caracter matching a unicode
# stdscr.getch() returns the unicode of a pressed character
while (cmd != 'q'):
    cmd = stdscr.getkey()
    
    if cmd == 'h':
        display_help()
    elif cmd == 'b':
        generate_board()
    elif cmd == 'KEY_RIGHT':
        display_help()
        pass
    else:
        continue

quit_program()


# maybe not use classes, only functions
# maybe implement a buffer system like vim
class kanban:
    def __init__(self, title):
        
        self.backlog = []
        self.inProgress = []
        self.done = []
        
        self.title = title

    # add a task to the backlog
    def add_task(self, task, due):
        self.backlog.append({'task': task, 'due': due})


    # mark a task as in progress
    def move_progress(self, index):
        self.inProgress.append(self.backlog[index])
        self.backlog.pop(index)


    # mark a task as done and move it to the done list
    def move_done(self, index):
        self.done.append(self.inProgress[index])
        self.inProgress.pop(index)


    # sort the tasks taks by date
    def sort(self):
        sorted_list = sorted(self.backlog, key=lambda k: k['due'])
        self.backlog = sorted_list

        sorted_list = sorted(self.inProgress, key=lambda k: k['due'])
        self.inProgress = sorted_list

        sorted_list = sorted(self.done, key=lambda k: k['due'])
        self.done = sorted_list

    # show the whole list
    def show(self):

        self.sort()

        max = len(self.backlog)
        if len(self.inProgress) > max:
            max = len(self.inProgress)
        if len(self.done) > max:
            max = len(self.done)
        
        max_len = 11
        if self.backlog:        # if that returns true, the list  exists and contains items
            for i in range(0, len(self.backlog)):
                if len(self.backlog[i]['task']) > max_len:
                    max_len = len(self.backlog[i]['task'])
                
        if self.inProgress:
            for i in range(0, len(self.inProgress)):
                if len(self.inProgress[i]['task']) > max_len:
                    max_len = len(self.inProgress[i]['task'])

        if self.done:
            for i in range(0, len(self.done)):
                if len(self.done[i]['task']) > max_len:
                    max_len = len(self.done[i]['task'])

        print('BACKLOG' + (max_len - 7) * ' ', '| IN PROGRESS' + (max_len - 11) * ' ',  '| DONE' + (max_len - 4) * ' ')
        print((max_len * 3 + 6) * '-')
        for i in range(0, max):
            if i >= len(self.backlog):
                p_backlog = '-' + (max_len - 1) * ' '
            else:
                p_backlog = self.backlog[i]['task'] + (max_len - len(self.backlog[i]['task'])) * ' '
            
            if i >= len(self.inProgress):
                p_inProgress = '-' + (max_len - 1) * ' '
            else:
                p_inProgress = self.inProgress[i]['task'] + (max_len - len(self.inProgress[i]['task'])) * ' '

            if i >= len(self.done):
                p_done = '-' + (max_len - 1) * ' '
            else:
                p_done = self.done[i]['task'] + (max_len - len(self.done[i]['task'])) * ' '

            print(f'{p_backlog} | {p_inProgress} | {p_done}')
        
        print((max_len * 3 + 6) * '-')
        

''' LABS KEY TESTING AREA '''
'''
list1 = kanban('ToDo List 1')

list1.add_task('SK Kolloquium', '09.02.2021')
list1.add_task('Rewe Kolloquium', '02.02.2021')
list1.add_task('GPM M3', '07.02.2021')

list1.show()

print(' ')

list1.move_progress(0)
list1.move_progress(1)
list1.move_done(1)
list1.show()
'''