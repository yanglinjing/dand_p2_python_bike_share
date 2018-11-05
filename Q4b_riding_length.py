## HINT: The csv module reads in all of the data as 【strings】, including numeric values. You will need a function to convert the strings into an appropriate 【numeric】 type before you aggregate data.
## TIP: For the Bay Area example, the average trip length is 14 minutes and 3.5% of trips are longer than 30 minutes.

def riding_length(filename):
    with open (filename, 'r') as f:
        reader = csv.DictReader(f)

        #初始值0
        total_length = 0
        n_over30 = 0
        n_total = 0

        for row in reader:
            duration = float(row['duration'])
            total_length += duration
            n_total += 1
            if duration > 30:
                n_over30 += 1

        average_length = total_length / n_total
        p_over30 = n_over30 / n_total
    return(average_length, p_over30)

#---------带入表格数据----
data_file = {'Chicago': './data/Chicago-2016-Summary.csv', 'NYC': './data/NYC-2016-Summary.csv', 'Washington': './data/Washington-2016-Summary.csv'}

for city in data_file:
    average_length, p_over30 = riding_length(data_file[city])
    average_length = round(average_length, 2)
    p_over30 = round(p_over30 *100, 2)

    summary = "The average trip length for {} is {} minutes, with {}% people having a ride for more than 30 minutes.".format(city, average_length, p_over30)
    print(summary)
