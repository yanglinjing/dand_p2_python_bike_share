## Use this and additional cells to collect all of the trip times as a list and then use pyplot functions to generate a histogram of trip times. ##

# load library
import matplotlib.pyplot as plt

# this is a 'magic word' that allows for plots to be displayed
# inline with the notebook. If you want to know more, see:
# http://ipython.readthedocs.io/en/stable/interactive/magics.html
%matplotlib inline

def retrive_data(filename):
    with open (filename, 'r') as f:
        reader = csv.DictReader(f)
        #因为文件自动关闭，所以所有内容都要在with open里
        data = []
        for row in reader:
            data.append(float(row['duration']))
        return data

data_files = ['./data/Chicago-2016-Summary.csv', './data/NYC-2016-Summary.csv', './data/Washington-2016-Summary.csv']
data = []
for data_file in data_files:
    data.append(retrive_data(data_file))

plt.hist(data)
plt.title('Distribution of Trip Durations')
plt.xlabel('Duration (m)')
plt.show()
