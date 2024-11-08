import curses

def dropdown_menu(screen, options, title="Select an Option"):
    # Get the screen dimensions
    height, width = screen.getmaxyx()

    # Set initial position and selected option
    current_selection = 0
    max_y, max_x = 10, max(len(option) for option in options) + 4

    # Calculate position to center the dropdown menu
    win_y = max_y // 2
    win_x = 1

    # Create a new window for the dropdown menu
    menu_win = curses.newwin(max_y, max_x, win_y, win_x)
    menu_win.box()

    # Display title above options
    screen.addstr(win_y - 1, win_x, title, curses.A_BOLD)
    screen.refresh()

    while True:
        # Clear menu window and redraw box
        menu_win.clear()
        menu_win.box()

        # Display each option, highlighting the selected one
        for idx, option in enumerate(options):
            x = 2
            y = idx + 1
            if idx == current_selection:
                menu_win.addstr(y, x, option, curses.A_REVERSE)  # Highlight selected option
            else:
                menu_win.addstr(y, x, option)

        # Refresh the menu window to show changes
        menu_win.refresh()

        # Get user input for navigation
        key = screen.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1  # Move selection up
        elif key == curses.KEY_DOWN and current_selection < len(options) - 1:
            current_selection += 1  # Move selection down
        elif key == ord('\n'):  # Enter key
            menu_win.clear()
            menu_win.refresh()

            screen.addstr(win_y - 1, win_x, " " * len(title))
            screen.refresh()
            return options[current_selection]  # Return selected option

        elif key == ord('q'):  # Optional: press 'q' to quit
            menu_win.clear()
            menu_win.refresh()

            screen.addstr(win_y - 1, win_x, " " * len(title))
            screen.refresh()
            return None  # Exit dropdown without selection
