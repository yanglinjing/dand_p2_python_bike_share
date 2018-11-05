##Question 5:
##Use the parameters of the .hist() function to plot the distribution of trip times for the 【Subscribers】 in your selected city. Do the same thing for only the 【Customers】.
##Add limits to the plots so that only trips of 【duration less than 75 minutes】 are plotted. As a bonus, set the plots up so that bars are in 【five-minute wide intervals】.

def retrive_duration(filename, user_type = 'Subscriber'):
    data = []
    with open (filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['user_type'] == user_type:
                duration = float(row['duration'])
                if duration < 75:
                    data.append(duration)
    return data

def draw_duration_plot(data, city, user_type):
    plt.hist(data, bins = 15, range = (0, 75))
    plt.title('Trip Durations of {}s in {}'.format(user_type, city))
    plt.xlabel('Duration (m)')
    plt.show()

#-----------实例------------
data_files = {'Chicago': './data/Chicago-2016-Summary.csv', 'NYC': './data/NYC-2016-Summary.csv', 'Washington': './data/Washington-2016-Summary.csv'}
user_types = ['Subscriber', 'Customer']

for city in data_files:
    for user_type in user_types:
        draw_duration_plot(retrive_duration(data_files[city], user_type), city, user_type)
