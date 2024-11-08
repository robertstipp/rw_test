#!/usr/bin/env python

import curses

def heading(screen):
    # Clear the screen
    screen.clear()

    # Define the message to display
    heading = "Reaction Wheel Test Script"
    
    # Set the position to the top-left corner
    x = 1
    y = 1

    # Add the message to the screen at the top-left corner
    screen.addstr(y, x, heading, curses.A_BOLD)
    line_y = y + 1  # Position the line one row below the heading
    screen.hline(line_y, x, curses.ACS_HLINE, len(heading))
    # Refresh the screen to show the message
    screen.refresh()



def sub_heading(screen, message):
    x = 1
    y = 3

    # Add the message to the screen at the top-left corner
    screen.addstr(y, x, message, curses.A_ITALIC)

