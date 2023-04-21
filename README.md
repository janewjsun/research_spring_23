# research_spring_23
This repository contains two python scripts to analyze a given collection of traffic trajectories in two ways: first, as a whole, and second, via a sliding window. The collection of trajectories is stored in MongoDB, and it is trajectory-based rather than timestamp-based. Connected MongoDB collections have relevant queries such as "first_timestamp", "coarse_vehicle_class", and so on. 

## requirements
To run this program, you will need:
- python 3
- the following python libraries/modules:
  - pymongo
  - urllib
  - concurrent.futures
  - seaborn
  - matplotlib
  - optional, for upload: requests
  
## usage
1) analyzing traffic trajectories as a whole:
- run overall_processing.py with any method such as on terminal in the file's directory
``` 
python3 overall_processing.py
```
- should return a static plot with five subplots, along with axes titles
2) analyzing trajectories via a sliding window
- run animation_viz_test.py with any method such as on terminal in the file's directory
``` 
python3 animation_viz_test.py
```
- should return a dynamic plot with five subplots, along with axes titles, that shows how the data changes over time


note: you must connect to the database via secure vpn server

## author
created by Jane with starter code such as connection to MongoDB by Yanbing

created for the I-24 Motion Project https://i24motion.org/ as part of Vanderbilt's Institute for Software Integrated Systems

spring 2023
