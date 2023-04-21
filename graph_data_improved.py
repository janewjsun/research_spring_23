# this file takes in the information from testMongoDB, which comes from running data_process_improved
# functions, and plots each of them on an axis

import seaborn as sns

# takes a list of speeds and graphs it onto ax1
def graph_cur_avg_speed(speed, ax1):
    sns.kdeplot(data=speed, ax = ax1, color = "palevioletred", fill = True)
    ax1.set_ylabel("frequency (%)")
    ax1.set_xlabel("speed (mph)")
    ax1.set_title("distribution of speeds")

    #todo: automatically set bounds based on data variability
    ax1.set_xlim(left = 65, right = 150)
    ax1.set_ylim(bottom = 0, top = 0.10)


# takes a list of accelerations and graphs it onto ax2
def graph_cur_avg_accel(accel, ax2):
    sns.kdeplot(data=accel, ax = ax2, color = "palevioletred", fill = True)
    ax2.set_ylabel("frequency (%)")
    ax2.set_xlabel("acceleration (f/s^2)")
    ax2.set_title("distribution of accelerations")
    ax2.set_xlim(left = -3, right = 3)
    ax2.set_ylim(bottom = 0, top = 0.8)


# takes a dictionary of lane occupations and graphs it onto ax3
def graph_lane_occupation(lanes, ax3):
    names = list(lanes.keys())
    values_pre = list(lanes.values())
    ttl = sum(values_pre)
    values = [i/ttl for i in values_pre]
    ax3.bar(range(len(lanes)), values, tick_label=names, color = "palevioletred")
    ax3.set_ylabel("frequency (%)")
    ax3.set_xlabel("lane of highway")
    ax3.set_title("distribution of lane locations")
    ax3.set_ylim(bottom=0, top=0.25)

# takes a dictionary of vehicle classes (types of vehicles) and graphs it onto ax4
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
    ax4.set_ylim(bottom=0, top = 0.5)

# takes a list of accelerations and graphs it onto ax2
def graph_traj_length(lengths, ax5):
    sns.kdeplot(lengths, ax = ax5, color = "palevioletred", fill = True)
    ax5.set_ylabel("frequency (%)")
    ax5.set_xlabel("length (feet)")
    ax5.set_title("distribution of trajectory lengths")
    # ax5.set_xlim(left = 1000, right = 2000)
    # ax5.set_ylim(bottom = 0, top = 0.01)

    # todo: lengths will be short at the start & end of trajectory because traj data is incomplete
    # could fix this by filtering out data where traj starts before + ends after timestamp cutoff
