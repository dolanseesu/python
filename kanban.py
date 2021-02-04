'''
todo-app that uses a kanban principle

There will be 3 areas:
    - backlog
    - in progress
    - done

'''

import curses
import sys

def get_input():
    cmd = stdscr.getch()
    #return cmd
    if cmd == 'h':
        stdscr.addstr(2, 0, 'a', curses.A_BOLD)
        stdscr.addstr(2, 10, 'add new task')
        # etc.
        cmd = stdscr.getch()
    elif cmd == 'q':
        curses.echo()
        curses.nocbreak()
        stdscr.keypad(False)

        curses.endwin()



# initialize screen
stdscr = curses.initscr()

# set tui parameters
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

stdscr.resize(100, 100)

stdscr.addstr(0, 0, '---KANBAN PLANNING TOOL---', curses.A_BOLD)
stdscr.addstr(1, 0, 'Please enter a command (\'h\' fior help, \'q\' to quit).')
stdscr.refresh()

#get_input()

#cmd = stdscr.getch()

#curses.napms(2000)

while True:
    cmd = stdscr.getkey()
    
    if cmd == 'h':
        stdscr.addstr('\na - add new task')
        
        stdscr.addstr('\nd - delete selected task')
        
        stdscr.addstr('\ns - save kanban list to file')
        stdscr.addstr('\nq - quit')
        stdscr.refresh()
    elif cmd == 'q':
        curses.echo()
        curses.nocbreak()
        stdscr.keypad(False)

        curses.endwin()
        sys.exit()
    else:
        continue



# maybe not use classes, only functions
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
        
        max_task_backlog = 7
        if self.backlog:        # if that returns true, the list  exists and contains items
            for i in range(0, len(self.backlog)):
                if len(self.backlog[i]['task']) > max_task_backlog:
                    max_task_backlog = len(self.backlog[i]['task'])
                
        max_task_progress = 11
        if self.inProgress:
            for i in range(0, len(self.inProgress)):
                if len(self.inProgress[i]['task']) > max_task_progress:
                    max_task_progress = len(self.inProgress[i]['task'])

        max_task_done = 4
        if self.done:
            for i in range(0, len(self.done)):
                if len(self.done[i]['task']) > max_task_done:
                    max_task_done = len(self.done[i]['task'])

        print('BACKLOG' + (max_task_backlog - 7) * ' ', '| IN PROGRESS' + (max_task_progress - 11) * ' ',  '| DONE' + (max_task_done - 4) * ' ')
        print((max_task_backlog + max_task_progress + max_task_done + 8) * '-')
        for i in range(0, max):
            if i >= len(self.backlog):
                p_backlog = '-' + (max_task_backlog - 1) * ' '
            else:
                p_backlog = self.backlog[i]['task'] + (max_task_backlog - len(self.backlog[i]['task'])) * ' '
            
            if i >= len(self.inProgress):
                p_inProgress = '-' + (max_task_progress - 1) * ' '
            else:
                p_inProgress = self.inProgress[i]['task'] + (max_task_progress - len(self.inProgress[i]['task'])) * ' '

            if i >= len(self.done):
                p_done = '-' + (max_task_done - 1) * ' '
            else:
                p_done = self.done[i]['task'] + (max_task_done - len(self.done[i]['task'])) * ' '

            print(f'{p_backlog} | {p_inProgress} | {p_done}')
        
        print((max_task_backlog + max_task_progress + max_task_done + 8) * '-')
        

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