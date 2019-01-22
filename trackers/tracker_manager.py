from trackers.triad_openvr import *
import time



#iniate connected trackers
v = triad_openvr()
amount_connected = v.get_connected_trackers()

#adds newly connected devices to the device list
def renew_devices():
    global v
    v = triad_openvr()
    global amount_connected
    amount_connected = v.get_connected_trackers()
    return amount_connected

#gets the position of one specific tracker
#returns the values in a dictionary
#KeyError means the specified tracker was not found
def get_position(tracker="tracker_1"):
    pos_keys = ["x","y","z","yaw","pitch","roll"]
    positions = {}
    i = 0
    try:
        for each in v.devices[tracker].get_pose_euler():
            txt=""
            txt += "%.4f" % each
            positions[pos_keys[i]] = float(txt)
            i += 1
        return positions
    except KeyError:
        print("Device: {0} not found, tracker was not initialized at start of game".format(tracker))



#gets the position of all available trackers
#returns these values in a list containing dictionarys
def get_all_positions():
    list_measurements = []
    for i in range (1,amount_connected+1):
        list_measurements.append(get_position("tracker_"+str(i)))
    return list_measurements
