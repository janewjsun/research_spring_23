# this file sets up the visualization grid and runs functions that make plots to be put in the grid


# time thing is a very basic way of showing time it run this file
# import time
# now1 = time.time()


import matplotlib as mpl
import matplotlib.pyplot as plt

import graph_data_improved

def graph(data):
    cur_avg_speed, cur_avg_accel, lanes_occupied, vehicle_classes, lengths = data

    fontsize = 5

    figure = plt.figure()

    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left = 0.125, right = 0.9, bottom = 0.1, top = 0.9, wspace=0.2, hspace=0.5)

    gs = mpl.gridspec.GridSpec(nrows=4, ncols=2, height_ratios=[1,4,4,4])

    title = figure.add_subplot(gs[0,0:2])
    title.set_axis_off()
    title.text(0.47,0.5,"Plots", fontsize=20, color="#808080")

    # indiv
    i1 = figure.add_subplot(gs[1,0])
    i2 = figure.add_subplot(gs[1,1])
    i3 = figure.add_subplot(gs[2,0])
    i4 = figure.add_subplot(gs[2,1])
    i5 = figure.add_subplot(gs[3,0])

    graph_data_improved.graph_cur_avg_speed(cur_avg_speed, i1)
    graph_data_improved.graph_cur_avg_accel(cur_avg_accel, i2)
    graph_data_improved.graph_lane_occupation(lanes_occupied,i3)
    graph_data_improved.graph_vehicle_class(vehicle_classes,i4)
    graph_data_improved.graph_traj_length(lengths, i5)


    i6 = figure.add_subplot(gs[3,1])
    i6.tick_params(left = False, right = False , labelleft = False ,
                    labelbottom = False, bottom = False)

    # now2=time.time()
    # print(now2-now1)
    plt.show()

