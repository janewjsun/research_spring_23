import json
import numpy as np


FILE = "/Users/janesun/Desktop/spring23_research/1_130/groundtruth_scene_1_130__cajoles_processed.json"


with open(FILE) as file:
    data = json.load(file)

# graphs speed and acceleration information of car trajectories
def graph_speed_accel(ax1,ax2):
    speed = []
    accel = []
    ttl = 0
    for set in data:
        ttl+=1

        # just concatenate the lists
        for i in range(1, len(set['speed'])):
            speed.append(set['speed'][i][2])
            if i == 1: continue
            accel.append(set['accel'][i][2])

    ax1.hist(speed, weights=np.ones(len(speed)) / len(speed), color = "palevioletred")
    ax1.set_ylabel("frequency (%)")
    ax1.set_xlabel("speed (mph)")
    ax1.set_title("distribution of speeds")

    ax2.hist(accel, range = (-3,3), weights=np.ones(len(accel))/len(accel), color = "palevioletred")
    ax2.set_ylabel("frequency (%)")
    ax2.set_xlabel("acceleration (f/s^2)")
    ax2.set_title("distribution of accelerations")



# prints data regarding lane change information for car trajectories
def graph_lane_changes(ax):
    ttl_lc, num_changes = 0,0
    lanes = {'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'W1': 0, 'W2': 0,
                      'W3': 0, 'W4': 0, 'W5': 0, 'W6': 0}
    for set in data:
        if len(set['lane_changes']) > 1:
            ttl_lc += 1
            num_changes += len(set['lane_changes']) - 1
        for chng in set['lane_changes']:
            lanes[chng[0]] += 1

    names = list(lanes.keys())
    values_pre = list(lanes.values())
    ttl = sum(values_pre)
    values = [i/ttl for i in values_pre]

    ax.bar(range(len(lanes)), values, tick_label=names, color = "palevioletred")
    ax.set_ylabel("frequency (%)")
    ax.set_xlabel("lane of highway")
    ax.set_title("distribution of lane locations")


def graph_vehicle_class(ax):
    vehicle_class = {}
    classes = ["sedan", "midsize", "pickup", "van", "semi", "truck", "motorcycle"]
    for set in data:
        cl = set['coarse_vehicle_class']

        vehicle_class[classes[cl]] = vehicle_class.get(classes[cl], 0) + 1

    sort_dict = dict(sorted(vehicle_class.items()))
    keys = list(sort_dict.keys())
    values = [i/len(data) for i in list(sort_dict.values())]

    ax.bar(range(len(sort_dict)), values, tick_label=keys, color = "palevioletred")
    ax.set_ylabel("frequency (%)")
    ax.set_xlabel("vehicle type")
    ax.set_title("distribution of vehicle types")


def graph_trajectory_lengths(ax):

    lengths = []
    for set in data:
        lengths.append(abs(set["ending_x"]-set["starting_x"]))

    ax.hist(lengths, weights=np.ones(len(lengths)) / len(lengths), color = "palevioletred")
    ax.set_ylabel("frequency (%)")
    ax.set_xlabel("length (feet)")
    ax.set_title("distribution of trajectory lengths")