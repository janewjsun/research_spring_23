#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:38:44 2022
​
@author: yanbing_wang
"""

# utilize a sliding window to process data from MongoDB collection and graph each window on the dashboard

from pymongo import MongoClient
import urllib

import data_process_improved
from concurrent.futures import ThreadPoolExecutor
import data_visualization.visualization_grid as viz_grid

# if __name__ == '__main__':

username = urllib.parse.quote_plus('readonly')
password = urllib.parse.quote_plus('mongodb@i24')
client = MongoClient('mongodb://%s:%s@10.80.4.91' % (username, password))
db = client["reconciled"]  # put database name here
# col = db["groundtruth_scene_1__yawns"]  # put collection name here
col = db["groundtruth_scene_1_130__cajoles"]


LANES = {'E1': [0, 12], 'E2': [12, 24], 'E3': [24, 36], 'E4': [36, 48], 'E5': [48, 60],
         'E6': [60, 72], 'W1': [72, 84], 'W2': [84, 96], 'W3': [96, 108], 'W4': [108, 120],
         'W5': [120, 132], 'W6': [132, 144]}
COARSE_VEHICLE_CLASSES = ["sedan", "midsize", "pickup", "van", "semi", "truck", "motorcycle"]
def process_doc(doc):

    ## todo: fix calculate_speed_accel to not have return value
    data_process_improved.calculate_speed_accel(doc, cur_avg_speed, cur_avg_accel)
    data_process_improved.find_lane_changes(doc, lanes_occupied, LANES)
    data_process_improved.find_vehicle_class(doc, vehicle_classes, COARSE_VEHICLE_CLASSES)
    data_process_improved.calculate_trajectory_lengths(doc, lengths)

# get the time range of the entire collection

t_max = col.find().sort("first_timestamp", -1).limit(1)[0]["first_timestamp"]
t_min = col.find().sort("first_timestamp", 1).limit(1)[0]["first_timestamp"]
print(t_max - t_min)

# specify rolling time window and increment
time_window = 10
increment = 5
l, r = t_min, t_min+time_window

while r < t_max:
    # query for everything that's in [l, r)
    query = {"first_timestamp": {"$gte": l,
                                 "$lt": r}}  # query for all documents whose first_timestamp is within the range [l, r)
    cursor = col.find(query)

    cur_avg_accel = []
    cur_avg_speed = []
    lanes_occupied = {'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'W1': 0, 'W2': 0,
                      'W3': 0, 'W4': 0, 'W5': 0, 'W6': 0}
    vehicle_classes = {"sedan": 0, "midsize": 0, "pickup": 0, "van": 0, "semi": 0, "truck": 0,
                       "motorcycle": 0}
    lengths = []

    data = [cur_avg_speed,cur_avg_accel,lanes_occupied,vehicle_classes,lengths]
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(process_doc, doc) for doc in cursor]
    viz_grid.graph(data)

    # increment range window
    l += increment
    r += increment
