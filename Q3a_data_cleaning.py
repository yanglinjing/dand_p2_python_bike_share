def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of 【minutes】.

    Remember that Washington is in terms of 【milliseconds】 while Chicago and NYC are in terms of 【seconds】.

    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """

    # YOUR CODE HERE
    # 获取时间
    if 'tripduration' in datum:
        #Chicago & NYC
        duration = float(datum['tripduration'])
    else:
        #Washington
        duration = float(datum['Duration (ms)']) / 1000

    #换算成分钟(没有四舍五入，保留小数)
    duration = duration / 60

    #print(duration)
    return duration

#测试：
#duration_in_mins(example_trips['Washington'], 'Washington')

# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 13.9833,
         'Chicago': 15.4333,
         'Washington': 7.1231}

for city in tests:
    assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001

#---------------------------------------------

def time_of_trip(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the month, hour, and day of the week in
    which the trip was made.

    Remember that NYC includes seconds, while Washington and Chicago do not.

    HINT: You should use the datetime module to parse the original date
    strings into a format that is useful for extracting the desired information.
    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    """

    # YOUR CODE HERE
    if 'starttime' in datum:
        start_time = datum['starttime']
    else:
        start_time = datum['Start date']

    hour = int(start_time.split(' ')[1].split(':')[0])

    #-----获取年月日（string)，用datetime.strptime转换为日期格式，
    #-----以便获取星期几------
    dt = start_time.split(' ')[0]
    #因为'%Y%m%d'必须是4/2/2，所以要给个位数的月份、日期前面写上0
    month = dt.split('/')[0]
    if len(month) == 1:
        month = '0' + month
    day = dt.split('/')[1]
    if len(day) == 1:
        day = '0' +day
    year = dt.split('/')[2]
    #把string转为datatime对象
    dt = datetime.strptime(year + month + day, '%Y%m%d')

    #用完month之后，把它转为数字
    month = int(month)

    #获取星期几0-6 datetime.today().weekday()
    #获取星期几1-7 .isoweekday()
    wkd = dt.isoweekday()
    if wkd == 1:
        day_of_week = 'Monday'
    elif wkd == 2:
        day_of_week = 'Tuesday'
    elif wkd == 3:
        day_of_week = 'Wednesday'
    elif wkd == 4:
        day_of_week = 'Thursday'
    elif wkd == 5:
        day_of_week = 'Friday'
    elif wkd == 6:
        day_of_week = 'Saturday'
    elif wkd == 7:
        day_of_week = 'Sunday'

    return (month, hour, day_of_week)


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': (1, 0, 'Friday'),
         'Chicago': (3, 23, 'Thursday'),
         'Washington': (3, 22, 'Thursday')}

for city in tests:
    assert time_of_trip(example_trips[city], city) == tests[city]

#---------------------------------------------
def type_of_user(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the type of system user that made the
    trip.

    Remember that Washington has different category names compared to Chicago
    and NYC.
    """

    # YOUR CODE HERE
    if 'Customer' in datum:
        user_type = datum['Customer']
    elif 'usertype' in datum:
        user_type = datum['usertype']
    else:
        user_type = datum['Member Type']
        if user_type == 'Registered':
            user_type = 'Subscriber'
        elif user_type == 'Casual':
            user_type = 'Customer'

    return user_type


# Some tests to check that your code works. There should be no output if all of
# the assertions pass. The `example_trips` dictionary was obtained from when
# you printed the first trip from each of the original data files.
tests = {'NYC': 'Customer',
         'Chicago': 'Subscriber',
         'Washington': 'Subscriber'}

for city in tests:
    assert type_of_user(example_trips[city], city) == tests[city]
