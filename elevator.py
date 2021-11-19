#!/usr/bin/env python3

import sys
import json
import math
import os

if(len(sys.argv) != 4):
    print("Usage:")
    print("python elevator.py <elevator.json> <calls.csv> <callsOut.csv>")

    sys.exit(-1)

elevFileString = sys.argv[1]
callFileString = sys.argv[2]
callFile2String = sys.argv[3]

os.system("type nul > " + callFile2String)

elevFile = open(elevFileString, "r")
callFile = open(callFileString, "r")
callFile2 = open(callFile2String, "a")

elevatorJson = json.loads(elevFile.read())

calls = callFile.read().split("\n")

def calcTimeElev(elevator, srcLevel, dstLevel):
    total_time = 0
    total_time += float(elevator["_openTime"]) * 2
    total_time += float(elevator["_closeTime"]) * 2
    total_time += float(elevator["_startTime"]) * 2
    total_time += float(elevator["_stopTime"]) * 2
    total_time += abs(int(elevator["_currentFloor"]) - srcLevel) / float(elevator["_speed"])
    total_time += abs(srcLevel - dstLevel) / elevator["_speed"]

    return total_time

def calcDeltaLevels(elevator, srcLevel, dstLevel):
    deltaLevels = abs(int(elevator["_currentFloor"] - srcLevel)) + abs(srcLevel - dstLevel)
    return deltaLevels
    
def findElevatorById(array, _id):
    for obj in array:
        if(obj["_id"] == _id):
            return obj
            
    return None


elevatorsArray = elevatorJson["_elevators"]
for elevator in elevatorsArray:
    elevator["_currentFloor"] = 0
    
waiting_time = 0
uncompleted_calls = 0
id1, id2 = "288113381", "206467292"
prev_time = 0

for call in calls:
    callString = call.split(",")[0]  # Not Required
    currentTime = float(call.split(",")[1])
    srcLevel = int(call.split(",")[2])
    dstLevel = int(call.split(",")[3])
    elevStatus = call.split(",")[4]  # Not Required
    indexElev = int(call.split(",")[5])

    time = currentTime - prev_time
    min = -1
    calculatedTime = 0
    firstTime = True

    for elevator in elevatorsArray:
        if(srcLevel < int(elevator["_minFloor"]) or srcLevel > int(elevator["_maxFloor"])):
            continue

        if(dstLevel < int(elevator["_minFloor"]) or dstLevel > int(elevator["_maxFloor"])):
            continue
            

        calculatedTime = calcTimeElev(elevator, srcLevel, dstLevel) - time
        calculatedDelta = calcDeltaLevels(elevator, srcLevel, dstLevel)

        if(calculatedTime < 0):
            continue
        
        if(calculatedDelta < min or firstTime):
            min = calculatedDelta
            indexElev = int(elevator["_id"])
            firstTime = False
    
    newCallString = callString + "," + str(currentTime) + "," + str(srcLevel) + "," + str(dstLevel) + "," + elevStatus + "," + str(indexElev) + "\n"
    callFile2.write(newCallString)

    prev_time = currentTime

    if(indexElev != -1):
        findElevatorById(elevatorsArray, indexElev)["_currentFloor"] = dstLevel
        waiting_time += calculatedTime
    else:
        uncompleted_calls += 1

     
        
print("de Owners: " + id1 + ", " + id2 + ". Total waiting time: " + str(waiting_time) + ". Average waiting time: " + str(waiting_time / len(calls)) + ". Uncompleted calls: " + str(uncompleted_calls) + ".")

elevFile.close()
callFile.close()
callFile2.close()