import trackers.tracker_manager as mg
import easygui
import json

dict_metingen = {}

b = easygui.buttonbox(msg="Zet 1 tracker aan en plaats de tracker in een hoek", choices=["Neem meting", "Exit"])

if b == "Neem meting":
    dict_metingen[0] = mg.get_position("tracker_1")

for i in range(1,4):
    b = easygui.buttonbox(msg="Plaats de tracker de volgende hoek", choices=["Neem meting", "Exit"])
    if b == "Neem meting":
        dict_metingen[i] = mg.get_position("tracker_1")

easygui.buttonbox(msg="De callibratie is klaar", choices=["klaar"])


list_x = []
list_y = []


for i in range(0,4):
    list_x.append(dict_metingen[i]["x"])
    list_y.append(dict_metingen[i]["z"])


dict_maximal = {}

dict_maximal["min_x"] = (min(list_x))
dict_maximal["max_x"] = (max(list_x))
dict_maximal["min_y"] = (min(list_y))
dict_maximal["max_y"] = (max(list_y))





with open('calibratie.json', 'w') as fp:
    json.dump(dict_maximal, fp)