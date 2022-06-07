# Date: 06/02
# Date: 06/06: Modification of Print Commands.. using functions instead
# Date: 06/07: Added slot number and route-engine master ship
import json
from rich import print

stream = open('show_chassis_routing_engine.json', 'r') # accessing the json file in read mode.

mx104_dict = json.load(stream) # loading the json content into dictionary 

index_toggle = mx104_dict['route-engine-information'][0]['route-engine'] # indexing on route-engine object

toggle_re0 = index_toggle[0] # indexing the route-engine 0 content
toggle_re1 = index_toggle[1] # indexing the route-engine 1 content

def slotNumber(re_toggle):
    """Indexing the Slot Number Data"""
    return re_toggle['slot'][0]['data']

def reMastership(re_toggle):
    """Indexing the Mastership-State Object"""
    return re_toggle['mastership-state'][0]['data']

def tempToggle(re_toggle):
    """Indexing the Temperature Data"""
    return re_toggle['temperature'][0]['data']

def printInfo(re_toggle):
    """Fetching the Current Temperature Data"""
    curr_temp = tempToggle(re_toggle)
    slot_num = slotNumber(re_toggle)
    mastership = reMastership(re_toggle)
    print(f"Route-Engine Mastership-State    : {mastership}")
    print(f"Route-Engine Slot Number         : {slot_num}")
    print(f"Route-Engine Current Temperature : {curr_temp}\n")

printInfo(toggle_re0)
printInfo(toggle_re1)






