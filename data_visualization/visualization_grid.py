# this file sets up the visualization grid and runs functions that make plots to be put in the grid


# time thing is a very basic way of showing time it run this file
import time
now1 = time.time()


import matplotlib as mpl
import matplotlib.pyplot as plt

import graph_analysis_by_timestamp as by_timestamp
import graph_data_improved

fontsize = 5

figure = plt.figure()

plt.rcParams.update({'font.size': 8})
plt.subplots_adjust(left = 0.125, right = 0.9, bottom = 0.1, top = 0.9, wspace=0.2, hspace=0.5)

gs = mpl.gridspec.GridSpec(nrows=5, ncols=4, height_ratios=[1,1,4,4,4])

title = figure.add_subplot(gs[0,0:4])
title.set_axis_off()
title.text(0.47,0.5,"Plots", fontsize=20, color="#808080")


indiv_title = figure.add_subplot(gs[1,0:2])
indiv_title.text(0.3,0.5,"Individual Trajectories", fontsize=13, color="#808080")
indiv_title.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

timestamp_title = figure.add_subplot(gs[1,2:4])
timestamp_title.text(0.3,0.5,"Timestamped Trajectories", fontsize=13, color="#808080")
timestamp_title.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

# indiv
i1 = figure.add_subplot(gs[2,0])
i2 = figure.add_subplot(gs[2,1])
# by_car.graph_speed_accel(i1, i2)


i3 = figure.add_subplot(gs[3,0])
# by_car.graph_lane_changes(i3)

i4 = figure.add_subplot(gs[3,1])
# by_car.graph_vehicle_class(i4)


i5 = figure.add_subplot(gs[4,0])
# by_car.graph_trajectory_lengths(i5)

graph_data_improved.graph(i1, i2, i3, i4, i5)

i6 = figure.add_subplot(gs[4,1])
i6.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

#timestamp

t1 = figure.add_subplot(gs[2,2])
by_timestamp.graph_follow_distance_distribution(t1)

t2 = figure.add_subplot(gs[2,3])
by_timestamp.graph_follow_distance_change_distribution(t2)

t3 = figure.add_subplot(gs[3,2])
t3.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
t4 = figure.add_subplot(gs[3,3])
t4.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
t5 = figure.add_subplot(gs[4,2])
t5.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
t6 = figure.add_subplot(gs[4,3])
t6.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

now2=time.time()
print(now2-now1)
plt.show()
