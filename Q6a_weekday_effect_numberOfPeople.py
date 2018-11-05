##Is the pattern of ridership different on the 【weekends】 versus 【weekdays】? On what days are Subscribers most likely to use the system? What about Customers? Does the 【average duration】 of rides change depending on the day of the week?

#---------星期几的骑车人数--------
def calculate_user_numbers_day_of_week(day_of_week, n_user):
    if day_of_week == 'Monday':
        n_user[0] += 1
    elif day_of_week == 'Tuesday':
        n_user[1] += 1
    elif day_of_week == 'Wednesday':
        n_user[2] += 1
    elif day_of_week == 'Thursday':
        n_user[3] += 1
    elif day_of_week == 'Friday':
        n_user[4] += 1
    elif day_of_week == 'Saturday':
        n_user[5] += 1
    elif day_of_week == 'Sunday':
        n_user[6] += 1
    return n_user

#------------subscriber或customer在每周的每一天的骑车人数-------
def calculate_user_numbers(filename, user_type):
    with open (filename) as f:
        reader = csv.DictReader(f)
        n_user = [0,0,0,0,0,0,0]
        for row in reader:
            if row['user_type'] == user_type:
                calculate_user_numbers_day_of_week(row['day_of_week'], n_user)
    return n_user

def draw_plot(data_subscribers, data_customers, y_label, city):
    y1 = data_subscribers
    y2 = data_customers
    x1 = range(1,8)
    x2 = range(1,8)

    plt.plot(x1,y1,label='Subscribers',linewidth=3,color='r',marker='o', markerfacecolor='blue',markersize=12)

    plt.plot(x2,y2,label='Customers')

    plt.title('{} in {} during the week'.format(y_label, city))
    plt.xlabel('Day of Week')
    plt.ylabel('{}'.format(y_label))

    plt.legend()
    plt.show()

data_files = {'Chicago': './data/Chicago-2016-Summary.csv', 'NYC': './data/NYC-2016-Summary.csv', 'Washington': './data/Washington-2016-Summary.csv'}

for city in data_files:
    n_subscribers = calculate_user_numbers(data_files[city], 'Subscriber')
    n_customers = calculate_user_numbers(data_files[city], 'Customer')
    draw_plot(n_subscribers, n_customers, 'Number of people using bikes', city)
