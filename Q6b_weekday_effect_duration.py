

#---------星期几的骑车总时长--------
def calculate_duration_day_of_week(day_of_week, duration, length):
    if day_of_week == 'Monday':
        duration[0] += length
    elif day_of_week == 'Tuesday':
        duration[1] += length
    elif day_of_week == 'Wednesday':
        duration[2] += length
    elif day_of_week == 'Thursday':
        duration[3] += length
    elif day_of_week == 'Friday':
        duration[4] += length
    elif day_of_week == 'Saturday':
        duration[5] += length
    elif day_of_week == 'Sunday':
        duration[6] += length
    return duration

#-----------subscriber或customer在星期几的骑车总时长---------
def calculate_total_duration(filename, user_type):
    with open(filename) as f:
        reader = csv.DictReader(f)
        duration = [0,0,0,0,0,0,0]
        for row in reader:
            if row['user_type'] == user_type:
                length = float(row['duration'])
                calculate_duration_day_of_week(row['day_of_week'], duration, length)
        return duration

#---------subscriber或customer在星期几的骑车平均时长----
def calculate_avg_duration(n_user, duration):
    avg_duration = [0,0,0,0,0,0,0]
    for n in range(0,7):
        avg_duration[n] = duration[n] / n_user[n]
    return avg_duration


for city in data_files:
    filename = data_files[city]
    duration_subscribers = calculate_avg_duration(calculate_user_numbers(filename, 'Subscriber'), calculate_total_duration(filename, 'Subscriber'))
    duration_customers = calculate_avg_duration(calculate_user_numbers(filename, 'Customer'), calculate_total_duration(filename, 'Customer'))
    draw_plot(duration_subscribers, duration_customers, 'Average duration of using bikes', city)
