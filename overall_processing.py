# this file processes trajectories with a single summarized subplot report of all trajectories.
# it utilizes multithreading for time efficiency, and can thus be used for trajectories with
# nearly 1 mil documents

from concurrent.futures import ThreadPoolExecutor

from pymongo import MongoClient
import urllib

import data_process_improved
import visualization_grid

username = urllib.parse.quote_plus('readonly')
password = urllib.parse.quote_plus('mongodb@i24')
client = MongoClient('mongodb://%s:%s@10.80.4.91' % (username, password))
db = client["reconciled"]  # put database name here
col = db["groundtruth_scene_1_130__cajoles"]

LANES = {'E1': [0, 12], 'E2': [12, 24], 'E3': [24, 36], 'E4': [36, 48], 'E5': [48, 60],
         'E6': [60, 72], 'W1': [72, 84], 'W2': [84, 96], 'W3': [96, 108], 'W4': [108, 120],
         'W5': [120, 132], 'W6': [132, 144]}
COARSE_VEHICLE_CLASSES = ["sedan", "midsize", "pickup", "van", "semi", "truck", "motorcycle"]

# runs every function in file data_process_improved, in just one function. takes in a doc.
def process_doc(doc):
    data_process_improved.calculate_speed_accel(doc, cur_avg_speed, cur_avg_accel)
    data_process_improved.find_lane_changes(doc, lanes_occupied)
    data_process_improved.find_vehicle_class(doc, vehicle_classes)
    data_process_improved.calculate_trajectory_lengths(doc, lengths)

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
    # for every doc, run process_doc and calculated data to the global lists defined above
    futures = [executor.submit(process_doc, doc) for doc in cursor]

data=[cur_avg_speed, cur_avg_accel, lanes_occupied, vehicle_classes, lengths]
visualization_grid.graph(data)
