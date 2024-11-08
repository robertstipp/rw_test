#!/usr/bin/env python
import curses
from test_1 import power_on_reaction_wheel
from test_1 import init_reaction_wheel, run_reaction_wheel_poweron_sequence, run_reaction_wheel_init_sequence, run_reaction_wheel_torque_sequence_single, run_reaction_wheel_torque_sequence_single


from header import heading
from header import sub_heading
from dropdown import dropdown_menu

# Define available commands

command_choices = ["Power On", "Power Off", "Init", "Torque", "Sequence", "Idle", "Exit"]
reaction_wheel_choices = ["Reaction Wheel A", "Reaction Wheel B", "Reaction Wheel C", "Reaction Wheel D"]
sequence_choices = ["Single", "Double", "All Combos", "Chaos"]

def main(screen):
    while True:
        # Clear the screen for each new command cycle
        screen.clear()
        
        # Call the heading function to display the heading and subheading
        message = ""
        heading(screen)
        sub_heading(screen, message)

        # First dropdown for command selection
        cmd_selection = dropdown_menu(screen, command_choices, "Select a Command")
        
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
            sequence_selection = dropdown_menu(screen, sequence_choices, "Select A Sequence")
            if sequence_selection == "Single":
                message += " -- " + sequence_selection
                sub_heading(screen, message)

                # Send confirmation
                send = dropdown_menu(screen, ["Send It", "Abort"], "Send or Abort")
                if send == "Send It":
                    run_reaction_wheel_poweron_sequence()
                    run_reaction_wheel_init_sequence()
                    run_reaction_wheel_torque_sequence_single(1)
                    
                else:
                    screen.addstr(4, 1, "Your command has been Aborted", curses.COLOR_RED)

            
        
        # Refresh and wait briefly before next loop
        screen.refresh()
        curses.napms(2000)  # Pause to avoid accidental double presses


curses.wrapper(main)
    

