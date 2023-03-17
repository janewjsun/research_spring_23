# this file takes in the information from testMongoDB, which comes from running data_process_improved
# functions, and plots each of them on an axis

# todo: have different functions for each graph instead of one large function

import numpy as np

import testMongoDB

speed = testMongoDB.cur_avg_speed
accel = testMongoDB.cur_avg_accel
lanes = testMongoDB.lanes_occupied
vehicle_class = testMongoDB.vehicle_classes
lengths = testMongoDB.lengths

def graph(ax1, ax2, ax3, ax4, ax5):

    # one speed per trajectory thus len(trajectory) = len(speed)
    data_length = len(speed)
    ax1.hist(speed, weights=np.ones(len(speed)) / len(speed), color = "palevioletred")
    ax1.set_ylabel("frequency (%)")
    ax1.set_xlabel("speed (mph)")
    ax1.set_title("distribution of speeds")

    ax2.hist(accel, range = (-3,3), weights=np.ones(len(accel))/len(accel), color = "palevioletred")
    ax2.set_ylabel("frequency (%)")
    ax2.set_xlabel("acceleration (f/s^2)")
    ax2.set_title("distribution of accelerations")


    names = list(lanes.keys())
    values_pre = list(lanes.values())
    ttl = sum(values_pre)
    values = [i/ttl for i in values_pre]

    ax3.bar(range(len(lanes)), values, tick_label=names, color = "palevioletred")
    ax3.set_ylabel("frequency (%)")
    ax3.set_xlabel("lane of highway")
    ax3.set_title("distribution of lane locations")

    keys = list(vehicle_class.keys())
    values = [i/data_length for i in list(vehicle_class.values())]

    ax4.bar(range(len(vehicle_class)), values, tick_label=keys, color = "palevioletred")
    ax4.set_ylabel("frequency (%)")
    ax4.set_xlabel("vehicle type")
    ax4.set_title("distribution of vehicle types")
    # ax4.tick_params(axis='x', labelrotation=45)

    ax5.hist(lengths, weights=np.ones(len(lengths)) / len(lengths), color = "palevioletred")
    ax5.set_ylabel("frequency (%)")
    ax5.set_xlabel("length (feet)")
    ax5.set_title("distribution of trajectory lengths")