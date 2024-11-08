#!/usr/bin/env python
import curses
from test_1 import power_on_reaction_wheel
from test_1 import init_reaction_wheel

from header import heading
from header import sub_heading
from dropdown import dropdown_menu

# Define available commands
COMMANDS = ["power_on", "power_off", "reset", "status"]

def display_menu(screen, selected_index):
    """
    Displays the command menu and highlights the selected command.
    """
    screen.clear()
    height, width = screen.getmaxyx()
    for idx, command in enumerate(COMMANDS):
        x = width // 2 - len(command) // 2
        y = height // 2 - len(COMMANDS) // 2 + idx
        if idx == selected_index:
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, command)
            screen.attroff(curses.color_pair(1))
        else:
            screen.addstr(y, x, command)
    screen.refresh()

# def main(screen):
#     # Initialize color pair for highlighted text
#     curses.start_color()
#     curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)

#     # Set up initial selected index
#     selected_index = 0

#     # Run the command menu loop
#     while True:
#         display_menu(screen, selected_index)
        
#         # Get user input
#         key = screen.getch()

#         # Navigate menu
#         if key == curses.KEY_UP:
#             selected_index = (selected_index - 1) % len(COMMANDS)
#         elif key == curses.KEY_DOWN:
#             selected_index = (selected_index + 1) % len(COMMANDS)
#         elif key == ord('\n'):  # Enter key
#             command = COMMANDS[selected_index]
#             screen.clear()
#             screen.addstr(0, 0, f"Executing command: {command}\n")
#             screen.refresh()
#             curses.napms(500)  # Pause to show selected command
#             execute_command(command)
#             break
#         elif key == ord('q'):  # Quit with 'q'
#             break


import curses

reaction_wheel_choices = ["Reaction Wheel A", "Reaction Wheel B", "Reaction Wheel C", "Reaction Wheel D"]
sequence_choices = ["Reaction Wheel A", "Reaction Wheel B", "Reaction Wheel C", "Reaction Wheel D"]

def main(screen):
    while True:
        # Clear the screen for each new command cycle
        screen.clear()
        
        # Call the heading function to display the heading and subheading
        message = ""
        heading(screen)
        sub_heading(screen, message)

        # First dropdown for command selection
        cmd_selection = dropdown_menu(screen, ["Power On", "Power Off", "Init", "Torque", "Sequence", "Idle", "Exit"], "Select a Command")
        
        # Check if user wants to exit
        if cmd_selection == "Exit" or cmd_selection is None:
            break  # Exit the loop if the user selects "Exit" or presses "q"

        # Update message and display sub-heading
        message += cmd_selection
        sub_heading(screen, message)

        # Additional dropdowns based on command selection
        if cmd_selection == "Power On":
            # Select a wheel
            wheel_selection = dropdown_menu(screen, reaction_wheel_choices, "Select A Wheel")
            if wheel_selection:
                message += " -- " + wheel_selection
                sub_heading(screen, message)

                # Select a destination
                designation_selection = dropdown_menu(screen, ["Dev", "Odin Primary Ethernet", "Odin Secondary Ethernet"], "Select A Destination")
                if designation_selection:
                    message += " -- " + designation_selection
                    sub_heading(screen, message)

                    # Send confirmation
                    send = dropdown_menu(screen, ["Send It", "Abort"], "Send or Abort")
                    if send == "Send It":
                        curses.start_color()
                        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
                        screen.addstr(4, 1, "Your command has been Sent", curses.A_BOLD)
                        power_on_reaction_wheel(reaction_wheel_choices.index(wheel_selection) + 9, designation_selection)
                    else:
                        screen.addstr(4, 1, "Your command has been Aborted", curses.COLOR_RED)

        if cmd_selection == "Init":
            # Select a wheel
            wheel_selection = dropdown_menu(screen, reaction_wheel_choices, "Select A Wheel")
            if wheel_selection:
                message += " -- " + wheel_selection
                sub_heading(screen, message)

                # Select a destination
                designation_selection = dropdown_menu(screen, ["Dev", "Odin Primary Ethernet", "Odin Secondary Ethernet"], "Select A Destination")
                if designation_selection:
                    message += " -- " + designation_selection
                    sub_heading(screen, message)

                    # Send confirmation
                    send = dropdown_menu(screen, ["Send It", "Abort"], "Send or Abort")
                    if send == "Send It":
                        init_reaction_wheel(reaction_wheel_choices.index(wheel_selection), designation_selection)
                    else:
                        screen.addstr(4, 1, "Your command has been Aborted", curses.COLOR_RED)
        
        # Refresh and wait briefly before next loop
        screen.refresh()
        curses.napms(2000)  # Pause to avoid accidental double presses

        if cmd_selection == "Sequence":
            # Select a wheel
            wheel_selection = dropdown_menu(screen, sequence_choices, "Select A Sequence")
            if wheel_selection:
                message += " -- " + wheel_selection
                sub_heading(screen, message)

                # Select a destination
                designation_selection = dropdown_menu(screen, ["Dev", "Odin Primary Ethernet", "Odin Secondary Ethernet"], "Select A Destination")
                if designation_selection:
                    message += " -- " + designation_selection
                    sub_heading(screen, message)

                    # Send confirmation
                    send = dropdown_menu(screen, ["Send It", "Abort"], "Send or Abort")
                    if send == "Send It":
                        init_reaction_wheel(reaction_wheel_choices.index(wheel_selection), designation_selection)
                    else:
                        screen.addstr(4, 1, "Your command has been Aborted", curses.COLOR_RED)
        
        # Refresh and wait briefly before next loop
        screen.refresh()
        curses.napms(2000)  # Pause to avoid accidental double presses


curses.wrapper(main)
    

def execute_command(command):
    """
    Executes the specified command by calling the relevant function.
    """
    if command == "power_on":
        power_on_reaction_wheel()
    elif command == "power_off":
        print("Powering off reaction wheel...")
        # Add relevant function call here
    elif command == "reset":
        print("Resetting reaction wheel...")
        # Add relevant function call here
    elif command == "status":
        print("Retrieving reaction wheel status...")
        # Add relevant function call here
    else:
        print(f"Unknown command: {command}")

# Run the main function within curses wrapper to handle UI input
curses.wrapper(main)
