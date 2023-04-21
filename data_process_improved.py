# this file processes data by pymongo documents

# lane boundaries
LANES = {'E1': [0, 12], 'E2': [12, 24], 'E3': [24, 36], 'E4': [36, 48], 'E5': [48, 60],
         'E6': [60, 72], 'W1': [72, 84], 'W2': [84, 96], 'W3': [96, 108], 'W4': [108, 120],
         'W5': [120, 132], 'W6': [132, 144]}

# vehicle types
VEHICLE = ["sedan", "midsize", "pickup", "van", "semi", "truck", "motorcycle"]


# this code takes in a specific document, and two lists that house all the speed and acceleration
# data across all trajectories. it calculates the speed and acceleration of "doc"'s data, saving
# every 10th data point in all_cur_speed and all_cur_accel. the unit is in feet and seconds
def calculate_speed_accel(doc, all_cur_speed, all_cur_accel):
    x_pos = doc["x_position"]
    time = doc["timestamp"]
    ctr = 0
    prev_x = x_pos[0]
    prev_speed, cur_speed = 0,0
    for i in range(1, len(x_pos)):
        cur_x = x_pos[i]
        time_diff = time[i] - time[i - 1]

        if i==1:
            continue

        # speed: feet/sec; accel: feet/sec^2
        momentary_speed = abs((cur_x - prev_x)) / (time_diff)
        momentary_accel = (prev_speed - momentary_speed) / (time_diff)

        if ctr == 10:
            ctr = 0
            all_cur_speed.append(momentary_speed)
            all_cur_accel.append(momentary_accel)

        prev_x = cur_x
        prev_speed=momentary_speed

        ctr+=1


# this code takes in a document and a dic of all lane occupation across all trajectories. it finds
# the lanes that this document occupies based on the lane boundaries LANES
def find_lane_changes(doc, lanes_occupied):

    y_pos = doc["y_position"]
    prev, cur = None, None
    for i in range(len(y_pos)):
        y=y_pos[i]
        for lane, rnge in LANES.items():
            if rnge[0] < y <= rnge[1]:
                cur = lane
                if not prev:
                    prev = cur
                    lanes_occupied[prev] += 1
                break

        # lane change occurs
        if prev != cur:
            lanes_occupied[prev] += 1
            prev = cur


# this code takes in a doc and a dictionary keeping track of all vehicle classes in the trajs. it
# updates this dictionary
def find_vehicle_class(doc, vehicle_class):
    cars_class = doc["coarse_vehicle_class"]
    class_name = VEHICLE[cars_class]
    vehicle_class[class_name] += 1

# this code takes in a doc and a list keeping track of all trajectory lengths. it calculates the
# length of "doc"'s trajectory and updates the list
def calculate_trajectory_lengths(doc, lengths):
    lengths.append(abs(doc["ending_x"]-doc["starting_x"]))