# code to upload photo to internal viz_dev site

from datetime import datetime
import requests

now = datetime.now()
rn = now.strftime("%Y-%m-%d_%H-%M-%S")
photo = '/Users/janesun/Desktop/spring23_research1/mar27_photo.png'
url = 'http://viz-dev.isis.vanderbilt.edu:5991/upload?type=jane_viz'
files = {'upload_file': open(photo, 'rb')}
ret = requests.post(url, files=files)
print(ret)
if ret.status_code == 200:
    print('Uploaded!')
