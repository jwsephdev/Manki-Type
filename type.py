import curses

def main(stdscr):
    target = "hello world"
    typed = ""

    curses.curs_set(1)
    stdscr.nodelay(False)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2,  curses.COLOR_BLACK, curses.COLOR_RED)  
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) 

    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)
    UNTYPED = curses.color_pair(3) | curses.A_DIM

    while True:
        stdscr.clear()

        for i, char in enumerate(target):
            if i < len(typed):
                if typed[i] == char:
                    attr = GREEN
                else:
                    attr = RED
            else:
                attr = UNTYPED
                
            stdscr.addch(0, i, char, attr)

        stdscr.refresh()

        if len(typed) >= len(target):
            break

        ch = stdscr.getch()

        if ch in (curses.KEY_BACKSPACE, 127, 8):
            typed = typed[:-1]
        elif 32 <= ch <= 126:
            typed += chr(ch)

    stdscr.addstr(2, 0, "Done! Press any key to exit.")
    stdscr.getch()

curses.wrapper(main)