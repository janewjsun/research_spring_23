# this processes data by pymongo documents, functions are compatible w/ multi-threading or
# collection-based processing

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

        momentary_speed = abs((cur_x - prev_x)) / (time_diff)
        momentary_accel = (prev_speed - momentary_speed) / (time_diff)

        if ctr == 10:
            ctr = 0
            all_cur_speed.append(momentary_speed)
            all_cur_accel.append(momentary_accel)

        prev_x = cur_x
        prev_speed=momentary_speed

        # momentary_speed = abs((cur_x - prev_x) / (time_diff))
        # car_avg_speed = (car_avg_speed*(i-1) + momentary_speed) / (i) # (i-1) here because speed is for 2 distances
        # prev_x = cur_x
        #
        # if i==1:
        #     prev_speed = car_avg_speed
        #     continue
        #
        # momentary_accel = abs((prev_speed-car_avg_speed)/(time_diff))
        # car_avg_accel = (car_avg_accel*(i-2) +momentary_accel)/(i-1)
        # prev_speed=car_avg_speed
        ctr+=1
    return all_cur_speed, all_cur_accel



def find_lane_changes(doc, lanes_occupied, lanes):

    y_pos = doc["y_position"]
    prev, cur = None, None
    for i in range(len(y_pos)):
        y=y_pos[i]
        for lane, rnge in lanes.items():
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

def find_vehicle_class(doc, vehicle_class, class_meanings):
    cars_class = doc["coarse_vehicle_class"]
    class_name = class_meanings[cars_class]
    vehicle_class[class_name] += 1

def calculate_trajectory_lengths(doc, lengths):
    if abs(doc["ending_x"]-doc["starting_x"]) < 0:
        print(abs(doc["ending_x"]-doc["starting_x"]))
    lengths.append(abs(doc["ending_x"]-doc["starting_x"]))