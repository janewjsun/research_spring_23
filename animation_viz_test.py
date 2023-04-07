# testing out the animation function on data processed via sliding window


import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pymongo import MongoClient
import urllib
import data_process_improved
import seaborn as sns

username = urllib.parse.quote_plus('readonly')
password = urllib.parse.quote_plus('mongodb@i24')
client = MongoClient('mongodb://%s:%s@10.80.4.91' % (username, password))
db = client["reconciled"]  # put database name here
col = db["groundtruth_scene_1_130__cajoles"]
# col = db["63643fafd11ece4cb356b2ed__wvcithmergeallnodes"]

# get the time range of the entire collection
t_max = col.find().sort("first_timestamp", -1).limit(1)[0]["first_timestamp"]
t_min = col.find().sort("first_timestamp", 1).limit(1)[0]["first_timestamp"]

# specify rolling time window and increment
time_window = 10
increment = 5
l, r = t_min, t_min+time_window



def graph(speed_lst):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    sns.kdeplot(data=speed_lst, ax=ax, color="palevioletred", fill=True)
    print(type(ax))
    return ax

plots = []

fig, (ax1,ax2) = plt.subplots(1,2)
big_speed = []
big_accel = []
while r < t_max:
    query = {"first_timestamp": {"$gte": l,
                                 "$lt": r}}  # query for all documents whose first_timestamp is within the range [l, r)
    cursor = col.find(query)

    speed_lst = []
    accel_lst = []
    while cursor.alive:
        doc = cursor.next()
        data_process_improved.calculate_speed_accel(doc, speed_lst, accel_lst)
    # plot = graph(speed_lst)
    # plots.append(plot)
    big_speed.append(speed_lst)
    big_accel.append(accel_lst)

    l += increment
    r += increment

def update(frame):
    global ax1, ax2
    # ax.clear()
    #
    # print('x',type(plots[frame]))

    ax1.clear()
    speed_lst=big_speed[frame]
    sns.kdeplot(data=speed_lst, ax=ax1, color="palevioletred", fill=True)
    ax1.set_xlim(65, 150)
    ax1.set_ylim(0, 0.07)

    ax2.clear()
    accel_lst = big_accel[frame]
    sns.kdeplot(data=accel_lst, ax=ax2, color="palevioletred", fill=True)
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(0, 0.8)

    # ax = plots[frame]

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(big_speed), interval=100, repeat=True)
plt.show()
