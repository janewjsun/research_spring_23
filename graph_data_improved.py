# this file takes in the information from testMongoDB, which comes from running data_process_improved
# functions, and plots each of them on an axis

# todo: have different functions for each graph instead of one large function

import testMongoDB as datasource

import seaborn as sns
import numpy as np

def graph_cur_avg_speed(speed, ax1):
    #kde plot better represents this data
    sns.kdeplot(data=speed, ax = ax1, color = "palevioletred", fill = True)
    # ax1.hist(speed, weights=np.ones(len(speed)) / len(speed), color = "palevioletred")
    ax1.set_ylabel("frequency (%)")
    ax1.set_xlabel("speed (mph)")
    ax1.set_title("distribution of speeds")
    # ax1.set_xlim(left = 50, right = 160)
    # ax1.set_ylim(bottom = 0, top = 0.04)

def graph_cur_avg_accel(accel, ax2):
    sns.kdeplot(data=accel, ax = ax2, color = "palevioletred", fill = True)
    # ax2.hist(accel, range = (-3,3), weights=np.ones(len(accel))/len(accel), color = "palevioletred")
    ax2.set_ylabel("frequency (%)")
    ax2.set_xlabel("acceleration (f/s^2)")
    ax2.set_title("distribution of accelerations")
    # ax2.set_xlim(left = -5, right = 5)
    # ax2.set_ylim(bottom = 0, top = 0.8)

def graph_lane_occupation(lanes, ax3):
    names = list(lanes.keys())
    values_pre = list(lanes.values())
    ttl = sum(values_pre)
    values = [i/ttl for i in values_pre]
    ax3.bar(range(len(lanes)), values, tick_label=names, color = "palevioletred")
    ax3.set_ylabel("frequency (%)")
    ax3.set_xlabel("lane of highway")
    ax3.set_title("distribution of lane locations")

def graph_vehicle_class(vehicle_class, ax4):
    data_length = 0
    for k,v in vehicle_class.items():
        data_length += v
    keys = list(vehicle_class.keys())
    values = [i/data_length for i in list(vehicle_class.values())]

    ax4.bar(range(len(vehicle_class)), values, tick_label=keys, color = "palevioletred")
    ax4.set_ylabel("frequency (%)")
    ax4.set_xlabel("vehicle type")
    ax4.set_title("distribution of vehicle types")


def graph_traj_length(lengths, ax5):
    sns.kdeplot(lengths, ax = ax5, color = "palevioletred", fill = True)
    # ax5.hist(lengths, weights=np.ones(len(lengths)) / len(lengths), color = "palevioletred")
    ax5.set_ylabel("frequency (%)")
    ax5.set_xlabel("length (feet)")
    ax5.set_title("distribution of trajectory lengths")
    ax5.set_xlim(left = 1000, right = 2000)
    ax5.set_ylim(bottom = 0, top = 0.01)