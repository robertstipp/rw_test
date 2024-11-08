#!/usr/bin/env python

import requests
import time
import datetime
import uuid
import json



reaction_wheel_A_io = 9
reaction_wheel_B_io = 10
reaction_wheel_C_io = 11
reaction_wheel_D_io = 12

reaction_wheel_A = 0
reaction_wheel_B = 1
reaction_wheel_C = 2
reaction_wheel_D = 3



wait_time = 10


token = 111
operator = "bobby"

powermanager_title = "Power Manager"
source = "Ground"
internal_target = "Primary"

# Targets
odin_primary_target = "Odin Primary Ethernet"
odin_secondary_target = "Odin Secondary Ethernet"
dev = "Dev"





id = 0


def genHeader(title,id):
  header = {}
  header["ID"] = id
  header["Time"] = str(datetime.datetime.now())
  header["Source"] = "GROUND"
  header["InternalTarget"] = "PRIMARY"
  header["Title"] = title
  header["Description"] = str(uuid.uuid4())
  id += 1
  return header



# hostname = "http://192.168.20.20:8083/command/new"
hostname = "http://localhost:8083/command/new"


def power_on_reaction_wheel(io_target,designation):
    if designation not in [odin_primary_target, odin_secondary_target, dev]:
        print("\rError: must be a valid designation")
        return False  
    
    if io_target not in [9, 10, 11, 12]:
        print("\rError: reaction wheel is not a valid io_target")
        return False  
    reaction_wheelname = chr(ord("A") + io_target - 9)
    payload = {
        "Data": {
            "name": "Power Manager",
            "header": genHeader(f"Sequence {id} - Power On Reaction Wheel {reaction_wheelname}", id),
            "data": {
                "Target": io_target,
                "Enable": True
            }
        },
        "Target": designation,
        "Mission": 2,
        "Title": "Power Manager"
    }

    headers = {
        "Content-Type": "application/json",
        "Token": str(token),
        "User": operator
    }

    try:
        response = requests.post(hostname, json=payload, headers=headers)
        if response.status_code != 200:
            print("\rRequest not accepted.")
            return False
    except requests.exceptions.RequestException as e:
        print("\rError during request:", e)
        return False

    print(f"\rCommand Accepted Power Manager Enable Reaction Wheel {reaction_wheelname} from {designation}")
    return True


def init_reaction_wheel(reaction_wheel_destination,designation):
    if designation not in [odin_primary_target, odin_secondary_target, dev]:
        print("\rError: must be a valid designation")
        return False  
    
    if reaction_wheel_destination not in [0,1,2,3]:
        print("\rError: reaction wheel is not a valid reaction_wheel_destination")
        return False  
    reaction_wheelname = chr(ord("A") + reaction_wheel_destination)
    payload = {
        "Data": {
            "name": "Reaction Wheel Init",
            "header": genHeader(f"Sequence {id} - Init Reaction Wheel {reaction_wheelname}", id),
            "data": {
                "Destination": reaction_wheel_destination,
            }
        },
        "Target": designation,
        "Mission": 2,
        "Title": "Reaction Wheel Init"
    }

    headers = {
        "Content-Type": "application/json",
        "Token": str(token),
        "User": operator
    }

    try:
        response = requests.post(hostname, json=payload, headers=headers)
        if response.status_code != 200:
            print("\rRequest not accepted.")
            return False
    except requests.exceptions.RequestException as e:
        print("\rError during request:", e)
        return False

    print(f"Command Accepted Init Reaction Wheel {reaction_wheelname} from {designation}")
    return True

def idle_reaction_wheel(reaction_wheel_destination,designation):
    if designation not in [odin_primary_target, odin_secondary_target, dev]:
        print("\rError: must be a valid designation")
        return False  
    
    if reaction_wheel_destination not in [0,1,2,3]:
        print("\rError: reaction wheel is not a valid reaction_wheel_destination")
        return False  
    reaction_wheelname = chr(ord("A") + reaction_wheel_destination)
    payload = {
        "Data": {
            "name": "Reaction Wheel Idle",
            "header": genHeader(f"Sequence {id} - Idle Reaction Wheel {reaction_wheelname}", id),
            "data": {
                "Destination": reaction_wheel_destination,
            }
        },
        "Target": designation,
        "Mission": 2,
        "Title": "Reaction Wheel Idle"
    }

    headers = {
        "Content-Type": "application/json",
        "Token": str(token),
        "User": operator
    }

    try:
        response = requests.post(hostname, json=payload, headers=headers)
        
        if response.status_code != 200:
            print("\rRequest not accepted.")
            return False
    except requests.exceptions.RequestException as e:
        print("\rError during request:", e)
        return False

    print(f"\rCommand Accepted Idle Reaction Wheel {reaction_wheelname} from {designation}")
    return True


def torque_reaction_wheel(reaction_wheel_destination,torque, designation):
    if torque > 0.067 or torque < -0.067:
        print("\rError: must be a within range -0.066 0.066")
        return False  
    if designation not in [odin_primary_target, odin_secondary_target, dev]:
        print("\rError: must be a valid designation")
        return False  
    
    if reaction_wheel_destination not in [0,1,2,3]:
        print("\rError: reaction wheel is not a valid reaction_wheel_destination")
        return False  
    reaction_wheelname = chr(ord("A") + reaction_wheel_destination)
    payload = {
        "Data": {
            "name": "Reaction Wheel Torque Setpoint",
            "header": genHeader(f"Sequence {id} - Torque Reaction Wheel {reaction_wheelname} to {str(torque)}", id),
            "data": {
                "Torque": torque,
                "Destination": reaction_wheel_destination,
            }
        },
        "Target": designation,
        "Mission": 2,
        "Title": "Reaction Wheel Torque Setpoint"
    }

    headers = {
        "Content-Type": "application/json",
        "Token": str(token),
        "User": operator
    }

    try:
        response = requests.post(hostname, json=payload, headers=headers)
        
        if response.status_code != 200:
            print("\rRequest not accepted.")
            return False
    except requests.exceptions.RequestException as e:
        print("\rError during request:", e)
        return False

    print(f"\rCommand Accepted Torque Reaction Wheel {reaction_wheelname} to {str(torque)} from {designation}")
    return True



def run_reaction_wheel_poweron_sequence():
  for i in range(4):
    power_on_reaction_wheel(i + 9, odin_primary_target)
    power_on_reaction_wheel(i + 9, odin_secondary_target)

def run_reaction_wheel_init_sequence():
  for i in range(4):
    init_reaction_wheel(i, odin_primary_target)

def run_reaction_wheel_idle_sequence():
  for i in range(4):
    idle_reaction_wheel(i, odin_primary_target)

def run_reaction_wheel_torque_sequence_single(reaction_wheel_destination,wait_time):
  torque_reaction_wheel(reaction_wheel_destination,0.066 ,dev)
  print("Waiting")
  time.sleep(wait_time)
  torque_reaction_wheel(reaction_wheel_destination,-0.066 ,dev)
  idle_reaction_wheel(reaction_wheel_destination,odin_primary_target)

# run_reaction_wheel_poweron_sequence()
# time.sleep(1)
# run_reaction_wheel_init_sequence()
# time.sleep(1)
# run_reaction_wheel_idle_sequence()

# idle_reaction_wheel(0, odin_primary_target)
# run_reaction_wheel_torque_sequence_single(0,10)

# print("ALL DONE")

def run_reaction_wheel_torque_sequence_double(initial_wheels, followers,wait_time):
  if len(set([*initial_wheels, *followers])) != 4:
    print("This is a triple wheel test. Please provide two array of wheels of size 3 and 1 with no duplicates")
    return
  if len(initial_wheels) != 2:
    print("This is a double wheel test. The initial wheel needs to be an array 2 wheel")
    return
  if len(followers) != 2:
    print("This is a double wheel test. The follower wheel needs to be an array 2 wheel")
    return 
  for i in initial_wheels: 
    torque_reaction_wheel(i,0.066 ,dev)
  print("waiting")
  time.sleep(wait_time)
  for i in followers: 
    torque_reaction_wheel(i,0.066 ,dev)

def run_reaction_wheel_torque_sequence_triple(initial_wheels, followers,wait_time):
  if len(set([*initial_wheels, *followers])) != 4:
    print("This is a triple wheel test. Please provide two array of wheels of size 3 and 1 with no duplicates")
    return
  if len(initial_wheels) != 3:
    print("This is a triple wheel test. Please provide and array of 3 wheels")
    return
  if len(followers) != 1:
    print("This is a triple wheel test. The follower wheel needs to be an array 1 wheel")
    return 
  
  for i in initial_wheels: 
    torque_reaction_wheel(i,0.066 ,dev)
  print("waiting")
  time.sleep(wait_time)
  for i in followers: 
    torque_reaction_wheel(i,0.066 ,dev)



# run_reaction_wheel_torque_sequence_double([0,1],[2,3], 10)
# run_reaction_wheel_torque_sequence_double([0,2],[1,3], 10)
# run_reaction_wheel_torque_sequence_triple([0,2,0],[1], 10)
