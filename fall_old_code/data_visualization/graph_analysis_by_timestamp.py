import json
import seaborn as sns

FILE = '/Users/janesun/Desktop/spring23_research/1_130/groundtruth_scene_1_130__cajoles_transformed_by_car.json'

with open(FILE) as file:
    by_car_by_timestamp = json.load(file)

# prints basic stats including distribution of follow distances
def graph_follow_distance_distribution(ax):
    distances = []
    for car in by_car_by_timestamp:
        if not by_car_by_timestamp[car].get('follow distance'): continue
        follow_dist = by_car_by_timestamp[car]['follow distance']

        for tuple in follow_dist:
            distances.append(tuple[1])
            # dist = round(tuple[1]/50) * 50
            # dic[dist] = dic.get(dist,0)+1

    # include values of follow distance that had 0 frequency so dictionary has keys of equal
    # intervals


    # ax.hist(distances, weights = np.ones(len(distances))/len(distances), color = "palevioletred")
    sns.kdeplot(distances, ax = ax, color = "palevioletred", fill = True)

    # for i in range(min(dic.keys()), max(dic.keys())+1, 50):
    #     dic[i] = dic.get(i,0)
    # sort_dict = dict(sorted(dic.items()))
    # names = list(sort_dict.keys())
    # values = list(sort_dict.values())
    #
    # # ax.hist(dic)
    # ax.bar(range(len(sort_dict)), values, tick_label=names)
    ax.set_ylabel("frequency (%)")
    ax.set_xlabel("follow distance (ft)")
    ax.set_title("distribution of follow distances")



# prints basic stats including distribution of the change in follow distances
def graph_follow_distance_change_distribution(ax):
    distance_changes = []
    for car in by_car_by_timestamp:
        if not by_car_by_timestamp[car].get('follow distance'): continue
        follow_dist = by_car_by_timestamp[car]['follow distance']
        for idx, tuple in enumerate(follow_dist[:-1]):
            # only if same car
            if tuple[0] != follow_dist[idx+1][0]: continue
            diff = tuple[1] - follow_dist[idx+1][1]
            # diff = round(diff/2)*2
            # dic[diff] = dic.get(diff, 0)+1
            distance_changes.append(diff)

    # ax.hist(distance_changes, weights = np.ones(len(distance_changes))/len(distance_changes)
    #         , color = "palevioletred")
    sns.kdeplot(distance_changes, ax = ax, color = "palevioletred", fill = True)

    # # include values of follow distance change that had 0 frequency so dictionary has keys of
    # # equal intervals
    # for i in range(min(dic.keys()), max(dic.keys())+1, 2):
    #     dic[i] = dic.get(i,0)
    #
    # sort_dict = dict(sorted(dic.items()))
    # names = list(sort_dict.keys())
    # values = list(sort_dict.values())
    #
    # ax.bar(range(len(sort_dict)), values, tick_label=names)
    ax.set_ylabel("frequency (%)")
    ax.set_xlabel("change in follow distance (feet)")
    ax.set_title("distribution of change in follow distances")

