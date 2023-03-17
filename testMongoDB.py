from concurrent.futures import ThreadPoolExecutor, as_completed

from pymongo import MongoClient
import urllib

import data_process_improved

# if __name__ == '__main__':
username = urllib.parse.quote_plus('readonly')
password = urllib.parse.quote_plus('mongodb@i24')
client = MongoClient('mongodb://%s:%s@10.80.4.91' % (username, password))
db = client["reconciled"]  # put database name here
col = db["tm_900_raw_v4.1__1"]
# col = db["63898d48d430891009401330__post12"]  # put collection name here

LANES = {'E1': [0, 12], 'E2': [12, 24], 'E3': [24, 36], 'E4': [36, 48], 'E5': [48, 60],
         'E6': [60, 72], 'W1': [72, 84], 'W2': [84, 96], 'W3': [96, 108], 'W4': [108, 120],
         'W5': [120, 132], 'W6': [132, 144]}
COARSE_VEHICLE_CLASSES = ["sedan", "midsize", "pickup", "van", "semi", "truck", "motorcycle"]

# my original method of processing — takes about double the amount of time as the threadpoolexecutor
#
# cursor = col.find({})
# cnt = 0
# cur_avg_accel = []
# cur_avg_speed = []
# lanes_occupied = {'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'W1': 0, 'W2': 0,
#                   'W3': 0, 'W4': 0, 'W5': 0, 'W6': 0}
# vehicle_classes = {"sedan": 0, "midsize": 0, "pickup": 0, "van": 0, "semi": 0, "truck": 0,
#                "motorcycle": 0}
# lengths = []
#
# while cursor.alive:
#     doc = cursor.next()
#     cnt+=1
#
#     # in fps
#     speed, accel = data_process_improved.calculate_speed_accel(doc)
#     cur_avg_speed.append(speed)
#     cur_avg_accel.append(accel)
#     data_process_improved.find_lane_changes(doc, lanes_occupied, LANES)
#     data_process_improved.find_vehicle_class(doc, vehicle_classes, COARSE_VEHICLE_CLASSES)
#     data_process_improved.calculate_trajectory_lengths(doc, lengths)


def process_doc(doc):

    ## todo: fix calculate_speed_accel to not have return value
    speed, accel = data_process_improved.calculate_speed_accel(doc)
    data_process_improved.find_lane_changes(doc, lanes_occupied, LANES)
    data_process_improved.find_vehicle_class(doc, vehicle_classes, COARSE_VEHICLE_CLASSES)
    data_process_improved.calculate_trajectory_lengths(doc, lengths)
    return (speed, accel)

cursor = col.find({})
cnt = 0
cur_avg_accel = []
cur_avg_speed = []
lanes_occupied = {'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'W1': 0, 'W2': 0,
                  'W3': 0, 'W4': 0, 'W5': 0, 'W6': 0}
vehicle_classes = {"sedan": 0, "midsize": 0, "pickup": 0, "van": 0, "semi": 0, "truck": 0,
               "motorcycle": 0}
lengths = []

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(process_doc, doc) for doc in cursor]

    for future in as_completed(futures):
        speed, accel = future.result()
        cur_avg_speed.append(speed)
        cur_avg_accel.append(accel)

