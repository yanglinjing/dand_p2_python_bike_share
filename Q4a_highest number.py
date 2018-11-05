def number_of_trips(filename):
    """
    This function reads in a file with trip data and reports the number of
    trips made by subscribers, customers, and total overall.
    """
    with open(filename, 'r') as f_in:
        # set up csv reader object
        reader = csv.DictReader(f_in)

        # initialize count variables
        n_subscribers = 0
        n_customers = 0

        # tally up ride types
        for row in reader:
            if row['user_type'] == 'Subscriber':
                n_subscribers += 1
            else:
                n_customers += 1

        # compute total number of rides
        n_total = n_subscribers + n_customers

        # return tallies as a tuple
        return(n_subscribers, n_customers, n_total)

#-------------------------
## Modify this and the previous cell to answer Question 4a. Remember to run ##
## the function on the cleaned data files you created from Question 3.      ##

data_file = {'Chicago': './data/Chicago-2016-Summary.csv', 'NYC': './data/NYC-2016-Summary.csv', 'Washington': './data/Washington-2016-Summary.csv'}
for city in data_file:
    n_subscribers, n_customers, n_total = number_of_trips(data_file[city])

    p_subscribers = round(n_subscribers / n_total *100, 2)
    p_customers = round(n_customers / n_total *100, 2)

    summary = "{}: {} subscribers ({}%), {} customers ({}%), {} in total".format(city, n_subscribers, p_subscribers, n_customers, p_customers, n_total)
    print(summary)

#In [47]: '{:,}'.format(1234567890)
#Out[47]: '1,234,567,890'
