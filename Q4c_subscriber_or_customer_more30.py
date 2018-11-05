#Question 4c: Choose one city. Within that city, which type of user takes longer rides on average: Subscribers or Customers?

def compare_subscriber_customer(filename):
    with open (filename, 'r') as f:
         reader = csv.DictReader(f)

         n_subscribers = 0
         length_subscribers = 0
         n_customers = 0
         length_customers = 0

         for row in reader:
             duration = float(row['duration'])
             if row['user_type'] == 'Subscriber':
                 n_subscribers += 1
                 length_subscribers += duration
             else:
                 n_customers += 1
                 length_customers += duration

         avg_subscribers = length_subscribers / n_subscribers
         avg_customers = length_customers / n_customers

         return(avg_subscribers, avg_customers)

#-----------实例-----
filename = './data/Chicago-2016-Summary.csv'
avg_subscribers, avg_customers = compare_subscriber_customer(filename)
summary = "In Chicago, the average riding length of subscribers is {} minutes, whereas that of customers is {}.".format(round(avg_subscribers,2), round(avg_customers,2))
print(summary)
