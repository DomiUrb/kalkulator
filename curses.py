import curses

screen = curses.initscr()

curses.start_color()

screen.addstr("Pogrubiony", curses.A_BOLD)
screen.addstr("podświetlony", curses.A_STANDOUT)
screen.addstr("podkreślony", curses.A_UNDERLINE)
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
screen.addstr("CZERWONY ALARM!!!", curses.color_pair(1))

screen.refresh()

curses.napms(6000)
curses.endwin()

print("Zakończono...")
